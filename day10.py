def reverse_order(starting_position, reverse_len, list_to_rev):
    if reverse_len == 0:
        return list_to_rev
    if starting_position + reverse_len <= len(list_to_rev):
        rev_part = list_to_rev[starting_position : starting_position+reverse_len]
        return list_to_rev[:starting_position] + rev_part[::-1] + list_to_rev[starting_position+reverse_len:]
    else:
        exceding = starting_position + reverse_len - len(list_to_rev)
        rev_part = list_to_rev[starting_position:] + list_to_rev[:exceding]
        reversed = rev_part[::-1]
        begining = reversed[-exceding:]
        middle = list_to_rev[exceding : starting_position]
        end = reversed[:-exceding]
        assert len(begining) + len(middle) + len(end) == len(list_to_rev)

        return begining + middle + end

# a = [0,1,2,3,4]
# b = reverse_order(0,3,a)
# c = reverse_order(3,4,b)
# d = reverse_order(1,5,c)
# print(d)
#
input_lengths = [129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108]
circular_list = [i for i in range(256)]

#input_lengths = [3, 4, 1, 5]
#circular_list = [0, 1, 2, 3, 4]
current_position = 0
skip_size = 0

def mix(input_lengths):
    global circular_list, skip_size, current_position
    for el in input_lengths:
        circular_list = reverse_order(current_position, el, circular_list)
        current_position = (current_position + skip_size + el) % (len(circular_list))
        skip_size += 1

mix(input_lengths)
print(circular_list[0]*circular_list[1])

# --------- part 2 --------------

circular_list = [i for i in range(256)]
current_position = 0
skip_size = 0

#input_chars = '129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108'
input_chars = '129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108'
input_ascii = [ord(x) for x in input_chars]
input_ascii += [17, 31, 73, 47, 23]

for i in range(64):
    mix(input_ascii)

def make_denser(sequence):
    assert len(sequence) % 16 == 0
    num_of_output = len(sequence) // 16
    output_sequence = []
    for i in range(num_of_output):
        current_xored = 0
        for j in range(16):
            current_xored = current_xored ^ sequence[i*16+j]
        output_sequence.append(current_xored)
    return output_sequence

a = make_denser(circular_list)

def make_hexes(input_list):
    out_string = ''
    for el in input_list:
        hexed = hex(el)[2:]
        if len(hexed) == 1:
            hexed = '0' + hexed
        out_string += hexed
    return out_string

b = make_hexes(a)
print(b)
