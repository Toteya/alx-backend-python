#!/usr/bin/env python3
"""
test_client: contains unittests for client module
"""
from client import GithubOrgClient
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import patch
from unittest.mock import PropertyMock


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

    def test_public_repos_url(self):
        """ Tests the public_repos_url method
        """
        fake_json = {'repos_url': 'OK'}
        # mock_org.return_value = fake_json

        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = fake_json
            obj = GithubOrgClient('org_name')
            self.assertEqual(obj._public_repos_url, 'OK')
