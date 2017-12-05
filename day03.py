puzzle_input = 265149
#puzzle_input = 1024

from math import sqrt, floor

if puzzle_input == 1:
    print("total steps: 0")

elif sqrt(puzzle_input) % 1 < 0.0001 and int(sqrt(puzzle_input)%2) == 1:
    print("total steps: {}".format((sqrt(puzzle_input)//2)*2))

else:
    closest_full_square_side = floor(sqrt(puzzle_input))
    if closest_full_square_side % 2 == 0:
        closest_full_square_side -= 1
    print("smaller square side: {}".format(closest_full_square_side))


    min_num_of_steps = closest_full_square_side//2 + 1
    print("min num of steps: {}".format(min_num_of_steps))
    outer_layer = puzzle_input - closest_full_square_side**2
    print("outer layer: {}".format(outer_layer))
    max_additional_steps = min_num_of_steps
    print("max additional steps: {}".format(max_additional_steps))
    if outer_layer == 0 :
        additional_steps = 0
    else:
        additional_steps = abs(outer_layer%(2*max_additional_steps)-max_additional_steps)
    print("additional steps: {}".format(additional_steps))
    print("total steps: {}".format(min_num_of_steps+additional_steps))

# ------------------- part 2 --------------------------------

def move_vector(vector, step):
    return (vector[0] + step[0], vector[1] + step[1])

neighbours = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1, -1], [-1,1], [-1,-1]]
moves = [[1,0], [-1,0], [0,1], [0,-1]]

already_filled = dict()

def get_next_cell(current, all_pos):
    max_pos = round(sqrt(len(all_pos))/2 + 0.00001)  # python round function has error - it returns 0 for x=0.5
    for el in moves:
        new_pos = move_vector(current, el)
        if all_pos.get(new_pos) == None and abs(new_pos[0]) <= max_pos and abs(new_pos[1]) <= max_pos:
            return new_pos
    raise Exception("cannot count new position for this entry: {}".format(current))

def get_sum_of_neighbours(current, all_pos):
    summ = 0
    for nei in neighbours:
        value = all_pos.get(move_vector(current, nei))
        if value is not None:
            summ += value
    return summ

already_filled[(0,0)] = 1
cell_value = 0
last_cell = (0,0)

while cell_value <= puzzle_input:
    new_cell = get_next_cell(last_cell, already_filled)
    cell_value = get_sum_of_neighbours(new_cell, already_filled)
    already_filled[new_cell] = cell_value
    last_cell = new_cell
    print("{} : {}".format(last_cell, already_filled[last_cell]))
