# CarFinder program

# List of authorized vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

def print_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.3")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. Exit")

def print_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

def search_vehicle():
    vehicle_name = input("\nPlease Enter the full Vehicle name: ").strip()
    # Checking if the vehicle is in the list
    if vehicle_name in AllowedVehiclesList:
        print(f"\n{vehicle_name} is an authorized vehicle")
    else:
        print(f"\n{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again")

def add_vehicle():
    new_vehicle = input("\nPlease Enter the full Vehicle name you would like to add: ").strip()
    AllowedVehiclesList.append(new_vehicle)
    print(f"\nYou have added \"{new_vehicle}\" as an authorized vehicle")

def main():
    while True:
        print_menu()
        user_input = input("Enter your choice: ")

        if user_input == "1":
            print_vehicles()
        elif user_input == "2":
            search_vehicle()
        elif user_input == "3":
            add_vehicle()
        elif user_input == "4":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid input, please try again.")

# Running the program
if __name__ == "__main__":
    main()