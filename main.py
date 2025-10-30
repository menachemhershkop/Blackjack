from core.deck import build_standard_deck, shuffle_by_suit
# from core.game_logic import deal_two_each, dealer_play, run_full_game

from core.game_logic import deal_two_each, run_full_game

if __name__=='__main__':
    cards=build_standard_deck()
    deck=shuffle_by_suit(build_standard_deck())
    player={"hand":[]}
    dealer={"hand":[]}
    run_full_game(deck,player,dealer)
