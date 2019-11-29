# This problem was asked by Amazon.

# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

# For example, given the array [34, -50, 42, 14, -5, 86], 

# the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

# Do this in O(N) time.

#either take the number or leave it
#how to decide if we take the number.
#if we do not take any number, the max sum would be 0.
#if we take the number, we have to consider.
#the number taken, does it contribute the answer?
#if we take this number, does it change our answer?
#have a current max sum ready.

#if we encounter a negative number, we need to combine any other consecutive negative numbers.
#this is our look ahead check.


def maxSumContiguous(numList):
    maxSum = 0
    negativeSum = 0
    for num in numList:
        #2 cases
        #case 1: positive numbers only
        if num > 0:
            #if we encounter a positive number we need to check if the max sum needs to be changed
            #also taking into account of any number of negative numbers we have passed
            #if the current max sum is less than maxSum+current number+ any negative numbers we have passed
            if maxSum < maxSum + num + negativeSum:
                #if it is, we need to change it,
                #maxSum will take the current value
                maxSum += num + negativeSum
                print(maxSum)
            else:
                #there was too many negative numbers, negative numbers brought the sum down that it wasnt
                #worth it, so we check to see which value is the max, maxSum or current num value.
                maxSum = max(num,maxSum)
            #resets negativeSum
            negativeSum = 0
        #encountered a negative number
        #simply add them up and record them
        #if we encounter more, keep recording their sum
        else:
            negativeSum += num
    return maxSum

#O(N) time since we look at each value in the list once