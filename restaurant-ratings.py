# your code goes here

import sys

filename = sys.argv[1]

def list_ratings(filename):
    """
    """

    restaurant_data = {}

    with open(filename) as scores:

        for line in scores:
            line = line.rstrip()
            line = line.split(":")

            restaurant = line[0]
            rating = int(line[1])

            restaurant_data[restaurant] = rating

    user_restaurant = raw_input("What restaurant would you like to rate? > ")
    user_rating = int(raw_input("Please rate %s on a scale of 1 to 5: " % user_restaurant)) 

    restaurant_data[user_restaurant] = user_rating   

    for restaurant, rating in sorted(restaurant_data.items()):
        print "%s is rated at %s." % (restaurant, rating) 


list_ratings(filename)