with open("Day13", 'r') as f:
    input_info = f.readlines()

bus_ids = []
bus_taken = [0, 0]
earliest_ts = int(input_info[0])
for ids in input_info[1].split(','):
    bus_ids.append(ids)

bus_taken[1] = 1000

for ids in bus_ids:
    if ids.isnumeric():
        bus_id = int(ids)
        last_loop_num = earliest_ts // bus_id
        wait_time = bus_id * (last_loop_num+1) - earliest_ts
        if wait_time < bus_taken[1]:
            bus_taken[0] = bus_id
            bus_taken[1] = wait_time


t = 0
step = 1
bus_info = [(int(i), j) for j, i in enumerate(bus_ids) if i != 'x']     # contains id and offset from first bus

for bus_id, time_difference in bus_info:
    while (t + time_difference) % bus_id != 0:
        t += step
    step *= bus_id

print("Part 1: ", bus_taken[0] * bus_taken[1])
print("Part 2: ", t)
