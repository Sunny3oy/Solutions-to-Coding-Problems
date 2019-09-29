# This problem was asked by Google.
# Given the root to a binary tree, implement serialize(root), 
# which serializes the tree into a string, and deserialize(s), 
# which deserializes the string back into the tree.

# For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def serialize(root):
    results = root.val
    queue = [root]
    while queue:
        currentNode = queue.pop(0)
        
        if currentNode.left:
            results = results + ' ' + currentNode.left.val
            queue.append(currentNode.left)
        else:
            results = results + ' null'
        
        if currentNode.right:
            results = results + ' ' + currentNode.right.val
            queue.append(currentNode.right)
        else:
            results = results + ' null'
    return results

def deserialize(inputString):
    inputList = inputString.split(' ')
    counter = -1
    while inputList[counter] == 'null':
        inputList.pop()
        counter -= 1
    
    #trimming finished
    counter = 1    
    root = Node(inputList[0])
    queue = [root]
    size = len(inputList)
    while counter < size:
        currentNode = queue.pop(0)
        if inputList[counter] != 'null':
            currentNode.left = Node(inputList[counter])
            queue.append(currentNode.left)
        counter += 1
        
        if counter == size:
            break
        
        if inputList[counter] != 'null':
            currentNode.right = Node(inputList[counter])
            queue.append(currentNode.right)
        counter += 1
            
    return root

testTree = Node('1',Node('2',Node('4',Node('8')),Node('5',Node('9'))),Node('3',Node('6'),Node('7',Node('10'))))
print(serialize(testTree))

root = deserialize(serialize(testTree))
print(root.right.left.val)