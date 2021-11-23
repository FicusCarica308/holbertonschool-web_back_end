#!/usr/bin/env python3
""" More unittests """
import unittest
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Tests for all tGithubOrgClient class methods """

    @parameterized.expand([("google", {"payload": True}),
                           ("abc", {"payload": False})])
    @patch('client.get_json')
    def test_org(self, test, test_payload, patch):
        """ Tests 'org' class method """
        # patch setup
        patch.return_value = test_payload
        
        client = GithubOrgClient(test)
        self.assertEqual(client.org, test_payload)
        patch.assert_called_once()

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, patch):
        """ Tests '_public_repos_url' class method that
        has been turned into a property by 'memoize' """
        patch.return_value = {"repos_url": "test_value"}
        client = GithubOrgClient('abc')
        result = client._public_repos_url
        self.assertEqual(result, "test_value")

if __name__ == "__main__":
    unittest.main()
