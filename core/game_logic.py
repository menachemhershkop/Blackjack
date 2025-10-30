def calculate_hand_value(hand: list[dict]) -> int:
    if hand['rank'] == "Q" or hand['rank'] == "J" or hand['rank'] == "K":
        return 10
    elif hand['rank'] == "A":
        return 1
    return int(hand['rank'])
def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    pass
def dealer_play(deck: list[dict], dealer: dict) -> bool:
    pass

