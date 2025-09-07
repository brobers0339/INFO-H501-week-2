import numpy as np


# update/add code below ...
def ways(cents, coin_types=[1, 5]):

    #initalizes variables to keep track of total ways to make change, a list of the different ways to make change, and sorts the coin types in descending order
    
    ways_total = 0
    list_ways = [] 
    coin_types = sorted(coin_types, reverse=True) 

    #the following for loop iterates through the range of 0 to the maximum number of nickels that can fit into the given cents
    #in each iteration, it calculates the remaining cents after using the current number of nickels in that iteration, which is also the amount of pennies needed to make change
    #assuming the number of pennies is non-negative, we can add one to the total number of ways to make change and add the current combination of nickels and pennies to the list of ways
    
    for nickels in range(cents//5 + 1): 
        pennies = cents - (nickels * 5)
        if pennies >= 0: 
            ways_total += 1 
            list_ways.append((nickels, pennies))

    #adds print statements to show the different ways to make change for user readability
    #finally returns the total number of ways to make change
    
    print("The following are ways to make change for", cents, "cents using nickels and pennies:")
    for way in list_ways: 
        print(f'{way[0]} nickels and {way[1]} pennies') 
    return ways_total 


#optional variation for any coin types

def ways(cents, coin_types=[1, 5]):

    #initializes variables to keep track of total ways to make change, a list of different ways to make change, and sorts the coin types in descending order
    #initializes a variable to keep track of the number of different coin types given in the function instance
    #the list of ways is a filler to replace the yield function due to the return needed at the end of the function that will still allow us to store and display the different ways to make change

    list_ways = [] 
    sorted_coin_types = sorted(coin_types, reverse=True)
    ways_total = 0
    length_coin_types = len(sorted_coin_types)

    #the following for loops iterate through the range of 0 to the maximum number of each coin type that can fit into the given cents
    #in each iteration, it determines if there are any remaining coin types that need to be looped through
    #if there are no remaining coin types, it calculates the remaining cents after using the current number of highest value coins in that iteration, which is also the amount of pennies needed to make change
    #assuming the number of pennies is non-negative, we can add one to the total number and add the current combination of coins to the list of ways to make change
    
    #if there are remaining coin types, it loops through the next highest coin value and repeats the process until all coin types have been looped through
    #the innermost loop calculates the remaining cents after using the current number of highest, second highest, and third highest coin values (if applicable) in that iteration, which is also the amount of pennies needed to make change
    #assuming the number of pennies is non-negative, we can add one to the total number and add the current combination of coins to the list of ways to make change

    for highest_coin in range(cents // sorted_coin_types[0] + 1):
        if length_coin_types == 2:
            pennies = cents - (highest_coin * sorted_coin_types[0])
            if pennies >= 0:
                ways_total += 1
                list_ways.append((highest_coin, pennies))
        else: 
            for second_highest_coin in range(cents // sorted_coin_types[1] + 1):
                if length_coin_types == 3:
                    pennies = cents - (highest_coin * sorted_coin_types[0]) - (second_highest_coin * sorted_coin_types[1]) 
                    if pennies >= 0:
                        ways_total += 1 
                        list_ways.append((highest_coin, second_highest_coin, pennies)) 
                else:
                    for third_highest_coin in range(cents // sorted_coin_types[2] + 1):
                        pennies = cents - (highest_coin * sorted_coin_types[0]) - (second_highest_coin * sorted_coin_types[1]) - (third_highest_coin * sorted_coin_types[2])
                        if pennies >= 0: 
                            ways_total += 1 
                            list_ways.append((highest_coin, second_highest_coin, third_highest_coin, pennies))

    #finally, we use print statements to show all of the different ways to make change for user readability
    #first, we have to iterate through the list of ways to make change, and then iterate through each coin type in that way to display the number of each coin type used in that way to make change
    #finally, we return the total number of ways to make change

    print("The following are the ways to make change for", cents, "cents using the coin types:", sorted_coin_types)
    for way in list_ways: 
        for coin in range(len(way)):
            print(f'{way[coin]} of {sorted_coin_types[coin]} cent coins', end=', ' if coin < len(way)-1 else '\n')
    return ways_total


#this function, lowest score, takes in two numpy arrays: one containing names and the other containing corresponding scores
#it finds the lowest score in the scores array using np.min and finds the index of that lowest score using np.argmin, all of which is printed out for user readability
#it then returns the name found at the index of the lowest score in the scores array (which corresponds to the name of the person with the lowest score)

def lowest_score(names, scores):
    print("The lowest score is", np.min(scores), "from:", names[np.argmin(scores)]) 
    return names[np.argmin(scores)]

#the sort_names function takes in two numpy arrays: one containing names and the other containing corresponding scores
#it zips the two arrays together into a list of tuples, where each tuple contains a score and its corresponding name
#it then sorts this list of tuples in descending order based on the score values
#next, it iterates through the sorted list of scores and names and appends just the names to the new list in order of descending score values
#it prints out the sorted list of names and scores for user readability and returns just the sorted names

def sort_names(names, scores):
    sorted_list = sorted(zip(scores, names), reverse=True) 
    sorted_name = [] 
    for name in range(len(sorted_list)): 
        sorted_name.append(sorted_list[name][1])
    print("Names sorted by descending scores:\n", sorted_list)
    return sorted_name
