class VehicleCalculation:
    def __init__(self, v1, v2, s, t):
        self.v1 = v1
        self.v2 = v2
        self.s = s
        self.t = t

    def distance(self):
        return round((self.v1 * self.t + self.v2 * self.t + self.s), 4)


calculation1 = VehicleCalculation(90, 110, 65, 3)
calculation1.distance()

calculation2 = VehicleCalculation(65.5, 90.4, 20.9, 1.5)
calculation2.distance()

calculation3 = VehicleCalculation(70, 85.6, 32.6, 2)
calculation3.distance()