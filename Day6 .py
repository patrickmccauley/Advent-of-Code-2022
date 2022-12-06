file = open('input.txt')
characters= []
for line in file:
  for char in range(0, len(line)):
    characters.append(line[char])

def part1():
  for x in range(3, len(characters)-3):
    
    first = characters[x]
    second = characters[x - 1]
    third = characters[x + -2]
    fourth = characters[x + -3]
    
    variables = [first, second, third, fourth]
    
    if len(set(variables)) == len(variables):
      return(str("part 1: characters processed before start of packet = ") + str(x + 1)) 
      
def part2():
  for x in range(13, len(characters)-3):
    
    first = characters[x]
    second = characters[x - 1]
    third = characters[x - 2]
    fourth = characters[x - 3]
    fifth = characters[x - 4]
    sixth = characters[x - 5]
    seventh = characters[x -6]
    eight = characters[x - 7]
    ninth = characters[x -8]
    tenth = characters[x - 9]
    eleventh = characters[x - 10]
    twelfth = characters[x - 11]
    thirteenth = characters[x -12]
    fourteenth = characters[x - 13]
    
    variables = [first, second, third, fourth, fifth, sixth, seventh, eight, ninth, tenth, eleventh, twelfth, thirteenth, fourteenth ]
    
    if len(set(variables)) == len(variables):
      return(str("part 2: characters processed before start of packet = ") + str(x + 1))  
      break
  
print(part1())
print(part2())


