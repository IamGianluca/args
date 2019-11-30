from distutils.util import strtobool
from typing import Any, List

__all__ = ["Args"]


def str2bool(value: str) -> bool:
    return bool(strtobool(value.lower()))


def str2int(value: str) -> int:
    return int(value)


def str2str(value: str) -> str:
    return value


class Args:
    get_cast_func = {"": str2bool, "#": str2int, "*.": str2str}

    def __init__(self, pattern: str, values: List[str]):
        self.pattern = pattern
        self.values = values
        self.map = self._map_key_values()

    def _map_key_values(self) -> dict:
        m = dict()
        for schema in self.pattern.split(","):
            v = self._cast(to=schema, value=self.values[0])
            m[schema[0]] = v
        return m

    def _cast(self, to: str, value: str) -> Any:  # Union[bool, str, int]
        cast_func = self.get_cast_func[to[1:]]
        return cast_func(value)

    def get_bool(self, key: str) -> bool:
        return self.map[key]

    def get_int(self, key: str) -> int:
        return self.map[key]

    def get_str(self, key: str) -> str:
        return self.map[key]
