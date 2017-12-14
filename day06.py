input_puzzle = "11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11".split()
start_combination = tuple([int(x) for x in input_puzzle])

already_seen = dict()
already_seen[start_combination] = 0

current_combination = start_combination
steps = 0
while True:
    steps += 1
    current_modyfiable = list(current_combination)
    max_index = current_combination.index(max(current_combination))
    value_to_redistribute = current_modyfiable[max_index]
    current_modyfiable[max_index] = 0
    redistributing_index = (max_index + 1) % len(current_modyfiable)
    while value_to_redistribute > 0:
        current_modyfiable[redistributing_index] += 1
        value_to_redistribute -= 1
        redistributing_index = (redistributing_index + 1) % len(current_modyfiable)
    current_combination = tuple(current_modyfiable)
    if current_combination in already_seen:
        print("found after step: {}".format(steps))
        print("loop size: {}".format(steps - already_seen[current_combination]))
        break
    else:
        already_seen[current_combination] = steps
