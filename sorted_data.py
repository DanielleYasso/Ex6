

filename = open("scores.txt")

####################
# Using an empty list

# rest_listing = []

# for line in filename:
#     rest_data = line.strip()
#     rest_listing.append(rest_data)

# rest_listing.sort()

# for pair in rest_listing: 
#     name, rating = pair.split(":")
#     print "Restaurant %s is rated at %s" %(name, rating) 


###################
#Using an empty dictionary

rest_dict = {}
rating_dict = {}

for line in filename: 
    rest_data = line.strip()
    name, rating = rest_data.split(":")
    rest_dict[name] = rating
    rating_dict.setdefault(rating, []).append(name)

print "Numerically sorted ratings:"
for rating, restaurants in sorted(rating_dict.items()):
    for restaurant in sorted(restaurants): # format and alphabetize within rating
        print "Restaurant %s is rated at %s" % (restaurant, rating) 

print "***********************"
print "Alphabetized restaurants:"
for restaurant, rating in sorted(rest_dict.items()):
    print "Restaurant %s is rated at %s" % (restaurant, rating) 


# filtered_list = filter(lambda x: x % 2 == 0, number_list)