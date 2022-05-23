import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import collections
from matplotlib import font_manager,rc
import matplotlib as mpl
import numpy as np
from PIL import Image

font_path = './malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
mpl.rcParams['axes.unicode_minus']=False # -값 오류나지않게
rc('font' ,family=font_name)

df = pd.read_csv('./datasets/movie_review_2018_2022.csv')
print(df.head())

words = df.iloc[461,1]
print(words)

words = words.split()
print(words)

worddict = collections.Counter(words)
worddict = dict(worddict)
print(worddict)

movie_mask = np.array(Image.open('./datasets/leaf.png'))

print(movie_mask)
wordcloud_img = WordCloud(
    background_color='white' , max_words=50,mask=movie_mask,
    font_path = './malgun.ttf ').generate_from_frequencies(worddict)


plt.figure(figsize=(6,4))
plt.imshow(wordcloud_img , interpolation='bilinear')
plt.axis('off')
plt.show()