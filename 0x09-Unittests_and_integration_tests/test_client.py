#!/usr/bin/env python3
""" More unittests """
import unittest
from unittest import mock
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([({"license": {"key": "my_license"}},
                            "my_license", True),
                           ({"license": {"key": "other_license"}},
                            "my_license", False)])
    def test_has_license(self, repo, license_key, expected):
        """ tests has_license class method """
        client = GithubOrgClient('abc')
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(("org_payload", "repos_payload", "expected_repos",
                      "apache2_repos"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration tests """
    @classmethod
    def setUpClass(cls):
        """ Class method for setup """
        custom_payload = [cls.org_payload,
                          cls.repos_payload,
                          cls.org_payload,
                          cls.repos_payload]
        cls.get_patcher = patch('requests.get')
        cls.patcher = cls.get_patcher.start()
        cls.patcher.return_value.json.side_effect = custom_payload
        
    def test_public_repos(self):
        """ Test method """
        client = GithubOrgClient('google')
        result = client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """ Test method """
        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos("apache-2.0"),
                         self.apache2_repos)

    @classmethod
    def tearDownClass(cls):
        """ Class method for tearDown """
        cls.patcher.stop()


if __name__ == "__main__":
    unittest.main()
