from driver import Driver
from chempionship import Chempionship

chempion1 = Chempionship("Mark O'hara")
chempion2 = Chempionship("Alex Hank")
chempion3 = Chempionship("Adams Scott")


drivers = Driver()
drivers.getName(chempion1)
drivers.getName(chempion2)
drivers.getName(chempion3)
print(drivers.getDrivers())
