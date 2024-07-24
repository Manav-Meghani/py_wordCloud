from wordcloud import WordCloud
import matplotlib.pyplot as plt
TXT_FILE = "C:\\Users\\manav\\AppData\\Local\\Programs\\Python\\Python312\\Speach_of_life.txt"
text = open(TXT_FILE, mode="r", encoding="utf-8").read()
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
