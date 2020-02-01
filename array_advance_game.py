'''
Description:
Is it possible to advance from the start of the given array, which contains non-negative integers, to the last element given that the maximum you can advance from a position is based on the value of the array at the index you are currently present on?

Leetcode: 55. Jump Game
'''

def array_advance(A):
    # Set furthest to 0
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_idx


A = [3,3,1,0,2,0,1]
print(array_advance(A))
B = [3,2,0,0,2,0,1]
print(array_advance(B))
C = [1,1,1,0]
print(array_advance(C))
