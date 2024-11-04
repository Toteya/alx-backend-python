#!/usr/bin/env python3
"""
test_client: contains unittests for client module
"""
from client import GithubOrgClient
import fixtures
from parameterized import parameterized
from parameterized import parameterized_class
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
        fake_json = {'Key': 'DATA'}
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
            result_expected_repos = [
                "ruby-openid-apps-discovery",
                "anvil-build",
                "googletv-android-samples",
            ]
            self.assertEqual(obj.public_repos(), result_expected_repos)
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expected):
        """ Tests GithubOrgClient.has_license method
        """
        self.assertEqual(GithubOrgClient.has_license(repo, key), expected)


@parameterized_class([
    {'repos_payload': fixtures.TEST_PAYLOAD[0][0]},
    {'expected_repos': fixtures.TEST_PAYLOAD[0][1]},
    {'org_payload': fixtures.TEST_PAYLOAD[0][1][1]['owner']},
    {'apache2_repos': fixtures.TEST_PAYLOAD[0][3]}
])
class TestIntegrationGithubOrgClient(TestCase):
    """
    Integration test for client.GithubOrgClient
    """
    @classmethod
    def setUpClass(cls, get_patcher):
        """ Initialises testing paramters for the test class
        """
        # fake_json = fixtures.TEST_PAYLOAD.
        cls.get_patcher = patch('utils.requests.get')
        mock_request_get = get_patcher.start()

        # mock_request_get.return_value.json.return_value

        def request_get(url):
            """ Side effect of the mock get request to allow the given url to
            be matched to the correct payload
            """
            if url == 'https://api.github.com/orgs/google':
                return cls.org_payload
            if url == "https://api.github.com/orgs/google/repos":
                return cls.expected_repos

        get_patcher.side_effect = request_get

    @classmethod
    def tearDownClass(cls):
        """ Tears down test conditions for the class
        """
        cls.get_patcher.stop()
        pass
