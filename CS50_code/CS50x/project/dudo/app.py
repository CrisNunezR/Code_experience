import os
import random
import math
import inspect

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from flask import jsonify

from helpers import apology, login_required
from datetime import datetime
from dudo import Game



# Configure application
app = Flask(__name__)

# Custom filter
#app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# global variables
global active_sessions
active_sessions = {} # global variable to store the active sessions
global game
global game_id

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///dudo.db")

# Defines machine players
global number_machine_players
global all_players_list

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        active_sessions[session["user_id"]] = True

        # Redirect user to home page
        return redirect("/new_game")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""
    # Remove the user from the active_sessions dictionary
    if session.get("user_id") in active_sessions:
        del active_sessions[session["user_id"]]

    # Forget any user_id
    session.clear()
    # Redirect user to login form
    return redirect("/login")

#register a new user
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # check if reqached via POST -> a username and password were entered
    if request.method == "POST":

        user = request.form.get('username').strip()
        password = request.form.get('password').strip()
        pwd_confirm = request.form.get('confirmation').strip()

        if password == "":
            return apology("Must provide a password", 400)

        if user == "":
            return apology("Must provide username", 400)

        if password != pwd_confirm:
            return apology("Password confirmation does not match", 400)

        #print("register() line 124: db.execute("SELECT username FROM users WHERE username = ?;", user)[0]['username']")
        try:
            user_db = db.execute("SELECT username FROM users WHERE username = ?;", user)[0]['username'].strip()
        except:
            #all checks passed, hash pwd and insert user in users table and redirect to login
            hashpass = generate_password_hash(password)
            db.execute("INSERT INTO users (username, score, hash) values(?, ?, ?);", user, 100, hashpass)
            return render_template("login.html")
        else:
            if user_db == user:
                return apology("Username taken, please choose a different one", 400)
            else:
                #all checks passed, hash pwd and insert user in users table and redirect to login
                hashpass = generate_password_hash(password)
                db.execute("INSERT INTO users (username, cash, hash) values(?, ?, ?);", user, 10000, hashpass)
                return render_template("login.html")
    else:
        return render_template("register.html")

#change password of registered user
@app.route("/change_pwd", methods=["GET", "POST"])
@login_required
def change_pwd():
    """Change password"""

    if request.method == "POST":

        #check current password
        curr_pwd_user =  request.form.get('curr_pwd')
        if not check_password_hash(db.execute("SELECT hash FROM users WHERE id = ?;", session["user_id"])[0]['hash'], curr_pwd_user):
            return apology("Wrong current password")

        new_pwd = request.form.get('new_pwd')

        if new_pwd == curr_pwd_user:
            return apology("New password equal to former")

        #update hash_value with new password
        new_hashpass = generate_password_hash(new_pwd)
        db.execute("UPDATE users SET hash = ? where id = ?;", new_hashpass, session["user_id"])
        return render_template("login.html")

    else:
        user = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])[0]['username']
        return render_template("change_pwd.html", user = user)

@app.route("/new_game", methods=["GET", "POST"])
@login_required
def new_game():

    # Check if the user is logged in
    if session.get("user_id") is None:
        # User is not logged in, redirect to the login form
        return redirect("/login")

    # Get the number of active sessions (logged-in users)
    num_logged_in_users = len(active_sessions)

    # if no users logged in, execute logout and go to login (to control errors)
    if num_logged_in_users == 0:
        #print(f"new_game() line 184: no users logged in")
        if session.get("user_id") in active_sessions:
            del active_sessions[session["user_id"]]
            # Forget any user_id
            session.clear()
            # Redirect user to login form
            #print("new_game() line 190: should redirect to login")
        return redirect("/login")

    if request.method == "POST":
        # Render the template and pass num_logged_in_users to it
        if request.form.get("auto_players") != "":
            auto_players_needed = max(0, 4 - num_logged_in_users) # min number of players is 4
            #print("new_game() line 197: getting non-null message from form")
            try:
                number_auto_players = int(request.form.get("auto_players").strip())
            except:
                return apology(f"Must enter integer value of at least {auto_players_needed}", 403)

            if number_auto_players < auto_players_needed:
                return apology(f"Must enter integer value of at least {auto_players_needed}", 403)

            global number_machine_players
            number_machine_players = number_auto_players

            return redirect("/start_game")

        return render_template("new_game.html", human_players = num_logged_in_users)
    else:
        return render_template("new_game.html", human_players = num_logged_in_users)

@app.route("/start_game")
@login_required
def start_game():

    #global number_machine_players
    machine_players = []
    for i in range(number_machine_players):
        player_name = "Auto player " + str(i+1)
        machine_players.append(player_name)

    """*********** INITIAL SET UP  ***********"""

    # get names of human players. Since active_sessions contains the active players in the form { 1: True, 2: True, 3: False}
    active_ids = [session_id for session_id, is_active in active_sessions.items() if is_active]
    if len(active_ids) > 1:
        ids_str = ', '.join(map(str, ids))      # convert the list into comma separated string
    elif len(active_ids) == 1:
        ids_str = active_ids[0]
    else:
        raise ValueError('No human players')    # notice that with this I'm not allowing solo machine games
    query = f"SELECT username FROM users WHERE id IN ({ids_str})"
    human_usernames = [row['username'] for row in db.execute(query)]

    # create a list of all the players in the game, both human and machines
    global all_players_list
    all_players_list = human_usernames + machine_players

    # randomise the list of players
    random.shuffle(all_players_list)

    print(f"start_game() line 245: {all_players_list}")         # **********************************************************

    # Create instance of Game class with all players' names
    print('start_game() line 248: all good up to 247')          # **********************************************************
    global game
    game = Game(all_players_list)

    # mark human players (automate players are defined by default)
    for index in range(len(all_players_list)):
        if all_players_list[index] in human_usernames:
            game._players[index].type = 'human'

    """*********** BEGIN ROUNDS ***********"""
    # define initial values ************************************
    total_curr_dice = game.dice_in_game()
    bet, suit = game._current_bet

    game.shuffle_new_hand()
    #if game.players_in_game() == 1:
    #    winner = [player_instance.name for player_instance in game._players if player_instance.status][0]
    #    previous_bets = db.execute("SELECT username, bet FROM bets WHERE game_id = ?;", game_id)
    #    render_template("game_end.html", winner = winner, previous_bets = previous_bets)

    # define game id
    global game_id
    game_id_str = db.execute("SELECT max(game_id) FROM bets;")
    print(f"start_game() line 271: max game id: {game_id_str[0]['max(game_id)']}")               # **********************************************************
    if game_id_str[0]['max(game_id)'] is not None:
        game_id = int(game_id_str[0]['max(game_id)']) + 1
    else:
        game_id = 1

    # show own hand to human player
    this_id_str = session.get("user_id")                                  # only human players have sessions
    query = f"SELECT username FROM users WHERE id IN ({this_id_str})"
    human_username = [row['username'] for row in db.execute(query)]
    #print(f"start_game() line 281: {human_username}")
    this_player_idx = all_players_list.index(human_username[0])
    #print(f"start_game() line 283: {player_idx}")
    own_hand = game._players[this_player_idx].hand

    # execute automate routine to get bets and record them
    while game._players[game._current_bidder_index].type != 'human' and game.players_in_game() > 1:
        non_human_bet(bet, suit, total_curr_dice)

    if game.players_in_game() == 1:
        winner = [player_instance.name for player_instance in game._players if player_instance.status][0]
        previous_bets = db.execute("SELECT username, bet FROM bets WHERE game_id = ?;", game_id)
        render_template("game_end.html", winner = winner)

    # go to page to get bet from human user and loop
    next_player = all_players_list[game.valid_next_player_index(game._current_bidder_index)]
    prev_bettor_idx = game.valid_previous_player_index(game._current_bidder_index)      # notice that current_bidder is equivalent to this_player_idx since we only show updates for human players
    current_bettor = game._players[prev_bettor_idx].name

    # update values before showing on page
    bet, suit = game._current_bet
    current_nbr_players = game.players_in_game()
    total_curr_dice = game.dice_in_game()

    # Get infor for previous bets table
    previous_bets = db.execute("SELECT username, bet FROM bets WHERE game_id = ?;", game_id)

    if bet == 0 and suit == 0:
        current_bet = "No bets yet"
    else:
        current_bet = f"{bet} dice of suit {suit} by {current_bettor}"

    return render_template("in_round.html", current_bet = current_bet, total_players = current_nbr_players, total_dice = total_curr_dice, next_player=next_player, own_hand = own_hand, previous_bets = previous_bets)


def non_human_bet(bet,suit, total_dice):
    """function to simulate bet for non-human players"""

    global game_id

    curr_idx = game._current_bidder_index

    # get action from automate player
    action, new_bet, new_suit = game._players[curr_idx].make_bet(bet, suit, total_dice)
    bet_ = str(new_bet) + " of " + "suit: " + str(new_suit)

    #register bet in db
    username = game._players[curr_idx].name
    print(f"non_human_bet() line 329: {username}")                                                  # **********************************************************


    print(f"non_human_bet() line 332: {action} by {game._players[game._current_bidder_index].name}")         # **********************************************************
    match action:
        case 'raise':
            db.execute("INSERT INTO bets (username, game_id, bet, time_stamp) values (?,?,?,?);", username,game_id,bet_,datetime.now())
            game.place_bet(new_bet, new_suit)                           # this updates game.bet and game._player.index
        case 'call':
            bet_ = "called: " + bet_
            db.execute("INSERT INTO bets (username, game_id, bet, time_stamp) values (?,?,?,?);", username,game_id,bet_,datetime.now())
            loser_idx, count_suit = game.call_bet(new_bet, new_suit)
            loser_txt = f"lost a die. There were {count_suit}" if game._players[loser_idx].status == True else f"Left game. There were {count_suit}"
            db.execute("INSERT INTO bets (username, game_id, bet, time_stamp) values (?,?,?,?);", game._players[loser_idx].name,game_id,loser_txt,datetime.now())
            game._current_bet = (0,0)
            if game.players_in_game() == 1:
                print(f"non_human_bet() line 344: We got a winner!")
                winner = [player_instance.name for player_instance in game._players if player_instance.status][0]
                previous_bets = db.execute("SELECT username, bet FROM bets WHERE game_id = ?;", game_id)
                return render_template("game_end.html", winner = winner, previous_bets = previous_bets)

            game.shuffle_new_hand()



@app.route("/in_round", methods=["GET", "POST"])
@login_required
def in_round():

    # define current state of the game to populate in_round.html information
    global game_id
    global game
    curr_bet, curr_suit = game._current_bet
    curr_active_players = game.players_in_game()
    total_active_dice = game.dice_in_game()
    next_player = game._players[game.valid_next_player_index(game._current_bidder_index)].name
    own_hand = game._players[game._current_bidder_index].hand
    current_bettor = game._players[game._current_bidder_index].name
    previous_bets = db.execute("SELECT username, bet FROM bets WHERE game_id = ?;", game_id)

    if curr_bet == 0 and curr_suit == 0:
        current_bet = "No bets yet"
    else:
        current_bet = f"{curr_bet} dice of suit {curr_suit} by {game._players[game.valid_previous_player_index(game._current_bidder_index)].name}"

    print(f'in_round() line 373')
    call_action = False
    # check that only current human bettor can place the bet (not other human players whose turn has not come yet)
    # if session.get("user_id") !=

    if request.method == "POST":
        new_bet_str = request.form.get('bet').strip()
        new_suit_str = request.form.get('suit').strip()

        print(f"test call button: {call_action}")

        # check if human player challenged the previous bet
        call_action_form = request.form.get("call")
        call_action = call_action_form == "True"
        print(f"test call button after: {call_action}")

        if call_action:
            print(f"went into call_action with call_action={call_action}" )
            username = game._players[game._current_bidder_index].name
            bet_ = str(curr_bet) + " of " + "suit: " + str(curr_suit)
            bet_ = "called: " + bet_
            db.execute("INSERT INTO bets (username, game_id, bet, time_stamp) values (?,?,?,?);", username,game_id,bet_,datetime.now())
            loser_idx, count_suit = game.call_bet(curr_bet, curr_suit)
            loser_txt = f"lost a die. There were {count_suit}" if game._players[loser_idx].status == True else f"Left game. There were {count_suit}"
            db.execute("INSERT INTO bets (username, game_id, bet, time_stamp) values (?,?,?,?);", game._players[loser_idx].name,game_id,loser_txt,datetime.now())

            if game.players_in_game() == 1:
                print(f"in_round() line 393: We got a winner!")
                winner = [player_instance.name for player_instance in game._players if player_instance.status][0]
                previous_bets = db.execute("SELECT username, bet FROM bets WHERE game_id = ?;", game_id)
                db.execute("INSERT INTO games (game_id, winner_name) VALUES (?, ?);", game_id, winner)
                return render_template("game_end.html", winner = winner, previous_bets = previous_bets)
            else:
                # if current human player lost challenge, reload in_round
                # if current human player won the challenge, check player that lost and
                    # call in_round if human player
                    # execute non_human_bet if not human (consider that next player will be human since we call it from here so we'll execute only once)

                # shuffle new round
                game._current_bet = (0,0)
                game.shuffle_new_hand()

                bet, suit = game._current_bet
                total_dice = game.dice_in_game()

                # current player not-human reload until player is human
                while game._players[game._current_bidder_index].type != 'human':
                    non_human_bet(bet,suit, total_dice)

                # update  data
                prev_bettor_idx = game.valid_previous_player_index(game._current_bidder_index)
                current_bettor = game._players[prev_bettor_idx].name
                bet, suit = game._current_bet

                # this needs to be checked if automate player placed a bet before
                if suit == 0:
                    current_bet = "No bets yet"
                else:
                    current_bet = f"{bet} dice of suit {suit} by {prev_bettor_idx}"

                next_player = all_players_list[game.valid_next_player_index(game._current_bidder_index)]
                own_hand = game._players[game._current_bidder_index].hand

                # update values before showing on page
                current_nbr_players = game.players_in_game()
                total_curr_dice = game.dice_in_game()

                # Get infor for previous bets table
                previous_bets = db.execute("SELECT username, bet FROM bets WHERE game_id = ?;", game_id)

                return render_template("in_round.html", current_bet = current_bet, total_players = current_nbr_players, total_dice = total_curr_dice, next_player=next_player, own_hand = own_hand, previous_bets = previous_bets)

        print(f'did not go into call action. call action={call_action}')

        # load new bet by player
        try:
            new_bet = int(new_bet_str)
            new_suit = int(new_suit_str)
        except ValueError:
            return render_template("in_round.html", current_bet=current_bet, total_players = curr_active_players, total_dice = total_active_dice, next_player=next_player, own_hand = own_hand, previous_bets = previous_bets)

        # Validate new bet

        # if changing TO Ases, are they larger than 1/2 previous bet + 1?
        if new_suit == 1 and curr_suit != 1:
            if new_bet < (math.floor(curr_bet/2) + 1):
                print('in_round() line 431: test 1')
                return render_template("in_round.html", current_bet=current_bet, total_players = curr_active_players, total_dice = total_active_dice, next_player=next_player, own_hand = own_hand, previous_bets = previous_bets)

        # if changing FROM Asses to other suit, is bet larger than double + 1?
        if curr_suit == 1 and new_suit != 1:
            if new_bet < (curr_bet*2 + 1):
                print('in_round() line 437: test 2')
                return render_template("in_round.html", current_bet=current_bet, total_players = curr_active_players, total_dice = total_active_dice, next_player=next_player, own_hand = own_hand, previous_bets = previous_bets)

        # same suit, is bet larger than previous bet?
        if curr_suit == new_suit:
            if new_bet <= curr_bet:
                print('in_round() line 449: test 3')
                return render_template("in_round.html", current_bet=current_bet, total_players = curr_active_players, total_dice = total_active_dice, next_player=next_player, own_hand = own_hand, previous_bets = previous_bets)

        # change suit, new_suit must be larger and bet must be at least equal to current
        if curr_suit != new_suit and new_suit !=1:
            if new_suit < curr_suit:
                print('in_round() line 455: test 4')
                return render_template("in_round.html", current_bet=current_bet, total_players = curr_active_players, total_dice = total_active_dice, next_player=next_player, own_hand = own_hand, previous_bets = previous_bets)
            # if new suit is larger, bet must be at least as large as current
            else:
                if new_bet < curr_bet:
                    print('in_round() line 460: test 5')
                    return render_template("in_round.html", current_bet=current_bet, total_players = curr_active_players, total_dice = total_active_dice, next_player=next_player, own_hand = own_hand, previous_bets = previous_bets)

        print(f"in_round() line 463: raised bet by {game._players[game._current_bidder_index].name}")
        # resgister new bet on record
        username = game._players[game._current_bidder_index].name
        bet_ = str(new_bet) + " of " + "suit: " + str(new_suit)
        db.execute("INSERT INTO bets (username, game_id, bet, time_stamp) VALUES (?,?,?,?);", username,game_id,bet_,datetime.now())

        # update Game instance and define new player
        game.place_bet(new_bet, new_suit)

        print('in_round() line 472: ready for next player')
        # new loop until next human player
        while game._players[game._current_bidder_index].type != 'human' and game.players_in_game() > 1:
            bet, suit = game._current_bet
            non_human_bet(bet, suit, game.dice_in_game())

        if game.players_in_game() == 1:
            print(f"in_round() line 479: We got a winner!")
            winner = [player_instance.name for player_instance in game._players if player_instance.status][0]
            previous_bets = db.execute("SELECT username, bet FROM bets WHERE game_id = ?;", game_id)
            db.execute("INSERT INTO games (game_id, winner_name) VALUES (?, ?);", game_id, winner)
            return render_template("game_end.html", winner = winner, previous_bets = previous_bets)

        # go to page to get bet from human user and loop
        next_player = all_players_list[game.valid_next_player_index(game._current_bidder_index)]
        prev_bettor_idx = game.valid_previous_player_index(game._current_bidder_index)      # notice that current_bidder is equivalent to this_player_idx since we only show updates for human players
        current_bettor = game._players[prev_bettor_idx].name

        # update values before showing on page
        bet, suit = game._current_bet
        current_nbr_players = game.players_in_game()
        total_curr_dice = game.dice_in_game()
        own_hand = game._players[game._current_bidder_index].hand

        # Get infor for previous bets table
        previous_bets = db.execute("SELECT username, bet FROM bets WHERE game_id = ?;", game_id)

        if bet == 0 and suit == 0:
            current_bet = "No bet yet"
        else:
            current_bet = f"{bet} dice of suit {suit} by {current_bettor}"

        return render_template("in_round.html", current_bet = current_bet, total_players = current_nbr_players, total_dice = total_curr_dice, next_player=next_player, own_hand = own_hand, previous_bets = previous_bets)


@app.route("/history")
@login_required
def hall_of_fame():
    """Show history of winners"""
    winners = db.execute('SELECT winner_name, COUNT(*) AS count FROM games GROUP BY winner_name;')

    return render_template("history.html", players_scores = winners)


@app.route("/test", methods=["GET", "POST"])
def test():

    if request.method == "POST":
        call = False
        # Get the updated test value from the form submission
        updated_test = int(request.form.get("test"))

        # manage the call button
        updated_test = int(request.form.get("test"))
        print(f"updated button: {updated_test}")

        # Get the 'call' value from the form submission
        call = request.form.get("call")
        print(f"test call button: {call}")

        # Perform further actions with the updated test value
        # For example, you can update a database or perform any necessary processing here

        # After processing, you can render a response or redirect to another page
        return render_template("test.html", test=updated_test)

    # If it's a GET request, simply render the template with the current test value
    test = 1  # You can set the initial value of the test variable here
    return render_template("test.html", test=test)
