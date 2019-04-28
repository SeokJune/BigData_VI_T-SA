
#import dbModule
from wordcloud import WordCloud
#import numpy as np
#from PIL import Image
import matplotlib.pyplot as plt

class Visualization:
    def visualize(self, b):        

        wc=WordCloud(background_color='white',max_words=2000)
        wc=wc.generate_from_frequencies(b)

        plt.figure(figsize=(12,12))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.show()
