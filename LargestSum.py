# This problem was asked by Airbnb.
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
# Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, 
# since we pick 2, 6, and 5. 
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

#the idea
#we can either take the current value we are looking at or skip it
#case 1 taking the value
#if we take the value, then it must be greater than the previous value, 
#if we add the 2nd previous value and it is greater than it

#case 2 skip it
#if we skip the value, then the value previous is greater than the addition of the current+previous2

#we keep track of the largest sum so far in the current list input
#at a certain index, we can replace it with the largest sum so far
#if it meets certain conditions
def sumNonAdjacent(numList):
    #first make sure the first 2 values in numList follows a certain order
    #that is either we take the value or skip it
    if numList[0] > numList[1]:
        #we know if the first value is greater than the 2nd value, we should replace the 2nd value with the first
        numList[1] = numList[0]
    #else it is in the correct order, in that case we skip the first value
    
    #now we look at the list starting from 2
    for index in range(2,len(numList)):
        #looking at the next value,
        #should we take it or skip it?
        #if the current number + the highest sum(previous 2) greater than the sum that is previous?
        if numList[index]+numList[index - 2] > numList[index-1]:
            #if it is we take it
            numList[index] = numList[index]+numList[index - 2]
        else:
            #else we can just skip it, so carry over then previous sum
            numList[index] = numList[index - 1]
    print(numList)
    #once we finish, the last value of the inputList should hold the max sum of non-adjacent numbers
    return numList[-1]


numList = [2, 4, 6, 2, 5]
print(sumNonAdjacent(numList))

numList = [5, 1, 1, 5]
print(sumNonAdjacent(numList))