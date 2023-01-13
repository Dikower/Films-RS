import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
from surprise.prediction_algorithms.knns import KNNBasic
from surprise import Dataset, Reader

import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv('./models/processed.csv')
with open('./models/sim_model.pkl', 'rb') as file:
  similarity = pickle.load(file)


with open('./models/knn_model.pkl', 'rb') as file:
  knn = pickle.load(file)


ratings = pd.read_csv("./dataset/ratings_small.csv")
movie_md = pd.read_csv("./dataset/movies_metadata.csv")
movie_md = movie_md[movie_md['vote_count']>55][['id', 'title']]
movie_ids = [int(x) for x in movie_md['id'].values]
ratings = ratings[ratings['movieId'].isin(movie_ids)]
ratings.reset_index(inplace=True, drop=True)

movie_md_full = pd.read_csv("./dataset/movies_metadata.csv").replace([np.nan], [None])
movie_md_full['movieId'] = movie_md_full['id']
movie_md_full = movie_md_full[movie_md_full['movieId'].str.isnumeric()]
movie_md_full['movieId'] = movie_md_full['movieId'].astype(int)
movie_md_full['id'] = movie_md_full['movieId'].astype(int)
movie_md_full = movie_md_full.sort_values(by='vote_count', ascending=False)


def similar_movies(movie_id):
  id_of_movie = df[df['id']==movie_id].index[0]
  distances = similarity[id_of_movie]
  movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:10]

  films = []
  for i in movie_list:
    films.append(df.iloc[i[0]])
  films = pd.DataFrame(films)
  films = films.merge(movie_md_full, 'left', on='id').rename(columns={'title_x': 'title'})

  return films.to_dict('records')


def get_recommendations(user_id, top_n):
  user_movie_interactions_matrix = ratings.pivot(index='userId', columns='movieId', values='rating')
  non_interacted_movies = user_movie_interactions_matrix.loc[user_id][user_movie_interactions_matrix.loc[user_id].isnull()].index.tolist()

  films = []
  for item_id in non_interacted_movies:
    est = knn.predict(user_id, item_id).est
    film = movie_md_full[movie_md_full['id'] == item_id]
    if not film.empty:
      film['est'] = est * 2
      films.append(film)

  recommendations = pd.concat(films)
  recommendations = recommendations.sort_values(by='est', ascending=False)
  return recommendations.head(top_n).to_dict('records')