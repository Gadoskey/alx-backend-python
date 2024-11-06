#!/usr/bin/env python3

'''
  Author: Gadoskey
'''
import unittest
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient.org method."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("utils.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        # Set up the mock return value for get_json
        expected_response = {"name": org_name, "repos_url"
                             : f"https://api.github.com/orgs/{org_name}/repos"}
        mock_get_json.return_value = expected_response

        # Initialize GithubOrgClient and call the org method
        client = GithubOrgClient(org_name)
        result = client.org

        # Assertions
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected_response)
