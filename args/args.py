from distutils.util import strtobool
from typing import List

__all__ = ["Args"]


class Args:
    def __init__(self, pattern: str, values: List[str]):
        self.pattern = pattern
        self.values = values
        self.map = self._map_key_values()

    def _map_key_values(self) -> dict:
        m = dict()
        for schema in self.pattern.split(","):
            v = self._cast_bool(self.values[0])
            m[schema] = v
            break
        return m

    def _cast_bool(self, value) -> bool:
        return strtobool(value.lower())

    def get_bool(self, key: str) -> bool:
        return self.map[key]
