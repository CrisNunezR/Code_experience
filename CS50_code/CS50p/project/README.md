# DUDO - A GAME OF CHANCE WITH DICE
#### Video Demo:  <https://youtu.be/KOWwtoYpBCc>
#### Description:
**_DUDO_** (meaning 'doubt' in Spanish) is a popular dice game in Chile. Though the rules somewhat vary depending on who you play it with, the basic idea doesn’t change much.

Usually played between 4 to 10 people (though there’re no rules on the maximum number of players, it tends to get messier with more than 10 players), each of which gets a sort of non-translucent cup (generally made of leather) -which is called **_cacho_**- and 5 six-sided dice.

![this is a cacho](cacho.jpg)

To begin the game, all players roll their dice within the lethear cup and hide the resulting hand within it from the rest of the players. Hence, each player is allowed to see just their own hand (not the other players’).

With that, one player begins betting on how many dice of a given suit he/she defines are there between all the players. For example, a player might say: “There are 10 dice of suit 2 in the game”. The next player has to either increase the bet or call the one he/she received. If a bet is called, all the players show their hands to count how many dice of the betted suit are in the game. If there were fewer dice, the player who made the bet loses a dice. If there were at least as many dice as the bet, the player who called the bet loses one die. The game continues until only one player remains with dice in hand, who is then declared the winner.

The code I prepared simulates a simplified version of the game that:
*   allows as many players as the user wants
*   allows for dice with more than 6 sides
*   allows for players to be human or simulated by the computer
*   simulated players follow certain rules based on the probability of bets

Some of the rules that define the behaviour of simulated players are:
*   when a simulated player receives a bet it calculates the probability of having at least as many dice as the bet states for that given suit in the number of dice held by the rest of the players (considering those in his/her own hand)

>Calculating the probability of a bet deserves a separate section. Having exactly '*x*' repetitions of a given suit within '*n*' dice (or, equivalently, '*n*' throws of the same die) can be defined by the following combinatorial equation:
>$$P(X=x) = \binom{n}{x}p^x(1-p)^{(n-x)}$$
> Where '*p*' is the probability if having '*x*' when thowing a die one time which, for a fair 6-sided die is 1/6.
>But we need the probability of having '**_x or more_**' dice, so we actually need to calculate this equation:
>$$P(X>=x) = 1 - \sum_{i=1}^{x}\binom{n}{x}p^x(1-p)^{(n-x)}$$
>The 'calc_prob' method in the Player class calculates this probability.


*   if the probability of having at least as many dice is lower than a given **minimum** value (defined by the **global variable min_prob** as 25%), the simulated player will call the bet
*   if the calculated probability is not lower than the threshold defined by **min_prob**, the simulated player will **increase the bet**.
>To increase the bet, the simulated player uses a method that:
>*   analyses its own hand,
>*  evaluates if it makes sense to change the suit by a suit in its hand (if the probability of the strongest suit in its hand is larger than the probability of the current suit in the bet), or keet the current suit in the bet, and
>*  increases the bet either by one die or, if the simulated player **_feels lucky_** (which is simulated by another method that  randomly choses a value from the global variable 'luck_dial' which is a list of "True" and "False" values in a combination that defines the "**appetite for risk**" of the simulated player, currently set resembling a coin toss, i.e. ["True", "False"]), it increases the beet up to the moment where the probability of having that many dice in the total of the dice in play falls below 30% (this 30% is hardcoded)

This way, the game can be played by just simulated players or with as many human players as the user decides.

#### Code details:

Although the code uses 3 functions separate from the main() function, I preferred to implement most of its code compenents in 2 classes: **Player** and **Game**.

I decided to use classes instead of functions because they are better suited for elements that will need characteristics and actions which will also have different values per instance of those clases. With this structure it is easier to have different players to a game and different games playing in parallel.

First, let's describe the **3 functions**:

*   **creates_players()**: is a function that receives no parameters, but prompts the user for names for as many players as he/she wants to participate in a game. This function uses '*Control+d*' to terminate players input and controls that at least 2 players are entered (testing this function with pytest proved somewhat complicated as we'll see later on).

*   **define_human_players**([list of players]): this function receives a list containing the player names that the used entered using '*creates_players()*' and begins by asking the user if there're human players or he/she wants to simulate a whole game with just automatic players. In case there are human players in the list, the function continues asking the user to define if the player is human or not by going through all the players's list. This function controls that values entered by the user are just 'y' or 'n'.

*   **launch_game**([Game class instance]): this function receives an instance of the Game class and controls the end of that game by validating that there's only one player in the game (which happens when all other players lost their dice).

Now let's review the **2 classes** that compose the core of the code:

###   **class Game**

This class controls the flow of the game. It can receive a list of players' names as argument and contains **4 attributes**:

*   **_players**: has a list of instances of class Player, one for each player in the game (be it human or simulated).
*   **_current_bidder_index**: that stores the player that made the curreent bet as an index of the _players list.
*   **_current_bet**: that stores the current bet as a a pair containing (number, suit). This value is initialised as (0,0) to identify the beginning of a new round (start of the game or after a player loses a die and dice are shuffled again).
*   **total_dice**: stores the current number of dice in the game between all players.

This class also has the following **methods**:

*   **players_names()**: is a setter for the _players attribute. If the Game class is used without a list of players' names, this method prompts the user for players' names. Then, this method populates the _players attribute creating class Player instances using either a list of names given to the Game class or entered by the user. This might be somewhat redudant given the function '*creates_players()*' but I decided to maintain this method since it allows the use of the code without the that function if needed. Notice that this method does not consider human players, though. Notice that there's also a getter method 'players()'

*   **add_player()**: is simply used to create an instance of class Player for a given player name and quantity of dice. This method is used with a for loop to populate the _players attribute when initialising the Game class (\__init\__).

*   **start_round()**: this is the core function of the class. It triggers the shuffle of the dice -using method shuffle_new_hand()- request the current player for an action (either call a bet or increase it) using the '*make_bet*' method of the Player class, executes that action and **returns the number of players in the game**. This last value allows the definition of a loop that calls this function as long as there's more than 1 player still in the game. The method also prints out the current bet and the name of the player that made it as a reminder to all players.

*   **shuffle_new_hand()**: this method shuffles the remaining dice for every player still in the game. This is method triggers 2 methods in the Player class: 'shuffle()' and 'freq()' that limits the dice to shuffle to only the remaining dice for each player and calculates how many times every suit is repeated in a player's hand, respectively. The method also remainds all players of the start of a new round and how many dice are still in the game.

*   **valid_next_player_index()**: this method is used to change the turn of player's making a bet during the game while keeping score of those players that left the game (by losing all their dice). Notice that this method uses the Modulo Operator to efficienly move through the _players attribute.

*   **valid_previous_player_index()**: this method is mainly used to define the player to lose a dice when a bet is called and there aren't as many dice as stated by the bet. This also needs to control for players that left the game before the current round. Since this player is also the one making the current bet, this method is used to remaind the rest of the players who's making the present bet.

*   **place_bet()**: is simply used to update the current bet in the instance of the Game class and move the bet to the next player.

*   **call_bet()**: this method shows to the rest of the players (prints out) that the current player called the bet and calls the method 'reveal_hands()' to define how many repetitions there are for the betted suit. Then it defines who the loser player is, calls the Player class '*decrease_die()*' for that player's instance, decreases the total dice in the game by 1, reinitialises the bet to (0,0) and assigns the next player if current player loses his/her last die and leaves the game.

*   **reveal_hands()**: counts how many times a given suit is repeated in the dice of the active players.

*   **reveal_winner()**: validates that there's only one last player active and returns his/her name and the number of dice he/she still has in hand.


###   **class Player**

This class controls every player's actions and defines how simulated players act. It has **5 attributes**:

*   **name**: stores the name of the player
*   **dice_in_hand**: stores the remaining dice the player has (initially 5 by default).
*   **status**: defines if the player is still actinve in the game (True) or has left the game by losing all of his/her dice (False).
*   **_freq**: defines the type of player as 'human' or 'automate'.

The class has also the following **methods**:

*   **shuffle()**: shuffles the remaining dice in hand for the player by randomly selecting a value between 1 and 6 as many times as there are dice in the player's hand (defined by the 'dice_in_hand' attribute) and then assings the values as a list to the **hand** attribute of the current instance player.

*   **show_hand()**: this method simply returns the attribute **hand** of the instance. I decided to use it instead of just calling the attribute to have a clearer name and be able to easily show more information if needed.

*   **freq()**: this method uses the Counter library to calculate the frequency with which every die is repeated in the player's hand.

*   **make_bet()**: this method, together with raise_bet() and increase_max(), are the heart of the code. It controls the new bet for human players, limiting suit values between 1 and 6 and repetitions to bet requesting that the value be higher than the current bet's. It also request the human player for his/her action (either 'call' or 'bet').
For 'automate' or 'machine' players, this method defines whether to call the bet (if the probability of there being at least as many dice as the bet is lower than 25%) or to raise it (when the player has enough dice of that suit in hand or when the probability of having that many dice in total is high enough -higher than 25%). Something I'll try to include later is to have some perception of the behaviour of other players during the game in order to define how much the automate player should 'believe' in their bets. At the moment, reviewing the probability of the hand does not really take into account what the players (humen) have been betting during the game or whether they have been caught lying. This will be something intesting to include.

*   **raise_bet()**:for non-human players, this method reviews the player's hand and defines if it's strong enough to change the betted suit (now defined as when the strongest suit of the player has more repetitions than what the current betted suit states) or continue with the current suit. It also defines whether to increase the bet by just 1 die or increase it enough to make the probability of having that many dice in the whole game is lower than 30% (this is done using the 'increase_max()' method). One thing I enjoyed was including a random definition for when the automate player does this in the "feel_lucky" method.

*   **increase_max()**: this method uses the '**calc_prob**' method to increase the betted quantity of a given suit until the probability of having that many dice in the game falls below 30% (this 30% at the moment is defined as a global variable called **_'max_prob'_**).

*   **feel_lucky()**: this is a very simple method that uses a list with a combination of True and False values to define whether the automate player 'feels lucky' by randomly choosing one value between them. Thus, with ['True', 'False'] the player is not a risk taker or conservative... but we can change this by adding more 'True' (to make it more more of a risk taker) or more 'False' (to make it more conservative).

*   **calc_prob()**: this method calculates the probability of having at least some repetition of a given dice in a total. This is used considering the repetitions that the bet would need excluding the ones that the player has in hand.

*   **decrease_die()**: this method reduces the attribute '**dice_in_hand** for that instance of Player by one and turns the attribute '**status**' to False if the player loses his/her last die. It also tells all the players when the current player leaves the game.

*   **increase_die()**: this method does the opposite of 'decrease_die'. It increases the number of dice in the player's hand up to the max defined (by dafault 5). This is done when a player guesses correctly the nnumber of repetitions of a suit in the whole game. This is not used at the moment as this option is not yet included in this version of the game.

*   **\__str\__**: I included this method to have an easy way to look at a player while developing the code.

###   **Testing the code with Pytest**

To test the functions we need to simulate entries by a user.
After looking around for ways to do this, I found the unittest.mock library and its 'patch' component. These allows us to simulate entries including a '**_Ctrl+d_**' command using "**side_effect=[EOFError]**" with **_patch_**.

Notice that 'side_effect' does not differentiate when there are sequential entries with different 'input' commands, so we need to include all the entries in the sequence that we want to test. For example, if I wanted to test the '*define_human_players*' function, which asks first if there are 'human players' in the game and *then* asks the user to define which players are human and which are simulated by going through all the players, we will need to include 'y' first to answer whether there are indeed human players in the game and then 'y' or 'n' for every player in the game.

So, to simulate entries for a game with 3 players with the first of them being a human player, we will need to use this **side_effect=["y", "y", "n", "n"].**