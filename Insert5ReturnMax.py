#given an interger N, find the max value if we were to insert the digit 5 in the number.

# N = 268 return 5268

#idea
#turn N into a string and loop over it with enumeration
#if the value of the first digit is less than 5, then return that value with 5 inserted in front.
#if it is a negative number, skip the '-' sign. if the first digit is greater than 5, return that value with 5 inserted
#if each of the loop ends without returning, then we will return 5 inserted at the end of the string.

def insert5returnmax(N):
    
    strN = str(N) #turns the input into string
    insert = 0 #index to insert in
    
    if strN[0] == "-": #negative number
        strN = strN[1:]
        for index,digit in enumerate(strN):
            if (int(digit)) > 5:
                insert = index
                return("-"+strN[:insert]+"5"+strN[insert:])
            else:
                insert = index+2
                continue
        return("-"+strN[:insert]+"5"+strN[insert:])
    else: #positive number
        for index,digit in enumerate(strN):
            if (int(digit)) < 5:
                insert = index
                return(strN[:insert]+"5"+strN[insert:])
            else:
                insert = index+1
                continue
        return(strN[:insert]+"5"+strN[insert:])

print(insert5returnmax(-10))
print(insert5returnmax(670))
print(insert5returnmax(0))
print(insert5returnmax(-999))
print(insert5returnmax(999))
