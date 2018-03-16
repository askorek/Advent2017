with open("day18_input.txt") as f:
    input_data = f.read().splitlines()

input_data = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2""".splitlines()

num_of_instructions = len(input_data)

registers = {}

def double_fun(fun, x, y):
    try:
        y = int(y)
    except ValueError:
        y = registers[y]
    if fun == 'set':
        registers[x] = y
    elif fun == 'add':
        registers[x] += y
    elif fun == 'mul':
        registers[x] *= y
    elif fun == 'mod':
        registers[x] %= y
    else:
        raise ValueError("Function {} not impletented".format(fun))

def snd(x):
    global sound
    sound = x

def rcv(x):
    print('recovering sound {}'.format(sound))

def jgz(x, y):
    global position
    try:
        y = int(y)
    except ValueError:
        y = registers[y]
    try:
        x = int(x)
    except ValueError:
        x = registers[x]

    if x > 0:
        position = (position + y) % num_of_instructions

position = 0
while True:
    command = input_data[position].split()
    if len(command) == 3 and command[0] != 'jgz':
        double_fun(command[0], command[1], command[2])
    elif command[0] == 'jgz':
        jgz(command[1], command[2])
        continue
