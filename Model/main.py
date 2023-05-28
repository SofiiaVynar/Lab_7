from Manager.AircraftManager import AircraftManager
from Model.Drone import Drone
from Model.Glider import Glider
from Model.Helicopter import Helicopter
from Model.Plane import Plane


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


if __name__ == "__main__":
    main()