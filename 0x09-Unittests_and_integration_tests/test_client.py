#!/usr/bin/env python3
""" More unittests """
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized

class TestGithubOrgClient(unittest.TestCase):
    """ Tests for all tGithubOrgClient class methods """

    @parameterized.expand([("google", {"payload": True}),
                           ("abc", {"payload": False})])
    @patch('utils.get_json')
    def test_org(self, test, test_payload, patch_res):
        """ Tests 'org' class method """
        print(patch_res)
        patch_res.json.return_value = test_payload
        patch_res.json.assert_called_once()
        print(patch_res.json)
        pass
    
if __name__ == "__main__":
    unittest.main()
