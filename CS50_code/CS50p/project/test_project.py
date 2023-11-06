import pytest
from project import creates_players, launch_game, define_human_players, Game, Player
from unittest.mock import patch


"""Tests function launch_game()"""
# Define test scenarios using pytest.mark.parametrize
@pytest.mark.parametrize("player_names", [
    (["Player1", "Player2"]),  # Test case 1
    (["Player1", "Player2", "Player3"]),  # Test case 2
    (["Player1", "Player2", "Player3", "Player4"])  # Test case 3
])
def test_launch_game(player_names):
    # Create a game instance with the provided player names
    game_instance = Game(player_names)

    # Use patch to simulate user input (Ctrl+D to exit)
    with patch("builtins.input", side_effect=[EOFError]):
        # Call the launch_game function and get the winner's name
        winner_name, remaining_dice = launch_game(game_instance)

    # Assert that the expected winner's name is one of the players and remaining dice is between [1,5]
    assert winner_name in player_names
    assert 1 <= remaining_dice <=5

"""Tests function creates_players()"""
def test_creates_players():
    # Define test cases

    # Test case 1: Valid input with at least 2 players
    input_values = ["Player1", "Player2", EOFError]
    with patch("builtins.input", side_effect=input_values):
        result = creates_players()
    assert isinstance(result, Game)

    # Test case 2: Invalid input with less than 2 players
    input_values = ["Player1", EOFError]
    with patch("builtins.input", side_effect=input_values):
        result = creates_players()
    assert result == -1

    # Test case 3: Simulate Ctrl+D (EOFError)
    with patch("builtins.input", side_effect=EOFError):
        result = creates_players()
    assert result == -1


"""Tests function creates_players()"""
def test_define_human_players():
    # Define test cases

    # Test case 1: No human players
    with patch("builtins.input", side_effect=["n"]):
        players_list = [Player("Player1"), Player("Player2"), Player("Player3")]
        result = define_human_players(players_list)
        assert result == []

    # Test case 2: One human player
    with patch("builtins.input", side_effect=["y", "y", "n", "n"]):
        players_list = [Player("Player1"), Player("Player2"), Player("Player3")]
        result = define_human_players(players_list)
        assert result == [0]

    # Test case 3: Multiple human players
    with patch("builtins.input", side_effect=["y", "y", "n", "y", "n", "y", "n"]):
        players_list = [Player("Player1"), Player("Player2"), Player("Player3"), Player("Player4"), Player("Player5"), Player("Player6")]
        result = define_human_players(players_list)
        assert result == [0, 2, 4]


# Run the tests
if __name__ == "__main__":
    pytest.main()

