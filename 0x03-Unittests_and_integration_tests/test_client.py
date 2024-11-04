#!/usr/bin/env python3
"""
test_client: contains unittests for client module
"""
from client import GithubOrgClient
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import patch

class TestGithubOrgClient(TestCase):
    """
    Tests client.GitHubOrgClient class
    """

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ Tests org method
        """
        fake_json = {'Status': 'OK'}
        mock_get_json.return_value = fake_json
        obj = GithubOrgClient(org_name)
        url = 'https://api.github.com/orgs/{}'.format(org_name)
        self.assertEqual(obj.org, fake_json)
        mock_get_json.assert_called_once_with(url)
