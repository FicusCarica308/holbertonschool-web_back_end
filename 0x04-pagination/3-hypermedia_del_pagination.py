#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """[summary]

        Args:
            index (int, optional): [description]. Defaults to None.
            page_size (int, optional): [description]. Defaults to 10.

        Returns:
            Dict: [description]
        """
        keyError = True
        skip_ammount = 0
        self.indexed_dataset()
        assert index <= len(self.__indexed_dataset)
        pairs = {"index": index, "data": [],
                 "page_size": page_size,
                 "next_index": index + page_size}
        while keyError is not False:
            test = index + skip_ammount
            try:
                pairs["data"].append([self.__indexed_dataset[test],
                                     self.__indexed_dataset[test + 1]])
                keyError = False
            except KeyError:
                skip_ammount += 1
        return pairs
