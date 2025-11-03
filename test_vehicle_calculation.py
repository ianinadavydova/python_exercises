import unittest

from vehicle_calculation import VehicleCalculation


class TestBasicFunctions(unittest.TestCase):
    """Class for testing vehicles methods"""

    def test_from_csv_data(self):
        data = []

        with open("cars.csv","r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                values = line.split(";")
                #print(values)
                values_float = [float(i) for i in values]

                value1 = values_float[0]
                value2 = values_float[1]
                value3 = values_float[2]
                value4 = values_float[3]

                value_expected = values_float[4]

                test_calculation = VehicleCalculation(value1, value2,  value3, value4)

                self.assertEqual(value_expected, test_calculation.distance())

if __name__ == '__main__':
    unittest.main()
