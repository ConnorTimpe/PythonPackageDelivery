from HashTable import HashTable
from datetime import time

# The constants used later in the file
AVERAGE_TRUCK_SPEED = 18  # miles per hour
MINUTES_PER_HOUR = 60

# Obtains the hashtable instance from HashTable.py
hashtable = HashTable.get_instance()


# This method takes all three trucks and delivers the carried packages.
# Truck one and two are delivered first, then the first driver to return begins delivery with truck 3
# Space-time complexity is O(N)
def perform_delivery(truck_one, truck_two, truck_three):
    print("Starting delivery")

    update_delivery_status(truck_one)
    update_delivery_status(truck_two)

    start_time = time(8, 0, 0)  # start delivery at 8am

    truck_one_finish_time = deliver(truck_one, start_time)
    truck_two_finish_time = deliver(truck_two, start_time)

    current_time = find_earliest_truck_return(truck_one_finish_time, truck_two_finish_time)

    update_delivery_status(truck_three)
    deliver(truck_three, current_time)

    print("Delivery finished!")


# This method loops through all packages on the truck and updates its delivery time and status
# Space-time complexity is O(N)
def deliver(truck, start_time):
    current_time = start_time
    for package in truck:
        package[8] = start_time
        current_time = update_time(current_time, package)
        package[10] = "Delivered"  # package_delivery_status
    return current_time


# This method updates the time the next package was delivered
# Space-time complexity is O(1)
def update_time(current_time, package):
    distance_to_next_package = package[12]

    time_to_deliver = distance_to_next_package / AVERAGE_TRUCK_SPEED * MINUTES_PER_HOUR
    time_to_deliver_minutes = int(time_to_deliver % 60)
    time_to_deliver_hours = int(time_to_deliver // 60)

    updated_hour = current_time.hour + time_to_deliver_hours + ((current_time.minute + time_to_deliver_minutes) // 60)
    updated_minutes = (current_time.minute + time_to_deliver_minutes) % 60

    current_time = current_time.replace(hour=updated_hour, minute=updated_minutes)

    package[9] = current_time  # set package delivery time to current_time

    return current_time


# Updates the package delivery status to Out for Delivery
# Space-time complexity is O(N)
def update_delivery_status(truck):
    for package in truck:
        package[10] = "Out for delivery"


# Finds which driver returns to the hub first so that they can begin delivering the packages in the third truck
# Space-time complexity is O(1)
def find_earliest_truck_return(time_1, time_2):
    # Find min of time 1 and time 2
    return time_1 if time_1 < time_2 else time_2
