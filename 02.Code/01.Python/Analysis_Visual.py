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
    # Read CSV File: initialize_president.csv
    # ----------------------------------------------------------------------------------------------
    def __init__(self, date, query):
        # Set Param
        self.date = date
        self.query = query
        # Read Data(the 19th presiential election)
        self.realVoteData = pd.read_csv('../initialize_president.csv', encoding = 'euc-kr', header = 1)
        # Set Text
        self.title = '19대 대통령 선거'
        # Path(Hangle Font)
        ## sudo apt-get install fonts-nanum*
        self.hPath = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
    # ----------------------------------------------------------------------------------------------
    # Set matplotlib Param
    # ----------------------------------------------------------------------------------------------
    def setPlt(self, title, titleSize):
        # Set Hangle Font, size / Graph size
        font_name = font_manager.FontProperties(fname = self.hPath).get_name()
        rc('font', family = font_name)
        # rc('figure', figsize = (20, 10)) or
        plt.get_current_fig_manager().full_screen_toggle()
        # Set Title
        plt.suptitle(title, fontsize = titleSize)
        # Set Text(Date, Query)
        fromDate = '-'.join([self.date[0][0:4], self.date[0][4:6], self.date[0][6:8]])
        toDate = '-'.join([self.date[1][0:4], self.date[1][4:6], self.date[1][6:8]])
        plt.text(10 * 2.54 * 15.5, -10, '(기간: ' + fromDate + ' ~ ' + toDate + ')', ha = 'right', wrap=True, fontsize = 20, color = 'red')
        plt.text(10 * 2.54 * 15.5, -1, '(쿼리: ' + self.query + ')', ha = 'right', wrap=True, fontsize = 20, color = 'red')
    # ----------------------------------------------------------------------------------------------
    # Word Cloud with kCountData(TWITTER - KEYWORD_COUNT)
    # ----------------------------------------------------------------------------------------------
    def wordCloud(self, kCountData):
        # Set Word Cloud
        wc = WordCloud(font_path = self.hPath,      # Font Path
                       background_color = 'white',  # Backgroud Color
                       max_words = 1000,            # Maximum Number of Words
                       contour_width = 5)
        # Add Data(tweetData(Word, Frequency)) in Word Cloud
        wc = wc.generate_from_frequencies(dict(kCountData))
        # Set Display an Image
        plt.imshow(wc,                          # Array-like or PIL image
                   interpolation = 'bilinear')  # 'none', 'nearest', 'bilinear', 'bicubic', etc.
        # Set x,y axis (off - invisible)
        plt.axis('off')
        # Set plt
        self.setPlt('19대 대통령 선거 Word Count 결과', 50)
        # Graph Output
        plt.show()
    # ----------------------------------------------------------------------------------------------
    # Line Graph with sJsonData(TWITTER - S_JSON
    # ----------------------------------------------------------------------------------------------
    def line(self, sJsonData):
        print(sJsonData)
# --------------------------------------------------------------------------------------------------
# test
# https://zzsza.github.io/development/2018/08/24/data-visualization-in-python/
# --------------------------------------------------------------------------------------------------
