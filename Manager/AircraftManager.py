from typing import List


class AircraftManager:
    def __init__(self):
        self.aircraft_list = []

    def add_aircraft(self, aircraft):
        self.aircraft_list.append(aircraft)

    def find_with_max_speed_more_than(self, speed):
        return list(filter(lambda a: a.max_speed > speed, self.aircraft_list))

    def find_with_manufacturer(self, manufacturer):
        return list(filter(lambda a: a.manufacturer == manufacturer, self.aircraft_list))
