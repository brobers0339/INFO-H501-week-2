import numpy as np


# update/add code below ...

def ways(cents, coin_types=[1, 5]):
    ways_total = 0 #counts number of ways to make change
    coin_types = sorted(coin_types, reverse=True) #sort coin types in descending order so we start with the largest coin value
    for nickels in range(cents//5 + 1): #iterate through range of 0 to max number of nickels that can fit into cents
        pennies = cents - (nickels * 5) #calculate remaining cents after using nickels at the current iteration
        if pennies >= 0: #only count valid combinations where pennies is non-negative
            ways_total += 1 #add one to the valid combinations count
    yield ways_total #returns the total number of ways to make change

def lowest_score(names, scores):
    lowest_score_name = names[np.argmin(scores)]
    return lowest_score_name

def sort_names(names, scores):
    sorted_list = sorted(zip(scores, names), reverse=True)
    return sorted_list