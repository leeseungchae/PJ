import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread
import pickle

df_reviews = pd.read_csv('./crawling_data/datasets/Game_reviews_ALL_Preprocessing_2.csv')
df_reviews.info()

Tfidf = TfidfVectorizer(sublinear_tf=True)
Tfidf_matrix = Tfidf.fit_transform(df_reviews['cleaned_sentences'])

with open('./models/tfidf01.pickle', 'wb') as f:
    pickle.dump(Tfidf, f)
mmwrite('./models/Tfidf_Game_review01.mtx', Tfidf_matrix)
print('end')