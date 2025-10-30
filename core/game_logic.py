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
    print("Player scour is ", player)
    print("dealer scour is", dealer)
def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while dealer['hand']<= 17:
        dealer['hand']+=calculate_hand_value(deck.pop())
    if dealer['hand'] >21:
        print("dealer score is", dealer['hand'],"dealer if falls, you win!!!")
        return False
    print(dealer)
    return True
def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck,player,dealer)
    player_scour=0
    sre=0
    while True:
        game=ask_player_action()
        if game =="H":
            player_hand=deck.pop()
            print(player_hand)
            player_scour+=calculate_hand_value(player_hand)
            print((player_scour))
            if player_scour >21:
                print("Game Over...")
                break
            continue
        if game =="S":
            deal=dealer_play(deck,dealer)
            if not deal:
                print(deal)
                break
            if deal:
                if player_scour >sre:
                    print("player is won")
                    break
                if player_scour<sre:
                    print("dealer is won")
                    break
                else:
                    print("tie")
                    break
        break