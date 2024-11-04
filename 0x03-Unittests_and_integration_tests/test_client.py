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
        fake_payload = {
            'login': 'google',
            'url': 'https://api.github.com/orgs/google',
            'repos_url': 'https://api.github.com/orgs/google/repos'
        }

        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = fake_payload
            obj = GithubOrgClient('google')
            self.assertEqual(obj._public_repos_url, fake_payload['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Tests the public_repos method
        """
        fake_payload = [
            {
                "id": 3248507,
                "node_id": "MDEwOlJlcG9zaXRvcnkzMjQ4NTA3",
                "name": "ruby-openid-apps-discovery",
            },
            {
                "id": 3975462,
                "node_id": "MDEwOlJlcG9zaXRvcnkzOTc1NDYy",
                "name": "anvil-build",
            },
            {
                "id": 5072378,
                "node_id": "MDEwOlJlcG9zaXRvcnk1MDcyMzc4",
                "name": "googletv-android-samples",
            }
        ]
        mock_get_json.return_value = fake_payload
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            obj = GithubOrgClient('google')
            fake_payload_repos = [
                "ruby-openid-apps-discovery",
                "anvil-build",
                "googletv-android-samples",
            ]
            self.assertEqual(obj.public_repos(), fake_payload_repos)
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()
