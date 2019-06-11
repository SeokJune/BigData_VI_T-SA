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
## sudo apt-get install fonts-nanum*
# --------------------------------------------------------------------------------------------------
#  Class Name: Analysis_Visual
# Method list: Generator
#            : preprocessData, setPlt, setLabel, autoLabel, setTextList
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
        rc('figure', figsize = (10, 5))
    # ----------------------------------------------------------------------------------------------
    # Preprocessing 
    # ----------------------------------------------------------------------------------------------
    def preprocessData(self, kCountData, stat = 0):
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
            data['PP(3)'] = round(data['COUNT'] / data['COUNT'].sum() * 100, 3)
            data['PP(3)_'] = round(data['COUNT_'] / data['COUNT_'].sum() * 100, 3)
        return data
    # ----------------------------------------------------------------------------------------------
    # Set matplotlib Param
    # ----------------------------------------------------------------------------------------------
    def setPlt(self, title, titleSize = 40, textNum = 0):
        # Set Title
        plt.suptitle(title, fontsize = titleSize)
        # Set Text(Date, Query)
        fromDate = '-'.join([self.date[0][0:4], self.date[0][4:6], self.date[0][6:8]])
        toDate = '-'.join([self.date[1][0:4], self.date[1][4:6], str(int(self.date[1][6:8]) - 1).zfill(2)])
        if textNum == 1:
            plt.text(10 * 2.54 * 15.5, -10, '(기간: ' + fromDate + ' ~ ' + toDate + ')', ha = 'right', wrap=True, fontsize = 20, color = 'red')
            plt.text(10 * 2.54 * 15.5, -1, '(쿼리: ' + self.query + ')', ha = 'right', wrap=True, fontsize = 20, color = 'red')
    # ----------------------------------------------------------------------------------------------
    # Set X, Y label
    # ----------------------------------------------------------------------------------------------
    def setLabel(self, xl, yl):
        # Set X Label
        plt.xlabel(xl, fontsize = 20)
        # Set X Label
        plt.ylabel(yl, fontsize = 20)
    # ----------------------------------------------------------------------------------------------
    # Set X Value
    # ----------------------------------------------------------------------------------------------
    def autoLabel(self, ax, rects, xpos = 'center'):
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0, 'right': 1, 'left': -1}

        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy = (rect.get_x() + rect.get_width() / 2, height),
                        xytext = (offset[xpos] * 3, 3),
                        textcoords = "offset points",
                        ha = ha[xpos], va = 'bottom')
    # ----------------------------------------------------------------------------------------------
    # Set Text list(fontsize, weight)
    # ----------------------------------------------------------------------------------------------
    def setTextList(self, tList, fs = 10, w = 'bold'):
        for i in range(0, len(tList)):
            tList[i].set_fontsize(fs)
            if w != '':
                tList[i].set_weight(w)
    # ----------------------------------------------------------------------------------------------
    # Word Cloud with kCountData(TWITTER - KEYWORD_COUNT)
    # ----------------------------------------------------------------------------------------------
    def wordCloud(self, kCountData):
        # Set plt
        self.setPlt('19대 대통령 선거 Word Count 결과', 40, 1)
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
        data = pd.merge(pd.merge(pd.merge(pd.merge(pd.DataFrame(list(sJsonData[0]), columns = ['DATE', '문재인']),
                                                   pd.DataFrame(list(sJsonData[1]), columns = ['DATE', '홍준표']), on = 'DATE'),
                                          pd.DataFrame(list(sJsonData[2]), columns = ['DATE', '안철수']), on = 'DATE'),
                                 pd.DataFrame(list(sJsonData[3]), columns = ['DATE', '유승민']), on = 'DATE'),
                        pd.DataFrame(list(sJsonData[4]), columns = ['DATE', '심상정']), on = 'DATE')
        # Set plt
        self.setPlt('19대 대통령 선거기간(2017-04-18 ~ 2017-05-09)동안 일별 후보 언급 횟수')
        # Set Line
        plt.plot(data['DATE'], data['문재인'], lw = 2, marker = 'o')
        plt.plot(data['DATE'], data['홍준표'], lw = 2, marker = 'o')
        plt.plot(data['DATE'], data['안철수'], lw = 2, marker = 'o')
        plt.plot(data['DATE'], data['유승민'], lw = 2, marker = 'o')
        plt.plot(data['DATE'], data['심상정'], lw = 2, marker = 'o')
        plt.legend(('문재인', '홍준표', '안철수', '유승민', '심상정'), loc = 'upper right', fontsize = 'xx-large')
        plt.grid()
        # Set Label
        self.setLabel('Date', 'Count')
        #Graph Output
        plt.get_current_fig_manager().full_screen_toggle()
        plt.show()
    # ----------------------------------------------------------------------------------------------
    # Bar Graph with kCountData(TWITTER - KEYWORD_COUNT)
    # ----------------------------------------------------------------------------------------------
    def bar(self, kCountData, stat = 0):
        # Preprocessing
        data = self.preprocessData(kCountData, stat)
        # Set Bar
        if stat == 1:
            # Set plt
            self.setPlt('19대 대통령 선거기간(2017-04-18 ~ 2017-05-09)동안 언급된 키워드(TOP 10)')
            plt.bar(data['KEYWORD'], data['COUNT'])
            # Set Label
            self.setLabel('Keyword', 'Count')
        else:
            # the x locations for the groups
            ind = np.arange(len(data['KEYWORD']))
            # the width of the bars
            width = 0.35
            # Set ax
            fig, ax = plt.subplots()
            p1 = ax.bar(ind - width / 2, round(data['COUNT'] / data['COUNT'].sum() * 100, 3), width, label = '트윗 언급')
            p2 = ax.bar(ind + width / 2, round(data['COUNT_'] / data['COUNT_'].sum() * 100, 3), width, label = '실제 득표')
            # title
            ax.set_title('\n\n\n\n', fontsize = 5)
            # label
            ax.set_xlabel('Candidate', fontsize = 20)
            ax.set_ylabel('Count(%)', fontsize = 20)
            # x axis
            ax.set_xticks(ind)
            ax.set_xticklabels(data['KEYWORD'])
            ax.legend(fontsize = 'xx-large')
            self.autoLabel(ax, p1, 'center')
            self.autoLabel(ax, p2, 'center')
            # add layout
            fig.tight_layout()
            # title
            self.setPlt('후보 TOP5 트윗 언급률(%) 및 실제 득표율(%)')
        #Graph Output
        plt.get_current_fig_manager().full_screen_toggle()
        plt.show()
    # ----------------------------------------------------------------------------------------------
    # Stacked Bar Graph with kCountData(TWITTER - KEYWORD_COUNT)
    # ----------------------------------------------------------------------------------------------
    def stackedBar(self, kCountData):
        # Preprocessing
        data = self.preprocessData(kCountData)
        dataList = data[['PP(3)', 'PP(3)_']].values.tolist()
        # the x locations for the groups
        ind = np.arange(2)
        # the width of the bars: can also be len(x) sequence
        width = 0.35
        # bar
        fig, ax = plt.subplots()
        p1 = ax.bar(ind, dataList[0], width)
        p2 = ax.bar(ind, dataList[1], width, bottom = dataList[0])
        p3 = ax.bar(ind, dataList[2], width, bottom = [a + b for a, b in zip(dataList[0], dataList[1])])
        p4 = ax.bar(ind, dataList[3], width, bottom = [a + b + c for a, b, c in zip(dataList[0], dataList[1], dataList[2])])
        p5 = ax.bar(ind, dataList[4], width, bottom = [a + b + c + d for a, b, c, d in zip(dataList[0], dataList[1], dataList[2], dataList[3])])
        # title
        ax.set_title('\n\n\n\n', fontsize = 5)
        # label
        ax.set_ylabel('Count(%)', fontsize = 20)
        ax.set_xticks(ind)
        ax.set_xticklabels(('트윗 언급', '실제 득표'))
        ax.set_yticks(np.arange(0, 110, 5))
        ax.legend((p5[0], p4[0], p3[0], p2[0], p1[0]), data['KEYWORD'].sort_values(ascending = [False]), fontsize = 'xx-large')
        # add layout
        fig.tight_layout()
        # Set title
        self.setPlt('후보 TOP5 트윗 언급률(%) 및 실제 득표율(%)')
        #Graph Output
        plt.get_current_fig_manager().full_screen_toggle()
        plt.show()
    # ----------------------------------------------------------------------------------------------
    # Pie Graph with kCountData(TWITTER - KEYWORD_COUNT)
    # ----------------------------------------------------------------------------------------------
    def pie(self, kCountData):
        # Preprocessing
        data = self.preprocessData(kCountData)
        # pie
        fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2, figsize = (9, 9))
        ax1.set_title('트윗 언급', fontsize = 30)
        patches, texts, autotexts = ax1.pie(data['COUNT'], explode = (0.01, 0.01, 0.01, 0.01, 0.01), labels = data['KEYWORD'], autopct = '%1.3f%%', startangle = -360 * data['PP(3)'].head(1).values[0] / 100 + 90)
        self.setTextList(texts, 20, '')
        self.setTextList(autotexts, 15)
        ax2.set_title('실제 득표', fontsize = 30)
        patches, texts, autotexts = ax2.pie(data['COUNT_'], explode = (0.01, 0.01, 0.01, 0.01, 0.01), labels = data['KEYWORD'], autopct = '%1.3f%%', startangle = -360 * data['PP(3)_'].head(1).values[0] / 100 + 90)
        self.setTextList(texts, 20, '')
        self.setTextList(autotexts, 15)
        # add layout
        fig.tight_layout()
        # Set title
        self.setPlt('후보 TOP5 트윗 언급률(%) 및 실제 득표율(%)')
        #Graph Output
        plt.get_current_fig_manager().full_screen_toggle()
        plt.show()
# --------------------------------------------------------------------------------------------------
# test
# https://zzsza.github.io/development/2018/08/24/data-visualization-in-python/
# --------------------------------------------------------------------------------------------------
