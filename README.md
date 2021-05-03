# war_simulation
A simulation of the card game "war"

War Rules

Preparation
  1.	Shuffle the 52-card deck
  2.	Assign half the deck to player one and the other half to player two
	Gameplay begins
	With each turn there are two possibilities:
  1.	One player’s card is greater than the other.
      a.	The losing card is then placed on the bottom of the winning player’s deck followed by the winning card.
  2.  The cards are the same value.
      a.	Each player takes the top three cards from their deck and places them down in front of them facedown.
      b.	The following card is then used to determine who wins this round of war. The person who wins the round of war then takes all the cards at stake and places        them on the bottom of their pile in the order described in the first possibility (losing player card, winning player card, etc. until the card that                  determined who won war).
	Winning
	If a player has all 52 cards in their deck they win.

   Unique situations and how to play them
-	If war is currently in progress and the two players have the same value card again the war process is just repeated (placing three cards down and competing with the card thereafter).
-	If war is in progress and one player does not have any more cards to do war with (either they don’t have three cards to place down or they don’t have the fourth card to compete with) they automatically lose.
-	If extended war (a situation where the same value card continues to come up in war causing each player to place another three cards down until someone wins) is going on and both players’ do not have any more cards to play with the player with the most cards in their deck automatically wins.
-	There is also a very small possibility that each player has the same number of cards in their deck (which is always half the deck, 26) when the situation directly above happens which means the players will go into something I call, reverse war.
-	In reverse war, each player takes the last card they can use and compares it with the other player. This continues (taking the next last card and then the next, so on and so forth) until one player has a higher valued card than the other signifying a win for the one with the higher valued card.
-	In an even smaller chance, (something that never happened in any of this project’s simulations and is extremely improbable) if every single card compared in the reverse war is of the same value, then there is a draw. This is the only way to get a draw.

Important notes:
-	During a sequence of war that is all considered one turn. For example, if war begins on turn 15 and the cards being compared are the same value yet again then the placing down of another three cards and battling again is still a part of turn 15.
-	A deck’s strength is a summation of each card’s value (with ace being high) within a given deck. Numerically this means an ace was valued at 13, a two at 1, three at 2, and so and so forth. 

Information on how to change the code is all the way on the bottom in the comments. 

After running the simulations this program will give you the following:
- A win breakdown with how many times player one won, how many times player two won, and how many draws there were
- The percentage of times the stronger deck won
- A breakdown of the turns with: average turns per game, min, max, median, and range of turns and the values at the 10th, 25th, 75th, and 90th percentiles
- A histogram will pop up breaking down the turns taken in each game
