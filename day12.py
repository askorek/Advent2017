with open("day12_input.txt") as f:
    puzzle_input = f.read().splitlines()

# connected_to_zero = set()
#
def parse_line(line):
    current = int(line.split('<->')[0])
    rest = line.split('<->')[1].split()
    connected = [int(x.replace(',', '')) for x in rest]
    return current, connected

connected_to_zero = set()
start_size = 0
end_size = None
while start_size != end_size:
    start_size = len(connected_to_zero)
    for line in puzzle_input:
        current, connected = parse_line(line)
        if current == 0:
            connected_to_zero.add(current)
        if current in connected_to_zero or any(connected) in connected_to_zero:
            connected_to_zero.add(current)
            connected_to_zero |= set(connected)
    end_size = len(connected_to_zero)


# ----------------------------- part 2 ------------------------
elements_left = set(range(2000))
list_of_groups = list()
while len(elements_left) > 0:
    first_el_of_set = elements_left.pop()
    new_group = set()
    new_group.add(first_el_of_set)
    start_size = 0
    end_size = None
    while start_size != end_size:
        start_size = len(new_group)
        for line in puzzle_input:
            current, connected = parse_line(line)
            # this strange construction with intesection because 'in' does not work properly
            if current in new_group or len(set(connected).intersection(new_group)) > 0:
                new_group.add(current)
                new_group |= set(connected)
                elements_left.discard(current)
                [elements_left.discard(x) for x in connected]
        end_size = len(new_group)
    list_of_groups.append(set(new_group))