def ask_player_action() -> str:
    while True:
        player_choice=input("Enter your choice. H for HIT. S for STAND: ")
        answer= "s", "h", "S","H"
        if player_choice in answer:
            return player_choice.upper()

