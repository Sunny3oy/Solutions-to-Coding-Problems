#Given days of the week as 3 letter strings and given k, find out which day of the week it is.

#idea
#use a dict to assign number values.
#use mod to figure out which day of the week it should be

def KdaysLater(str,int):
    
    days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
    nums = [x for x in range(7)]
    daysToNums = dict(zip(days,nums)) #Creates a dict with days as the keys and nums as the values  
    
    dayOfWeek = (daysToNums[str]+int)%7 #first find out which day you are on, then add that to the int and mod by 7
    
    for keys in daysToNums.keys(): #loop through the keys in the dict
        if dayOfWeek == daysToNums[keys]: #if there is a match with the dayOfWeek and the value of daysToNums[keys], then return the key
            return(keys)

print(KdaysLater("Sat",23))
