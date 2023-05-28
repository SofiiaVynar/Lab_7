from Model.Aircraft import Aircraft


class Plane(Aircraft):
    half_weight = 1.6

    def __init__(self, manufacturer, max_speed, wings_span, weight):
        super().__init__(manufacturer, max_speed)
        self.wings_span = wings_span
        self.weight = weight

    def get_max_flying_distance(self):
        return int((self.max_speed ** 2) / 20 * self.wings_span)

    def get_max_delivery_weight(self):
        return int(self.half_weight * self.weight)

    def __str__(self):
        return f"Plane(manufacturer={self.manufacturer}, max_speed={self.max_speed}, " \
               f"wings_span={self.wings_span}, weight={self.weight})"
