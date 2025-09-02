# ROCK PAPER SICSSOR GAME
'''
Cases:
A- Rock
Rock - Paper = tie
Rock - Paper = Paper win
Rock - scissor = Rock wine

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper Scissor win
'''

import random 

item_List = ['Rock','Paper','Scissor']

print("--- --- --- ROCK PAPER SCISSOR GAME --- --- ---")
print("===============================================")
while True:
        
    user_choice = input("\nEnter your move (Rock✊ - Paper✋ - Scissor✌️) or (exit): ").lower()
    comp_choice = random.choice(item_List)


    print(f"User choice = {user_choice.title()}, Computer choice = {comp_choice}")


    if user_choice == comp_choice.lower():
        print("Both chooses same: Match Tie!")

    elif user_choice == "rock":
        if comp_choice == "paper":
            print("Paper covers Rock: Computer win")
        else:
            print("Rock smashes Scissor: You win")
    elif user_choice == "paper":
        if comp_choice.lower() == "scissor":
            print("Scissor cuts Paper: Computer win")
        else:
            print("Paper covers Rock: You win")

    elif user_choice == "scissor":
        if comp_choice.lower() == "rock":
            print("Rocks smashes Scissor: Computer win")
        else:
            print("Scissor cuts Paper: You win")
    elif user_choice == "exit":
        print("GoodBye! Thanks for playing 😊")
        break
    else:
        print("Invalid Input! Make sure you enter valid option.")
