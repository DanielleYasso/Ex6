

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

print "***********************"
print "Numerically sorted ratings:"
for rating, restaurants in sorted(rating_dict.items()):
    for restaurant in sorted(restaurants): # alphabetize within rating
        print "Restaurant %s is rated at %s" % (restaurant, rating) 

print "***********************"
print "Numerically sorted using 2nd tuple item:"
for restaurant, rating in sorted(rest_dict.items(), key=lambda x: x[1]):
    print "Restaurant %s is rated at %s" % (restaurant, rating) 

print "***********************"
print "Alphabetized restaurants:"
for restaurant, rating in sorted(rest_dict.items()):
    print "Restaurant %s is rated at %s" % (restaurant, rating) 
