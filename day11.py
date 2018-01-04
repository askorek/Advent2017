# based on https://www.redblobgames.com/grids/hexagons/ - cube coordinates

with open("day11_input.txt") as f:
    input_sequence = f.read().split(',')


x = 0
y = 0
z = 0
max = 0

for el in input_sequence:
    if el == 'n':
        y += 1
        z -= 1
    elif el == 's':
        y -= 1
        z += 1
    elif el == 'nw':
        y += 1
        x -= 1
    elif el == 'se':
        y -= 1
        x += 1
    elif el == 'sw':
        x -= 1
        z += 1
    elif el == 'ne':
        z -= 1
        x += 1
    distance = (abs(x) + abs(y) + abs(z))/2
    if distance > max:
        max = distance

print("end distance: {}".format(distance))
print("max distance: {}".format(max))
