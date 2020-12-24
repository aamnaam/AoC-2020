def get_row(seat_id):
    row_id = seat_id[: 7]
    top = 127
    rear = 0
    for x in row_id:
        if x == 'F':
            top = int((top + rear + 1) / 2) - 1
        else:
            rear = int((top + rear + 1) / 2)
    return top


def get_column(seat_id):
    column_id = seat_id[7:]
    top = 7
    rear = 0
    for x in column_id:
        if x == 'L':
            top = int((top + rear + 1) / 2) - 1
        else:
            rear = int((top + rear + 1) / 2)
    return top


def main():
    seat_ids = open("Seats").readlines()
    max_number = 0
    all_seats = []
    for each_id in seat_ids:
        seat_number = get_row(each_id) * 8 + get_column(each_id)
        all_seats.append(seat_number)
    all_seats.sort()
    print(f"Part 1: {all_seats[-1]}")
    for x in range(0, len(all_seats)):
        if all_seats[x+1] != all_seats[x]+1:
            print(f"Part 2: {all_seats[x]+1}")
            break


main()
