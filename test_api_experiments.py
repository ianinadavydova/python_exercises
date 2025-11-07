import os
import unittest

import requests
from nose2.tools import params


def get_test_data_versions():
    versions = []
    x = 0.1
    for i in range(30):
        versions.append(round(x, 1))
        x += 0.1
    return versions

class TestCsvData(unittest.TestCase):

    def setUp(self):
        token = os.getenv("TOKEN")
        self.headers = {
            "accept": "application/json",
            #"Authorization": "Token DG5rv4GfXMCK06EH9Bjq0WbAr2LhTmGtUha3rWaMYzbJKnsr"
            "Authorization": f"Token {token}",
        }


    #@params(*get_test_data_versions())
    def test_versions_statues(self):
        list_test_data = get_test_data_versions()
        list_error = []
        list_ok = []

        for i in range(30):
            url = f"https://api.eco-movement.com/api/ocpi/cpo/{list_test_data[i]}/locations?limit=10&offset=0"
            response = requests.get(url, headers=self.headers)
            try:
                self.assertEqual(200, response.status_code)
                self.assertEqual(1000, response.json()["status_code"], url)
                list_ok.append(list_test_data[i])
            except AssertionError:
                list_error.append(list_test_data[i])

        print(list_error)
        print(list_ok)
