#!/usr/bin/env python3
"""[summary]
"""
import csv
import math
from typing import List, Tuple


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """[summary]

        Args:
            page (int, optional): [description]. Defaults to 1.
            page_size (int, optional): [description]. Defaults to 10.

        Returns:
            List[List]: [description]
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        index_range = self.index_range(page, page_size)
        self.dataset()
        return (self.__dataset[index_range[0]:index_range[1]])
