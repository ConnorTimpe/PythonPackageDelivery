import csv
from HashTable import HashTable

# Obtains the hashtable instance from HashTable.py
hashtable = HashTable.get_instance()

# Constant used in the file for how many packages each truck can hold
TRUCK_SIZE = 16

# Initializing all three trucks
truck_one = []
truck_two = []
truck_three = []

# Initializes a list for packages that have been seen, but not yet loaded into a truck
non_priority_packages = []


# This method takes a package and determines its priority in order to load it most efficiently
# Space-time complexity is O(1)
def load_priority_trucks(package_value):
    if "truck 2" in package_value[7]:
        truck_two.append(package_value)
        package_value[11] = True
    if "Delayed" in package_value[7]:
        truck_three.append(package_value)
        package_value[11] = True
    if "Wrong address listed" in package_value[7]:
        package_value[1] = "410 S State St"  # update address
        package_value[4] = "84111"            # update zip
        truck_three.append(package_value)
        package_value[11] = True
    if not package_value[11]:
        non_priority_packages.append(package_value)


# This method loads the remaining lower priority packages.
# Packages that are required to be delivered before the end of the day are loaded into truck one or two,
#   which will be delivered before truck three
# Space-time complexity is O(N)
def load_remaining_trucks():
    for non_priority_package in non_priority_packages:
        if not non_priority_package[11] and non_priority_package[5] != "EOD" and len(truck_one) < TRUCK_SIZE:
            truck_one.append(non_priority_package)
            non_priority_package[11] = True
        if not non_priority_package[11] and len(truck_two) < TRUCK_SIZE:
            truck_two.append(non_priority_package)
            non_priority_package[11] = True
        if not non_priority_package[11] and len(truck_three) < TRUCK_SIZE:
            truck_three.append(non_priority_package)
            non_priority_package[11] = True


# Reads the package data from the package csv file, adds them to the hashtable, and begins the loading process
# Space-time complexity is O(N)
with open('WGUPSPackageData.csv', encoding='utf-8-sig') as packages_csv_file:
    readCSV = csv.reader(packages_csv_file, delimiter=',')

    for package in readCSV:
        package_id = package[0]
        package_address = package[1]
        package_city = package[2]
        package_state = package[3]
        package_zip = package[4]
        package_delivery_deadline = package[5]
        package_weight = package[6]
        package_note = package[7]
        package_delivery_start = ''  # [8]
        package_delivered_time = ''  # [9]
        package_delivery_status = 'At hub'  # [10]
        package_loaded = False  # [11]
        distance_to_next_stop = -1  # [12] This gets initialized in optimize trucks function
        full_package = [package_id, package_address, package_city, package_state,
                        package_zip, package_delivery_deadline, package_weight, package_note,
                        package_delivery_start, package_delivered_time, package_delivery_status,
                        package_loaded, distance_to_next_stop]

        key = package_id
        value = full_package

        hashtable.insert(key, value)

        load_priority_trucks(value)
    load_remaining_trucks()


# Returns the hashtable after it has been loaded with packages
# Space-time complexity is O(1)
def get_hash_table():
    return hashtable


# Returns truck one loaded, but not optimized
# Space-time complexity is O(1)
def get_truck_one():
    return truck_one


# Returns truck two loaded, but not optimized
# Space-time complexity is O(1)
def get_truck_two():
    return truck_two


# Returns truck three loaded, but not optimized
# Space-time complexity is O(1)
def get_truck_three():
    return truck_three
