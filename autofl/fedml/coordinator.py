from typing import Callable, List, Tuple

import tensorflow as tf
from numpy import ndarray

from .ops import get_model_params, set_model_params
from .participant import Participant


class Coordinator:
    def __init__(
        self, controller, model: tf.keras.Model, participants: List[Participant]
    ) -> None:
        self.controller = controller
        self.model = model
        self.participants = participants

    def replace_model(self, model_fn: Callable[..., tf.keras.Model]) -> None:
        self.model = model_fn()
        for p in self.participants:
            model = model_fn()
            p.replace_model(model)

    # Common initialization happens implicitly: By updating the participant weights to
    # match the coordinator weights ahead of every training round we achieve common
    # initialization.
    def fit(self, num_rounds: int):
        for training_round in range(num_rounds):
            # Determine who participates in this round
            indices = self.controller.indices()
            print("\nRound", str(training_round + 1), "- participants", indices)
            # Collect training results from the participants of this round
            thetas = []
            for index in indices:
                theta = self._single_step(index)
                thetas.append(theta)
            # Aggregate training results
            theta_prime = self.controller.aggregate(thetas)
            # Update own model parameters
            set_model_params(self.model, theta_prime)

    def _single_step(self, random_index: int) -> List[List[ndarray]]:
        participant = self.participants[random_index]
        # Push current model parameters to this participant
        theta = get_model_params(self.model)
        participant.update_model_parameters(theta)
        # Train for a number of steps
        participant.train(1)  # TODO don't train a full episode, just a few steps
        # Pull updated model parameters from participant
        theta_prime = participant.retrieve_model_parameters()
        return theta_prime

    def evaluate(self, x_test: ndarray, y_test: ndarray) -> Tuple[float, float]:
        # FIXME use Dataset
        x_test = x_test / 255.0
        loss, accuracy = self.model.evaluate(x_test, y_test)
        return loss, accuracy