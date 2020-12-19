curr_x = curr_y = 0
wayp_x = 10
wayp_y = 1
curr_dir = 0
curr_ortn = 0
directions = ["E", "S", "W", "N"]


def move(movement):
    global curr_x, curr_y, curr_dir
    parameter = int(movement[1:])
    if movement.startswith("N"):
        curr_y += parameter
    elif movement.startswith("S"):
        curr_y -= parameter
    elif movement.startswith("E"):
        curr_x += parameter
    elif movement.startswith("W"):
        curr_x -= parameter
    elif movement.startswith("F"):
        move(f"{directions[curr_dir]}{parameter}")

    else:
        turn = (parameter // 90)
        if movement.startswith("R"):
            curr_dir = (curr_dir + turn) % 4
        else:
            curr_dir = (curr_dir - turn) % 4


def move_waypoint(movement):
    global wayp_x, wayp_y
    parameter = int(movement[1:])
    if movement.startswith("N"):
        wayp_y += parameter
    elif movement.startswith("S"):
        wayp_y -= parameter
    elif movement.startswith("E"):
        wayp_x += parameter
    elif movement.startswith("W"):
        wayp_x -= parameter


def rotate_waypoint(rotation):
    global wayp_x, wayp_y
    angle = 0
    parameter = int(rotation[1:])
    if rotation.startswith("R"):
        angle = 360 - parameter
    elif rotation.startswith("L"):
        angle = parameter

    if angle == 90:
        helper = wayp_x
        wayp_x = -1 * wayp_y
        wayp_y = +1 * helper
    elif angle == 180:
        wayp_x = -1 * wayp_x
        wayp_y = -1 * wayp_y
    elif angle == 270:
        helper = wayp_x
        wayp_x = +1 * wayp_y
        wayp_y = -1 * helper


def move_ship_to_wayp(movement):
    global curr_x, curr_y, wayp_y, wayp_x
    number = int(movement[1:])
    if movement.startswith("F"):
        curr_x += number * wayp_x
        curr_y += number * wayp_y


def reset():
    global curr_x, curr_y, curr_ortn, curr_dir
    curr_y = curr_x = curr_ortn = curr_dir = 0


def main():
    with open("Day12", 'r') as f:
        movements = f.read().splitlines()
    for movement in movements:
        move(movement)
    print("Part 1: ", abs(curr_x) + abs(curr_y))

    reset()

    for movement in movements:
        move_waypoint(movement)
        rotate_waypoint(movement)
        move_ship_to_wayp(movement)
    print("Part 2: ", curr_x, curr_y)


if __name__ == '__main__':
    main()
