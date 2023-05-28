from Model.aircraft import Aircraft


class Drone(Aircraft):
    power_type = {"li_po_batteries", "ni_cad_batteries"}

    def __init__(self, manufacturer, max_speed, battery_capacity, energy_consumption_per_minute):
        super().__init__(manufacturer, max_speed)
        self.battery_capacity = battery_capacity
        self.energy_consumption_per_minute = energy_consumption_per_minute

    def get_max_flying_distance(self):
        return int(self.battery_capacity / self.energy_consumption_per_minute * self.max_speed)

    def get_max_delivery_weight(self):
        return 0

    def __str__(self):
        return f"Drone(manufacturer={self.manufacturer}, max_speed={self.max_speed}, " \
               f"battery_capacity={self.battery_capacity}, " \
               f"energy_consumption_per_minute={self.energy_consumption_per_minute})"
