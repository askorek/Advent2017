start_a = 516
start_b = 190

# start_a = 65
# start_b = 8921

factor_a = 16807
factor_b = 48271
divider = 2147483647

def gen_next(previous, factor, divider, allow_multiple):
    while True:
        next = (previous*factor) % divider
        if next % allow_multiple == 0:
            return next
        else:
            previous = next

def check_if_match(value1, value2):
    return bin(value1)[-16:] == bin(value2)[-16:]


matched = 0
old_a = start_a
old_b = start_b
max_range = 5000000
for i in range(max_range):
    new_a = gen_next(old_a, factor_a, divider, 4)
    new_b = gen_next(old_b, factor_b, divider, 8)
    if check_if_match(new_a, new_b):
        matched += 1
    old_a = new_a
    old_b = new_b
    if i%400000 == 0:
        print("Progress: {}%".format(100.0*i/max_range))

print(matched)