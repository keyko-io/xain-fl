# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from numproto.protobuf.ndarray_pb2 import (
    NDArray as numproto___protobuf___ndarray_pb2___NDArray,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class ClientMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TrainResult(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def theta(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[numproto___protobuf___ndarray_pb2___NDArray]: ...

        def __init__(self,
            *,
            theta : typing___Optional[typing___Iterable[numproto___protobuf___ndarray_pb2___NDArray]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ClientMessage.TrainResult: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"theta"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"theta",b"theta"]) -> None: ...

    unkown_instruction = ... # type: bool

    @property
    def result(self) -> ClientMessage.TrainResult: ...

    def __init__(self,
        *,
        result : typing___Optional[ClientMessage.TrainResult] = None,
        unkown_instruction : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ClientMessage: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"request",u"result",u"unkown_instruction"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"request",u"result",u"unkown_instruction"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"request",b"request",u"result",b"result",u"unkown_instruction",b"unkown_instruction"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"request",b"request",u"result",b"result",u"unkown_instruction",b"unkown_instruction"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"request",b"request"]) -> typing_extensions___Literal["result","unkown_instruction"]: ...

class ServerMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TrainConfig(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def theta(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[numproto___protobuf___ndarray_pb2___NDArray]: ...

        def __init__(self,
            *,
            theta : typing___Optional[typing___Iterable[numproto___protobuf___ndarray_pb2___NDArray]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ServerMessage.TrainConfig: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"theta"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"theta",b"theta"]) -> None: ...

    reconnect_in = ... # type: int

    @property
    def train_config(self) -> ServerMessage.TrainConfig: ...

    def __init__(self,
        *,
        reconnect_in : typing___Optional[int] = None,
        train_config : typing___Optional[ServerMessage.TrainConfig] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ServerMessage: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"instruction",u"reconnect_in",u"train_config"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"instruction",u"reconnect_in",u"train_config"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"instruction",b"instruction",u"reconnect_in",b"reconnect_in",u"train_config",b"train_config"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"instruction",b"instruction",u"reconnect_in",b"reconnect_in",u"train_config",b"train_config"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"instruction",b"instruction"]) -> typing_extensions___Literal["reconnect_in","train_config"]: ...