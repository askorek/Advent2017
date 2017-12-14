with open("day09_input.txt") as f:
    puzzle_data = f.read()

def filter_garbage(text):
    output = []
    inside_garbage = False
    skip_next = False
    garbage_counter = 0
    for letter in text:
        if skip_next:
            skip_next = False
            continue
        if not inside_garbage and letter == '<':
            inside_garbage = True
            continue
        if inside_garbage and letter == '!':
            skip_next = True
            continue
        if inside_garbage and letter == '>':
            inside_garbage = False
            continue
        if inside_garbage:
            garbage_counter += 1
            continue
        else:
            output.append(letter)

    print('garbages count: {}'.format(garbage_counter))
    return ''.join(output)

def count_score(text):
    filtered = filter_garbage(text)
    total_score = 0
    level = 0
    for letter in filtered:
        if letter == '{':
            level += 1
        elif letter == '}':
            total_score += level
            level -= 1
        else:
            continue
    assert level == 0
    return total_score


test3 = '{{{},{},{{}}}}'
print(count_score(puzzle_data))