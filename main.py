from fastapi import FastAPI, HTTPException
from enum import Enum
app = FastAPI()

class GenerateURLChoices(Enum):
    UlTRA = "Ultra Nate"

@app.get('/')
async def index():
    return {'hello': 'world'}

@app.get('/about')
async def about():
    return "About this fast api"
MOVIES = [
    {
        "id": "1", 
        "title": "Free", 
        "artist": "Ultra Nate", 
        "duration": "220", 
        "last_play": "2018-05-17 16:56:21"
    }, 
    {
        "id": "2", 
        "title": "Ain't Nobody", 
        "artist": "Rufus, Chaka Khan", 
        "duration": "216", 
        "last_play": "2017-10-18 15:15:26"
    }, 
    {
        "id": "3", 
        "title": "Haven't Met You Yet", 
        "artist": "Michael Buble", 
        "duration": "236", 
        "last_play": "2017-04-01 08:31:33"
    }, 
    {
        "id": "4", 
        "title": "I Got You Babe", 
        "artist": "UB40Chrissie Hynde", 
        "duration": "177", 
        "last_play": "2016-02-25 11:40:40"
    }
]

@app.get('/movies')
async def movies() ->list[dict]:
    #movies = next((m for m in movies), None)
    return MOVIES

@app.get('/movies/{m_id}')
async def movies(m_id:GenerateURLChoices):
    movies = next((m for m in MOVIES if m['id'] == m_id), None)
    return movies

@app.get('/movies/artist/{artist}')
async def get_artist_name(artist):
    return [ a for a in MOVIES if a['artist'] == artist ]

