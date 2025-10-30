def build_standard_deck() -> list[dict]:
    cards={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":1}
    suite=["H","C","D","S"]
    full_cards=[]
    for i in cards:
        for j in suite:
            full_cards.append({"rank":i,"suite":j})
    return full_cards
def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    pass