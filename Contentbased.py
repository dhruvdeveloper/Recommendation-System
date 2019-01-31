import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

metadata = pd.read_csv('dataset/tmdb_5000_movies.csv', low_memory=False)
# print(metadata.head())

C = metadata['vote_average'].mean()
# print(C)

m = metadata['vote_count'].quantile(0.90)


#print(type(metadata))
q_movies = metadata.copy().loc[metadata['vote_count'] >= m]
#w_movies = pd.DataFrame(data=q_movies)

print(q_movies.shape)


def wr(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    return (v / (v + m) * R) + (m / (m + v) * C)


q_movies['score'] = q_movies.apply(wr,axis=1)
q_movies = q_movies.sort_values('score',ascending=False)

#print(q_movies[['title', 'vote_count', 'vote_average', 'score']].head(15))
#print(metadata['overview'].head())

tfidf = TfidfVectorizer(stop_words='english')

metadata['overview'] = metadata['overview'].fillna('')

tfidf_matrix = tfidf.fit_transform(metadata['overview'])

cosine_sim = linear_kernel(tfidf_matrix,tfidf_matrix)

indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()


def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    x = {
        'movieName': metadata['title'].iloc[movie_indices].to_dict().values(),
        'movieLink': metadata['homepage'].iloc[movie_indices].to_dict().values(),
        'movieBudget': metadata['budget'].iloc[movie_indices].to_dict().values()
    }

    return x


def get_recommendationstemp(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:10]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies

    x = {
        'movieName': metadata['title'].iloc[movie_indices].to_dict().values(),
        'movieLink': metadata['homepage'].iloc[movie_indices].to_dict().values(),
        'movieBudget': metadata['budget'].iloc[movie_indices].to_dict().values()
    }
    return x


def get_recommendationstemp2(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:3]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies

    x = {
        'movieName': metadata['title'].iloc[movie_indices].to_dict().values(),
        'movieLink': metadata['homepage'].iloc[movie_indices].to_dict().values(),
        'movieBudget': metadata['budget'].iloc[movie_indices].to_dict().values()
    }
    return x

