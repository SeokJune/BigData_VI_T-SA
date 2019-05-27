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
from wordcloud import WordCloud
# Graph drawing and Word Count Output Module
## pip3 install matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
# Graph drawing Module
## pip3 install pyecharts
import pyecharts
## sudo apt-get install fonts-nanum*
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
    def __init__(self, date, query):
        # Read Data(the 19th presiential election)
        self.realVoteData = pd.read_csv('../initialize_president.csv', encoding = 'euc-kr', header = 1)
        # Set Text
        self.title = '19대 대통령 선거'
        # Path(Hangle Font)
        ## sudo apt-get install fonts-nanum*
        self.hPath = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
        # Set Hangle Font, size / Graph size
        font_name = font_manager.FontProperties(fname = self.hPath).get_name()
        rc('font', family = font_name)
        # rc('figure', figsize = (20, 10)) or
        plt.get_current_fig_manager().full_screen_toggle()
        # Set Text(Date, Query)
        fromDate = '-'.join([date[0][0:4], date[0][4:6], date[0][6:8]])
        toDate = '-'.join([date[1][0:4], date[1][4:6], date[1][6:8]])
        plt.text(10 * 2.54 * 15.5, -10, '(기간: ' + fromDate + ' ~ ' + toDate + ')', ha = 'right', wrap=True, fontsize = 20, color = 'red')
        plt.text(10 * 2.54 * 15.5, -1, '(쿼리: ' + query + ')', ha = 'right', wrap=True, fontsize = 20, color = 'red')
    # ----------------------------------------------------------------------------------------------
    # 
    # ----------------------------------------------------------------------------------------------
    def wordCloud(self, tweetData):
        a = dict(tweetData)
        # Set Word Cloud
        wc = WordCloud(font_path = self.hPath,      # Font Path
                       background_color = 'white',  # Backgroud Color
                       max_words = 1000)            # Maximum Number of Words
        # Add Data(tweetData(Word, Frequency)) in Word Cloud
        wc = wc.generate_from_frequencies(a)
        # Set Display an Image
        plt.imshow(wc,                          # Array-like or PIL image
                   interpolation = 'bilinear')  # 'none', 'nearest', 'bilinear', 'bicubic', etc.
        # Set x,y axis (off - invisible)
        plt.axis('off')
        # Set Title, text
        plt.suptitle(self.title + 'WordCount 결과', fontsize = 50)
        # Graph Output
        plt.show()
# --------------------------------------------------------------------------------------------------
# test
# https://zzsza.github.io/development/2018/08/24/data-visualization-in-python/
# --------------------------------------------------------------------------------------------------
