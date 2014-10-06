rest_listing = []

filename = open("scores.txt")

for line in filename:
    rest_data = line.strip()
    rest_listing.append(rest_data)

rest_listing.sort()

for pair in rest_listing: 
    name, rating = pair.split(":")
    print "Restaurant %s is rated at %s" %(name, rating) 




