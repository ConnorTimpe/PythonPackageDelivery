# Created by Connor Timpe, #000976484

from datetime import datetime
from ReadPackages import get_hash_table
from OptimizeTrucks import get_distance_csv, get_address_csv, get_total_distance, find_shortest_path
from ReadPackages import get_truck_one, get_truck_two, get_truck_three
from PerformDelivery import perform_delivery

# Obtains the hashtable instance
hashtable = get_hash_table()


# This method displays an introduction message
# Space-time complexity is O(1)
def display_intro():
    print("Welcome to the WGUPS tracking system")


# This method displays the options for the user interface
# Space-time complexity is O(1)
def display_user_options():
    print("Please enter a number:")
    print("'1' for package lookup, ")
    print("'2' to display status of all packages,")
    print("'3' to view delivery overview,")
    print("'4' to view total miles travelled, or ")
    print("'5' to exit")


# This method allows for the user to lookup a specific package by package ID
# Space-time complexity is O(1)
def lookup():
    print("Please enter a package ID: ")
    user_input = input()
    package_key_value = hashtable.lookup(user_input)
    package = package_key_value[1]

    print("Package id: ", package[0])
    print("Package address: ", package[1])
    print("Package city: ", package[2])
    print("Package zip code: ", package[4])
    print("Package weight: ", package[6])
    print("Package delivery deadline: ", package[5])
    print("Package delivery status: ", package[10])
    print("Package began delivery at: ", package[8], " and was delivered at: ", package[9])
    print()


# This method displays the status of all packages at the specified time
# Space-time complexity is O(N)
def display_all():
    at_hub = []
    out_for_delivery = []
    delivered = []

    print("Please enter a time in the format HH:MM to view package statuses at that time: ")
    user_input = input()
    display_time = datetime.strptime(user_input, '%H:%M')
    print("Displaying status of all packages at ", display_time.time())

    all_packages = hashtable.get_all()

    for package in all_packages:
        package_delivery_start = datetime.strptime(str(package[8]), '%H:%M:%S')
        package_delivered_time = datetime.strptime(str(package[9]), '%H:%M:%S')

        if package_delivery_start > display_time:
            at_hub.append(package[0])
        elif package_delivered_time > display_time:
            out_for_delivery.append(package[0])
        else:
            delivered.append(package[0])

    print("Package statuses at ", display_time.time(), ":")
    print("At hub: ", at_hub)
    print("Out for delivery: ", out_for_delivery)
    print("Delivered: ", delivered)
    print()


# This method displays the delivery information of each package
# Space-time complexity is O(N)
def view_end_of_day_info(truck_one_optimized, truck_two_optimized, truck_three_optimized):
    print("Truck 1: ")
    for package in truck_one_optimized:
        print("Package", package[0], "began delivery at: ", package[8], "and was delivered at: ", package[9])
    print()

    print("Truck 2: ")
    for package in truck_two_optimized:
        print("Package", package[0], "began delivery at: ", package[8], "and was delivered at: ", package[9])
    print()

    print("Truck 3: ")
    for package in truck_three_optimized:
        print("Package", package[0], "began delivery at: ", package[8], "and was delivered at: ", package[9])
    print()


# This method shows the total miles travelled
# Space-time complexity is O(N)
def view_miles_travelled(truck_one_optimized, truck_two_optimized, truck_three_optimized):
    truck_one_total_distance = get_total_distance(truck_one_optimized)
    truck_two_total_distance = get_total_distance(truck_two_optimized)
    truck_three_total_distance = get_total_distance(truck_three_optimized)
    total_distance = truck_one_total_distance + truck_two_total_distance + truck_three_total_distance

    print("Truck one total distance travelled: ", "{:.2f}".format(truck_one_total_distance), "miles")
    print("Truck two total distance travelled: ", "{:.2f}".format(truck_two_total_distance), "miles")
    print("Truck three total distance travelled: ", "{:.2f}".format(truck_three_total_distance), "miles")
    print("Total distance of all trucks: ", "{:.2f}".format(total_distance), "miles")
    print()


class Main:
    display_intro()

    # Retrieves the loaded trucks from ReadPackages.py
    truck_one = get_truck_one()
    truck_two = get_truck_two()
    truck_three = get_truck_three()

    # Optimizes the delivery order of each truck by using the greedy algorithm in OptimizeTrucks.py
    truck_one_optimized = find_shortest_path(truck_one)
    truck_two_optimized = find_shortest_path(truck_two)
    truck_three_optimized = find_shortest_path(truck_three)

    # Begins delivery of the packages while updating time and delivery statuses
    perform_delivery(truck_one_optimized, truck_two_optimized, truck_three_optimized)

    # This is the loop that allows for user interaction
    # Space-time complexity is O(N)
    running = True
    while running:
        try:
            display_user_options()
            user_input = input()
            if user_input == '1':
                lookup()
            elif user_input == '2':
                display_all()
            elif user_input == '3':
                view_end_of_day_info(truck_one_optimized, truck_two_optimized, truck_three_optimized)
            elif user_input == '4':
                view_miles_travelled(truck_one_optimized, truck_two_optimized, truck_three_optimized)
            elif user_input == '5':
                print("exiting...")
                running = False
            else:
                print("invalid input.")
                running = False
        except ValueError as e:
            print(e)

