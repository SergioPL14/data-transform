import json

# Opening JSON file
f = open('inputs/clean_bookings.json')

# returns JSON object as
# a dictionary
data: object = json.load(f)

# Closing file
f.close()
