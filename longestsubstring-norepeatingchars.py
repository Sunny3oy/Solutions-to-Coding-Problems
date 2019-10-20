def lengthofLongestSubstring(s):
  dic = {}
  res,start = 0,0
  for index,ch in enumerate(s):
    if ch in dic:
      print("ch: ", ch)
      res = max(res,index-start)
      print("res: ", res," ","index: ",index)
      print("dic[ch]: ",dic[ch])
      start = max(start,dic[ch]+1)
      print("start", start)
    
    dic[ch] = index
    print("dic[ch] AFTER the if-statement: ",dic[ch])
    print()
  return max(res,len(s)-start)

print(lengthofLongestSubstring("abcabcbb"))

print()

print(lengthofLongestSubstring("bbbbb"))

print()

print(lengthofLongestSubstring("pwwkew"))
