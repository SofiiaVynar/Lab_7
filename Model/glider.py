from Model.aircraft import Aircraft


class Glider(Aircraft):
    power_type = {"electric_engine", "jet_engine"}

    def __init__(self, manufacturer, max_speed, acceleration_speed, wing_chord_length):
        super().__init__(manufacturer, max_speed)
        self.acceleration_speed = acceleration_speed
        self.wing_chord_length = wing_chord_length

    def get_max_flying_distance(self):
        return self.acceleration_speed * self.wing_chord_length * 15

    def get_max_delivery_weight(self):
        return 0

    def __str__(self):
        return f"Glider(manufacturer={self.manufacturer}, max_speed={self.max_speed}, " \
               f"acceleration_speed={self.acceleration_speed}, wing_chord_length={self.wing_chord_length})"
