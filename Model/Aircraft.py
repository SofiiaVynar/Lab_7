from abc import ABC, abstractmethod


class Aircraft(ABC):
    def __init__(self, manufacturer=None, max_speed=0):
        self.manufacturer = manufacturer
        self.max_speed = max_speed

    @abstractmethod
    def get_max_flying_distance(self):
        pass

    @abstractmethod
    def get_max_delivery_weight(self):
        pass

    def __str__(self):
        return f"Aircraft: Manufacturer={self.manufacturer}, Max Speed={self.max_speed}"
