def reverse_order(starting_position, reverse_len, list_to_rev):
    if starting_position + reverse_len <= len(list_to_rev):
        rev_part = list_to_rev[starting_position : starting_position+reverse_len]
        return list_to_rev[:starting_position] + rev_part[::-1] + list_to_rev[starting_position+reverse_len:]
    else:
        exceding = starting_position + reverse_len - len(list_to_rev)
        rev_part = list_to_rev[starting_position:] + list_to_rev[:exceding]
        reserved = rev_part[::-1]
        return reserved[-exceding:] + list_to_rev[exceding: starting_position] + \
               list_to_rev[len(list_to_rev) - exceding - 1:starting_position] + reserved[:-exceding]

# a = [0,1,2,3,4]
# b = reverse_order(0,3,a)
# c = reverse_order(3,4,b)
# d = reverse_order(1,5,c)
# print(d)

# input_lengths = [129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108]
# circular_list = [i for i in range(256)]

input_lengths = [3, 4, 1, 5]
circular_list = [0, 1, 2, 3, 4]
current_position = 0
skip_size = 0

for el in input_lengths:
    print(el)
    circular_list = reverse_order(current_position, el, circular_list)
   # assert len(circular_list) == 256
    current_position = (current_position + skip_size + el) % (len(input_lengths) + 1)
    skip_size += 1

print(circular_list)
print(circular_list[0]*circular_list[1])