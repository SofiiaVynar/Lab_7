class Helicopter:
    """
    Helicopter class.
    -----------------
    Attributes:
    model : str
        helicopter model.
    current_altitude: int
        Current altitude of helicopter.
    max_altitude : int
        Max altitude of Helicopter.
    fuel_capacity : int
        Fuel capacity of helicopter.
    current_fuel : int
        Current fuel of helicopter.
    id : int
        Helicopter id.
    -------------------
    Methods:
    takeOff():
        lifts the helicopter to a height of 100 meters.
    ascend(altitude):
        raises the helicopter to the specified height.
    descend(altitude):
        lowers the helicopter to the specified height
        and provides for checking whether the height does not become negative.
        If the height should become negative,
        it should be assumed that the flight height should become equal to 0.
    refuel(fuel):
        adds the specified amount of fuel to the helicopter and provides a tank overflow check.
    """
    __instance = None

    def __init__(self, model=None, current_altitude=0, max_altitude=0, fuel_capacity=0, current_fuel=0, ID=100):
        self.ID = ID
        self.model = model
        self.current_altitude = current_altitude
        self.max_altitude = max_altitude
        self.fuel_capacity = fuel_capacity
        self.current_fuel = current_fuel

    def takeOff(self):
        self.current_altitude += 100

    def ascend(self, altitude):
        if self.current_altitude + altitude <= self.max_altitude:
            self.current_altitude += altitude
        else:
            self.current_altitude = self.max_altitude

    def descend(self, altitude):
        if self.current_altitude - altitude < 0:
            self.current_altitude = 0
        else:
            self.current_altitude -= altitude

    def refuel(self, fuel):
        if self.current_fuel + fuel <= self.fuel_capacity:
            self.current_fuel += fuel
        else:
            self.current_fuel = self.fuel_capacity

    @staticmethod
    def get_instance():
        if Helicopter.__instance is None:
            Helicopter.__instance = Helicopter()
        return Helicopter.__instance