with open('testfile.txt', 'r') as file:
    data = file.read().split()

#how many trees are  visible
#test file returns 21

arr = ([])
for line in data:
    temp  = []
    for char in line:
        
        temp.append(char)
    arr.append(temp)

def isVisable(x, y):

    val = arr[x][y]
    left = arr[x][0:y]
    right = arr[x][y+1:]
    above = []
    below = []
    
    for line in range(0, x ):
        dig = arr[line][y]
        above.append(dig)
        below = []
        
    for line in range(x + 1, len(arr)):
        dig = arr[line][y]
        below.append(dig)
        
    if val > max(left) or val > max(right) or val > max(above) or val > max(below):
        return True
    else:
        return False

#count alltree on permiter
perimeterTrees = ((len(arr[0]) * 2 - 4) + len (arr * 2))

def testEachTree():
    visCount = 0
    for lineNum in range(1, len(arr)-1):
        x = lineNum
        for index in range(1,len(arr[lineNum])-1):
            y = index
            if isVisable(x, y) is True:
                visCount = visCount + 1
    visCount = visCount + perimeterTrees
    return visCount       

def rating(x, y):

    val = arr[x][y]
    left = arr[x][0:y]
    
    right = arr[x][y+1:]
    above = []
    below = []
    
    for line in range(0, x):
        dig = arr[line][y]
        above.append(dig)
        
        
        
    for line in range(x + 1, len(arr)):
        dig = arr[line][y]
        below.append(dig)
    
    
    rightView = 0
    leftView = 0
    upView = 0
    downView = 0
    
    left.reverse()
    above.reverse()
    
    for tree in right:
        rightView += 1
        if tree >= val:
            break
    
    for tree in left:
        leftView += 1
        if tree >= val:
            break
    
    for tree in above:
        upView += 1
        if tree >= val:
            break
        
    for tree in below:
        downView += 1
        if tree >= val:
            break
    
    rating = (leftView * rightView * upView * downView)
    return(rating)


def findBestView():
    best = []
    for lineNum in range(0, len(arr)):
        x = lineNum
        for index in range(0, len(arr[lineNum])):
            y = index
            
            
            score = rating(x,y)
            best.append(score)
            best.sort(reverse=True)
            
    return best[0]
    
print('part one : ' +str(testEachTree()))    
print('part two : ' + str(findBestView()))

            
    
