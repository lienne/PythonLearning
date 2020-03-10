# Dictionaries are maps! Key-Value pairs of data.

# Let's make a social platform called FriendFace.
# FriendFace post
# user_id = 209
# message = "D5 E5 C5 C4 G4"
# datetime = "20230215T124231Z"
# location = (44.590533, -104.715556)

# Inputs are called keys,
# outputs are called values.
post = {"user_id":209, "message":"D5 E5 C5 C4 G4", "datetime":"20230215T124231Z", "location":(44.590533, -104.715556)}
print(type(post))
print(post)

post2 = dict(message="SS Cotopaxi", language="English")
print(type(post2))
print(post2)

# Add additional pieces of data by using brackets
post2["user_id"] = 209
post2["datetime"] = "19771116T093001Z"
print(post2)

# Accessing Data in a Dictionary
print(post2['message'])
# print(post2['location']) # throws KeyError bc key does not exist in dict

if 'location' in post2:
    print(post2['location'])
else:
    print("The post does not contain a location value.")

try:
    print(post2['location'])
except KeyError:
    print("The post does not contain a location value.")

# get method
loc = post2.get('location', None)
print(loc)

# Iterating through all key-value pairs
print("Iterating through all key-value pairs of post:")
for key in post.keys():
    value = post[key]
    print(key, "=", value)

# Another way of iterating
print("Another way of iterating: the items() method")
for key, value in post.items():
    print(key, "=", value)

# Removing data from ditc: pop, popitem, clear