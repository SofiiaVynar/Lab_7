class SetManager:
    def __init__(self, aircraft_manager):
        self.aircraft_manager = aircraft_manager
        self.index = 0

    def __iter__(self):
        return self

    def __len__(self):
        return sum(len(aircraft.power_type) for aircraft in self.aircraft_manager)

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError("No index")

        for aircraft in self.aircraft_manager:
            power_types = list(aircraft.power_type)
            if index < len(power_types):
                return power_types[index]
            index -= len(power_types)

    def __next__(self):
        if self.index >= len(self):
            self.index = 0
            raise StopIteration

        value = self[self.index]
        self.index += 1
        return value
