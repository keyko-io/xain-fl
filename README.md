# XAIN Federated Learning

This is the main source code repository for [xain-fl](https://www.xain.io/).

To get started, take a look at the documentation: https://xain-fl.readthedocs.io/en/latest

For developers, see [CONTRIBUTING.md](./CONTRIBUTING.md)


# Spike: XAIN FL Framework

At the time of this writing (`xain-fl v0.8`) the xain fl framework is composed
of the:
- **platform**: contains the coordinator and other services (written in rust)
- **sdk**: python sdk that contains the participant code. This is also where we
  define the actual machine learning training tasks. The [documentation and
  tutorial](https://xain-fl.readthedocs.io/projects/xain-sdk/en/latest/tutorial.html)
  show how it works.

#### Federation learning session flow

1. A coordinator is setup with the session parameters: `rounds`, `min_clients`,
   and `participants_ratio`.
2. Participants connect to the coordinator.
3. The coordinator waits until at least `min_clients` are connected to the
   coordinator.
4. Once the coordinator has enough participants connected it starts a round.
5. The coordinator starts by selecting a subset of the participants (depending
   of the `participants_ratio` setting)
6. At the beginning of a round each participant requests the global model (the
   weights of the current model)
7. With the model each participant executes the machine learning task on their
   own data
8. After each participant finishes their machine learning task they upload
   their update model to the coordinator.
9. After the coordinator receives the updated models from all the participants
   that are part of the round it runs the aggregation to compute the new global
   model.
10. The coordinator starts a new round and repeats steps 5 to 9

> **Note:** Although I refer only the coordinator and participants in this flow,
the xain fl framework actually splits the coordinator into two services
(coordinator and aggregator)



## Running the platform

1. Start the platform using
   [`docker-compose`](https://github.com/keyko-io/xain-fl/blob/master/docker/docker-compose.yml)

```bash
$ docker-compose -f docker/docker-compose.yml up
```

This will start both the `coordinator` which is responsible for managing the
`participants` and coordinating the federated learning session, and the
`aggregator` which is responsible for aggregation the individual models of each
participant into one global model.

It will also start a variety of others services useful for development,
debugging and monitoring:
- [swagger ui](http://localhost:80): The REST API specification for the
  coordinator. In the top _explore_ bar of swagger you can also type
  `./aggregator.yml` to see the REST API specification for the aggregator.
- [grafana](http://localhost:3000/dashboards): The default username and
  password for grafana is `admin`. The most helpful dashboard is the
  _Coordinator Metrics_ dashboard that shows information about the state of the
  federated learning session.

#### Changing the coordinator parameters

The `coordinator` service in the [docker-compose
file](https://github.com/keyko-io/xain-fl/blob/master/docker/docker-compose.yml)
uses the
[configs/docker-dev-coordinator.toml](https://github.com/keyko-io/xain-fl/blob/master/configs/docker-dev-coordinator.toml)
configuration file. This file can be used to change the behavior of the
coordinator.

The important settings are under the `federated_learning` section:
- **`rounds`**: the number of rounds the session will run
- **`participants_ratio`**: The ratio of connected participants that will be
  selected for each round.
- **`min_clients`**: The minimum number of participants that need to participate
  in each round (the coordinator will wait until enough participants are
  connected before starting a round)


## Running the python example

1. Install example and dependencies (recommend doing this inside a virtual
   environment)

```bash
$ pip install python/sdk
$ pip install python/client_examples/keras_house_prices
```

2. Download the dataset from
   [Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)
   (account required)

3. Prepare the data

```bash
$ cd python/client_examples/keras_house_prices
$ mkdir data
$ cd data
$ unzip house-prices-advanced-regression-techniques.zip
$ split-data --data-directory data --number-of-participants 10
$ cd ..
```

4. Run the python example

```bash
$ ./run.sh 10
```

## Resources

- [xain-fl repo](https://github.com/xainag/xain-fl)
- [python sdk documentation and
  tutorial](https://xain-fl.readthedocs.io/projects/xain-sdk/en/latest/tutorial.html)
- [Towards Federated Learning at Scale](https://arxiv.org/pdf/1902.01046.pdf)
