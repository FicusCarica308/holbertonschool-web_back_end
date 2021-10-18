#!/usr/bin/env python3
"""
[summary]
Contains a single python function definition this time using
complex type annotations (inpits List from typing for subscriptable List class)
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """[summary]
    A type-annotated function sum_list which takes a list input_list of floats
    as argument and returns their sum as a float.
    Args:
        input_list (list[float]): list of floats we are adding together

    Returns:
        float: The sum of all the numbers in input_list
    """
    sum = 0
    for num in input_list:
        sum += num
    return(sum)
