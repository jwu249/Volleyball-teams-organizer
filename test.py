import csv
import random

# Helper function that reads the CSV file
def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

# Helper function to write out the teams
def write_teams_csv(teams, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for team_name, players in teams.items():
            writer.writerow([team_name])
            for player in players:
                writer.writerow([player])
            writer.writerow([])

def assign_teams(players):
    # Initialize teams
    teams = {'Team 1': [], 'Team 2': [], 'Team 3': [], 'Team 4': [], 'Team 5': [], 'Team 6': []}

    # Initialize positions
    positions = {
        'Setter': 1,
        'Outside': 2,
        'Right Side': 1,
        'Libero': 1,
        'Middle': 1
    }

    # Separate players based on their preferred positions
    players_by_position = {position: [] for position in positions}
    for player in players:
        position = player['Preferred Position 🫡 (There is no guarantee of the choice as more people might join the teams)']
        if position in positions:
            players_by_position[position].append(player)
    print(players_by_position)

    # Assign 1 setter to each team
    for team_name, players in teams.items():
        setter = [player for player in players_by_position['Setter'] if player not in sum(teams.values(), [])]
        if setter:
            teams[team_name].append(setter.pop())

    # Assign 2 outsides to each team
    for team_name, players in teams.items():
        outsides = [player for player in players_by_position['Outside'] if player not in sum(teams.values(), [])]
        if len(players) < 3:
            while len(players) < 3 and outsides:
                teams[team_name].append(outsides.pop())

    # Assign 1 right side to each team
    for team_name, players in teams.items():
        right_side = [player for player in players_by_position['Right Side'] if player not in sum(teams.values(), [])]
        if len(players) < 4 and right_side:
            teams[team_name].append(right_side.pop())

    # Assign 1 libero to each team
    for team_name, players in teams.items():
        libero = [player for player in players_by_position['Libero'] if player not in sum(teams.values(), [])]
        if len(players) < 5 and libero:
            teams[team_name].append(libero.pop())

    # Assign 1 middle to each team
    for team_name, players in teams.items():
        middle = [player for player in players_by_position['Middle'] if player not in sum(teams.values(), [])]
        if len(players) < 6 and middle:
            teams[team_name].append(middle.pop())

    # Add remaining players to teams with unfilled positions
    for team_name, players in teams.items():
        while len(players) <= 6:
            for position, player_list in players_by_position.items():
                if len(players) <= 6:
                    for player in player_list:
                        if player not in sum(teams.values(), []):
                            teams[team_name].append(player)
                            player_list.remove(player)
                            break

    # Swap players based on who they want to play with
    for team_name, players in teams.items():
        for i, player in enumerate(players):
            if player['Any one you want to be on the same team with? (Limited to 1 other)']:
                preferred_partner = player['Any one you want to be on the same team with? (Limited to 1 other)']
                for other_player in players:
                    if other_player['Full Name'] == preferred_partner and other_player['Preferred Position 🫡 (There is no guarantee of the choice as more people might join the teams)'] == player['Preferred Position 🫡 (There is no guarantee of the choice as more people might join the teams)']:
                        players[i], players[players.index(other_player)] = other_player, player

    return teams


def main():
    input_file = 'Competitive - VolleybAAAll Night 03_21 (Responses) - Form Responses 1.csv'
    output_file = 'volleyball_teams.csv'

    players = read_csv(input_file)
    random.shuffle(players)  # Shuffle players to randomize the order of teams
    teams = assign_teams(players)
    write_teams_csv(teams, output_file)

if __name__ == "__main__":
    main()
