
import pandas as pd

Politics= pd.read_csv('./crawling_data/naver_news_politics.csv', sep=',')
Economic= pd.read_csv('./crawling_data/naver_news_Economic.csv', sep=',')
Social= pd.read_csv('./crawling_data/naver_news_Social.csv', sep=',')
Culture= pd.read_csv('./crawling_data/naver_news_Culture_20220330.csv', sep=',')
IT= pd.read_csv('./crawling_data/naver_news_IT_20220330.csv', sep=',')
World= pd.read_csv('./crawling_data/naver_news_World_20220330.csv', sep=',')



df_sum = pd.DataFrame()

df_sum= pd.concat([Politics, Economic, Social, Culture, IT, World ], axis='rows')

print(df_sum.head())
print(df_sum.info())

df_sum.to_csv('./naver_news_sum.csv')