# This problem was asked by Stripe.
# Given an array of integers, 
# find the first missing positive integer in linear time and constant space. 
# In other words, 
# find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.
# For example, 
# the input [3, 4, -1, 1] should give 2. 
# The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

#Idea
#look at the current number
#does it match up with it's index?
#try to match up values to their index

def Find2ndSmallestInt(numList):
    index = 0
    while index < len(numList):
        #if the current value at index is not equal to the value of it's index
        #if it's a negative number, ignore it, assume that it is in the right place
        #if it's a number that is out of bound of the list index, assume it's at the right place
        if numList[index] != index and numList[index] < len(numList) and numList[index] >= 0:
            #make the swap
            print("Current value at index is ", numList[index])
            tempVal = numList[index]
            #make sure the numbers are not the same
            #if it is the same, dont make the swap, skip it
            if numList[index] != numList[tempVal]:
                print("swaping ", numList[index])
                numList[index] = numList[tempVal]
                numList[tempVal] = tempVal
                print(numList)
            else:
                #skips the value
                print("same value at the swapping index, skip this")
                index += 1
        else:
            #skips the value
            index += 1
    for index,num in enumerate(numList[1:]):
        if index+1 != num:
            return index+1

numList = [5,2,0,4,6,1,-1,-2,99,-3,7,8,8,-1,-2,10,10]
smallestIntNotInList = Find2ndSmallestInt(numList)
print(smallestIntNotInList)