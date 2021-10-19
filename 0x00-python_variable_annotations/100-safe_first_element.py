#!/usr/bin/env python3
"""[summary]
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """[summary]

    Args:
        lst (Sequence[Any]): [description]

    Returns:
        Union[Any, None]: [description]
    """
    if lst:
        return lst[0]
    else:
        return None