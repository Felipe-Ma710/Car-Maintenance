import json


class Car:
    def __init__(self, make, model, year, owner, oil_changes=None, fuel_ups=None):
        self.make = make
        self.model = model
        self.year = year
        self.owner = owner
        self.oil_changes = oil_changes if oil_changes is not None else []
        self.fuel_ups = fuel_ups if fuel_ups is not None else []

    def display_name(self):
        return f"{self.year} {self.make} {self.model} - {self.owner}"

    def display_oil_changes(self):
        if not self.oil_changes:
            print("No oil changes to display.")
        else:
            print("\nOil Changes:")
            for i, oil_change in enumerate(self.oil_changes):
                print(f"Oil Change #{i + 1}")
                print(f"Date: {oil_change['date']}")
                print(f"Type: {oil_change['oil_type']}")
                print(f"Quantity: {oil_change['oil_quantity']}")
                print(f"Miles: {oil_change['oil_miles']}")
                print(f"Notes: {oil_change['additional_notes']}")
                print()

    def add_oil_change(self, date, oil_type, oil_quantity, oil_miles, additional_notes=None):
        oil_change_info = {
            'date': date,
            'oil_type': oil_type,
            'oil_quantity': oil_quantity,
            'oil_miles': oil_miles,
            'additional_notes': additional_notes
        }
        self.oil_changes.append(oil_change_info)

    def add_transmission_oil_change

class CarManagement:
    def __init__(self):
        self.cars = load_cars("cars.json")

    def save_cars(self):
        cars_data = [
            {
                "make": car.make,
                "model": car.model,
                "year": car.year,
                "owner": car.owner,
                "oil_changes": car.oil_changes,
                "fuel_ups": car.fuel_ups
            }
            for car in self.cars
        ]
        with open("cars.json", 'w') as f:
            json.dump(cars_data, f, indent=4)

    def show_features_menu(self, car):
        while True:
            print("\nCar Features Menu")
            print("-------------------")
            print(f"Managing: {car.display_name()}")
            print("1. Add Oil Change")
            print("2. Add Fuel Up")
            print("3. Return to Main Menu")
            print("6. Print Oil Changes")

            choice = input("\nChoose an option: ")
            if choice == '1':
                date = input("Enter the date of the oil change (YYYY-MM-DD): ")
                oil_type = input("Enter the type of oil: ")
                oil_quantity = input("Enter the quantity of oil: ")
                oil_miles = input("Enter the miles at the time of the oil change: ")
                additional_notes = input("Enter any additional notes: ")

                car.add_oil_change(date, oil_type, oil_quantity, oil_miles, additional_notes)

                print(f"Added oil change.")
                self.save_cars()

            elif choice == '2':
                fuel_up_date = input("Enter the date of the fuel up (YYYY-MM-DD): ")
                car.fuel_ups.append(fuel_up_date)
                print(f"Added fuel-up on {fuel_up_date}.")
                self.save_cars()

            elif choice == '3':
                return
            elif choice == '6':
                car.display_oil_changes()
            else:
                print("Invalid choice. Please select again.")


def load_cars(filename):
    try:
        with open(filename, 'r') as f:
            cars_data = json.load(f)
        return [Car(
            make=car_data['make'],
            model=car_data['model'],
            year=car_data['year'],
            owner=car_data['owner'],
            oil_changes=car_data.get('oil_changes', []),
            fuel_ups=car_data.get('fuel_ups', [])
        ) for car_data in cars_data]
    except FileNotFoundError:
        return []


def main():
    manager = CarManagement()

    while True:
        print("\nCar Management Menu")
        print("-------------------")
        print("1. List Cars")
        print("2. Add Car")
        print("3. Select Car")
        print("4. Remove Car")
        print("5. Exit")

        choice = input("\nChoose an option: ")
        if choice == '1':
            if not manager.cars:
                print("No cars to list.")
            else:
                print("\nCars:")
                for i, car in enumerate(manager.cars, 1):
                    print(f"{i}. {car.display_name()}")

        elif choice == '2':
            make = input("Enter the make of the car: ")
            model = input("Enter the model of the car: ")
            year = input("Enter the year of the car: ")
            owner = input("Enter the owner of the car: ")

            new_car = Car(make=make, model=model, year=year, owner=owner)
            manager.cars.append(new_car)
            manager.save_cars()

        elif choice == '3':
            if not manager.cars:
                print("No cars to select.")
            else:
                print("\nCars:")
                for i, car in enumerate(manager.cars, 1):
                    print(f"{i}. {car.display_name()}")

                try:
                    car_number = int(input("Enter the number of the car to select: ")) - 1
                    if 0 <= car_number < len(manager.cars):
                        manager.show_features_menu(manager.cars[car_number])
                    else:
                        print("Invalid car number.")

                except ValueError:
                    print("Invalid number.")

        elif choice == '4':
            if not manager.cars:
                print("No cars to remove.")
            else:
                print("Select a Car to Remove:")
                for i, car in enumerate(manager.cars, 1):
                    print(f"{i}. {car.display_name()}")

                try:
                    car_number = int(input("Enter the number of the car to remove: ")) - 1
                    if 0 <= car_number < len(manager.cars):
                        removed_car = manager.cars.pop(car_number)
                        manager.save_cars()
                        print("Car removed successfully.")
                    else:
                        print("Invalid car number.")

                except ValueError:
                    print("Invalid number.")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    main()
