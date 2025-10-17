import unittest
import csv
from datetime import datetime
from decimal import Decimal


class TestCsvData(unittest.TestCase):

    def setUp(self):
        """Load CSV data and skip header row"""
        with open("export-token-0xa1290d69c65a6fe4df752f95823fae25cb99e5a7.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            self.rows = [row for row in reader if any(cell.strip() for cell in row)]

        # Skip header
        self.rows = self.rows[1:]

    def test_tx_hash_format(self):
        """First column should start with 0x and have length 66"""
        for i, row in enumerate(self.rows, start=1):
            tx_hash = row[0]
            self.assertTrue(tx_hash.startswith("0x"), f"Row {i}: tx_hash doesn't start with 0x")
            self.assertEqual(len(tx_hash), 66, f"Row {i}: tx_hash length is not 66")

    def test_timestamps_between_2025_and_now(self):
        """Each timestamp must be >= 2025-01-01 and <= current time"""
        min_date = datetime(2025, 1, 1)
        now = datetime.now()
        for i, row in enumerate(self.rows, start=1):
            ts = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
            self.assertGreaterEqual(
                ts,
                min_date,
                f"Row {i}: timestamp {row[3]} is before 2025-01-01"
            )
            self.assertLessEqual(
                ts,
                now,
                f"Row {i}: timestamp {row[3]} is in the future"
            )

if __name__ == '__main__':
    unittest.main()
