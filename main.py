from Helicopter import Helicopter


def main():
    helicopters = [
        Helicopter(),
        Helicopter("Fly-High", 500, 1000, 100, 100),
        Helicopter.getInstance(),
        Helicopter.getInstance()
    ]

    for helicopter in helicopters:
        helicopter.takeOff()
        helicopter.ascend(300)
        helicopter.descend(200)
        helicopter.refuel(50)

        print("Id:", helicopter.id)
        print("Model:", helicopter.model)
        print("Max altitude:", helicopter.max_altitude)
        print("Current altitude:", helicopter.current_altitude)
        print("Fuel capacity:", helicopter.fuel_capacity)
        print("Current fuel:", helicopter.current_fuel)
        print("\n")


if __name__ == "__main__":
    main()
