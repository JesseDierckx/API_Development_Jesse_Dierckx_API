from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Player(BaseModel):
    ranking: int
    first_name: str
    last_name: str
    team: str
    age: int
    games_played: int
    wins: int
    losses: int

class Team(BaseModel):
    ranking: int
    name: str
    games_played: int
    wins: int
    losses: int

player_1 = {"ranking": 1, "first_name": "Luka", "last_name": "Dondic", "team": "Dallas Mavericks", "age": 23,"games_played": 13, "wins": 8, "losses": 5}
players = {0: player_1}

team_1 = {"ranking": 1,"name": "Boston Celtics","games_played": 16,"wins": 13, "losses": 3}
teams = {0: team_1}



@app.post("/player")
async def create_player(player: Player):
    new_key = max(players, key=players.get)+1
    players[new_key] = player
    return players[new_key]

@app.get("/player")
def get_player():
    return players

@app.post("/team")
async def create_team(team: Team):
    new_key = max(teams, key=teams.get)+1
    teams[new_key] = team
    return teams[new_key]

@app.get("/team")
def get_team():
    return teams