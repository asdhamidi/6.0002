###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================
# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # Checking if current combination of egg_weights and target weight are in memo.
    # Returning the value, if found.
    if (egg_weights, target_weight) in memo:
        return memo[(egg_weights, target_weight)]

    if len(egg_weights) == 0 or target_weight <= 0: # Base Case.
        return 0
    elif egg_weights[-1] > target_weight: # Removing element if beyond limit.
        return dp_make_weight(egg_weights[:-1], target_weight, memo)
    else:
        # withCurrent will hold value of branch with egg of -1th index include. 
        # withoutCurrent will hold value of branch without egg of -1th index include. 

        withCurrent = (1 + dp_make_weight(egg_weights, (target_weight - egg_weights[-1]), memo))
        withoutCurrent = dp_make_weight(egg_weights[:-1], target_weight, memo)


        if withoutCurrent == 0: # Base Case for comparision.
            # Adding current combo of egg weights and target weight to dicitonary with the better choice.
            memo[(egg_weights, target_weight)] = withCurrent 
            return withCurrent
        elif withCurrent < withoutCurrent : # Returning better of two results.
            memo[(egg_weights, target_weight)] = withCurrent
            return withCurrent
        else:
            memo[(egg_weights, target_weight)] = withoutCurrent
            return withoutCurrent


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()