from core.player_io import ask_player_action


def calculate_hand_value(hand: list[dict]) -> int:
    if hand['rank'] == "Q" or hand['rank'] == "J" or hand['rank'] == "K":
        return 10
    elif hand['rank'] == "A":
        return 1
    return int(hand['rank'])

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player['hand'] =calculate_hand_value(deck.pop())
    player['hand'] += calculate_hand_value(deck.pop())
    dealer['hand']=calculate_hand_value(deck.pop())
    dealer['hand'] += calculate_hand_value(deck.pop())
    print("Player points is ", player)
    print("dealer points is", dealer)


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while dealer['hand']<= 17:
        dealer['hand']+=calculate_hand_value(deck.pop())
    if dealer['hand'] >21:
        print("dealer score is", dealer['hand'],"dealer if falls, you win!!!")
        return False
    print("dealer have", dealer['hand'], "scour. let's chek who win")
    return True


def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck,player,dealer)
    while True:
        game=ask_player_action()
        if game =="H":
            player_hand=calculate_hand_value(deck.pop())
            print("the cars is", player_hand)
            print("The value of the card is", player_hand)
            player['hand']+=player_hand
            print(f"pleyer hes {player['hand']} points")
            if player['hand'] >21:
                print("Game Over...")
                break
            elif player['hand']==21:
                print("you win with 21 points!!!")
                break
            continue

        if game =="S":
            deal=dealer_play(deck,dealer)
            if not deal:
                break
            if deal:
                if player['hand'] >dealer['hand']:
                    print("player is won")
                    break
                if player['hand']<dealer['hand']:
                    print(f'You heve {player['hand']} points th dealer hes {dealer['hand']}. ')
                    print("dealer is won")
                    break
                else:
                    print("You both have the same of points")
                    break
        break