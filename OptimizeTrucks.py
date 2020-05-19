import csv

# Initialize lists for distances and addresses
distances = []
addresses = []

# Constants used in the file
PACKAGE_DISTANCE_INDEX = 12
A_LARGE_NUMBER = 999999

# Read the distances from the distance csv file
# Space-time complexity is O(N)
with open('WGUPSDistances.csv', encoding='utf-8-sig') as distances_csv_file:
    readDistanceCSV = csv.reader(distances_csv_file, delimiter=',')
    for distance in readDistanceCSV:
        distances.append(distance)

# Read the addresses from the address csv file
# Space-time complexity is O(N)
with open('WGUPSPackageAddresses.csv', encoding='utf-8-sig') as package_addresses_csv_file:
    readAddressCSV = csv.reader(package_addresses_csv_file, delimiter=',')
    for address in readAddressCSV:
        addresses.append(address)


# A function to get the package distances
# Space-time complexity is O(1)
def get_distance_csv():
    return distances


# A function to get the package addresses
# Space-time complexity is O(1)
def get_address_csv():
    return addresses


# Calculates the total distance travelled by a particular truck
# Space-time complexity is O(N)
def get_total_distance(truck):
    total_distance = 0
    for package in truck:
        total_distance += package[PACKAGE_DISTANCE_INDEX]
    return total_distance


# Gets the distance from the current location to the next package using the information from the distance csv file
# Space-time complexity is O(1)
def get_distance(current_package_address_id, destination_package_address_id):
    this_distance = distances[int(destination_package_address_id)][int(current_package_address_id)]
    if this_distance == '':
        this_distance = float(distances[int(current_package_address_id)][int(destination_package_address_id)])

    return this_distance


# Gets the address id from the address csv file
# Space-time complexity is O(1)
def get_address_id(package):
    for address_value in addresses:
        if package[1] == address_value[2]:
            return address_value[0]


# This is the main function for the Greedy algorithm
# The algorithm loops through all unvisited packages in a truck and selects the closest one to travel to next
# Space-time complexity is O(N^2)
def find_shortest_path(truck):
    shortest_path = []
    distance_list = []
    unvisited = truck
    total_distance = 0
    current_address_id = 0  # hub
    next_package = truck[0]
    while len(unvisited) != 0:
        min_dist = A_LARGE_NUMBER
        for package in unvisited:
            package_address_id = get_address_id(package)
            current_distance = float(get_distance(current_address_id, package_address_id))
            if current_distance < min_dist:
                min_dist = current_distance
                next_package = package
                next_package_address_id = package_address_id

        next_package[12] = min_dist  # distance_to_next_stop
        shortest_path.append(next_package)
        distance_list.append(min_dist)
        current_address_id = next_package_address_id
        unvisited.remove(next_package)
        total_distance += min_dist

    return shortest_path

