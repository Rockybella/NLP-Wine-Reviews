
import pandas as pd
import seaborn as sns
#import matplotlib as plt
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import WordCloud, STOPWORDS


df = pd.read_csv('Documents\TDI\winemag-data-130k-v2.csv')

sns.set(style="whitegrid")

pricepoints=sns.catplot(x="points", y="price", data=df, height=20, kind="point", palette="muted")
plt.title('Price vs Ratings')

countryprice=sns.catplot(x="price", y="country", data=df, height=6, kind="bar", palette="muted")
plt.title('Price of Wine per Country')

countrypoints=sns.catplot(x="points", y="country", data=df, height=6, kind="bar", palette="muted")
plt.title('Scores of Wine per Country')
#typepoints=sns.catplot(x="points", y="taster_name", data=df, height=20, kind="bar", palette="muted")
#plt.title('Activity of Reviewers')



sortptsHigh_df=df.sort_values('points', ascending=False)
sortptsLow_df=df.sort_values('points', ascending=True)


commonWords=['wine', 'flavor', 'finnish', 'aroma', 'palate']
textHigh = ' '.join(sortptsHigh_df['description'].str.lower().values[:5000])
#for text in textHigh:
textHigh=textHigh.replace('wine',' ')
textHigh=textHigh.replace('flavor',' ')
textHigh=textHigh.replace('finish',' ')
#textHigh=textHigh.replace('aroma',' ')
textHigh=textHigh.replace('palate',' ')
#textHigh=textHigh.replace('fruit',' ')
#textHigh=textHigh.replace('rich',' ')
textHigh=textHigh.replace('note',' ')
textHigh=textHigh.replace('show',' ')
#textHigh=textHigh.replace('ripe',' ')

textLow = ' '.join(sortptsLow_df['description'].str.lower().values[:5000])
textLow=textLow.replace('wine',' ')
textLow=textLow.replace('flavor',' ')
textLow=textLow.replace('finish',' ')
#textLow=textLow.replace('aroma',' ')
textLow=textLow.replace('palate',' ')
#textLow=textLow.replace('fruit',' ')
#textLow=textLow.replace('rich',' ')
textLow=textLow.replace('note',' ')
textLow=textLow.replace('show',' ')
#textLow=textLow.replace('ripe',' ')

wordcloud = WordCloud(max_font_size=None,stopwords = set(STOPWORDS), background_color='white',
                      width=1200, height=1000).generate(textHigh)
plt.figure(figsize=(8,8))

plt.axis('off')
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Favorable')
plt.show


wordcloud = WordCloud(max_font_size=None,stopwords = set(STOPWORDS), background_color='white',
                      width=1200, height=1000).generate(textLow)
plt.figure(figsize=(8,8))
plt.axis('off')
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Unfavorable')
plt.show
