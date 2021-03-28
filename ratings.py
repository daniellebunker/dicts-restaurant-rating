"""Restaurant rating lister."""

def restaurant_ratings():

    restaurant_file = open('scores.txt')
    restaurant_names = {}
    #key is restaurasnt name and value is rating

    for line in restaurant_file:
        line = line.rstrip()
        line = line.split(":")
        name = line[0]
        rating = line[1]

        # print(rating)
        # print(name)

        if name:
            restaurant_names[name] = int(rating)
        
    print(restaurant_names)
        
    return restaurant_names

restaurant_ratings()
