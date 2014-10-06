

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

for line in filename: 
    rest_data = line.strip()
    name, rating = rest_data.split(":")
    rest_dict[name] = rating

key_list = rest_dict.keys()

key_list.sort()

for key in key_list:
    print "Restaurant %s is rated at %s" %(key, rest_dict[key]) 



