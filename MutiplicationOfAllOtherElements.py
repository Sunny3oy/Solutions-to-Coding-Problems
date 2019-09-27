# Given an array of integers, 
#return a new array such that each element at index i of the new array 
#is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], 
#the expected output would be [120, 60, 40, 30, 24]. 
#If our input was [3, 2, 1], 
#the expected output would be [2, 3, 6].
#Input :[5,2,4,7]
#Output:[56,140,70,40]

#Idea to solve
#first find the total number that all of the numbers mutiple to
#then just divide by the current number seen and add to the list

# Follow-up: what if you can't use division?

def sol(numList):
    value = 1
    for num in numList:
        value = value * num
    ans = [value//num for num in numList]
    return ans

numList = [5,2,4,7]
print(sol(numList))
print("-----------------------------------")

#A Solution without using divison
#brute force way is just to take the nums and mutiply it without the current num
def Timeshelper(numList):
    value = 1
    for num in numList:
        value = value*num
    return value

def solnoDivide(numList):
    ans = []
    for index,num in enumerate(numList):
        ans.append(Timeshelper(numList[:index]+numList[index+1:]))
    return ans

print(solnoDivide(numList))