import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from scipy.io import mmread, mmwrite
import pickle

df_reviews = pd.read_csv('./datasets/movie_review_2018_2022.csv')
df_reviews.info()


def getRecommendation(consine_sim):
    simScore = list(enumerate(consine_sim[-1]))
    print(simScore)
    print(len(simScore))

    simScore = sorted(simScore , key=lambda x:x[1] , reverse=True)
    simScore = simScore[1:11] #자기 자신빼기 때문에 1부터 시작
    movieidx = [i[0] for i in simScore]
    recMovieList = df_reviews.iloc[movieidx]
    return recMovieList.iloc[:, 0]

Tridf_matrix = mmread('./models/Tfidf_movie_review_mtx').tocsr()
with open('./models/tfidf.pickle','rb') as f:
    Tfidf = pickle.load(f)

# 영화 제목 이용
movie_idx = df_reviews[df_reviews['title']=='해피 데스데이 2 유'].index[0]
print(movie_idx)
print(df_reviews.iloc[movie_idx,0])

# #영화 index 이용
# movie_idx = 469
# print(movie_idx)
# print(df_reviews.iloc[movie_idx,0])

consine_sim = linear_kernel(Tridf_matrix[movie_idx], Tridf_matrix)
recommendation = getRecommendation(consine_sim)
print(recommendation)
