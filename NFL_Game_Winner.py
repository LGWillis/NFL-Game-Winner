# NFL Game Winner Predictor
# This program predicts the likely winner of an NFL game based on team odds to win the conference and make the playoffs.
# The odds are represented as a dictionary where the key is the combined preseason odds that team has to win their conference and make the playoffs
# and the value is the team name.

team_list = {-425: "Buffalo Bills", 3690: "Miami Dolphins",
              3645: "New England Patriots", 8000: "New York Jets", 
              -175: "Baltimore Ravens", 710: "Cincinnati Bengals", 
              10800: "Cleveland Browns", 2140: "Pittsburgh Steelers", 
              1255: "Houston Texans", 5200: "Indianapolis Colts", 
              4170: "Jacksonville Jaguars", 15425: "Tennessee Titans", 
              1070: "Denver Broncos", -100: "Kansas City Chiefs", 
              5340: "Las Vegas Raiders", 1070: "Los Angeles Chargers", 
              3260: "Dallas Cowboys", 8100: "New York Giants", -80: "Philadelphia Eagles", 
              700: "Washington Commanders", 1770: "Chicago Bears", 360: "Detroit Lions", 
              365: "Green Bay Packers", 995: "Minnesota Vikings", 3145: "Atlanta Falcons", 
              6250: "Carolina Panthers", 10600: "New Orleans Saints", 
              1335: "Tampa Bay Buccaneers", 3120: "Arizona Cardinals", 865: "Los Angeles Rams", 
              665: "San Francisco 49ers", 3165: "Seattle Seahawks"}

# Prompt user to enter two NFL teams
def get_team():
    global NFL_1, NFL_2
    NFL_1 = str(input("Enter the full name of team one: "))
    NFL_2 = str(input("Enter the full name of team two: "))
    NFL_1 = NFL_1.lower().title()
    NFL_2 = NFL_2.lower().title()

# Function to verify that the teams entered match a team in team_list and are not the same
def verify_nfl_team():
    if NFL_1 == NFL_2:
        print("Please enter two different teams")
        return get_team()
    elif NFL_1 not in team_list.values() or NFL_2 not in team_list.values():
        print("Please enter valid NFL Teams like the example provided.")
        return get_team()
    else:
        print(f"Let's see how the {NFL_1} fare against the {NFL_2}")

# Function to determine the likely winner based on odds to win the conference and make the playoffs
def team_odds():
    for key, value in team_list.items(): # Iterate through the dictionary to find the odds for each team
        if value == NFL_1: # Find the odds for team 1
            team_1_odds = key 
        if value == NFL_2: # Find the odds for team 2
            team_2_odds = key
    if team_1_odds < team_2_odds: # Compare the odds to determine the likely winner
        print(f"The {NFL_1} should beat {NFL_2}!")
    elif team_2_odds < team_1_odds:
        print(f"The {NFL_2} should beat {NFL_1}!")
    else: # If the odds are the same, print that there is no clear favorite
        print(f"The NFL game between the {NFL_1} and the {NFL_2} has no clear favorite")

def main(): # Main function to run the program
    print("Hello User, please give me a two nfl teams and I'll tell you who is likely to win the matchup!\n"
    "Example: Buffalo Bills\n")
    get_team()
    verify_nfl_team()
    team_odds()
    user_selection = input("Thank you for using the NFL Game Winner Predictor! Would you like to play again?[Y/N]: ").lower()
    if user_selection == 'y':
        main()
    else:
        print("OK, thanks for playing!")

if __name__ == "__main__": # Run the program
    main()