#JavaScript Object Notation

import json

# json.load(f):     Load JSON data from file (or file-like object)
# json.loads(s):    Load JSON data from a string
# json.dump(j, f):  Write JSON object to file (or file-like object)
# json.dumps(j):    Output JSON object as string

json_file = open("/home/belle/Development/PythonLearning/movie_1.txt", "r", encoding="utf-8")
movie = json.load(json_file)
json_file.close()

print(movie) # dictionary
print(type(movie))

print(movie["title"])
print(movie["actors"])
print(movie["release year"])

# You use the loads function if your JSON data arrives in the form of a string.
# Common in client-server applications where data is sent over the net.

value = """
    {"title": "Tron: Legacy",
    "composer": "Daft Punk",
    "release_year": 2010,
    "budget": 170000000,
    "actors": null,
    "won_oscar": false
    }"""

# Parse the JSON data from the string
tron = json.loads(value)
print(tron)

# Suppose you want to store the data about Gattaca in a database, or send it
# to a remote user.
# Use dumps method to convert dictionary into a valid JSON string.

# result is string in proper JSON format
json.dumps(movie, ensure_ascii=False) # preserves non-ASCII characters

# Let's now create a new object, convert it to JSON, and write it to a file.

movie2 = {}
movie["title"] = "Minority Report"
movie2["director"] = "Steven Spielberg"
movie2["composer"] = "John Williams"
movie2["actors"] = ["Tom Cruise", "Colin Farrell", "Samantha Morton", "Max von Sydow"]
movie2["is_awesome"] = True
movie2["budget"] = 102000000
movie2["cinematographer"] = "Janusz Kami\u0144ski"

file2 = open("/home/belle/Development/PythonLearning/movie_2.txt", "w", encoding="utf-8")
json.dump(movie2, file2, ensure_ascii=False)
file2.close()