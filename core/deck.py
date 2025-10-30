import random
def build_standard_deck() -> list[dict]:
    cards={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":1}
    suite=["H","C","D","S"]
    full_cards=[]
    for i in cards:
        for j in suite:
            full_cards.append({"rank":i,"suite":j})
    return full_cards

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    while swaps:
        first_card=random.randint(0,len(deck)-1)
        second_card=random.randint(0,len(deck)-1)
        if deck[first_card]['rank']!=deck[second_card]['rank']:
            if deck[first_card]['suite'] == "H":
                if second_card %5==0:
                    deck[first_card], deck[second_card] =deck[second_card], deck[first_card]
                    swaps-=1
                    continue
                continue
            elif deck[first_card]['suite'] == "C":
                if second_card % 3 == 0:
                    deck[first_card], deck[second_card] = deck[second_card], deck[first_card]
                    swaps -= 1
                    continue
                continue
            elif deck[first_card]['suite'] == "D":
                if second_card % 2 == 0:
                    deck[first_card], deck[second_card] = deck[second_card], deck[first_card]
                    swaps -= 1
                    continue
                continue
            elif deck[first_card]['suite'] == "S":
                if second_card % 7 == 0:
                    deck[first_card], deck[second_card] = deck[second_card], deck[first_card]
                    swaps -= 1
                    continue
                continue
            continue
    return deck
print(build_standard_deck()[1])