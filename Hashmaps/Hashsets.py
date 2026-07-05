s = set()

# add items into the set -> O(1)

s.add(1)
s.add(2)
s.add(3)

print(s)

# Lookup if item in set -> O(1)

if 1 in s:
    print(True)

if 4 not in s:
    print(True)

# remove item from set -> O(1)
s.remove(1)

print(s)


# set construction -> O(S) -> s is the length of the string

str  = "aaaabbbbeeeeooooi"
sett = set(str)

print(sett)


# loop in a set -> O(n)
for i in s:
    print(i)

