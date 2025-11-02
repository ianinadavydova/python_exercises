import json
import unittest
from datetime import datetime, timezone
from json import JSONDecoder, decoder


class TestCsvData(unittest.TestCase):

    def setUp(self):

        with open("cus_tran.json", mode="r", encoding="utf-8") as f:
            data = json.load(f)


        self.customers = data["customers"]
        self.amounts = []
        self.dates = []
        self.transactions = []

        for customer in self.customers:
            transactions = customer["transactions"]
            for transaction in transactions:
                self.transactions.append(transaction)
                self.amounts.append(transaction["amount"])
                transaction_data =  transaction["date"]
                transaction_data_from_string = datetime.strptime(transaction_data, "%Y-%m-%d").replace(tzinfo=timezone.utc)
                timestamp_transaction_data = int(transaction_data_from_string.timestamp())
                self.dates.append(timestamp_transaction_data)


    def test_transactions_validity(self):
        for customer in self.customers:
            transactions = customer["transactions"]
            for transaction in transactions:
                expected_keys = ["date", "amount"]
                keys = transaction.keys()
                for key in keys:
                    self.assertIn(key, expected_keys)















