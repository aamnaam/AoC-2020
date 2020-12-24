with open('Day22', 'r') as f:
    data = f.read().split('\n\n')

my_hand = crab_hand = []


def set_hands():
    global my_hand, crab_hand
    my_hand = list(map(int, data[0].split(':')[1].split()))
    crab_hand = list(map(int, data[1].split(':')[1].split()))


def combat_game():
    while my_hand and crab_hand:
        my_card = my_hand.pop(0)
        crab_card = crab_hand.pop(0)
        if my_card > crab_card:
            my_hand.extend([my_card, crab_card])
        else:
            crab_hand.extend([crab_card, my_card])


def count_points(winner_hand):
    total = 0
    winner_hand.reverse()
    for i, card_val in enumerate(winner_hand):
        total += (i + 1) * card_val
    return total


def declare_winner():
    if my_hand:
        print("You win with", count_points(my_hand), "points")
    else:
        print("Crab wins with", count_points(crab_hand), "points")


def recursive_game(hand1, hand2):
    games = set()
    while hand1 and hand2:
        if (game_state := tuple(hand1 + ['+'] + hand2)) in games:
            return [1], []
        else:
            games.add(game_state)

        c1 = hand1.pop(0)
        c2 = hand2.pop(0)

        if len(hand1) >= c1 and len(hand2) >= c2:
            sub1_cards, sub2_cards = recursive_game(hand1[:c1], hand2[:c2])
            if sub1_cards:
                hand1.extend([c1, c2])
            else:
                hand2.extend([c2, c1])
        elif c1 > c2:
            hand1.extend([c1, c2])
        elif c2 > c1:
            hand2.extend([c2, c1])
    return hand1, hand2


def main():
    global my_hand, crab_hand
    set_hands()
    combat_game()
    print("Game 1:")
    declare_winner()

    set_hands()
    my_hand, crab_hand = recursive_game(my_hand, crab_hand)
    print("Game 2:")
    declare_winner()


if __name__ == '__main__':
    main()
