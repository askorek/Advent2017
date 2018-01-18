def make_knot_hash(input_ascii):
    def reverse_order(starting_position, reverse_len, list_to_rev):
        if reverse_len == 0:
            return list_to_rev
        if starting_position + reverse_len <= len(list_to_rev):
            rev_part = list_to_rev[starting_position: starting_position + reverse_len]
            return list_to_rev[:starting_position] + rev_part[::-1] + list_to_rev[starting_position + reverse_len:]
        else:
            exceding = starting_position + reverse_len - len(list_to_rev)
            rev_part = list_to_rev[starting_position:] + list_to_rev[:exceding]
            reversed = rev_part[::-1]
            begining = reversed[-exceding:]
            middle = list_to_rev[exceding: starting_position]
            end = reversed[:-exceding]
            assert len(begining) + len(middle) + len(end) == len(list_to_rev)

            return begining + middle + end

    def mix(input_lengths, circular_list, skip_size, current_position):
        for el in input_lengths:
            circular_list = reverse_order(current_position, el, circular_list)
            current_position = (current_position + skip_size + el) % (len(circular_list))
            skip_size += 1
        return circular_list, current_position, skip_size

    def make_denser(sequence):
        assert len(sequence) % 16 == 0
        num_of_output = len(sequence) // 16
        output_sequence = []
        for i in range(num_of_output):
            current_xored = 0
            for j in range(16):
                current_xored = current_xored ^ sequence[i * 16 + j]
            output_sequence.append(current_xored)
        return output_sequence

    def make_hexes(input_list):
        out_string = ''
        for el in input_list:
            hexed = hex(el)[2:]
            if len(hexed) == 1:
                hexed = '0' + hexed
            out_string += hexed
        return out_string

    circular_list = [i for i in range(256)]
    current_position = 0
    skip_size = 0

    for i in range(64):
        circular_list, current_position, skip_size = mix(input_ascii, circular_list, skip_size, current_position)

    dense = make_denser(circular_list)
    hexed = make_hexes(dense)
    return hexed

def create_map_line(input_string):
    input_ascii = [ord(x) for x in input_string]
    input_ascii += [17, 31, 73, 47, 23]
    hash = make_knot_hash(input_ascii)
    output_line = []
    for letter in hash:
        output_line += bin(int(letter,16))[2:].zfill(4)
    assert len(output_line) == 128
    return ''.join(output_line)

count = 0
for i in range(128):
    line = create_map_line("hxtvlmkl-{}".format(i))
    count += line.count('1')
print("numebr of used squares: {}".format(count))

# --------- part 2 ------------
# based on https://en.wikipedia.org/wiki/Connected-component_labeling

map_ = {}
current_region_num = 0
for i in range(128):
    line = create_map_line("hxtvlmkl-{}".format(i))
    for j, letter in enumerate(line):
        if letter == '1':
            map_[(i, j)] = current_region_num
            current_region_num += 1

list_of_equivalences = []

for i in range(128):
    for j in range(128):
        if (i, j) not in map_:
            continue

        current_region = map_[(i, j)]
        if (i-1, j) in map_:
            older_region = map_[(i-1, j)]
            if current_region != older_region:
                for eq in list_of_equivalences:
                    if older_region in eq and current_region not in eq:
                        eq.append(current_region)
        if (i, j - 1) in map_:
            older_region = map_[(i, j-1)]
            if current_region != older_region:
                for eq in list_of_equivalences:
                    if older_region in eq and current_region not in eq:
                        eq.append(current_region)

        if (i, j - 1) in map_ and (i - 1, j) in map_:
            region_1 = map_[(i, j - 1)]
            region_2 = map_[(i -1, j)]

            if region_1 != region_2:
                list_1 = [x for x in list_of_equivalences if region_1 in x][0]
                list_2 = [x for x in list_of_equivalences if region_2 in x][0]
                if list_1 != list_2:
                    list_1 += list_2
                    list_of_equivalences.remove(list_2)
                    list_1.append(current_region)
                    list_1 = list(set(list_1))
            else:
                for eq in list_of_equivalences:
                    if region_1 in eq and current_region not in eq:
                        eq.append(current_region)

        if (i, j - 1) not in map_ and (i - 1, j) not in map_:
            list_of_equivalences.append([current_region])

print("regions: {}".format(len(list_of_equivalences)))


