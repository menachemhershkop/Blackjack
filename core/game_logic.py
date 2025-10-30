def calculate_hand_value(hand: list[dict]) -> int:
    if hand['rank'] == "Q" or hand['rank'] == "J" or hand['rank'] == "K":
        return 10
    elif hand['rank'] == "A":
        return 1
    return int(hand['rank'])
def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player.update(card1=deck.pop(),card2=deck.pop())
    dealer.update(card1=deck.pop(),card2=deck.pop())
    player_scour=0
    dealer_scour=0
    print(len(player))
    for i in player.values():
        print(i)
        player_scour+=calculate_hand_value(i)
    for i in dealer.values():
        dealer_scour += calculate_hand_value(i)
    print("Player scour is ", player_scour)
    print("dealer scour is", dealer_scour)
def dealer_play(deck: list[dict], dealer: dict) -> bool:
    dealer_scour=0
    while dealer_scour<= 17:
        dealer_hand=deck.pop()
        dealer_scour+=calculate_hand_value(dealer_hand)
    if dealer_scour >21:
        return True
    return True

