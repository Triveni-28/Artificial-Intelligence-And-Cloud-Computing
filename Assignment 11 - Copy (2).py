""" Assignment of 7th march """

import math

user1 = [5, 4, 1]
user2 = [4, 5, 1]
user3 = [1, 2, 5]

def distance(a, b):
    total = 0
    for i in range(len(a)):
        total += (a[i] - b[i]) ** 2
    return math.sqrt(total)

d1 = distance(user1, user2)
d2 = distance(user1, user3)

print("Distance between User1 and User2:", d1)
print("Distance between User1 and User3:", d2)

if d1 < d2:
    print("User1 is more similar to User2")
else:
    print("User1 is more similar to User3")