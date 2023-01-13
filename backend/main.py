import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from model import similar_movies, get_recommendations, movie_md_full, ratings

import pandas as pd
import pprint


app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins='*',
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


@app.get('/films')
def all_films(page: int):
  PAGE_SIZE = 20
  return movie_md_full.iloc[PAGE_SIZE * page: PAGE_SIZE * (page + 1)].to_dict('records')


@app.get('/film/{movie_id}')
def get_film_info(movie_id: int):
  return movie_md_full[movie_md_full['id'] == movie_id].to_dict('records')[0]


@app.get('/similar/{movie_id}')
def get_similar_movies(movie_id: int):
  return similar_movies(movie_id)


@app.get('/top_recommendations/{user_id}')
def get_user_recommendations(user_id: int):
  return get_recommendations(user_id, 20)


@app.get('/user_marks/{user_id}')
def get_user_marks(user_id: int):
  flt = []
  r = []
  for i, row in ratings[ratings.userId == user_id].iterrows():
    s = movie_md_full[movie_md_full['movieId'] == row['movieId']]
    if not s.empty:
      flt.append(s)
      r.append(row['rating'] * 2)
  flt = pd.concat(flt)
  flt['rating'] = r
  return flt.to_dict('records')


@app.get('/all_users')
def get_all_users():
  return ratings.userId.unique().tolist()


if __name__ == '__main__':
  uvicorn.run('main:app', use_colors=True, reload=True)
