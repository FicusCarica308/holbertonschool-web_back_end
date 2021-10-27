#!/usr/bin/env python3
"""[summary]
"""
import csv
import math
from typing import List, Tuple


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

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            assert page > 0
            assert page_size > 9
            