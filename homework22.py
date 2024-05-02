class Buiding:
    def __init__(self):
        self.numberOfFloors = 10
        self.buildingType = '10'

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


buiding = Buiding()

print(buiding)
