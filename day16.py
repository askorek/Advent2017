
def spin(dancers, position):
    new_dancers = dancers[-position:] + dancers[:-position]
    return new_dancers

def exchange(dancers, pos1, pos2):
    new_dancers = dancers[:]
    pos1_copy = dancers[pos1]
    new_dancers[pos1] = new_dancers[pos2]
    new_dancers[pos2] = pos1_copy
    return new_dancers

def partner(dancers, p1, p2):
    index1 = dancers.index(p1)
    index2 = dancers.index(p2)
    return exchange(dancers, index1, index2)

def parse(input_string, dancers):
    if input_string.startswith('s'):
        val = int(input_string[1:])
        return spin(dancers, val)
    elif input_string.startswith('x'):
        e1, e2 = [int(x) for x in input_string[1:].split('/')]
        return exchange(dancers, e1, e2)
    elif input_string.startswith('p'):
        p1 = input_string[1]
        p2 = input_string[-1]
        return partner(dancers, p1,p2)
    else:
        raise Exception

test_dancers = [chr(x) for x in range(97,102)]
test_commands = 's1,x3/4,pe/b'

for command in test_commands.split(','):
    test_dancers = parse(command, test_dancers)

dancers = [chr(x) for x in range(97,97+16)]

with open('day16_input.txt') as f:
    puzzle_input = f.read()

swap_commands = ''
for command in puzzle_input.split(','):
    if command[0] == 'p':
        swap_commands = swap_commands + ',' + command
        continue
    dancers = parse(command, dancers)

for command in swap_commands.split(',')[1:]:
    dancers = parse(command, dancers)

print(''.join(dancers))


#part 2
dancers = [chr(x) for x in range(97,97+16)]
known_list = []
repetitions = 1000000000
finished = False
for i in range(repetitions):
    dancers_string = ''.join(dancers)
    if dancers_string in known_list:
        print(known_list[repetitions % len(known_list)])
        break
    known_list.append(dancers_string)
    for command in puzzle_input.split(','):
        dancers = parse(command, dancers)


