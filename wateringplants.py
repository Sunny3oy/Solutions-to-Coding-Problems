#you have a row of flowers, each flower needs a certain amount of water
#you start 1 step on the left of the flowers, where the water fountain is
#how many steps must you take in order to water all the flowers while
#backtracking to refill the water if you are given a water bucket that holds
#x amount of water

#idea
#Since we must move through the list of flowers once and we start 1 step besides the flowers, we will travel it's full length.
#We will look and compare if we can water the current flower, if we cannot, we need to refill our bucket.
#to refill we will spend 2 times the steps to walk back
def waterplants(bucketSize, flowers):
    steps = len(flowers) #must move through the list of flowers
    initBucketSize = bucketSize #placeholder to refill water
    for index,flowerValue in enumerate(flowers):
        if bucketSize < flowerValue: #can we water the current flower? if we cant we want to refill it
            bucketSize = initBucketSize
            steps = steps + 2*(index) #steps needed are double to backtrack
        bucketSize -= flowerValue# we subtract the flowervalue from bucket of water
    return steps

row = [2,4,5,1,2]
print(waterplants(6,row))

row = [1,1,2]
print(waterplants(3,row))

row = [2,2,1,1,2]
print(waterplants(3,row))