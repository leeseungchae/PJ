from gensim.models import Word2Vec
import pandas as pd

review_word = pd.read_csv('./crawling_data/datasets/Game_reviews_ALL_Preprocessing_2.csv')
review_word.info()
review_word.dropna(inplace=True)
print(review_word.head())
review_word.info()

review_word['scores'] = review_word['scores'].astype(str)
print(review_word.iloc[-1])
review_word.info()
#exit()
cleaned_token_review = list(review_word['cleaned_sentences'])
print(cleaned_token_review[0])
cleaned_tokens = []
for sentence in cleaned_token_review:
    token = sentence.split()
    cleaned_tokens.append(token)
print(cleaned_tokens[0])

embedding_model = Word2Vec(cleaned_tokens, vector_size = 100, window = 4, min_count = 20, # 각각 100차원 min_count최소 20번 이상
                           # workers cpu개수 epochs = 학습개수 sg = 1 고정
                           workers = 4, epochs = 100, sg = 1)

embedding_model.save('./models/word2vecModel_Game.model')
#print(embedding_model.wv.vocab.key())
#print(len(embedding_model.wv.vocab.key()))