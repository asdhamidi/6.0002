###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import string
punc = "#$%&'()*+, -./:;<=>?@[]^_`{|}~\n"

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    f = open(filename, "r") # Opening file.
    data = {} # Initializing empty dictionary.
    while True:
        # Read One Line At A Attempt
        txt = f.readline().replace("\n", "") 

        # If an empty line is detected, end the loop.
        if txt == "":
            break
        cowData = txt.split(",") # Turning csv to a list.

        # Putting data in the dictionary.
        # Adding data of list to the dictionary. 0th index has name, 1st index has weight.
        data[cowData[0]] = int(cowData[1]) 

    f.close()
    return data



# Problem 2
def greedy_cow_transport(cows,limit=10):
    # Copy dicitionary to not mutate the original dictionary.
    cowData = cows.copy()
    # This returns a list of tuples in a sorted form. 
    # 0th index of each tuple has name. 1st index has weight.
    # I couldn't find a better way. Suggestions needed.
    cowData = sorted(cowData.items(), key=lambda x: x[1], reverse=True)

    # Initializing lists for total trips, current trips, and current trip capacity.
    trips = []
    currentTrip = []
    currentShipCapacity = 0

    # Running loop till there are no elements in the dict.
    while len(cowData):
        for cow in cowData:
            if cow[1] + currentShipCapacity <= limit:
                currentTrip.append(cow[0])
                currentShipCapacity += cow[1]
                cowData.remove(cow)
            else:
                continue
        
        # Adding each trip to total trips,
        # and changing values of current ship and capacity to default after each turn.
        trips.append(currentTrip)
        currentTrip = []
        currentShipCapacity = 0
    
    return trips

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
    continueSignal = False
    
    # Assuming worst case would be each cow being transported individually.
    trips = len(cows) 
    # This will store the best combination at the end to be returned.
    bestChoice = [] 
    for partition in get_partitions(cows.copy()):
        for sets in partition: # Going through each element of the sublists.
            sumOfElements = 0
            # Adding weights for each sublists.
            for element in sets:
                sumOfElements += cows[element]
            
            # If any sublist of a list breaks the weight limit, we move onto the next list.
            if sumOfElements > limit: 
                continueSignal = True
                break
        
        # If continueSignal is true, we just move to the next list, without comparing,
        # with best choice.
        if continueSignal:
            continueSignal = False
            continue
        
        # Comparing number of trips taken by current combo with the best combo.
        if len(partition) < trips:
            trips = len(partition)
            bestChoice = partition
    
    return bestChoice



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
    cowData = load_cows("ps1_cow_data.txt")

    start = time.time()
    greedy = greedy_cow_transport(cowData)
    end = time.time()
    print("Solution by Greedy Algorithm : ", greedy)
    print ("Time taken by Greedy Algorithm : ",(end - start))

    start = time.time()
    bruteForce = brute_force_cow_transport(cowData)
    end = time.time()
    print("Solution by Brute Force Algorithm : ", bruteForce)
    print ("Time taken by Brute Force Algorithm : ",(end - start)) 

compare_cow_transport_algorithms()