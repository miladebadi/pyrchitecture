from dataclasses import dataclass
from functools import partial
from typing import Union, Type, Any


@dataclass
class Success:
    value: Any = None


@dataclass
class Failure:
    value: Any


class Result:
    def __init__(
        self, result_class: Union[Type["Success"], Type["Failure"]], *args: Any
    ) -> None:
        self.result_instance = result_class(*args)

    def __bool__(self):
        return self.is_success()

    def is_success(self) -> bool:
        return isinstance(self.result_instance, Success)

    def is_failure(self) -> bool:
        return isinstance(self.result_instance, Failure)

    @property
    def value(self) -> Any:
        return self.result_instance.value

    @classmethod
    def success(cls, value: Any = None) -> "Result":
        return Result(Success, value)

    @classmethod
    def failure(cls, value: Any) -> "Result":
        return Result(Failure, value)


success = partial(Result, Success)
failure = partial(Result, Failure)
