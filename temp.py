import json
import csv

def is_valid_date(date):
    try:
        year, month, day = map(int, date.split('-'))
        if year < 1900 or year > 3000:
            return False
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        return True
    except ValueError:
        return False
def load_history(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def export_to_csv(mpg_history, maintenance_history):
    export_type = input("Which logs would you like to export? Enter 'fuel' for fuel-up entries or 'oil' for oil "
                        "change logs: ")
    filename = ""

    if export_type.lower() == 'fuel':
        filename = "fuel_logs.csv"
        keys = mpg_history[0].keys() if mpg_history else ['date', 'miles', 'gallons', 'mpg']
        with open(filename, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(mpg_history)
    elif export_type.lower() == 'oil':
        filename = "oil_logs.csv"
        keys = maintenance_history[0].keys() if maintenance_history else ['date', 'oil_quantity', 'oil_type', 'additional_notes']
        with open(filename, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(maintenance_history)
    else:
        print("Invalid input. Returning to main menu.")
        return

    print(f"{filename} exported successfully.")


def save_history(filename, history):
    with open(filename, 'w') as f:
        json.dump(history, f)


def calculate_mpg(miles_driven, gallons_filled):
    return miles_driven / gallons_filled


def print_fuel_up_entries(history):
    if not history:
        print("No fuel-up entries to show.")
        return

    total_mpg = 0
    num_entries = len(history)

    print("\nPast Fuel-Up Entries:")
    for i, entry in enumerate(history, 1):
        print(
            f"{i}. {entry['date']}: {entry['miles_driven']} miles, {entry['gallons_filled']} gallons, MPG: {entry['mpg']}")
        total_mpg += entry['mpg']

    average_mpg = total_mpg / num_entries
    print(f"\nAverage MPG across all entries: {average_mpg:.2f}")


def print_maintenance_logs(maintenance_history):
    if not maintenance_history:
        print("\nNo maintenance logs found.")
        return

    print("\nMaintenance Logs:")
    print("------------------")

    for i, entry in enumerate(maintenance_history, 1):
        print(f"Entry {i}:")
        print(f"  Date: {entry['date']}")
        print(f"  Oil Quantity: {entry['oil_quantity']} quarts")
        print(f"  Oil Type: {entry['oil_type']}")
        print(f"  Additional Notes: {entry['additional_notes']}")
        print()


def print_instructions():
    print("\nInstructions for Using MPG Calculator")
    print("-------------------------------------")
    print("1. After each fuel-up, reset your car's trip odometer to zero.")
    print("2. During your next fuel-up, note the trip odometer reading before resetting. This is your 'miles driven'.")
    print("3. Record the number of gallons filled during this fuel-up as 'gallons filled'.")
    print("4. Open the application and go to the 'MPG Calculator' option.")
    print("5. Enter the current date, miles driven, and gallons filled.")
    print("6. The application will calculate and display your MPG.")
    print("7. All entries will be saved for future reference.")
    print("8. You can view past fuel-up entries by choosing the 'Show Past Fuel-Up Entries' option.")
    print("9. If you have any questions, revisit this instruction set.")

def load_maintenance(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_maintenance(filename, maintenance):
    with open(filename, 'w') as f:
        json.dump(maintenance, f, indent=4)

def log_oil_change(maintenance_history):
    date = input("Enter the date of the oil change (YYYY-MM-DD): ")

    if not is_valid_date(date):
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return

    try:
        oil_quantity = float(input("Enter the amount of oil added (in quarts): "))
        if oil_quantity <= 0:
            print("Oil quantity should be a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    oil_type = input("Enter the type of oil used: ")
    additional_notes = input("Enter any additional notes (optional): ")

    maintenance_entry = {
        'date': date,
        'oil_quantity': oil_quantity,
        'oil_type': oil_type,
        'additional_notes': additional_notes
    }

    maintenance_history.append(maintenance_entry)
    print("Oil change logged successfully.")


class Car:
    def __init__(self, name):
        self.name = name


def save_cars(filename, cars):
    cars_data = [{"name": car.name} for car in cars]
    with open(filename, 'w') as f:
        json.dump(cars_data, f, indent=4)
def load_cars(filename):
    try:
        with open(filename, 'r') as f:
            cars_data = json.load(f)
            return [Car(name=car_data['name']) for car_data in cars_data]
    except FileNotFoundError:
        return []
def main():
    cars = load_cars("cars.json")
    while True:
        print("Car Management Menu")
        print("-------------------")
        print("1. List Cars")
        print("2. Add Car")
        print("3. Remove Car")
        print("4. Exit")

        choice = input("\nChoose an option: ")
        if choice == '1':
            for i, car in enumerate(cars, 1):
                print(f"{i}. {car.name}")
        elif choice == '2':
            new_car_name = input("Enter the name of the car: ")
            new_car = Car(name=new_car_name)
            cars.append(new_car)
            save_cars("cars.json", cars)

    #fuel_filename = "mpg_history.json"
    #maintenance_filename = "maintenance_history.json"

    # mpg_history = load_history(fuel_filename)
    # maintenance_history = load_maintenance(maintenance_filename)
    #
    # while True:
    #     print("\nMenu")
    #     print("-----")
    #     print("1. MPG Calculator")
    #     print("2. Show Past Fuel-Up Entries")
    #     print("3. Instructions")
    #     print("4. Log Oil Change")
    #     print("5. Show Past Oil Change Entries")
    #     print("6. Export Fuel-Up Entries Data to CSV")
    #     print("7. Exit")
    #
    #     choice = input("\nChoose an option: ")
    #
    #     if choice == '1':
    #         date = input("\nEnter the date (YYYY-MM-DD): ")
    #
    #         if not is_valid_date(date):
    #             print("Invalid date. Please try again.")
    #             continue
    #
    #         try:
    #             miles_driven = float(input("Enter miles driven since last fuel-up: "))
    #             gallons_filled = float(input("Enter gallons filled: "))
    #
    #             if miles_driven <= 0 or gallons_filled <= 0:
    #                 print("Miles driven and gallons filled should be positive.")
    #                 continue
    #
    #             mpg = calculate_mpg(miles_driven, gallons_filled)
    #             print(f"You achieved {mpg:.2f} MPG on this fuel-up.\n")
    #             mpg_history.append({
    #                 "date": date,
    #                 "miles_driven": miles_driven,
    #                 "gallons_filled": gallons_filled,
    #                 "mpg": round(mpg, 2)
    #             })
    #             save_history(fuel_filename, mpg_history)
    #         except ValueError:
    #             print("Please enter valid numbers for miles driven and gallons filled.")
    #
    #     elif choice == '2':
    #         print_fuel_up_entries(mpg_history)
    #
    #     elif choice == '3':
    #         print_instructions()
    #
    #     elif choice == '5':
    #         print_maintenance_logs(maintenance_history)
    #
    #     elif choice == '4':
    #         log_oil_change(maintenance_history)
    #         save_maintenance(maintenance_filename, maintenance_history)
    #
    #     elif choice == '6':
    #         export_to_csv(mpg_history, maintenance_history)
    #         #export_filename = input("Enter the name of the CSV file to export to (e.g., 'my_data.csv'): ")
    #
    #         #export_to_csv(export_filename, mpg_history)
    #
    #     elif choice == '7':
    #
    #         print("Exiting. Goodbye!")
    #
    #         break
    #
    #     else:
    #         print("Invalid choice. Please try again.")
    #

if __name__ == "__main__":
    main()
