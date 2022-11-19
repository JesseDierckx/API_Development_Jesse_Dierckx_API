from fastapi import Body, FastAPI
from pydantic import BaseModel, Field


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
    offensive_rebounds: float
    defensive_rebounds: float
    rebounds: float
    assists: float
    turnovers: float
    steals: float
    blocks: float
    personal_fouls: float
    points_per_game: float


players = [
    {"ranking": 1,"first_name": "Luka","last_name": "Dondic","team": "Dallas Mavericks","age": 23,"games_played": 13,"wins": 8,"losses": 5,"offensive_rebounds": 1.1,"defensive_rebounds": 7.8,"rebounds": 8.8,"assists": 7.8,"turnovers": 3.2,"steals": 2.1,"blocks": 0.6,"personal_fouls": 3.2},
    {"ranking": 2,"first_name": "Stephen","last_name": "Curry","team": "Golden State Warriors","age": 34,"games_played": 14,"wins": 6,"losses": 8,"offensive_rebounds": 0.6,"defensive_rebounds": 6.1,"rebounds": 6.8,"assists": 6.4,"turnovers": 2.6,"steals": 1.0,"blocks": 0.1,"personal_fouls": 2.0},
    {"ranking": 3,"first_name": "Joel","last_name": "Embiid","team": "Philadelphia 76ers","age": 28,"games_played": 10,"wins": 5,"losses": 5,"offensive_rebounds": 1.6,"defensive_rebounds": 8.5,"rebounds": 10.1,"assists": 4.1,"turnovers": 4.2,"steals": 0.6,"blocks": 1.8,"personal_fouls": 3.4},
    {"ranking": 4,"first_name": "Shai","last_name": "Gilgeous Alexander","team": "Oklahoma City Thunder","age": 24,"games_played": 14,"wins": 7,"losses": 7,"offensive_rebounds": 0.9,"defensive_rebounds": 3.6,"rebounds": 4.5,"assists": 5.9,"turnovers": 3.3,"steals": 1.9,"blocks": 1.4,"personal_fouls": 2.4},
    {"ranking": 5, "first_name": "Jayson", "last_name": "Tatum", "team": "Boston Celtics", "age": 24, "games_played": 15, "wins": 12, "losses": 3, "offensive_rebounds": 0.8, "defensive_rebounds": 6.6, "rebounds": 7.4, "assists": 4.1, "turnovers": 2.3, "steals": 0.9, "blocks": 1.4, "personal_fouls": 2.1},
    {"ranking": 6, "first_name": "Donovan", "last_name": "Mitchell", "team": "Cleveland Cavaliers", "age": 26, "games_played": 12, "wins": 7, "losses": 5, "offensive_rebounds": 0.9, "defensive_rebounds": 3.6, "rebounds": 4.5, "assists": 5.8, "turnovers": 3.3, "steals": 1.4, "blocks": 0.6, "personal_fouls": 2.8},
    {"ranking": 7, "first_name": "Kevin", "last_name": "Durant", "team": "Brooklyn Nets", "age": 34, "games_played": 15, "wins": 6, "losses": 9, "offensive_rebounds": 0.4, "defensive_rebounds": 6.1, "rebounds": 6.5, "assists": 5.3, "turnovers": 3.2, "steals": 0.9, "blocks": 1.9, "personal_fouls": 2.5},
    {"ranking": 8, "first_name": "Giannis", "last_name": "Antetokounmpo", "team": "Milwaukee Bucks", "age": 27, "games_played": 11, "wins": 9, "losses": 2, "offensive_rebounds": 1.8, "defensive_rebounds": 10.0, "rebounds": 11.8, "assists": 5.5, "turnovers": 3.6, "steals": 1.0, "blocks": 1.2, "personal_fouls": 3.0},
    {"ranking": 9, "first_name": "Ja", "last_name": "Morant", "team": "Memphis Grizzlies", "age": 23, "games_played": 13, "wins": 9, "losses": 4, "offensive_rebounds": 1.2, "defensive_rebounds": 4.9, "rebounds": 6.2, "assists": 6.8, "turnovers": 3.9, "steals": 1.2, "blocks": 0.3, "personal_fouls": 1.8},
    {"ranking": 10,"first_name": "Damian","last_name": "Lillard","team": "Portland Trail blazers","age": 32,"games_played": 9,"wins": 7,"losses": 2,"offensive_rebounds": 1.0,"defensive_rebounds": 3.7,"rebounds": 4.7,"assists": 6.6,"turnovers": 4.2,"steals": 0.6,"blocks": 0.3,"personal_fouls": 1.6}
]

player = {0: players}

#@app.post("/players/post/", response_model=list[players])
#async def create_player(players: Player):
#    return players

@app.get("/players/get/")
async def get_player():
    return players