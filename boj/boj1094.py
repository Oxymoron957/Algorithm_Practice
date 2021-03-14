x = int(input())

sticks = [64]

while sum(sticks) != x:    
    shortest_element = int(sticks.pop()/2)
    sticks.append(shortest_element)
    sticks.append(shortest_element)
    if sum(sticks[:-1]) >= x:
        sticks.pop()    
print(len(sticks))

    
