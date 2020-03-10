# Classes in Python

class User:
    pass

# Instance of the User class / an object
user1 = User()
user1.first_name = "Dave"
user1.last_name = "Bowman"
print(user1.first_name, user1.last_name)

first_name = "Arthur"
last_name = "Clarke"
print(first_name, last_name) # not attached to our User object

user2 = User()
user2.first_name = "Frank"
user2.last_name = "Poole"
print(user2.first_name, user2.last_name)

user1.age = 37
user2.favorite_book = "2001: A Space Odyssey"
print(user1.age)
# print(user2.age) # Attribute error

# Class Features
# - Methods
# - Initialization
# - Help text

# init method: initialization (the constructor)

print(40*"=")

import datetime

class User2:
    """A member of FriendFace. For now we are only storing their name and 
    birthday. But soon we will store an uncomfortable amount of user
    information."""


    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday # yyymmdd

        # Extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Return age of user in years."""
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd) # Date of birth
        age_in_days = (today - dob).days # timedelta object
        age_in_years = age_in_days / 365
        return int(age_in_years)


user = User2("Dave Bowman", "19710315")
print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)

print(user.age())
