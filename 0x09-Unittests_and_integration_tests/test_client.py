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

    @patch('client.get_json')
    def test_public_repos(self, patch_org):
        """ Tests the public_repos class method """
        patch_org.return_value = [{"name": "test/url"}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as patch_public_repos:
            patch_public_repos.return_value = 'test/url'
            client = GithubOrgClient('abc')
            result = client.public_repos()
            self.assertEqual(result[0], 'test/url')
            patch_public_repos.assert_called_once()
            patch_org.assert_called_once()
         

if __name__ == "__main__":
    unittest.main()
