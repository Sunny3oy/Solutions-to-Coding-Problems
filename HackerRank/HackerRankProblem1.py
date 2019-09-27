#Give a log file that contains log messages
#d104.aa.net - - [01/JUL/1995:00:00:15 - 0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786 
#return another file that has the gif name if it has a request of 200

#idea somehow split the and parse up each line store in list
#picking '/' might be a good delimiter
filename = 'log.txt'
contents = open(filename,"r")
f = open("ans.txt", "w")
f.close()
gifSet = set()
for line in contents:
    line+='/'
    lineContents = []
    string = ''
    for char in line:
        if char == '/':
            lineContents.append(string)
            string = ''
        else:
            string += char
    #correctly gotten what we need at this point
    #seems like we need to parse out the http code
    #parse out the gif name too
    
    httpRequest = lineContents[-1][5:9]
    gifName = lineContents[-2][0:len(lineContents[-2])-5]
    #print(httpRequest,gifName)

    #correctly parsed out what we need
    if httpRequest == '200 ' and gifName not in gifSet and gifName != '':
        gifSet.add(gifName)
        print(gifName)
        f = open("ans.txt","a")
        f.write(gifName+'\n')
        f.close()
contents.close()

