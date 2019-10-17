# This problem was asked by Snapchat.
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
# find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
#since 0-50 and 60-150 has no overlapping, they can share the same room
#30-75 overlaps 0-50 and 60-75 so it needs another room
#another example
#[(120, 160), (30, 75), (0, 50), (60, 150)]
#write a function to test for overlapping

#if no overlapping, can share 1 room
#idea
#using a heap
#always keep the end time of the room at the top of the min heap
#check the new time that is next
#if the start time of the next class is greater than the end time at the top of the heap
#then this class can use that room
#so we need to pop from the heap and push the new end time into the heap

#if the start time of the next class is less than the end time at the top of the heap
#then the next class cannot use that room, so a new room much be created

#in order for this logic to work, the room times much be sorted
from heapq import heappush, heappop
def minRooms(times):
    sortedTimes = sorted(times)
    heap = []
    for interval in sortedTimes:
        start = interval[0]
        end = interval[1]
        #if there is a heap and the top of the heap < start time
        #we can pop that value
        if heap and heap[0] < start:
            heappop(heap)
        #push the end time in
        heappush(heap, end)
        print(heap)
    return len(heap)
a = [(120, 160), (30, 75), (0, 50), (60, 150), (170,180),(155,175),(0,50)]
print(sorted(a))

print(minRooms(a))