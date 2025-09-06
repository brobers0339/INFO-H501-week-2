import numpy as np


# update/add code below ...

def ways(cents, coin_types=[1, 5]):
    ways_total = 0 #counts number of ways to make change
    list_ways = [] #list to store different ways to make change
    coin_types = sorted(coin_types, reverse=True) #sort coin types in descending order so we start with the largest coin value
    for nickels in range(cents//5 + 1): #iterate through range of 0 to max number of nickels that can fit into cents
        pennies = cents - (nickels * 5) #calculate remaining cents after using nickels at the current iteration
        if pennies >= 0: #only count valid combinations where pennies is non-negative
            ways_total += 1 #add one to the valid combinations count
        list_ways.append((nickels, pennies)) #list represents the yield function instead of using it due to the return needed at the end of the function
    #adds print statements to show the different ways to make change
    print("The following are ways to make change for", cents, "cents using nickels and pennies:")
    for way in list_ways: 
        print(f'{way[0]} nickels and {way[1]} pennies') #print out the different ways to make change
    return ways_total #returns the total number of ways to make change

'''
#optional variation for any coin types

def ways(cents, coin_types=[1, 5]):
    list_ways = [] #list to store different ways to make change
    sorted_coin_types = sorted(coin_types, reverse=True) #make sure coin values are sorted highest to lowest
    ways_total = 0 #counts number of ways to make change
    length_coin_types = len(sorted_coin_types) #finds number of different coin values given in the function instance
    for highest_coin in range(cents // sorted_coin_types[0] + 1): #starts first loop with the highest coin value
        if length_coin_types == 2: #if there are only two coin types, we know that the next coin value is 1 so we can calculate the remaining cents as pennies for all iterations of the highest coin value
            pennies = cents - (highest_coin * sorted_coin_types[0]) #calculate remaining cents after using the highest coin value at the current iteration
            if pennies >= 0: #only count valid combinations where pennies is non-negative
                ways_total += 1 #add one to the valid combinations count
                list_ways.append((highest_coin, pennies)) #list represents the yield function instead of using it due to the return needed at the end of the function
        else: #if there are more than two coin types, we need to loop through the next highest coin value
            for second_highest_coin in range(cents // sorted_coin_types[1] + 1): #loop through the second highest coin value (meaning all coin values are given 25, 10, and 5), no other possible coin values can occur after this loop
                if length_coin_types == 3: #if there are three coin types, we know that the next coin value is 1 so we can calculate the remaining cents as pennies for all iterations of the highest and second highest coin values
                    pennies = cents - (highest_coin * sorted_coin_types[0]) - (second_highest_coin * sorted_coin_types[1]) #calculate remaining cents after using the highest and second highest coin values at the current iteration
                    if pennies >= 0: #only count valid combinations where pennies is non-negative
                        ways_total += 1 #add one to the valid combinations count
                        list_ways.append((highest_coin, second_highest_coin, pennies)) #list represents the yield function instead of using it due to the return needed at the end of the function
                else: #if there are more than three coin types, we need to loop through the next highest coin value
                    for third_highest_coin in range(cents // sorted_coin_types[2] + 1): #loop through the third highest coin value (meaning all coin values are given 25, 10, 5, and 1), no other possible coin values can occur after this loop
                        pennies = cents - (highest_coin * sorted_coin_types[0]) - (second_highest_coin * sorted_coin_types[1]) - (third_highest_coin * sorted_coin_types[2]) #calculate remaining cents after using the highest, second highest, and third highest coin values at the current iteration
                        if pennies >= 0: #only count valid combinations where pennies is non-negative
                            ways_total += 1 #add one to the valid combinations count
                            list_ways.append((highest_coin, second_highest_coin, third_highest_coin, pennies)) #add the current iteration of coins to make change to list, this list replaces the yield function due to the return needed at the end of the function
    #use print statements to display the different ways to make change
    print("The following are the ways to make change for", cents, "cents using the coin types:", sorted_coin_types)
    for way in list_ways: 
        for coin in range(len(way)):
            print(f'{way[coin]} of {sorted_coin_types[coin]} cent coins', end=', ' if coin < len(way)-1 else '\n')
    return ways_total #returns the total number of ways to make change
'''

def lowest_score(names, scores):
    lowest_score_name = names[np.argmin(scores)]
    return lowest_score_name

def sort_names(names, scores):
    sorted_list = sorted(zip(scores, names), reverse=True)
    sorted_name = []
    for name in range(len(sorted_list)):
        sorted_name.append(sorted_list[name][1])
    return sorted_name
