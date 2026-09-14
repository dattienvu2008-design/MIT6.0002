###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    sep_list = []
    return_dict = {}
    with open(filename) as file:
        list_string = file.read().splitlines()
        for string in list_string:
            sep_list.append(string.split(sep=','))
    for cow in sep_list:
        return_dict[cow[0]] = int(cow[1])
    return return_dict
    

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cow_list = []
    trip_index = 0
    weight_left = 0
    return_list = []
    
    #Input: Dictionary of cow
    #Output: List of cow sorted from high to low weight
    for i in cows.keys():
        cow_list.append([i,cows.get(i)])
    cow_list.sort(key = lambda n:n[1], reverse=True)
    
    #print(cow_list) #debug
    removed_cow = []
    
    #Arrange cow to trips
    while len(cow_list) > 0:
        return_list.append([])
        weight_left = limit
        for cow in cow_list:
            if cow[1] <= weight_left:
                return_list[trip_index].append(cow[0])
                weight_left -= cow[1]
                removed_cow.append(cow)
                #print('Debug:', cow, return_list,weight_left,cow_list, '\n', sep='\n') #This is for debugging
        for removed in removed_cow:
            cow_list.remove(removed)
        removed_cow = []
        trip_index += 1
    return return_list

def greedy_cow_transport_2(cows, limit = 10):
    cow_list = []
    return_list = []
    for i in cows.keys():
        cow_list.append([i,cows[i]])
    cow_list.sort(key=lambda n:n[1],reverse=True)
    
    #grouping cows by weight
    weight_dict = {}    
    for cow in cow_list:
        if cow[1] not in weight_dict:
            weight_dict.update({cow[1]:[cow[0]]})
        elif cow[1] in weight_dict:
            weight_dict[cow[1]].append(cow[0])
    
    weight_left = 0
    trip_index = 0
    remaining_cows = len(cow_list)
    unique_weights = sorted(weight_dict.keys(), reverse=True)
    
    #Arrange cows to trips
    while remaining_cows > 0:
        return_list.append([])
        weight_left = limit
        for weight in unique_weights:
            while True:
                if weight <= weight_left and len(weight_dict[weight]) > 0:
                    return_list[trip_index].append(weight_dict[weight].pop())
                    weight_left -= weight
                    remaining_cows -= 1
                else:
                    break
            
        trip_index += 1
    return return_list
    
            
  
            
#These comments below are for debugging          
#print(greedy_cow_transport_2(load_cows('ps1_cow_data.txt')))
#print(greedy_cow_transport(load_cows('ps1_cow_data.txt')))


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    minimum_trips = None
    trip = 0
    return_list = []
    track = True
            
    current_total_weight = 0
    
    for partition in get_partitions(cows):
        for trip in partition:
            for cow in trip:
                current_total_weight += cows[cow]
                if current_total_weight > limit:
                    track = False
                    break
            current_total_weight = 0
            if track == False:
                break
        if track == True and (minimum_trips == None or len(partition) < minimum_trips):
            minimum_trips = len(partition)
            return_list = partition
        track = True
    return return_list

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start = time.time()
    print(brute_force_cow_transport(load_cows('ps1_cow_data.txt')))
    end = time.time()
    print(end-start)
    
    start = time.time()
    print(greedy_cow_transport(load_cows('ps1_cow_data.txt')))
    end = time.time()
    print(end-start)
    
    start = time.time()
    print(greedy_cow_transport_2(load_cows('ps1_cow_data.txt')))
    end = time.time()
    print(end-start)

compare_cow_transport_algorithms()

    




'''
#greedy_func_draft
temp_weight = 0
temp = 0
cow_list = []
weight_list = []
return_transport_list = []
for i in cows.keys():
    cow_list.append([i,cows[i]])
cow_list.sort(key=lambda n:n[1],reverse=True)
for i in cow_list:
    if i[1] != temp_weight:
        temp_weight = i[1]
        weight_list.append([i[1]])
        weight_list[temp].append(i[0])
        temp += 1
    elif i[1] == temp_weight:
        weight_list[temp-1].append(i[0])
#print(weight_list)  #uncomment to view list
print(cow_list)
'''
