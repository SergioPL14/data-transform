import json

# Opening JSON file
f = open('C:/Users/SergioPina/Documents/git/data-transform/datatransform/repository/clean_bookings.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Closing file
f.close()
