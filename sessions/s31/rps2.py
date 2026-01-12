"""
Random rps game from student submissions
"""
import random

def get_user_input():
    human_choice = input("Please enter your weapon choice:").lower()

    # error checking loop
    while human_choice != "r" and human_choice != "p" \
          and human_choice != "s" and human_choice != "q":
        print("ERROR. That's not a valid choice.")
        human_choice = input("Please enter your weapon choice:").lower()

    return human_choice

def process_outcome(ai_choice,human_choice,total_rcounter,total_ties,total_h_wins,total_c_wins):
    if ai_choice == "r" and (human_choice == "r"):
        print("TIE. Both picked R")
        total_rcounter = total_rcounter + 1
        total_ties = total_ties + 1
                            
    elif ai_choice == "s" and (human_choice == "s"):
        print("TIE. Both picked S")
        total_rcounter = total_rcounter + 1
        total_ties = total_ties +1

    elif ai_choice == "p" and (human_choice == "p"):
        print("TIE. Both picked P")
        total_rcounter = total_rcounter + 1
        total_ties = total_ties + 1

    elif ai_choice == "r" and (human_choice == "p"):
        print("HUMAN WINS! Human pick: p Computer pick: r")
        total_rcounter = total_rcounter + 1
        total_h_wins = total_h_wins + 1

    elif ai_choice == "s" and (human_choice == "r"):
        print("HUMAN WINS! Human pick: r Computer pick: s")
        total_rcounter = total_rcounter + 1
        total_h_wins = total_h_wins + 1

    elif ai_choice == "p" and (human_choice == "s"):
        print("HUMAN WINS! Human pick: s Computer pick: p")
        total_rcounter = total_rcounter + 1
        total_h_wins = total_h_wins + 1
              
    elif ai_choice == "r" and (human_choice == "s"):
        print("COMPUTER WINS! Human pick: s Computer pick: r")
        total_rcounter = total_rcounter + 1
        total_c_wins = total_c_wins + 1

    elif ai_choice == "p" and (human_choice == "r"):
        print("COMPUTER WINS! Human pick: r Computer pick: p")
        total_rcounter = total_rcounter + 1
        total_c_wins = total_c_wins + 1

    elif ai_choice == "s" and (human_choice == "p"):
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
        
        ai_choice = random.choice(["r","p","s"])
        
        human_choice = get_user_input()
       
        if human_choice == "q":
            break
        
        total_rcounter,total_ties,total_h_wins, \
total_c_wins = process_outcome(ai_choice, \
            human_choice,total_rcounter,total_ties,total_h_wins,total_c_wins)
           

    # ends program when input is equal to q
    if human_choice =="q":
        print("Thanks for playing.")
        print("We played a total of", total_rcounter ,"times")
        print("Total ties =", total_ties)
        print("Total wins for human =", total_h_wins)
        print("Total wins for computer =", total_c_wins)

main()
