# Hashmaps -> Dictionaries in python

# In Python:

# * HashSet → implemented using set -> stores only unique values eg - {1,2,3}
# * HashMap → implemented using dict -> stores key:value pairs - > ages = {"age": 26}

# Both use a hash table internally, which gives average O(1) time for insert(add), search(lookup), and delete(remove)

# note -> we can have dict inside a dict (hashmap inside the hashmap) , given key is not dict / hashmap. immutable like str and int is allowed !

# hashmap / dict in python 

d = {

    'a' : 1,
    'b' : 2,
    'c' : 3

}

print(d)

# add a key value pair in dict -> O(1)

d['d'] = 4

print(d)

# value corresponding to key in a dict -> O(1)
print(d['a'])

# lookup / search -> O(1)

if 'd' in d:
    print(True)

# Loop over the key:value pairs in dict -> O(N)

for k , v in d.items():
    print(f'key {k} : val {v}')

# used f- string

# remove from a dict -> O(1)

del d['d']

print(d)

