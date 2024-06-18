class Player:
    # Challenge 1: Update the Constructor
    def __init__(self, player_info):
        self.name = player_info["name"]
        self.age = player_info["age"]
        self.position = player_info["position"]
        self.team = player_info["team"]

    # NINJA BONUS: Add a get_team(cls, team_list) @class method
    @classmethod
    def get_team(cls, team_list):
        team = []
        for player_info in team_list:
            player = cls(player_info)
            team.append(player)
        return team


# Challenge 2: Create instances using individual player dictionaries.
kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}

jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}

kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}

# Create your Player instances here!
# player_jason = ???
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Forward",
        "team": "Philadelphia 76ers"
    },
    {
        "name": "Aaron Pogi",
        "age": 20,
        "position": "Center",
        "team": "Gwapings"
    }
]

# Challenge 3: Make a list of Player instances from a list of dictionaries
# ... (class definition and large list of players here)
new_team = []
# Write your for loop here to populate the new_team variable with Player objects.
for player_info in players:
    player = Player(player_info)
    new_team.append(player)

print("Player Kevin's Team:", player_kevin.team)
print("Player Jason's Team:", player_jason.team)
print("Player Kyrie's Team:", player_kyrie.team)

print("\nNew Team:")
for player in new_team:
    print(player.name, "-", player.team)

# Using get_team
new_team_alt = Player.get_team(players)

print("\nNew Team (get_team Method):")
for player in new_team_alt:
    print(player.name, "-", player.team)
