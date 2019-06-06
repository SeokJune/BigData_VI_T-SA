# Analysis_Visual.py
#  Title: Analysis and Visualization
# Author: Lee SeokJune
# --------------------------------------------------------------------------------------------------
# Import Module and Install
# --------------------------------------------------------------------------------------------------
# Library for handing DataFrame
## pip3 install pandas
import pandas as pd
## pip3 install numpy
import numpy as np
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
        # Set Hangle Font, size / Graph size
        font_name = font_manager.FontProperties(fname = self.hPath).get_name()
        rc('font', family = font_name)
    # ----------------------------------------------------------------------------------------------
    # Set matplotlib Param
    # ----------------------------------------------------------------------------------------------
    def setPlt(self, title, titleSize):
        # Set Title
        plt.suptitle(title, fontsize = titleSize)
        # Set Text(Date, Query)
        fromDate = '-'.join([self.date[0][0:4], self.date[0][4:6], self.date[0][6:8]])
        toDate = '-'.join([self.date[1][0:4], self.date[1][4:6], self.date[1][6:8]])
        if textNum == 1:
            plt.text(10 * 2.54 * 15.5, -10, '(기간: ' + fromDate + ' ~ ' + toDate + ')', ha = 'right', wrap=True, fontsize = 20, color = 'red')
            plt.text(10 * 2.54 * 15.5, -1, '(쿼리: ' + self.query + ')', ha = 'right', wrap=True, fontsize = 20, color = 'red')
    # ----------------------------------------------------------------------------------------------
    # Word Cloud with kCountData(TWITTER - KEYWORD_COUNT)
    # ----------------------------------------------------------------------------------------------
    def wordCloud(self, kCountData):
        # Set plt
        self.setPlt('19대 대통령 선거 Word Count 결과', 50)
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
        # Graph Output
        plt.get_current_fig_manager().full_screen_toggle()
        plt.show()
    # ----------------------------------------------------------------------------------------------
    # Line Graph with sJsonData(TWITTER - S_JSON)
    # ----------------------------------------------------------------------------------------------
    def line(self, sJsonData):
        # Preprocessing
        data = pd.merge(pd.merge(pd.merge(pd.merge(pd.DataFrame(list(sJsonData[0]), columns = ['DATE','문재인']),
                                                   pd.DataFrame(list(sJsonData[1]), columns = ['DATE','홍준표']), on = 'DATE'),
                                          pd.DataFrame(list(sJsonData[2]), columns = ['DATE','안철수']), on = 'DATE'),
                                 pd.DataFrame(list(sJsonData[3]), columns = ['DATE','유승민']), on = 'DATE'),
                        pd.DataFrame(list(sJsonData[4]), columns = ['DATE','심상정']), on = 'DATE')
        # Set plt
        self.setPlt('19대 대통령 선거기간(2017-04-16 ~ 2017-05-09)동안 일별 후보 언급 횟수', 40, 2)
        # Set Line
        plt.plot(data['DATE'], data['문재인'], lw = 2, marker = 'o')
        plt.plot(data['DATE'], data['홍준표'], lw = 2, marker = 'o')
        plt.plot(data['DATE'], data['안철수'], lw = 2, marker = 'o')
        plt.plot(data['DATE'], data['유승민'], lw = 2, marker = 'o')
        plt.plot(data['DATE'], data['심상정'], lw = 2, marker = 'o')
        plt.legend(('문재인', '홍준표', '안철수', '유승민', '심상정'), loc = 'upper right')
        #Graph Output
        plt.get_current_fig_manager().full_screen_toggle()
        plt.show()
    # ----------------------------------------------------------------------------------------------
    # Bar Graph with sJsonData(TWITTER - KEYWORD_COUNT)
    # ----------------------------------------------------------------------------------------------
    def bar(self, kCountData, stat = 0):
        # Preprocessing
        data = pd.DataFrame(list(kCountData), columns = ['KEYWORD', 'COUNT']).sort_values(['COUNT'], ascending = [False])
        if stat == 1:
            data = data.head(10)
        else:
            data = data[data['KEYWORD'].isin(['문재인', '홍준표', '안철수', '유승민', '심상정'])]
            data = pd.merge(data.sort_values(['KEYWORD']),
                            np.transpose(self.realVoteData)[0]['문재인':'심상정'].sort_index(),
                            left_on = ['KEYWORD'], right_index = True)
            data = data.rename(columns = {0 : 'COUNT_'})
            data['COUNT_'] = data['COUNT_'].replace(',', '', regex = True).astype('int')
        # Set Bar
        if stat == 1:
            # Set plt
            self.setPlt('19대 대통령 선거기간(2017-04-18 ~ 2017-05-09)동안 언급된 키워드(TOP 10)')
            plt.bar(data['KEYWORD'], data['COUNT'])
        else:
            # Set plt1
            plt.subplot(2, 1, 1)
            plt.title('19대 대통령 선거기간(2017-04-18 ~ 2017-05-09)동안 후보(TOP 5) 언급률', fontsize = 30)
            plt.bar(data['KEYWORD'], data['COUNT'] / data['COUNT'].sum() * 100, width = 0.2)
            plt.ylabel('COUNT(%)')
            # Set plt2
            plt.subplot(2, 1, 2)
            plt.title('후보(TOP 5)의 득표율', fontsize = 30)
            plt.bar(data['KEYWORD'], data['COUNT_'] / data['COUNT_'].sum() * 100, width = 0.2)
            plt.ylabel('COUNT(%)')
        #Graph Output
        plt.get_current_fig_manager().full_screen_toggle()
        plt.show()
# --------------------------------------------------------------------------------------------------
# test
# https://zzsza.github.io/development/2018/08/24/data-visualization-in-python/
# --------------------------------------------------------------------------------------------------
