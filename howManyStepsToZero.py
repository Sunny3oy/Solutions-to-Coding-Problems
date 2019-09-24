#Given a number that is repsersented in binary, find out how many steps it takes to reduce it to 0.
#if number is odd subtract 1. if odd, -1
#if even, divide by 2

#the idea let "011100" be the input. which is 28.
#in binary, the least signifcant digit is 2^0, then the next least is 2^1. ect
#find out the position/power of the most signifcant digit. It will take thatPower+1.
#the reason is since it is the power of 2, and it is even, then it will take that many divisons
#by 2 to reach 1, then we subtract 1 since we get an odd. 

#the remaining "1"s that are still in the string will count as 1 extra step to reach to 0
def StepsToZero(str):
    strlen = len(str) #find the len of str
    first1digit = strlen #assigns that len to first1digit. assumes that the first digit we encounter has 1.
    result = 0 #placeholder for return result
    
    for digit in str: #loop to find the first digit position that has "1".
        if digit == "1":
            result = first1digit #since binary starts their powers at 0, strlen should return the correct value we need. power+1
            break #once we find the first digit we break out of this loop
        else:
            first1digit = first1digit-1 #if digit not found, decrease first1digit by 1
    for digit in str[strlen-first1digit+1:]: #we must splice the string at the next location, right after the first1digit was found.
        #the len of the str - first1digit will give us the starting location of the first1digit, we want the next one.
        if digit == "1":
            result = result+1 #any remaining "1" in the string, means an extra step needed.
    return result

print(StepsToZero("011100"))