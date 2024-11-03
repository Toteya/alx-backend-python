#!/usr/bin/env python3
"""
module: test_utils
test utils
"""
from parameterized import parameterized
from unittest.mock import patch
from unittest import TestCase
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """
    Tests utils.access_nested_map
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Tests the utils.access_nested_map function """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Tests the utils.access_nested_map function Error conditions """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(TestCase):
    """
    Tests utils.get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """Tests utils.get_json that returns a json from a get request
        """
        mock_requests_get.return_value.json.return_value = test_payload

        self.assertEqual(get_json(test_url), test_payload)
        mock_requests_get.assert_called_once_with(test_url)
    

class TestMemoize(TestCase):
    """
    Tests utils.memoize
    """
    def test_memoize(self):
        """ Tests the utils.memoize decorator that memoizes a method
        """
        class TestClass:
            
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42
            test_obj = TestClass()
            response1 = test_obj.a_property
            response2 = test_obj.a_property
        
        self.assertEqual(response1, 42)
        self.assertEqual(response2, 42)
        mock_a_method.assert_called_once()

        


