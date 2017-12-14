class Reg:
    pass

with open("day08_input.txt") as f:
    puzzle_input = f.read().splitlines()

for line in puzzle_input:
    register_name = line.split()[0]
    string_to_exec = "Reg.{} = 0".format(register_name)
    exec(string_to_exec)

p2_maxx = -99999999
for line in puzzle_input:
    condition = line.split('if')[1].strip()
    condition = "Reg." + condition
    if eval(condition):
        register = line.split()[0]
        value = line.split()[2]
        operator = line.split()[1]
        if operator == 'inc':
            str_to_execute = "Reg.{} += {}".format(register, value)
        else:
            str_to_execute = "Reg.{} -= {}".format(register, value)
        exec(str_to_execute)
        if getattr(Reg, register) > p2_maxx:
            p2_maxx = getattr(Reg, register)

maxx = -999999999999999
for el in dir(Reg):
    if '__' not in el:
        if getattr(Reg, el) > maxx:
            maxx = getattr(Reg, el)

print("Part 1 answer: {}".format(maxx))
print("Part 2 answer: {}".format(p2_maxx))

