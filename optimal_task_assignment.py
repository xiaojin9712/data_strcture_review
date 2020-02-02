"""
Problem description:
Assign tasks to workers so that the time it takes to complete all the tasks is minimized given a count of workers and an array where each element indicates the duration of a task.
"""

A = [6,3,2,7,5,5]

A = sorted(A)
for i in range(0, len(A)//2):
    print(A[i], A[~i])
