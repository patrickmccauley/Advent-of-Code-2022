from os import read

# Read calorie inventory file.
with open('input.txt', "r") as f:
    data = f.read()
f.close()

#create stacks
stack = [["N", "B", "D", "T", "V", "G", "Z", 'j'], 
         ["S", "R", "M", "D", "W", "P", "F"], 
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


for x in range(0, len(data)-2):
    line = data[x]
    q = int(line[0:line.index(",")])
    y  = int(line[line.index(",") + 1: line.index(".")])
    z = int(line[line.index(".")+1])

    move_crate(q,y,z)
    print(stack)
    
#print final output
for j in range (0, 9):
     print(stack[j].pop())


    

    


    
        
    
    
    
    
    
    
    
    
    
        









#variables 


# for x in data:
#     count = count + x
#     if x == 0:
#         groupedSum.append(count)
#         count = 0

# for i in range(0,len(data)):
#     if data[i] == "":
#         data[i] = 0
#     else:
#         data[i] = int(data[i])
        

# newList = groupedSum
# newList.sort()
# topThree = newList[-3:]
# part1 = ""
# part2 = "sum of top 3 elves ="  + sum(newList[-3:])

    
    










