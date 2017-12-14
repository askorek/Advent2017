with open("day07_input.txt") as f:
    puzzle_input = f.read().splitlines()

all_programs = set()
for line in puzzle_input:
    program = line.split()[0]
    all_programs.add(program)

for line in puzzle_input:
    if ' -> ' in line:
        nodes = line.split('->')[1].split()
        for node in nodes:
            all_programs.discard(node.replace(",", ""))

print(all_programs)
name_of_root = all_programs.pop()

# ---------------------- part 2 -----------------------------

class Program(object):
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.subprograms = []
        self.all_above = 0

    def __repr__(self):
        return "{} ({}), subs: {}".format(self.name, self.size, self.subprograms)

    def get_all_above(self):
        total = 0
        for el in self.subprograms:
            if len(el.subprograms) == 0:
                total += el.size
            else:
                above_nodes = el.get_all_above()
                total = total + el.size + above_nodes
        self.all_above = total
        return total

    def is_balanced(self):
        if len(self.subprograms) == 0:
            self.balanced = True
            return True
        first = self.subprograms[0].get_all_above() + self.subprograms[0].size
        for el in self.subprograms:
            if el.get_all_above() + el.size != first:
                self.balanced = False
                return False
        self.balanced = True
        return True

all_programs = dict()
for line in puzzle_input:
    name = line.split()[0]
    size = int(line.split()[1].replace('(', '').replace(')', ''))
    new_program = Program(name, size)
    all_programs[name] = new_program

for line in puzzle_input:
    if ' -> ' in line:
        root = line.split()[0]
        nodes = line.split('->')[1].split()
        for node in nodes:
            node_pure_name = node.replace(",", "")
            all_programs[root].subprograms.append(all_programs[node_pure_name])


for el in all_programs:
    all_programs[el].is_balanced()

shortest = None
shortest_len = 9999999
for el in all_programs:
    if not all_programs[el].balanced:
        if len(all_programs[el].__str__()) < shortest_len:
            shortest_len = len(all_programs[el].__str__())
            shortest = all_programs[el]
print("shortest unbalanced: {} \n".format(shortest))


for el in shortest.subprograms:
    print(el)
    print(el.all_above + el.size)

diff = (1815 - 1823) + 1283
print("\nresult: {}".format(diff))