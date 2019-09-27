#We have a list of employees with a score levels
#we have a team size
#we have k 
#a number in which we will look at from the front and the back of the list

#Each iteration, we will pick the max number value score from the employees
#k from the left and k from the right
#find the max and remove that number from the scores

#repeats the process until the team size is reached

#example
#the list of scores are
#[17, 12, 10, 2, 7, 2, 11, 20, 8]
#team size is 3 and k is 4

#step 1
# [17, 12, 10, 2, 7, 2, 11, 20, 8]
# left side   17, 12, 10, 2
# right side   2, 11, 20, 8
# 20 is the biggest and will be added to the sum and removed from the list

#step 2
# [17, 12, 10, 2, 7, 2, 11, 8]
# left side   17, 12, 10, 2
# right side   7, 2, 11, 8
# 17 is the biggest and will be added to the sum and removed from the list

#step 3
# [12, 10, 2, 7, 2, 11, 8]
# left side   17, 12, 10, 2
# right side   7, 2, 11, 8
# 12 is the biggest and will be added to the sum and removed from the list

#so far we have 20+17+12 = 49
def teamFormation(score, team_size, k):
    # Write your code here
    ans = 0
    for i in range(team_size):
        indexToRemove = 0
        listSize = len(score)
        maxValueSoFar = 0
        left = score[:k]
        right = score[listSize-k:]
        for x in range(len(left)): #right side
            if maxValueSoFar < left[x]:
                maxValueSoFar = left[x]
                indexToRemove = x
        for x in range(len(right)):
            if maxValueSoFar < right[x]:
                maxValueSoFar = right[x]
                indexToRemove = listSize-k+x
        print(list1)
        value = score.pop(indexToRemove)
        print(value, "Index remove is " + str(indexToRemove))
        ans = ans+maxValueSoFar
    return ans
list1 = [17, 12, 10, 2, 7, 2, 11, 20, 8]
print(teamFormation(list1,3,4))
print("-----------------------------------")
list1 = [10,20,10,15,5]
print(teamFormation(list1,2,1))