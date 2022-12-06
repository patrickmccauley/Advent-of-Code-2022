from os import read

# Read calorie inventory file.
with open('input.txt', "r") as f:
    data = f.read()
f.close()

#create stacks
#firstrow = stack 1 enter bottom to top
stack = [['N', 'B', 'D', 'T', 'V', 'G', 'Z', 'J'], 
         ['S', 'R', 'M', 'D', 'W', 'P', 'F'], 
         ['V', 'C', 'R', 'S', 'Z'], 
         ['R', 'T','J','Z','P','H','G'],
         ['T','C','J','N','D','Z','Q','F'],
         ['N','V','P','W','G','S','F', 'M'],
         ['G', 'C', 'V', 'B', 'P', 'Q'],
         ['Z', 'B', 'P', 'N'],
         ['W', 'P', 'J'],
         ]


# Format data to integers.
data = data.splitlines()


##move_crate functions
#x = quantity  
#y = origin 
#z = destination

def move_crate(x,y,z):

  for i in range(x):
    stack[z-1].append(stack[y-1].pop())
  
  return stack

def move_multiple(x,y,z):
    tempstack = []
    for u in range(x):
        
        tempstack.append(stack[y-1].pop())
    
    for p in range(0,len(tempstack)):
        stack[z-1].append(tempstack.pop())
    
    return stack
    
#feeds parameters through 
for x in range(0, len(data)-2):
    line = data[x]
    q = int(line[0:line.index(",")])
    y  = int(line[line.index(",") + 1: line.index(".")])
    z = int(line[line.index(".")+1])
    
    
    #move_crate(q,y,z) #uncomment for part 1
    #move_multiple(q,y,z) #uncomment for part  2
    
#print final output\
print
print("final stack")
print(stack)
print
for x in stack:
    print (x[-1])

# if final output fails find the last letter of each stack manually
# for j in range (0, 9):
#     print(stack[j].pop())








