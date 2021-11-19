#!/usr/bin/env python3
""" """
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Class testing utils.access_nest_map from utils.py"""

    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)
                           ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests function with three different situations"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)),
                           ({"a": 1}, ("a", "b"))
                           ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Tests if a KeyError is raised when a non-existent key is in path"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
            self.assertEqual(error.exception, KeyError)


class TestGetJson(unittest.TestCase):
    """Class testing utils.get_json from utils.py"""

    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})
                           ])
    def test_get_json(self, url, payload):
        """tests if the function returns the proper json package"""
        mock = Mock()
        mock.json.return_value = payload
        with patch('requests.get', return_value=mock):
            actual_result = get_json(url)
            self.assertEqual(actual_result, payload)
            mock.json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
