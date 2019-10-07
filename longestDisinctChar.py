# This problem was asked by Amazon.
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
#longest Substring
#use a set to store the distinct characters
#as long as the set count is below or equal to 2, it is good
#will have to be a nested loop.
#start by looking at the string from the start 
#keep going until you reach the end or k amount of distinct char has been reached

#seems like the worst case would be a string with all same char
#not sure if there are ways to improve it

def longestSubstringK(string,k):
    size = len(string)
    print(size)
    #edge cases
    #if k is greater or equal to the size of string, that means we can take the whole string
    if k >= size:
        return string
    #
    returnString = ""
    for start in range(size-1):
        #if we found a string that had a certain length, and it is greater than the remaining substring to look at, then that
        #is the longest string we can find
        if len(returnString) > len(string[start:]):
            print("len of longest ",len(returnString))
            print("remaining substring len ",len(string[start:]))
            print("break out")
            break
        longestStringSoFar = ""
        charSet = set()
        count = 0
        for char in string[start:]:
            if char not in charSet:
                charSet.add(char)
                count += 1
            if count > k:
                break
            longestStringSoFar += char
            print(longestStringSoFar)
        print("ended one round")
        print("start is ", start)
        if len(returnString) < len(longestStringSoFar):
            returnString = longestStringSoFar
    return returnString

print(longestSubstringK("aaaaaaaaaaaaaaaaa",2))