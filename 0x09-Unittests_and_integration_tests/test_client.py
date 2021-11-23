#!/usr/bin/env python3
""" More unittests """
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Tests for all tGithubOrgClient class methods """

    @parameterized.expand([("google", {"payload": True}),
                           ("abc", {"payload": False})])
    @patch('client.get_json')
    def test_org(self, test, test_payload, patch_res):
        """ Tests 'org' class method """
        # patch setup
        patch_res.return_value = test_payload
        
        client = GithubOrgClient(test)
        self.assertEqual(client.org, test_payload)
        patch_res.assert_called_once()


if __name__ == "__main__":
    unittest.main()
