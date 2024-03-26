class Buiding:
    def __init__(self):
        self.numberOfFloors = 10
        self.buildingType = '11'

    def __eq__(self):
        return self.numberOfFloors == self.buildingType

buiding = Buiding()
print(buiding.__eq__())
