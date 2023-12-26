class Chempionship:
    def __init__(self, createdriver) -> None:
        self._createdriver = createdriver

    @property
    def createDriver(self):
        return self._createdriver

    def __str__(self) -> str:
        return f"Driver name -> {self._createdriver}"