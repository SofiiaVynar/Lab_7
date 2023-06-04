from Exception.exception import TakeOffException
from Manager.logger import logged
from Model.aircraft import Aircraft


class Helicopter(Aircraft):
    power_type = {"piston_powered", "turbine_powered"}

    def __init__(self, manufacturer, max_speed, model=None,
                 current_altitude=0, max_altitude=0, fuel_capacity=0,
                 current_fuel=0, id=100):
        super().__init__(manufacturer, max_speed)
        self.ID = id
        self.model = model
        self.current_altitude = current_altitude
        self.max_altitude = max_altitude
        self.fuel_capacity = fuel_capacity
        self.current_fuel = current_fuel
        self.ID = id

    @logged(TakeOffException, "file")
    def take_off(self):
        if self.current_altitude > self.max_altitude:
            raise TakeOffException("Can't take off, because of the current_altitude")
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

    def get_max_flying_distance(self):
        return int(self.current_fuel / self.fuel_capacity * self.max_speed)

    def get_max_delivery_weight(self):
        return 0

    def __str__(self):
        return f"Helicopter(id={self.ID},manufacturer={self.manufacturer}, max_speed={self.max_speed}, " \
               f"model={self.model}, current_altitude={self.current_altitude}, " \
               f"max_altitude={self.max_altitude}, fuel_capacity={self.fuel_capacity}, " \
               f"current_fuel={self.current_fuel})"
