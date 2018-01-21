
buffer = [0]
current_pos = 0
steps = 312

for value in range(1,2018):
    new_position = (current_pos + steps)%len(buffer)
    # print('before insserting on position {} : {}'.format(current_pos, buffer))
    pre = buffer[:new_position + 1]
    post = buffer[new_position + 1:]
    buffer = pre + [value] + post
    # print("after inserting: {}".format(buffer))
    current_pos = new_position + 1
    if value == 2017:
        print("part 1 value: {}".format(buffer[current_pos + 1]))
    if value % 50000 == 0:
        print("progress: {}%".format(value/500000))

# part 2 - not my idea to use deque + rotate, from AoC reddit
from collections import deque

spinlock = deque([0])

for i in range(1, 50000001):
    spinlock.rotate(-steps)
    spinlock.append(i)

pos_of_zero = spinlock.index(0)
print("part 2 value: {}".format(spinlock[(pos_of_zero + 1)])