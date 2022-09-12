from enum import unique
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel



class User(BaseModel):
    id: int.unique
    name: str
    #age: Optional[0<int<100] = None
    age: int
    email: str
    
class Game(BaseModel):
    id: int.unique
    name: str
    connected_user: Optional[str]
        
app = FastAPI()

@app.get("/games")
async def read_games_list():
    games_dict = {"name": [], "connected_users": []}
    for game in Game:
        games_dict ["name"].append(Game.name)
        for users in Game.connected_user:
            games_dict ["connected_users"].append(Game.connected_user)
        return games_dict

@app.get("/users/me")
async def read_user_me():
    return {"id": "the current user",
            "name": User.name,
            "age": User.age,
            "email": User.email,
            "games": Game.connected_user.dict()}

@app.put("/games/{id}/conn_2_game/")
async def create_new_pair(game: Game):
    game_dict = game.dict()
    if game.connected_user:
        new_gamer = input('Type user name')
        game_dict.update({"conected_users": new_gamer})
    return create_new_pair

