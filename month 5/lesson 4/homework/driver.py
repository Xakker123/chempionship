from chempionship import Chempionship


class Driver:
    def __init__(self) -> None:
        self.drivers: list[Chempionship] = []

    def getName(self, createdriver:Chempionship):
        self.drivers.append(createdriver)
        print(createdriver)

    def getDrivers(self):
        return self.drivers




