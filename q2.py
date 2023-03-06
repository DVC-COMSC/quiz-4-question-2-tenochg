
# ******************************
# Make your Code
# ******************************
inputs = []
inputslength = []

while True:
  x = input('Enter a string value: ')
  inputs.append(x)
  y = len(x)
  inputslength.append(y)
  if ('stop' or 'STOP') in inputs:
    break
    
maxv = 0
for c in inputslength[:-1]:
  if maxv == 0 or c > maxv:
    maxv = c
  for e in inputs[:-1]:
    if len(e) == maxv:
      longest = e
      break 
    
smallv = 0
for d in inputslength[:-1]:
  if smallv == 0 or d < smallv:
    smallv = d
  for g in inputs[:-1]:
    if len(g) == smallv:
      shortest = g
      break

print(e,g,end="\n")


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
