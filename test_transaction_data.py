import unittest
import csv
from datetime import datetime, timezone
from decimal import Decimal


class TestCsvData(unittest.TestCase):

    def setUp(self):
        """Load CSV data and skip header row"""
        with open("export-0xa1290d69c65a6fe4df752f95823fae25cb99e5a7.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            self.rows = [row for row in reader if any(cell.strip() for cell in row)]

        # Skip header
        self.rows = self.rows[1:]
        unix_ts_list = []
        for i, row in enumerate(self.rows):
            unix_ts = row[2]
            unix_ts_list.append(int(unix_ts))

        self.ts_min = min(unix_ts_list)
        self.ts_max = max(unix_ts_list)
        self.ts_min_time = datetime.fromtimestamp(self.ts_min, tz=timezone.utc)
        print(self.ts_min)
        print(self.ts_max)
        #self.ts_max_time = datetime.fromtimestamp(self.ts_max, tz=timezone.utc)


    def test_tx_hash_format(self):
        """First column should start with 0x and have length 66"""
        for i, row in enumerate(self.rows):
            tx_hash = row[0]
            self.assertTrue(tx_hash.startswith("0x"), f"Row {i}: tx_hash doesn't start with 0x: {tx_hash}")
            self.assertEqual(66, len(tx_hash), f"Row {i}: tx_hash length is not 66")

    def test_timestamps_between_2025_and_now(self):
        """Each timestamp must be >= 2025-01-01 and <= current time"""
        min_date_2025 = datetime(2025, 1, 1, tzinfo=timezone.utc)
        now = datetime.now(timezone.utc)

        for i, row in enumerate(self.rows):
            ts = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
            print("ts  from datetime = " + str(ts))
            unix_ts = int(ts.timestamp())
            print("unix_ts datetime to timestamp = " + str(unix_ts))

            #unix_ts = datetime.fromtimestamp(int(row[2]), tz=timezone.utc)

            self.assertGreaterEqual(
                unix_ts,
                self.ts_min,
                f"Row {i}: timestamp {row[3]} is not greater or equal {self.ts_min}"
            )
            self.assertLessEqual(
                unix_ts,
                self.ts_max,
                f"Row {i}: timestamp {row[3]} is not less or equal {self.ts_max}"
            )
            self.assertGreaterEqual(
                ts,
                min_date_2025,
                f"Row {i}: timestamp {row[3]} is before 2025-01-01"
            )
            self.assertLessEqual(
                ts,
                now,
                f"Row {i}: timestamp {row[3]} is in the future"
            )

if __name__ == '__main__':
    unittest.main()
