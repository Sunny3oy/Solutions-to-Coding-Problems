# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

#idea
#by doing this in one pass, we must somehow store what we have seen already.
#using a set can be a good way to store our work done so far

#when we encounter a number in the list
#we want to first check if the (target k - current number) is in the set.
#for example, if our current number is 10, our target k is 17. we need to check to see if 7 is in our set.
#if it is in our set, return true along with the current number and the matching number that was seen already.
def FindSumForK(target, numList):
    numbersSeenSoFar = set() #holds the numbers seen so far
    for currentNum in numList:
        possibleNum = target - currentNum
        if possibleNum in numbersSeenSoFar:
            print("Solution found:"+str(currentNum)+'+'+str(possibleNum)+'='+str(target))
            return True
        else:
            numbersSeenSoFar.add(currentNum)
    print("Not possible with this list of numbers")
    print(numList)
    print("with target = "+str(target))
    return False

numList = [10,15,3,7]
FindSumForK(17, numList)

numList = [10,15,3,7,9,20]
FindSumForK(30, numList)

numList = [10,15,3,7,9,20]
FindSumForK(32, numList)