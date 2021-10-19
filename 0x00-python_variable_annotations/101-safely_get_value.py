#!/usr/bin/env python3
"""[summary]
"""
from typing import Union, Mapping, Any, TypeVar


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'), None]) -> Union[Any, TypeVar('T')]:
    """[summary]

    Args:
        dct (Mapping): [description]
        key (Any): [description]
        default (Union[val, None]): [description]

    Returns:
        Union[Any, val]: [description]
    """
    if key in dct:
        return dct[key]
    else:
        return default
