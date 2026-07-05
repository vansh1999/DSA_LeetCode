# Input: str = "aabbbcddddde"

# Output: a - 2, b - 3, c - 1, d - 5, e - 1


str = "aabbbcddddde"


# using hashmap

new_str = {}


for i in str:

    if i not in new_str:
        new_str[i] = 1
    elif i in new_str:
        new_str[i] = new_str[i] + 1
        

print(new_str)

# Brute force

new_str = []

for i in str:

    if i not in new_str:
        count = 0
        for j in str:
            if j == i:
                count = count + 1
    
        print(i , '-' , count)
        new_str.append(i)
        


        

