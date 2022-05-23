import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from scipy.io import mmread, mmwrite
import pickle
from gensim.models import Word2Vec

df_reviews = pd.read_csv('./crawling_data/datasets/Game_reviews_ALL_Preprocessing_2.csv')
df_reviews.info()
def getRecommendation(cosine_sim):
    simScore = list(enumerate(cosine_sim[-1]))
    print(len(simScore))
    print(simScore)
    simScore = sorted(simScore, key=lambda x:x[1],
                      reverse=True)
    simScore = simScore[1:11]
    movieidx = [i[0] for i in simScore]
    recMovieList = df_reviews.iloc[movieidx]
    return recMovieList.iloc[:, 0]

Tfidf_matrix = mmread('./models/Tfidf_Game_review01.mtx').tocsr()
with open('./models/tfidf01.pickle', 'rb') as f:
    Tfidf = pickle.load(f)

# # 영화 제목을 이용
# movie_idx = df_reviews[df_reviews['title']=='기생충'].index[0]
# print(movie_idx)
# 영화 index를 이용
# movie_idx = 218
# print(df_reviews.iloc[movie_idx, 0])

embedding_model = Word2Vec.load('./models/word2vecModel_Game.model')
key_word = '과금'
sim_word = embedding_model.wv.most_similar(key_word, topn=10)
sentence = [key_word] * 11

words = []

for word, _ in sim_word:
    words.append(word)

for i, word in enumerate(words):
    sentence += [word] * (10 - 1)

sentence = ' '.join(sentence)
sentence_vec = Tfidf.transform([sentence])
cosine_sim = linear_kernel(sentence_vec, Tfidf_matrix)


#cosine_sim = linear_kernel(Tfidf_matrix[movie_idx], Tfidf_matrix)
recommendation = getRecommendation(cosine_sim)
print(recommendation)