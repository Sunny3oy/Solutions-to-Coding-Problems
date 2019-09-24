#problem
#we have domino pieces. each piece is repersented by 2 array. top and bottom.
#find out the min rotations for either the top or bottom to have the same values.

#looking at the first domino gives us valueable information

#either the top or bottom values will need to occur in all the dominos
#[1]
#[6]
#so the possible winning hand is to either see if it is possible to make all
#values on the top to be 1 or 6.
#or
#values on the botton to be 1 or 6.
#then we need to keep track if we want the top to be all 1's, how many rotations will it take
#so we need at max 4 counters.
#counters should be a dict type so it makes it easy to remove and add
#it will return the min value at the end.

def minrotations(top,bottom):
    firstpieceTop = top[0]
    firstpieceBottom = bottom[0]
    
    possibleWins = ['TopPieceStays','TopPieceRotate','BottomPieceStays','BottomPieceRotate']
    RotationCount = [0]*4
    dictPossibleWins = dict(zip(possibleWins,RotationCount))
    
    for index in range(len(top)):
        #check if the top/bottom value exsits in the top or the bottom
        #if the first piece top value does not occur in the current top or bottom, 
        #remove the possible way to win with the top piece
        #same for the bottom
        if firstpieceTop != top[index] and firstpieceTop != bottom[index] and 'TopPieceStays' in dictPossibleWins:
            del dictPossibleWins["TopPieceStays"]
            del dictPossibleWins["TopPieceRotate"]
        if firstpieceBottom != top[index] and firstpieceBottom != bottom[index] and 'BottomPieceStays' in dictPossibleWins:
            del dictPossibleWins["BottomPieceStays"]
            del dictPossibleWins["BottomPieceRotate"]
        
        #if top piece stays, then for it to increament, the bottom piece must be = firstpiecetop
        if 'TopPieceStays' in dictPossibleWins:
            if firstpieceTop == bottom[index]:
                dictPossibleWins['TopPieceStays'] += 1
        #if top piece rotate, then for it to increament, the top piece must be firstpiecetop        
        if 'TopPieceRotate' in dictPossibleWins:
            if firstpieceTop == top[index]:
                dictPossibleWins['TopPieceRotate'] += 1
                
        if 'BottomPieceStays' in dictPossibleWins:
            if firstpieceBottom == top[index]:
                dictPossibleWins['BottomPieceStays'] += 1
                
        if 'BottomPieceRotate' in dictPossibleWins:
            if firstpieceBottom == bottom[index]:
                dictPossibleWins['BottomPieceRotate'] += 1
        if len(dictPossibleWins) == 0:
            return('Not possible with these dominos')
    print(dictPossibleWins)
    
    return(min(dictPossibleWins.values()))

top =    [1,2,3,6,3,2]
bottom = [2,1,2,2,2,4]
            #       #
print(minrotations(top,bottom))
print("----------------------")
top =    [1,2,1,2,1,2,1]
bottom = [2,1,2,1,2,1,2]
            #   #   #
print(minrotations(top,bottom))
print("----------------------")
top =    [1,2,1,2,1,2,1,6]
bottom = [2,1,2,1,2,1,2,4]
                        #the last one killed it
print(minrotations(top,bottom))
print("----------------------")
top =    [1,2,1,2,1,2,1,6,5]
bottom = [2,1,2,1,2,1,2,1,1]
          #   #   #   #
print(minrotations(top,bottom))
print("----------------------")
top =    [1,2,1,2,1,2,1,6]
bottom = [2,1,2,1,2,1,2,2]
            #   #   #
print(minrotations(top,bottom))