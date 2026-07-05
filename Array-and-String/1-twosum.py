nums = [4,7,11,15,2]

target = 9

# main things is never compare i , j with 1, always have j + 1 ahead of i for comparision => so j in range (i+1 , len(nums))

for i in range(len(nums)):
    # print("i" , i)
    for j in range(i+1 , len(nums)):
        print("j" , j)
        if nums[i] + nums[j] == target:
            return [i,j]
         
     
    # i = i + 1

# Time complexity = O(n^2)


# Can we do 
# O(n)



