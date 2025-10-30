from core.deck import build_standard_deck, shuffle_by_suit
from core.game_logic import deal_two_each, dealer_play

if __name__=='__main__':
    # deal_two_each(shuffle_by_suit(build_standard_deck()),{},{})
    dealer_play(shuffle_by_suit(build_standard_deck()),{})