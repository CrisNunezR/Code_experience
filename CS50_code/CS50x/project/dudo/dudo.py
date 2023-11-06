import random
import math
from collections import Counter

#global variables
global min_prob, die_faces, dice_prob, init_dice_per_player, luck_dial, max_prob
min_prob = 0.25                 # minimum probability to call a bet
die_faces = 6
dice_prob = 1/die_faces
init_dice_per_player = 5
luck_dial = [True, False]       # initially set for 50%. Can also be [True, True, False] if feeling 'more lucky'
max_prob = 0.3



class Game:
    def __init__(self, names_list=None):
        """ Initialize players, current bet and total dice number
            self_players represents a list of instances of Player class
        """
        self._players = []
        player_class = []
        for name in names_list:
            player_class.append(self.add_player(name, init_dice_per_player))
        self._players = player_class
        self._current_bidder_index = 0
        self._current_bet = (0, 0)                                  # Initialise current_bet as a (0, 0)=(number, dice suit)
        self.total_dice = len(self._players)*init_dice_per_player   # Initialise total dice as 5 (or number defined) per player

    @property
    def players(self):
        return self._players

    @players.setter
    def players_names(self, names_list=None):
        """Assigns a list of class Player instances to the Game class instance either using user inputs or a given list"""
        player_class=[]
        for name in names_list:
            player_class.append(self.add_player(name, init_dice_per_player))
        self._players = player_class # Game._players is a list of Player instances

    def add_player(self, name=None, num_dice=init_dice_per_player):
        """creates instances of Player class and returns it"""
        return Player(name, num_dice)

    def start_round(self):
        """ Code to start a new round """

        #first shuffle if current bet == initial bet (0,0)
        num_dice, suit_value = self._current_bet
        if self._current_bet == (0,0):
            self.shuffle_new_hand()
        else:
            # define the player to bet and call method to bet
            bidder_index = self.valid_previous_player_index(self._current_bidder_index)
            print(f"Game.start_round() line 56: Current bet by {self._players[bidder_index].name}: suit {suit_value} repeats {num_dice} time(s) in {self.total_dice}.")

        action, new_dice_bet, new_suit_value = self._players[self._current_bidder_index].make_bet(num_dice, suit_value, self.total_dice)

        match action:
            case 'call':
                self.call_bet(num_dice, suit_value)

            case 'raise':
                """increase bet"""
                self.place_bet(new_dice_bet, new_suit_value)

            #case 'pass':
            #    #pass bet to next player
            #    self._current_bidder_index += 1 # bid goes to next player

        return sum(1 for player_instance in self._players if player_instance.status==True) #returns number of players still in the game

    def players_in_game(self):
        return sum(1 for player_instance in self._players if player_instance.status==True)

    def dice_in_game(self):
        return sum(player_instance.dice_in_hand for player_instance in self._players if player_instance.status==True)

    def shuffle_new_hand(self):
        """shuffle every active player's han and prints the number of players in the round and total dice in play"""
        players_in_game = sum(1 for player_instance in self._players if player_instance.status==True)
        print(f"Game.shuffle_new_hand() line 83: New round! {self.total_dice} dice and {players_in_game} player(s) in the game")
        for player_instance in self._players:
            if player_instance.status:                                                                                  # only valid players are shuffled
                player_instance.shuffle()
                player_instance.freq()

    def valid_previous_player_index(self, _current_bidder_index):
        """finds the previous valid player (who normally placed the current bet)"""
        current_index = _current_bidder_index
        n = len(self._players)
        for _ in range(n):
            current_index = (current_index - 1) % n     # Move to the next index
            if self._players[current_index].status:            # Valid player?
                return current_index
        return ValueError("No valid players in Game")

    def valid_next_player_index(self, _current_bidder_index):
        """finds the next valid player"""
        current_index = _current_bidder_index
        n = len(self._players)
        for _ in range(n):
            current_index = (current_index + 1) % n            # Move to the next index
            if self._players[current_index].status:            # Valid player?
                return current_index
        return ValueError("No valid players in Game")

    def place_bet(self, num_dice, suit_value):
        # Code to place a (new) bet
        self._current_bet = num_dice, suit_value
        self._current_bidder_index = self.valid_next_player_index(self._current_bidder_index) # bid goes to next player

    def call_bet(self, num_dice, suit_value):
        # Code to call the previous bet
        print(f"Game.call_bet() line 116: {self._players[self._current_bidder_index].name} calls the bet. Wins if there's fewer than {num_dice} dice of suit {suit_value} in the game.")
        count_suit = self.reveal_hands(suit_value) + self.reveal_hands(1) if suit_value != 1 else self.reveal_hands(1)
        self.show_hands()
        print(f"Game.call_bet() line 119: There were {count_suit} dice of suit {suit_value}.")
        if count_suit >= num_dice:
            loser_index = self._current_bidder_index
        else:
            loser_index = self.valid_previous_player_index(self._current_bidder_index)

        self._players[loser_index].decrease_die()           # notice that this also removes the player from the game if they have only 1 die
        self.total_dice -= 1
        self._current_bet = (0,0)                           # reinitialises bid to start another round
        if not self._players[loser_index].status:           # assigns next valid player if current player leaves the game
            self._current_bidder_index = self.valid_next_player_index(loser_index)
        return loser_index, count_suit

    def show_hands(self):
        # shows all the hands of active players
        print(f"Game.show_hands() line 134")
        for player in self._players:
            if player.status:
                print(f"Player {player.name} has {player.show_hand()}")

    def reveal_hands(self, suit_value):
        # Code to reveal hands and return the count of the real frequency of bidded suit in the game
        count_bid_suit = 0
        for player in self._players:
            if player.status == True:
                count_bid_suit += player._freq[suit_value]
        return count_bid_suit

    def reveal_winner(self):
        # Code to end the current round, show the winner and reinitialise bet to (1,1) to allow for new shuffle
        count = sum(1 for player_instance in self._players if player_instance.status==True)
        if count == 1:
            winner = [player.name for player in self._players if player.status][0]
            remaining_dice = [player.dice_in_hand for player in self._players if player.name == winner][0]
            #print(f"Player {winner} wins with {remaining_dice} dice remaining.")
            return winner, remaining_dice
        else:
            #print(f"Error: Game not finished as there's {count} players in the game still")
            return -1, -1

############################################################################
class Player:
    def __init__(self, name, num_dice=init_dice_per_player, type='automate'):
        self.name = name
        self.dice_in_hand = num_dice
        self.status = True                  # True: Player IN the Game | False: Player OFF the game
        self._freq = Counter()
        self.type = type

    def shuffle(self):
        """shuffles randomly the hand of the Player's instance"""
        self.hand = [random.randint(1,die_faces) for _ in range(self.dice_in_hand)]  # List of  objects

    def show_hand(self):
        """returns the hand of the Player's instance"""
        return self.hand

    def freq(self):
        """calculates its frequency histogram in _freq"""
        self._freq = Counter(self.hand)
        return self._freq                                                           # notice that this is used only if we print the method

    def make_bet(self, num_dice, suit_value, total_dice):
        """ Places bets based on probability:
            1st: calculates the probability of the bet received
            2nd: if prob is < glogal min_prob (25%) call the bet, else raise the bet
            3rd: To raise the bet, define whether to increase the suit or the dice_number
            4th: if increase in number, increase randomly up to probability + 10%
                if suit, increase randomly if suit is lower than 6
            """
        #request bet from user if Player.type == 'human'
        if self.type == 'human':
            if suit_value == 0:
                action = 'bet'
                print(f"Player.make_bet() line 193: {self.name}, your hand is {self.hand}, place your bet.")
            else:
                print(f"Player.make_bet() line 195: {self.name}, remember that your hand is {self.hand}.")
                action = input(f"Will you 'call' the current bet or make a new 'bet'? ").lower().strip()
                while action not in ['call', 'bet']:
                    action = input("Please enter just 'call' or 'bet': ").lower().strip()

            if action == 'call':
                return ('call', num_dice, suit_value)
            elif action == 'bet':
                while True:
                    try:
                        suit_value = int(input("    Enter suite [values 1 to 6]: ").strip())
                        if 0 < suit_value <= 6:
                            break
                    except ValueError:
                        print("Please enter only positive integers.")

                while True:
                    #num_dice = 1 if num_dice == 0 else num_dice
                    try:
                        new_bet = int(input(f"    Enter number of dice values ]{num_dice} to {total_dice}]: ").strip())
                        if num_dice < new_bet <= total_dice:
                            break
                    except ValueError:
                        print("Please enter only positive integers.")

                return ('raise', new_bet, suit_value)

        elif self.type == 'automate':
            if suit_value == 0:
                """if first bet in the round, make bet based on player's hand"""
                my_strongest_suit, freq_stronger_suit = self._freq.most_common()[0]
                new_suit = my_strongest_suit
                new_bid = self.increase_max(my_strongest_suit, freq_stronger_suit, total_dice - self.dice_in_hand) if self.feel_lucky() else freq_stronger_suit
                return ('raise', new_bid, new_suit)

            #calculates the prob of having {num_dice} - {at-hand} of the same {suit_value} in {total_dice} throws,
            in_hand = self._freq[suit_value] + self._freq[1] if suit_value != 1 else self._freq[suit_value] # number of dice for the given suit needed on the rest of the dice (considering that '1' or Ases are wildcards)

            dice_needed = max(0, num_dice - in_hand)                # avoids possibility of calculating fact(negative number)
            rem_dice = total_dice - self.dice_in_hand

            #if dice needed from the rest of players is more than they have, call the bet
            if rem_dice < dice_needed:
                return ('call', num_dice, suit_value)

            prob = self.calc_prob(suit_value, dice_needed,rem_dice)
            if in_hand >= num_dice:
                """player has in hand more than the current bid"""
                return ('raise', *self.raise_bet(num_dice, suit_value, total_dice, prob))           #notice the need to unpack result from "raise_bet"
            else:
                #if prob of current bet is lower than predefined minimum {min_prob}, then call the bet
                if prob < min_prob:
                    return ('call', num_dice, suit_value)
                else:
                    return ('raise', *self.raise_bet(num_dice, suit_value, total_dice, prob))   #notice the need to unpack result from "raise_bet"

    def raise_bet(self, curr_bid, curr_suit, total_dice, prob):
        """
            Checks player's hand. If the frequency in hand of my strongest suit is larger than the current bid, change the bidding suit
            Otherwise, if the prob that the rest of the players have enough of my strongest suite to increase the bid is larger than current bet,
            then increase the bet.
            Additionally, include a 'feel lucky' function to randomly increase to the max or by 1 dice the current bid
        """
        in_hand = self._freq[curr_suit]
        my_strongest_suit, freq_stronger_suit = self._freq.most_common()[0]

        # first check that my strongest suit is higher that current suit (otherwise I can't switch)
        if my_strongest_suit <= curr_suit:
            new_proposed_bid = self.increase_max(curr_suit, curr_bid, total_dice - self.dice_in_hand)
            new_bid = (curr_bid + 1) if new_proposed_bid <= curr_bid else new_proposed_bid
            return new_bid, curr_suit

        # else, check if it makes sense to change suit
        if freq_stronger_suit <= curr_bid:
            # I don't have a clearly better hand, need to assess

            # if I'm changing from 1s (Ases) I need to evaluate the prob of changing to double + 1
            if curr_suit == 1 and my_strongest_suit != 1:
                prob_strongest_suit = self.calc_prob(my_strongest_suit,curr_bid*2+1 - freq_stronger_suit, total_dice - self.dice_in_hand)
            else:
                prob_strongest_suit = self.calc_prob(my_strongest_suit,curr_bid - freq_stronger_suit, total_dice - self.dice_in_hand)

            if prob_strongest_suit <= prob:
                # My suit is not better bet that current suit. Increase bid according to 'perceived' luck
                new_suit = curr_suit
                new_proposed_bid = self.increase_max(curr_suit, in_hand, total_dice - self.dice_in_hand)
                new_bid = (curr_bid+1) if new_proposed_bid <= curr_bid else new_proposed_bid
                if not (new_bid > curr_bid and self.feel_lucky()):
                    new_bid = curr_bid + 1
            else:
                # My suit is better bet than current suit -> change suit and increase bet according to 'preceived' luck
                new_suit = my_strongest_suit
                new_proposed_bid = self.increase_max(my_strongest_suit, freq_stronger_suit, total_dice - self.dice_in_hand)
                new_bid = (curr_bid + 1) if new_proposed_bid <= curr_bid else new_proposed_bid
                if not (new_bid > curr_bid and self.feel_lucky()):
                    new_bid = curr_bid + 1
        else:
            # If I have a stronger game in hand than current bid, change the bidding suit
            new_suit = my_strongest_suit
            new_bid = self.increase_max(my_strongest_suit, freq_stronger_suit, total_dice - self.dice_in_hand) if self.feel_lucky() else curr_bid + 1

        return new_bid, new_suit

    def increase_max(self, suit, curr_bid, others_dice):
        """increases the bet up to a max according to a predefined threshold"""
        new_bid = curr_bid
        if curr_bid >= others_dice:     # this can happen when a player has too many dice against his/her oponents
            return new_bid
        else:
            while self.calc_prob(suit, new_bid, others_dice) > max_prob:
                new_bid += 1
            return new_bid

    def feel_lucky(self):
        return random.choice(luck_dial)

    def calc_prob(self, suit, num_of_dice, total_dice):
        """calculates the probability of having at least {num_of_dice} repetitions of a given suit in a total of {total_dice} throws"""
        """ NOTICE: this probability assumes that the suit we are testing for is not 1(As) """
        p = dice_prob
        less_than_x_prob = sum(math.comb(total_dice, k) * (p**k) * ((1 - p)**(total_dice - k)) for k in range(num_of_dice))
        at_least_x_prob = 1 - less_than_x_prob
        # now, to include the suit '1' as a wildcard, if we assume the suit we look for X != 1
        # remember that prob(X + Y) = prob(X) + prob(Y) - prob(X)*prob(Y) but if X cannot be 1, then prob(X)*prob(Y)=0
        # and prob(X + Y) = prob(X) + prob(Y)
        if suit == 1:
            final_prob = at_least_x_prob
        else:
            final_prob = 2*at_least_x_prob
        return final_prob

    def decrease_die(self):
        """decreases dice of player by one or leaves the game"""
        if self.dice_in_hand == 1:
            self.dice_in_hand = 0
            self.status = False
            print(f"Player.decrease_die() line 331:Player {self.name} left the game\n")
        else:
            self.dice_in_hand -= 1
            print(f"Player.decrease_die() line 334: Player {self.name} loses a die and now has {self.dice_in_hand}.\n")

    def increase_die(self):
        """If player bids for exactly a given number of dice (not fewer than), they can earn a die"""
        """this will not be implemented yet"""
        if self.dice_in_hand < init_dice_per_player:
            self.dice_in_hand += 1
        else: print(f"Player.increase_die() line 341: Can't increase dice number")