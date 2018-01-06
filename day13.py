
# input_ = """0: 3
# 1: 2
# 4: 4
# 6: 4""".splitlines()

with open("day13_input.txt") as f:
    input_ = f.read().splitlines()

firewall = dict()
for element in input_:
    depth, range_ = element.split(": ")
    firewall[int(depth)] = int(range_)

def travel_through_firewall(firewall, delay, fail_at_hit=False):
    end_of_firewall = max([int(x) for x in firewall])

    severity = 0
    for position in range(end_of_firewall + 1):
        if firewall.get(position) is not None:
            distance_in_time_when_firewall_at_top = (firewall[position] - 2)*2 + 2
            if (position + delay) % distance_in_time_when_firewall_at_top == 0:
                if fail_at_hit: return None
                severity += position*firewall[position]
    return severity

print(travel_through_firewall(firewall, 0))

# ----------- part 2 -------------
delay = 0
while True:
    severity = travel_through_firewall(firewall, delay, fail_at_hit=True)
    if severity == 0:
        print("severity = 0 for delay = {}".format(delay))
        break
    delay += 1
    if delay % 10000 == 0:
        print(delay)


