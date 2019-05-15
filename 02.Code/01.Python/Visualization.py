# Visualization.py
#     Title: Visualize using normalized data
#    Author: Seo JaeIck
# Create on: 2019.05.12
# --------------------------------------------------------------------------------------------------
# import module
# --------------------------------------------------------------------------------------------------
# A class that runs Word Cloud on Python.
from wordcloud import WordCloud
# A class that helps matrix operations.
import numpy as np
# A class that generates and operates on matrix data.
import pandas as pd
# A class that implements data visualization.
import matplotlib.pyplot as plt
import matplotlib as mpl
# --------------------------------------------------------------------------------------------------
# Set Parameter(Data)
# --------------------------------------------------------------------------------------------------
# Using Hangul in Python
## sudo apt-get install -y fonts-nanum*
mpl.rc('font', family='nanumgothic')
mpl.rc('axes', unicode_minus=False)

# Read the csv file that contains the actual data.
vote=pd.read_csv('../initialize_president.csv', encoding="euc-kr", header=1)
# Data Processing. Save candidates and votes data.
vote.drop('시도명', axis=1, inplace=True)
vote.drop('투표수', axis=1, inplace=True)
president_vote=vote.iloc[1]
voting=pd.to_numeric(president_vote.values)
# --------------------------------------------------------------------------------------------------
#  Class Name: Visualization
# Method list: base_linegraph, base_wordcloud, base_bargraph
#            : base_stackedbargraph, base_piegraph
#            : analysis_bargraph, analysis_stackedbargraph, analysis_piegraph
# -------------------------------------------------------------------------------------------------
class Visualization:
    # ----------------------------------------------------------------------------------------------
    # Line graph visualization using 'Json' data.
    # ----------------------------------------------------------------------------------------------
    def base_linegraph(self, b):         
        # Set the x and y axis of the line graph.
        plt.plot(b.keys(),   # X axis Data
                 b.values()) # Y axis Data
        # Set the title of the line graph.
        plt.title('Twitter used Count by date on a Line Graph')
        # Set the x axis label of the line graph.
        plt.xlabel('Date')
        # Set the y axis label of the line graph.
        plt.ylabel('Tweet Count')
        # Line graph visualization using JSON data
        plt.show()

    # ----------------------------------------------------------------------------------------------
    # Word Cloud visualization using 'HASHTAG_COUNT' data.
    # ----------------------------------------------------------------------------------------------
    def base_wordcloud(self, b):
        # Set a Path of Korean fonts
        path = '/home/vi/.local/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf/NanumBarunGothicUltraLight.ttf'
        # Set a word cloud
        wc=WordCloud(font_path=path,            # Set a Path of fonts
                     background_color='white',  # Background Color
                     max_words=2000)            # Maximum number of words
        # Create a word cloud
        wc=wc.generate_from_frequencies(b)
        # Set a title of word cloud
        plt.title('WordCloud')
        # Set a word cloud Output
        plt.imshow(wc,                          # Created word cloud
                   interpolation='bilinear')    # Plane Output
        # Screen output settings for x and y axis
        plt.axis('off')
        # Show word cloud
        plt.show()

    # ----------------------------------------------------------------------------------------------
    # Bar Graph visualization using 'HASHTAG_COUNT' data.
    # ----------------------------------------------------------------------------------------------
    def base_bargraph(self, b):
        plt.title('Number of hashtags used by date on a Bar Graph')
        plt.bar(list(b.keys()),list(b.values()))
        plt.xlabel('Keyword')
        plt.ylabel('Tweet Count')
        plt.show()


    def base_stackedbargraph(self, b):
        df=pd.DataFrame(list(b.values()),list(b.keys()), columns=['Count'])
        df.loc["ETC",:]=df['Count'][5:len(df)].sum()
        df=df.reset_index()
        df=df.drop(df.index[5:len(df)-1])
        df=df.set_index("index")
        df=df.reset_index()

        plt.bar('Count', df['Count'][0])
        plt.bar('Count', df['Count'][1], bottom=df['Count'][0])
        plt.bar('Count', df['Count'][2], bottom=sum(df['Count'][:2]))
        plt.bar('Count', df['Count'][3], bottom=sum(df['Count'][:3]))
        plt.bar('Count', df['Count'][4], bottom=sum(df['Count'][:4]))
        plt.bar('Count', df['Count'][5], bottom=sum(df['Count'][:5]))

        plt.title("Number of keywords used by date on a Stacked Bar Graph")
        plt.legend(df["index"], loc='center left',bbox_to_anchor=(1,0.5))
        plt.xlabel('Keyword')
        plt.ylabel('Tweet Count')
        plt.show()


    def base_piegraph(self, b):
        df=pd.DataFrame(list(b.values()),list(b.keys()), columns=['Count'])
        df.loc["ETC",:]=df['Count'][5:len(df)].sum()
        df=df.reset_index()
        df=df.drop(df.index[5:len(df)-1])
        df=df.set_index("index")
        df=df['Count'].astype('int')
        df=df.reset_index()

        count_sum=int(df["Count"].sum())
        countPer=[]
        for i in range(len(df)):
            countPer.append("%.1f%%" % float(df['Count'][i]/count_sum*100))
      
        result=[]
        for i in range(len(df)):
            result.append(str(df['Count'][i])+'\n'+countPer[i])


        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

        data=df["Count"]
        candidate = df["index"]

        wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)        

        bbox_props = dict(boxstyle="square", fc="w", ec="k", lw=0.72)
        kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            ax.annotate(result[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)
            ax.set_title("Pie Graph")

        plt.legend(df["index"], loc='center left',bbox_to_anchor=(1.3,0.7))
        plt.show()


    def analysis_bargraph(self, b):
        countlist=[b['문재인'],b['홍준표'],b['안철수'],b['유승민'],b['심상정']]
        candidate=['문재인','홍준표','안철수','유승민','심상정']
 
        df=pd.DataFrame(countlist,candidate, columns=['Tweet Count'])
        df2=pd.DataFrame(voting, president_vote.index,columns=['Vote Count'])
        dfResult=pd.concat([df,df2],axis=1)
        dfResult.plot.bar()
        plt.title('Supported Ratio on a Bar Graph')
        plt.xlabel('Candidate')
        plt.ylabel('Tweet Count')
        plt.show()


    def analysis_stackedbargraph(self, b):
        countlist=[b['문재인'],b['홍준표'],b['안철수'],b['유승민'],b['심상정']]
        candidate=['문재인','홍준표','안철수','유승민','심상정']

        df=pd.DataFrame(countlist,candidate, columns=['Tweet Count'])
        df=df.reset_index()
        df=df.set_index("index")
        df=df.reset_index()

        plt.title("Supported Ratio on a Stacked Bar Graph")
        plt.bar('Count', df['Tweet Count'][0], color='b')
        plt.bar('Count', df['Tweet Count'][1], bottom=df['Tweet Count'][0], color='g')
        plt.bar('Count', df['Tweet Count'][2], bottom=sum(df['Tweet Count'][:2]), color='r')
        plt.bar('Count', df['Tweet Count'][3], bottom=sum(df['Tweet Count'][:3]), color='c')
        plt.bar('Count', df['Tweet Count'][4], bottom=sum(df['Tweet Count'][:4]), color='m')
        plt.legend(df["index"], loc='center left',bbox_to_anchor=(1,0.5))


        plt.bar('Vote Count', voting[0], color='b')
        plt.bar('Vote Count', voting[1], bottom=voting[0], color='g')
        plt.bar('Vote Count', voting[2], bottom=sum(voting[:2]), color='r')
        plt.bar('Vote Count', voting[3], bottom=sum(voting[:3]), color='c')
        plt.bar('Vote Count', voting[4], bottom=sum(voting[:4]), color='m')

        plt.legend(president_vote.index,loc='center left',bbox_to_anchor=(1,0.5))
        plt.xlabel('19th Presidential election Vote rate')
        plt.ylabel('Tweet Count')
        plt.show()


    def analysis_piegraph(self, b):
        countlist=[b['문재인'],b['홍준표'],b['안철수'],b['유승민'],b['심상정']]
        candidate=['문재인','홍준표','안철수','유승민','심상정']
        count_sum=(countlist[0]+countlist[1]+countlist[2]+countlist[3]+countlist[4])
        df=pd.DataFrame(countlist,candidate, columns=['Tweet Count'])
        df=df.reset_index()
        df=df.set_index("index")
        df=df.reset_index()
        data = df["Tweet Count"]

        countPer=[]
        countPer.append("%.1f%%" % float(countlist[0]/count_sum*100))
        countPer.append("%.1f%%" % float(countlist[1]/count_sum*100))
        countPer.append("%.1f%%" % float(countlist[2]/count_sum*100))
        countPer.append("%.1f%%" % float(countlist[3]/count_sum*100))
        countPer.append("%.1f%%" % float(countlist[4]/count_sum*100))

        result=[]
        result.append(str(countlist[0])+'\n'+countPer[0])
        result.append(str(countlist[1])+'\n'+countPer[1])
        result.append(str(countlist[2])+'\n'+countPer[2])
        result.append(str(countlist[3])+'\n'+countPer[3])
        result.append(str(countlist[4])+'\n'+countPer[4])

        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
        wedges, autotexts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)        
        bbox_props = dict(boxstyle="square", fc="w", ec="k", lw=0.72)
        kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            ax.annotate(result[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)
            ax.set_title("Tweet Count on a Pie Graph")

        plt.setp(autotexts, size=9, weight="bold")
        plt.legend(df["index"], loc='center left',bbox_to_anchor=(1.3,0.7))



        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
        candidate = president_vote.index
        data = voting
        wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)        
        bbox_props = dict(boxstyle="square", fc="w", ec="k", lw=0.72)
        kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

        count_sum2=(voting[0]+voting[1]+voting[2]+voting[3]+voting[4])
        countPer2=[]
        countPer2.append("%.1f%%" % float(voting[0]/count_sum2*100))
        countPer2.append("%.1f%%" % float(voting[1]/count_sum2*100))
        countPer2.append("%.1f%%" % float(voting[2]/count_sum2*100))
        countPer2.append("%.1f%%" % float(voting[3]/count_sum2*100))
        countPer2.append("%.1f%%" % float(voting[4]/count_sum2*100))

        result2=[]
        result2.append(str(voting[0])+'\n'+countPer[0])
        result2.append(str(voting[1])+'\n'+countPer[1])
        result2.append(str(voting[2])+'\n'+countPer[2])
        result2.append(str(voting[3])+'\n'+countPer[3])
        result2.append(str(voting[4])+'\n'+countPer[4])

        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            ax.annotate(result2[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)
            ax.set_title("Voting Rate on a Pie Graph")

        plt.legend(candidate, loc='center left',bbox_to_anchor=(1.3,0.7))
        plt.show()
