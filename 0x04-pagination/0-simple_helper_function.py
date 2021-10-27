#!/usr/bin/env python3
"""[summary]
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """[summary]

    Args:
        page (int): [description]
        page_size (int): [description]

    Returns:
        Tuple[int, int]: [description]
    """
    start_index = (page * page_size) - page_size
    end_index = page * page_size
    return ((start_index, end_index))
