
class AircraftManager:
    def __init__(self):
        self.aircraft_list = []

    def add_aircraft(self, aircraft):
        self.aircraft_list.append(aircraft)

    def find_with_max_speed_more_than(self, speed):
        return list(filter(lambda a: a.max_speed > speed, self.aircraft_list))

    def find_with_manufacturer(self, manufacturer):
        return list(filter(lambda a: a.manufacturer == manufacturer, self.aircraft_list))

    def __len__(self):
        return len(self.aircraft_list)

    def __getitem__(self, index):
        return self.aircraft_list[index]

    def __iter__(self):
        return iter(self.aircraft_list)

    def get_max_delivery_weight_list(self):
        return [aircraft.get_max_delivery_weight() for aircraft in self.aircraft_list]

    def list_with_numbers(self):
        return [f"{index + 1}: {aircraft}" for index, aircraft in enumerate(self.aircraft_list)]

    def method_results(self):
        return [(aircraft, aircraft.get_max_delivery_weight()) for aircraft in self.aircraft_list]

    def check_battery_presence(self, battery_presence):
        return {"all": all(battery_presence(aircraft) for aircraft in self.aircraft_list),
                "any": any(battery_presence(aircraft) for aircraft in self.aircraft_list)}