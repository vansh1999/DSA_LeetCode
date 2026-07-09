# M1 Traditional method
# Prereq / Given array is sorted

# time O(log n)
# space O(1)

def binary_search(arr , target):

    n = len(arr)
    l , r = 0 , n-1

    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target:
            print(mid)
            return True
        elif arr[mid] < target:
            l=mid+1
        else:
            r=mid-1
    
    # if R crossed with L, RL -> not possible and means, elements not found hence false -> find ony when l<=r
    return False

print(binary_search([1,2,3,4,7] , 7))

# M2 - Over under T and F, based on condition

# M3 - Recursion

# time 
# Space 