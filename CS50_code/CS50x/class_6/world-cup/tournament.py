# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000

def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # TODO: Read teams into memory from file
    knockout_teams_file = sys.argv[1]  # reads the file stated in prompt

    with open(knockout_teams_file) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ",") #delivers a Dic

        for i in csv_reader:
            new_value = {'team': i['team'], 'rating': int(i['rating'])}
            teams.append(new_value)

    # TODO: Simulate N tournaments and keep track of win counts

    #initialize counts{} dic
    counts = {}
    for i in range(N):
        winner = simulate_tournament(teams)
        if winner in counts:
            counts[winner] = counts[winner] + 1
        else:
            counts[winner] = 1

    #print("Results for", N, " simulations")
    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")



def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])
    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO

    #simulates a round defining all the winners
    #teams_at_play = len(teams)

    #winners = []
    #1st round (16 teams)
    #winners = simulate_round(teams)

    #2nd round (8 teams)
    #winners = simulate_round(winners)

    #3rd round (4 teams)
    #winners = simulate_round(winners)

    winners = teams
    while len(winners) > 2:
        winners = simulate_round(winners)

    #final (2 teams)
    bool = simulate_game(winners[0], winners[1])

    if bool == True:
        return winners[0]['team']
    else:
        return winners[1]['team']


    #recursive call
    #if teams_at_play > 2:
    #    simulate_tournament((simulate_round(teams)))
    #else:
    #    if (simulate_game(teams[0], teams[1])) == True:
    #        return (teams[0])
    #    else:
    #        return (teams[1])


if __name__ == "__main__":
    main()
