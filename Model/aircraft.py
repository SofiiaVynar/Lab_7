from abc import ABC, abstractmethod


class Aircraft(ABC):
    power_type = set()

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

    def get_type(self, type):
        return {key: value for key, value in self.__dict__.items()
                if isinstance(value, type)}

    def __iter__(self):
        return iter(self.power_type)
