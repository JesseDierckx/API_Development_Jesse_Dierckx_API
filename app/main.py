from fastapi import FastAPI
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

players = [
    {"ranking": 1,"first_name": "Luka","last_name": "Dondic","team": "Dallas Mavericks","age": 23,"games_played": 13,"wins": 8,"losses": 5},
    {"ranking": 2,"first_name": "Stephen","last_name": "Curry","team": "Golden State Warriors","age": 34,"games_played": 14,"wins": 6,"losses": 8},
    {"ranking": 3,"first_name": "Joel","last_name": "Embiid","team": "Philadelphia 76ers","age": 28,"games_played": 10,"wins": 5,"losses": 5},
    {"ranking": 4,"first_name": "Shai","last_name": "Gilgeous Alexander","team": "Oklahoma City Thunder","age": 24,"games_played": 14,"wins": 7,"losses": 7},
    {"ranking": 5, "first_name": "Jayson", "last_name": "Tatum", "team": "Boston Celtics", "age": 24, "games_played": 15, "wins": 12, "losses": 3},
    {"ranking": 6, "first_name": "Donovan", "last_name": "Mitchell", "team": "Cleveland Cavaliers", "age": 26, "games_played": 12, "wins": 7, "losses": 5},
    {"ranking": 7, "first_name": "Kevin", "last_name": "Durant", "team": "Brooklyn Nets", "age": 34, "games_played": 15, "wins": 6, "losses": 9},
    {"ranking": 8, "first_name": "Giannis", "last_name": "Antetokounmpo", "team": "Milwaukee Bucks", "age": 27, "games_played": 11, "wins": 9},
    {"ranking": 9, "first_name": "Ja", "last_name": "Morant", "team": "Memphis Grizzlies", "age": 23, "games_played": 13, "wins": 9, "losses": 4},
    {"ranking": 10,"first_name": "Damian","last_name": "Lillard","team": "Portland Trail blazers","age": 32,"games_played": 9,"wins": 7,"losses": 2}
]

@app.post("/post/")
async def create_player(player: Player):
    return player

@app.get("/get/")
async def get_player():
    return player