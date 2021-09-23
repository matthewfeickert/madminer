from dataclasses import dataclass
from contextlib import suppress
from typing import Callable
from typing import Union


@dataclass
class Observable:

    name: str
    val_expression: Union[str, Callable]
    val_default: float = None
    is_required: bool = False

    def __post_init__(self):
        """Perform certain attribute quality assertions"""

        if isinstance(self.val_expression, str) is False:
            return

        with suppress(NameError):
            eval(self.val_expression)
