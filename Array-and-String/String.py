# String are immutable, but we can change the variable reference to new string object

# >>> name = "vansh"
# >>> name = "bob"
# >>> print(name)
# bob

# >>> print(name[0])
# b

# >>> name[0] = 'o'
# Traceback (most recent call last):
#   File "<python-input-10>", line 1, in <module>
#     name[0] = 'o'
#     ~~~~^^^
# TypeError: 'str' object does not support item assignment
# >>>

# This is what immutable means, python do not allow mutating element inside existing string object


# time complexity for different array operations

# unlike arrays, str modification requires creating a new string object
# Append to end -> O(n)
# Popping from end -> O(n)

# Insertion , not from end -> O(n) need to shift whole arr
# Deletion , not from end -> O(n) , same need to shift whole arr
# Modifying an element -> O(1)

# Random access -> O(1)
# checking if element exists -> O(n)