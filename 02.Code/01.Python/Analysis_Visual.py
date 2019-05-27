# 
# Analysis_Visual.py
#  Title: Analysis and Visualization
# Author: Lee SeokJune
# --------------------------------------------------------------------------------------------------
# Import Module and Install
# --------------------------------------------------------------------------------------------------
# Library for handing DataFrame
## pip3 install pandas
import pandas as pd
# Word Cloud related Module
## pip3 install wordcloud
import wordcloud as wc
# Graph drawing and Word Count Output Module
## pip3 install matplotlib
import matplotlib.pyplot as plt
# Graph drawing Module
## pip3 install pyecharts
import pyecharts
## sudo apt-get install -y fonts-nanum*
# --------------------------------------------------------------------------------------------------
#  Class Name: Analysis_Visual
# Method list: Generator
#            : wordCloud
#            : line, bar, stackedBar, pie
# --------------------------------------------------------------------------------------------------
class Analysis_Visual:
    # ----------------------------------------------------------------------------------------------
    # Generator
    # read: initialize_president.csv
    # ----------------------------------------------------------------------------------------------
    def __init__(self):
        # Read Data(the 19th presiential election)
        self.realVoteData = pd.read_csv('../initialize_president.csv', encoding = 'euc-kr', header = 1)
        # Set Hangle Font
        
    # ----------------------------------------------------------------------------------------------
    # 
    # ----------------------------------------------------------------------------------------------
    def wordCloud(self, tweetData):
        # Set Path(Hangle Font)
        path = os.path.expanduser('~') + '/.local/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf/NanumBarunGothicUltraLight.ttf'
        # Set Word Cloud
        wordcloud = wc(font_path = path,        # Font Path
                    backgroud_color = 'white',  # Backgroud Color
                    max_words = 2000)           # Maximum Number of Words
        # Add Data(tweetData(Word, Frequency)) in Word Cloud
        wordcloud = wc.getnerate_from_frequencies(tweetData)
        # Set Display an Image
        plt.imshow(wordcloud,                   # Array-like or PIL image
                   interpolation = 'bilinear')  # 'none', 'nearest', 'bilinear', 'bicubic', etc.
        #
        plt.axis()
        plt.show()

# --------------------------------------------------------------------------------------------------
# test
# https://zzsza.github.io/development/2018/08/24/data-visualization-in-python/
# --------------------------------------------------------------------------------------------------
a = Analysis_Visual()

import os
print(os.path.expanduser('~')+ '/.local/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf/NanumBarunGothicUltraLight.ttf')
