import numpy as np
import random
import matplotlib.pyplot as plt
import math as m

# Initial Deck Strength will be a sum of all the card values
# on a scale of 1 to 13 where 1 is a two card and 13 is an ace

# Numbers 1- 52 represent one of the 52 cards of the deck
# Order of deck:
# 1) Clubs
# 2) Hearts
# 3) Spades
# 4) Diamonds


def print_card_value(card):
    if card % 13 == 0:
        suit = (card // 13) - 1
    else:
        suit = (card // 13)

    value = card % 13 - 1

    card_suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
    card_values = [
        "Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
        "Eight", "Nine", "Ten", "Jack", "Queen", "King"
    ]

    print(card_values[value], "of", card_suits[suit])


def print_deck(deck):
    for i in range(len(deck)):
        print_card_value(deck[i])


# Card Strength Values
# Ace = 13
# 2 = 1
# 3 = 2
# 4 = 3
# 5 = 4
# 6 = 5
# 7 = 6
# 8 = 7
# 9 = 8
# 10 = 9
# Jack = 10
# Queen = 11
# King = 12


def card_strength(card):
    val = card % 13
    if val == 1:
        return 13
    elif val == 0:
        return 12
    else:
        return val - 1


def tot_deck_strength(deck):
    tot = 0
    for i in range(len(deck)):
        tot += card_strength(deck[i])

    return tot


def assign_retvals(a, b, c, d, e, f):
    retvals = []
    retvals.append(a)
    retvals.append(b)
    retvals.append(c)
    retvals.append(d)
    retvals.append(e)
    retvals.append(f)
    return retvals


def show_move(winner, turn, p1_card, p2_card):
    print("=================================")
    if winner == 1:
        print("Turn:", turn, "| Player 1 beats player 2")
    if winner == 2:
        print("Turn:", turn, "| Player 2 beats player 1")
    print("---------------------------------")
    print("Player 1 card:")
    print_card_value(p1_card)
    print("Player 2 card:")
    print_card_value(p2_card)


def no_shuffle_game_simulation(show_moves):
    # if show_moves == 1 then each move will be shown
    # function return vals:
    # retvals[0]:
    #   returns 1 if player 1 wins and returns 2 if player 2 wins
    #   returns 0 if there is a draw
    # retvals[1]:
    #   total turns in game
    # retvals[2]:
    #   player 1 initial deck strength
    # retvals[3]:
    #   player 2 initial deck strength
    # retvals[4]:
    #   player 1 deck (as a list)
    # retvals[5]:
    #   player 2 deck (as a list)

    deck = list(range(1, 53))
    random.shuffle(deck)

    # 26 is the middle value of the deck
    p1_deck = deck[:26]
    p2_deck = deck[26:]

    orig_p1_deck = p1_deck[:]
    orig_p2_deck = p2_deck[:]

    p1_deck_strength = tot_deck_strength(p1_deck)
    p2_deck_strength = tot_deck_strength(p2_deck)
    # p1_init_deck_strength.append(tot_deck_strength(p1_deck))
    # p2_init_deck_strength.append(tot_deck_strength(p2_deck))

    # Max of 5,000 turns to prevent an infinite loop
    for turns in range(5000):
        # if someone runs out of cards they have lost the game, other person
        # wins
        if len(p1_deck) == 0:
            return assign_retvals(2, turns, p1_deck_strength, p2_deck_strength,
                                  orig_p1_deck, orig_p2_deck)
        if len(p2_deck) == 0:
            return assign_retvals(1, turns, p1_deck_strength, p2_deck_strength,
                                  orig_p1_deck, orig_p2_deck)
        # Whenever someone wins the card they won goes on the bottom of the
        # deck first and then their personal card
        # p1 wins
        if (card_strength(p1_deck[0]) > card_strength(p2_deck[0])):
            p2_card = p2_deck.pop(0)
            p1_card = p1_deck.pop(0)
            p1_deck.append(p2_card)
            p1_deck.append(p1_card)
            if show_moves == 1:
                show_move(1, turns + 1, p1_card, p2_card)
        # p2 wins
        elif (card_strength(p1_deck[0]) < card_strength(p2_deck[0])):
            p1_card = p1_deck.pop(0)
            p2_card = p2_deck.pop(0)
            p2_deck.append(p1_card)
            p2_deck.append(p2_card)
            if show_moves == 1:
                show_move(2, turns + 1, p1_card, p2_card)
        # If one card is not greater than the other than they must go to war
        else:
            # while in war it is all considered a part of one turn
            if show_moves == 1:
                print("=================================")
                print("In war on turn", turns + 1)
            war = 1
            index = 4
            while war:
                # if a deck runs out of cards to do war with then the person
                # with the most cards would win
                if index >= len(p1_deck) and index >= len(p2_deck):
                    # if p1 has more cards then we give all the cards to p1
                    # signifying an automatic win
                    if len(p1_deck) > len(p2_deck):
                        war = 0
                        for i in range(len(p2_deck)):
                            p1_deck.append(p2_deck.pop(0))
                        if show_moves == 1:
                            print("War over")
                            print("Reason: Player 1 wins game due to larger"
                                  " deck after repeated cases of the same"
                                  " value card in war")
                    # if p2 has more cards then we give all the cards to p2
                    # signifying an automatic win
                    elif len(p1_deck) < len(p2_deck):
                        war = 0
                        for i in range(len(p1_deck)):
                            p2_deck.append(p1_deck.pop(0))
                        if show_moves == 1:
                            print("War over")
                            print("Reason: Player 2 wins game due to larger"
                                  " deck after repeated cases of the same"
                                  " value card in war")
                    # If they each have the same amount of cards then we go
                    # into more war
                    else:
                        war = 1
                        # index is -1 so we can work from the end of the deck
                        # to the beginning since we know that all cards are
                        # already out and being played and we must now go in
                        # reverse when we get to this branch
                        index = -1
                        while war:
                            # this if statement only checks the p1_deck since
                            # both decks are the same size in this else
                            # branch
                            if (abs(index) > len(p1_deck)):
                                # turns + 1 to count for turn currently on
                                return assign_retvals(0, turns + 1,
                                                      p1_deck_strength,
                                                      p2_deck_strength,
                                                      orig_p1_deck,
                                                      orig_p2_deck)
                            # p1 wins game because card has greater value
                            # and all cards were already at stake
                            if card_strength(p1_deck[index]) >\
                                    card_strength(p2_deck[index]):
                                war = 0
                                for i in range(len(p1_deck)):
                                    p1_deck.append(p2_deck.pop(0))
                                if show_moves == 1:
                                    print("War over")
                                    print("Reason: Player 1 wins game after"
                                          " comparing cards from the end since"
                                          " both players have same size decks"
                                          " and are deep in war")
                            # p2 wins game because card has greater value and
                            # all cards were already at stake
                            elif card_strength(p2_deck[index]) >\
                                    card_strength(p1_deck[index]):
                                war = 0
                                for i in range(len(p1_deck)):
                                    p2_deck.append(p1_deck.pop(0))
                                if show_moves == 1:
                                    print("War over")
                                    print("Reason: Player 2 wins game after"
                                          " comparing cards from the end since"
                                          " both players have same size decks"
                                          " and are deep in war")
                            index -= 1

                # p2_wins by default if there are no more cards in p1s deck to
                # to do war with
                elif index >= len(p1_deck):
                    war = 0
                    for i in range(len(p1_deck)):
                        p2_deck.append(p1_deck.pop(0))
                    if show_moves == 1:
                        print("War over")
                        print("Reason: Player 2 wins game after no more cards"
                              "to do war with in player 1's deck")
                # p1_wins by default if there are no more cards in p2 deck to
                # do war with
                elif index >= len(p2_deck):
                    war = 0
                    for i in range(len(p2_deck)):
                        p1_deck.append(p2_deck.pop(0))
                    if show_moves == 1:
                        print("War over")
                        print("Reason: Player 1 wins game after no more cards"
                              "to do war with in player 2's deck")
                # p1 wins the round of war
                elif (card_strength(p1_deck[index]) >
                        card_strength(p2_deck[index])):
                    war = 0
                    # cards at stake in war are added to p1's deck
                    for i in range(index + 1):
                        p1_deck.append(p2_deck.pop(0))
                        p1_deck.append(p1_deck.pop(0))
                    if show_moves == 1:
                        print("War over")
                        print("Reason: Player 1 wins after", index // 4,
                              "round(s) of war")
                # p2 wins the round of war
                elif (card_strength(p2_deck[index]) >
                        card_strength(p1_deck[index])):
                    war = 0
                    # cards at stake in war are added to p2's deck
                    for i in range(index + 1):
                        p2_deck.append(p1_deck.pop(0))
                        p2_deck.append(p2_deck.pop(0))
                    if show_moves == 1:
                        print("War over")
                        print("Reason: Player 2 wins after", index // 4,
                              "round(s) of war")
                # if no one wins then 3 more cards are laid out and the fourth
                # card is used for war which is why the index is increased by 4
                index += 4

    print(p1_deck)
    print(p2_deck)


def simulations(simulation_amt, show_moves):
    simulation_results = []
    # first value is how many simulations were run
    simulation_results.append(simulation_amt)
    for i in range(simulation_amt):
        simulation_results.append(no_shuffle_game_simulation(show_moves))

    return simulation_results

# function return vals (for reference):
# retvals[0]:
#   returns 1 if player 1 wins and returns 2 if player 2 wins
#   returns 0 if there is a draw
# retvals[1]:
#   total turns in game
# retvals[2]:
#   player 1 initial deck strength
# retvals[3]:
#   player 2 initial deck strength


def print_simulation_results(simulation_results):
    simulations_iter = simulation_results[0]
    p1_wins = 0
    p2_wins = 0
    draws = 0
    turns_list = []
    max_turns = 0
    min_turns = 5001
    total_turns = 0
    stronger_deck_wins = 0
    for i in range(simulations_iter):
        turns_list.append(simulation_results[i+1][1])
        total_turns += simulation_results[i+1][1]
        current_turns = simulation_results[i+1][1]

        if current_turns > max_turns:
            max_turns = current_turns
        if current_turns < min_turns:
            min_turns = current_turns

        if simulation_results[i+1][0] == 1:
            p1_wins += 1
            if simulation_results[i+1][2] > simulation_results[i+1][3]:
                stronger_deck_wins += 1
        elif simulation_results[i+1][0] == 2:
            p2_wins += 1
            if simulation_results[i+1][3] > simulation_results[i+1][2]:
                stronger_deck_wins += 1
        else:
            draws += 1

    average_turns_per_game = total_turns / simulations_iter
    stronger_deck_win_percentage = stronger_deck_wins / simulations_iter

    print("Win Breakdown\n")
    print("\tPlayer 1 Win(s):", p1_wins, "(",
          "{:.2%}".format(p1_wins / simulations_iter), ")")
    print("\tPlayer 2 Win(s):", p2_wins, "(",
          "{:.2%}".format(p2_wins / simulations_iter), ")")
    print("\tDraw(s):", draws, "\n")
    print("Percentage of Games the Stronger Deck Won:",
          "{:.2%}".format(stronger_deck_win_percentage))
    print("-------------------------------------------------")
    print("Breakdown of Turns in Game\n")
    print("\tAverage Turns per Game:", average_turns_per_game)
    print("\tMedian:", np.median(turns_list))
    print("\tMinimum:", min_turns)
    print("\tMaximum:", max_turns)
    print("\tRange:", max_turns - min_turns, "\n")
    print("\t10th percentile:", np.percentile(turns_list, 10))
    print("\t25th percentile:", np.percentile(turns_list, 25))
    print("\t75th percentile:", np.percentile(turns_list, 75))
    print("\t90th percentile:", np.percentile(turns_list, 90))

    x = list(range(0, max_turns, 200))
    # Data Visualization Section
    plt.hist(turns_list, bins=m.ceil(simulations_iter**0.5))
    plt.xticks(x)
    plt.show()


# USER-MODIFIABLE SECTION
# change first parameter in simulations function call to determine how many
# simulations are run
# If you want to run the simulation against your own list of values then you
# can make p1_deck and p2_deck set values (these lists are found in the
# function no_shuffle_game_simulation)
print_simulation_results(simulations(10000, 0))
