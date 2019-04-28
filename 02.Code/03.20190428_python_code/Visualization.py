#import dbModule
from wordcloud import WordCloud
#import numpy as np
#from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

class Visualization:
    def visualize(self, b):
        path = '/home/vi/.local/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf/NanumBarunGothicUltraLight.ttf'
        fontprop = fm.FontProperties(fname=path, size=18)
        wc=WordCloud(font_path=path,background_color='white',max_words=2000)
        wc=wc.generate_from_frequencies(b)

        plt.figure(figsize=(12,12))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.show()
