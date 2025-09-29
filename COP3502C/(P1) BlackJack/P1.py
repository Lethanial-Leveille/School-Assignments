import p1_random as p1
rng = p1.P1Random()
def deal_card(l):
    my_number = rng.next_int(13) + 1
    if my_number == 1:
        print("Your card is a ACE!")
        return l + 1
    elif my_number == 11:
        print("Your card is a JACK!")
        return l + 10
    elif my_number == 12:
        print("Your card is a QUEEN!")
        return l + 10
    elif my_number == 13:
        print("Your card is a KING!")
        return l + 10
    else:
        for i in range(14):
            if i == my_number:
                print(f"Your card is a {i}!")
                return i + l
def dealers_hand():
    dealers_number = rng.next_int(11) + 16
    print(f"Dealer's hand: {dealers_number}")
    return dealers_number
def compare_hands(u,d):
    if d > 21 or u > d:
        print("You win!\n")
        return True
    elif d == 21 or d > u:
        print("Dealer wins!\n")
        return False
def statistics(p,d,t,n):
    print(f"Number of Player wins: {p}")
    print(f"Number of Dealer wins: {d}")
    print(f"Number of tie games: {t}")
    print(f"Total # of games played is: {n-1}")
    print(f"Percentage of Player wins: {round((p/(n-1)*100),1)}%\n")

play_blackjack = True
num_of_games = 1
win_count = 0
lose_count = 0
tie_count = 0
hand = 0
while play_blackjack:
    print(f"START GAME #{num_of_games}\n")
    hand = deal_card(hand)
    print(f"Your hand is: {hand}\n")
    keep_playing = True
    while keep_playing:
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit\n")
        menu = int(input("Choose an option: "))
        print("")
        if menu == 1:
            hand = deal_card(hand)
            print(f"Your hand is: {hand}\n")
            if hand > 21:
                print("You exceeded 21! You lose.\n")
                num_of_games+=1
                hand = 0
                lose_count += 1
                keep_playing = False
            elif hand == 21:
                print("BLACKJACK! You win!\n")
                num_of_games += 1
                hand = 0
                win_count += 1
                keep_playing = False
        elif menu == 2:
            d_hand = dealers_hand()
            print(f"Your hand is: {hand}\n")
            num_of_games += 1
            if hand == d_hand:
                print("It's a tie! No one wins!\n")
                tie_count += 1
            else:
                if compare_hands(u=hand,d=d_hand):
                    win_count +=1
                else:
                    lose_count +=1
            hand = 0
            keep_playing = False
        elif menu == 3:
            statistics(p=win_count,d=lose_count,t=tie_count,n=num_of_games)
        elif menu == 4:
            play_blackjack = False
            break
        else:
            print("Invalid input!\n")
            print("Please enter an integer value between 1 and 4.")


