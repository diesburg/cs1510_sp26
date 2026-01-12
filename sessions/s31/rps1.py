"""
Random rps game from student submissions
"""

import random

def get_user_weapon():
    human_choice = input("Please enter your weapon choice:")

    # error checking loop
    while human_choice != "r" and human_choice != "p" and human_choice != "s" and human_choice != "q":
        print("ERROR. That's not a valid choice.")
        human_choice = input("Please enter your weapon choice:")

    return human_choice

def get_weapons():
    ai_choice = random.choice(["r","p","s"])
    human_choice = get_user_weapon()

    return ai_choice, human_choice

def process_winner(ai_choice,human_choice, total_rcounter,total_ties,total_h_wins,total_c_wins):
    if ai_choice == "r" and (human_choice == "r" or human_choice == "R"):
        print("TIE. Both picked R")
        total_rcounter = total_rcounter + 1
        total_ties = total_ties + 1
                            
    elif ai_choice == "s" and (human_choice == "s" or human_choice == "S"):
        print("TIE. Both picked S")
        total_rcounter = total_rcounter + 1
        total_ties = total_ties +1

    elif ai_choice == "p" and (human_choice == "p" or human_choice == "P"):
        print("TIE. Both picked P")
        total_rcounter = total_rcounter + 1
        total_ties = total_ties + 1

    elif ai_choice == "r" and (human_choice == "p" or human_choice == "P"):
        print("HUMAN WINS! Human pick: p Computer pick: r")
        total_rcounter = total_rcounter + 1
        total_h_wins = total_h_wins + 1

    elif ai_choice == "s" and (human_choice == "r" or human_choice == "R"):
        print("HUMAN WINS! Human pick: r Computer pick: s")
        total_rcounter = total_rcounter + 1
        total_h_wins = total_h_wins + 1

    elif ai_choice == "p" and (human_choice == "s" or human_choice == "S"):
        print("HUMAN WINS! Human pick: s Computer pick: p")
        total_rcounter = total_rcounter + 1
        total_h_wins = total_h_wins + 1
              
    elif ai_choice == "r" and (human_choice == "s" or human_choice == "S"):
        print("COMPUTER WINS! Human pick: s Computer pick: r")
        total_rcounter = total_rcounter + 1
        total_c_wins = total_c_wins + 1

    elif ai_choice == "p" and (human_choice == "r" or human_choice == "R"):
        print("COMPUTER WINS! Human pick: r Computer pick: p")
        total_rcounter = total_rcounter + 1
        total_c_wins = total_c_wins + 1

    elif ai_choice == "s" and (human_choice == "P" or human_choice == "p"):
        print("COMPUTER WINS! Human pick: p Computer pick: s")
        total_rcounter = total_rcounter + 1
        total_c_wins = total_c_wins + 1

    return total_rcounter,total_ties,total_h_wins,total_c_wins

def main():
    total_rcounter = 0
    total_ties = 0
    total_h_wins = 0
    total_c_wins = 0
    human_choice = "a"
        
    print("Each round you must select from one of the following weapons")
    print(" Enter r for rock")
    print(" Enter p for paper")
    print(" Enter s for scissors")
    print(" Enter q to quit")


    # list of options for rps results

    while not human_choice == "q":
        print()
        
        #Get weapons
        ai_choice, human_choice = get_weapons() 
        
       
        if human_choice == "q":
            break
        
        #Play the game
        total_rcounter,total_ties,total_h_wins,\
            total_c_wins = process_winner(ai_choice,human_choice, \
            total_rcounter, total_ties,total_h_wins,total_c_wins)

           

    # ends program when input is equal to q
    if human_choice =="q":
        print("Thanks for playing.")
        print("We played a total of", total_rcounter ,"times")
        print("Total ties =", total_ties)
        print("Total wins for human =", total_h_wins)
        print("Total wins for computer =", total_c_wins)


