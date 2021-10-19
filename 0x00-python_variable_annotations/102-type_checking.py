#!/usr/bin/env python3
"""[summary]
"""
from typing import Tuple, List, Any, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """[summary]

    Args:
        lst (Tuple): [description]
        factor (int, optional): [description]. Defaults to 2.

    Returns:
        List: [description]
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
