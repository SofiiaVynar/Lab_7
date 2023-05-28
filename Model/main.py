import functools

from Manager.aircraft_manager import AircraftManager
from Manager.set_manager import SetManager
from Model.drone import Drone
from Model.glider import Glider
from Model.helicopter import Helicopter
from Model.plane import Plane


def main():
    manager = AircraftManager()

    manager.add_aircraft(Helicopter("Fly-High", 500, "Tiny", 400, 700, 400, 300))
    manager.add_aircraft(Helicopter("Fly-High", 300, "Tin", 200, 500, 600, 400))
    manager.add_aircraft(Drone("Sin", 70, 2000, 10))
    manager.add_aircraft(Drone("Son", 60, 1500, 8))
    manager.add_aircraft(Plane("Vinnie", 600, 20, 10000))
    manager.add_aircraft(Plane("Vinna", 100, 10, 5000))
    manager.add_aircraft(Glider("PiN", 100, 150, 40))
    manager.add_aircraft(Glider("PiNi", 70, 100, 25))

    print("Aircraft:")
    for aircraft in manager.aircraft_list:
        print(aircraft)

    aircraft_with_speed_more_than = manager.find_with_max_speed_more_than(400)
    print("\n")
    print("Aircraft with max speed more than 400:")
    for aircraft in aircraft_with_speed_more_than:
        print(aircraft)

    searched_manufacturer = manager.find_with_manufacturer("PiN")
    print("\n")
    print("Searched manufacturer:")
    for aircraft in searched_manufacturer:
        print(aircraft)

    print("\n")
    print("Max delivery weight list:")
    print(manager.get_max_delivery_weight_list())

    print("\n")
    print("List with numbers:")
    for aircraft in manager.list_with_numbers():
        print(aircraft)

    print("\n")
    print("Method results:")
    for aircraft, result in manager.method_results():
        print(f"{aircraft}: {result}")

    print("\nObjects with int:")
    for aircraft in manager.aircraft_list:
        int_objects = aircraft.get_type(int)
        print(f"{aircraft.__class__.__name__}: {int_objects}")

    print("\n")
    battery_presence = lambda aircraft: isinstance(aircraft, Drone)
    battery_conditions_result = manager.check_battery_presence(battery_presence)
    print("All have batteries:", battery_conditions_result["all"])
    print("Any have batteries:", battery_conditions_result["any"])

    set_manager = SetManager(manager)
    print("\nAll power types:")
    for power_type in set_manager:
        print(power_type)

if __name__ == "__main__":
    main()
