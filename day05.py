with open("day05_input.txt") as f:
    puzzle_input = f.read().splitlines()

int_input = [int(x) for x in puzzle_input]

max_index = len(int_input) - 1

current_index = 0
steps = 0

while current_index <= max_index:
    current_index_old = current_index
    current_index += int_input[current_index]
    int_input[current_index_old] += 1
    steps += 1

print(steps)


# ------------------ part 2 ----------------
int_input = [int(x) for x in puzzle_input]

current_index = 0
steps = 0

while current_index <= max_index:
    current_index_old = current_index
    current_index += int_input[current_index]
    if int_input[current_index_old] >= 3:
        int_input[current_index_old] -= 1
    else:
        int_input[current_index_old] += 1
    steps += 1

print(steps)