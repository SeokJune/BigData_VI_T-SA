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
# Method list: linegraph, wordcloud, bargraph
#            : stackedbargraph, piegraph
# -------------------------------------------------------------------------------------------------
class Visualization:
    # ----------------------------------------------------------------------------------------------
    # Line graph visualization using 'Json' data.
    # ----------------------------------------------------------------------------------------------
    def linegraph(self, tweetData, query):    
        # Set the x, y axis and markers of the line graph.
        plt.plot(tweetData.keys(),   # X axis Data
                 tweetData.values(), # Y axis Data
                 label=query,    # Label name
                 marker='o',         # Marker type of graph
                 mfc='r')            # Marker's Color
        # Set the title of the line graph.
        plt.title('키워드 검색을 통한 날짜별 통계')
        plt.xticks(['2017-04-18','2017-04-25','2017-05-02', '2017-05-09'])
        # Set the y axis label of the line graph.
        plt.ylabel('트윗 갯수')
        # Grid Patterns Background
        plt.grid()
        # Location of Label
        plt.legend(loc='upper right')
        # Line graph visualization using JSON data
        plt.show()

    # ----------------------------------------------------------------------------------------------
    # Word Cloud visualization using 'KEYWORD_COUNT' data.
    # ----------------------------------------------------------------------------------------------
    def wordcloud(self, tweetData):
        # Set a Path of Korean fonts
        path = '/home/vi/.local/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf/NanumBarunGothicUltraLight.ttf'
        # Set a word cloud
        wc=WordCloud(font_path=path,            # Set a Path of fonts
                     background_color='white',  # Background Color
                     max_words=2000)            # Maximum number of words
        # Create a word cloud
        wc=wc.generate_from_frequencies(tweetData)
        # Set a word cloud Output
        plt.imshow(wc,                          # Created word cloud
                   interpolation='bilinear')    # Plane Output
        # Screen output settings for x and y axis
        plt.axis('off')
        # Show word cloud
        plt.show()

    # ----------------------------------------------------------------------------------------------
    # Bar Graph visualization using 'KEYWORD_COUNT' data.
    # ----------------------------------------------------------------------------------------------
    def bargraph(self, tweetData, base_analysis):
        # 'Base' is graphically displayed using 'KEYWORD_COUNT'.
        # 'Analysis' shows the graph using 'KEYWORD_COUNT' and comparison data.
        # Base=0, Analysis=1.
        # Analysis Bar Graph
        if base_analysis==1:
            # Save the number of times the names of the candidates.
            countlist=[tweetData['문재인'], tweetData['홍준표'], tweetData['안철수'], tweetData['유승민'], tweetData['심상정']]
            # Save candidates' names.
            candidate=['문재인','홍준표','안철수','유승민','심상정']
 
            # Data frame with 'Tweet Count' as a column
            df2=pd.DataFrame(countlist,candidate, columns=['트윗 횟수'])
            # Data frame with 'Vote Count' as a column
            df3=pd.DataFrame(voting, president_vote.index,columns=['투표율'])

            count_sum=sum(countlist)
            result=[]
            for i in range(len(df2)):
                result.append(int(countlist[i]/count_sum*100))
            result=pd.DataFrame(result,candidate,columns=['트윗 비율'])      
            # Connect the data frame.
            dfResult=pd.concat([result,df3],axis=1)

            # Outputs the number of votes and votes for each candidate side by side.
            dfResult.plot.bar()
            # Set a titles on a Bar Graph.
            plt.title('트위터 비율과 실제 투표율 비교')
            # Location of Label
            plt.legend(loc='upper right')

            # Show Bar Graph
            plt.show()   
        # Base Bar Graph
        else:
            # Create data frame using 'keyword_count'
            df=pd.DataFrame(list(tweetData.values()),list(tweetData.keys()), columns=['Count'])
             # Sort data frames in descending order by 'Count' value
            df=df.sort_values(['Count'],ascending=False)
            # Index resets.
            df=df.reset_index()
            # Eliminate remaining values except 'ETC', 1st to 5th.
            df=df.drop(df.index[10:])
            # Index Setting.
            df=df.set_index("index")
            # Index resets.
            df=df.reset_index()

            # Set the title of the bar graph.
            plt.title('상위 10개 키워드')
            # Set the x, y axis and markers of the bar graph.
            plt.bar(df['index'],df['Count'])
            # Set the y axis label of the bar graph.
            plt.ylabel('트윗 횟수')
            # Show bar graph
            plt.show()
                     
    # ----------------------------------------------------------------------------------------------
    # Stacked Bar Graph visualization using 'KEYWORD_COUNT' data.
    # ----------------------------------------------------------------------------------------------
    def stackedbargraph(self, tweetData, base_analysis):
        # Create data frame using 'keyword_count'
        df=pd.DataFrame(list(tweetData.values()),list(tweetData.keys()), columns=['Count'])
        # Sort data frames in descending order by 'Count' value
        df=df.sort_values(['Count'],ascending=False)
        # Sum of the remaining values except for 1st to 5th.
        df.loc["ETC",:]=df['Count'][10:len(df)].sum()
        # Index resets.
        df=df.reset_index()
        # Eliminate remaining values except 'ETC', 1st to 5th.
        df=df.drop(df.index[10:len(df)-1])
        # Index Setting.
        df=df.set_index("index")
        # Index resets.
        df=df.reset_index()
        # Analysis Stacked Bar Graph
        if base_analysis==1:
            # Save the number of times the names of the candidates.
            countlist=[tweetData['문재인'], tweetData['홍준표'], tweetData['안철수'], tweetData['유승민'], tweetData['심상정']]
            # Save candidates' names.
            candidate=['문재인','홍준표','안철수','유승민','심상정']

            # Data frame with '트윗 횟수' as a column
            df2=pd.DataFrame(countlist,candidate, columns=['트윗 횟수'])
            # Index resets.
            df2=df2.reset_index()
            # Index Setting.
            df2=df2.set_index("index")
            # Index resets.
            df2=df2.reset_index()

            # Data frame with '투표율' as a column
            df3=pd.DataFrame(voting, president_vote.index,columns=['투표율'])

            count_sum=sum(countlist)
            result=[]
            for i in range(len(df2)):
                result.append(int(countlist[i]/count_sum*100))
            result=pd.DataFrame(result,candidate,columns=['트윗 비율'])      



            # Set a titles on a Stacked Bar Graph.
            plt.title("트윗 비율과 투표율의 비교")
            # At the bottom of the Stacked Bar Graph. Bar color is blue.
            plt.barh('트윗 비율', result['트윗 비율'][0], color='b')
            # At the second bottom of the Stacked Bar Graph. Bar color is green
            plt.barh('트윗 비율', result['트윗 비율'][1], left=result['트윗 비율'][0], color='g')
            # At the third bottom of the Stacked Bar Graph. Bar color is red.
            plt.barh('트윗 비율', result['트윗 비율'][2], left=sum(result['트윗 비율'][:2]), color='r')
            # At the fourth bottom of the Stacked Bar Graph. Bar color is cyan.
            plt.barh('트윗 비율', result['트윗 비율'][3], left=sum(result['트윗 비율'][:3]), color='c')
            # At the top of the Stacked Bar Graph. Bar color is magenta.
            plt.barh('트윗 비율', result['트윗 비율'][4], left=sum(result['트윗 비율'][:4]), color='m')
            # Settings label
            plt.legend(df2["index"],            # Setting label's name
                       loc='center left',       # Label's location
                       bbox_to_anchor=(1,0.5))  # Detailed location of label

            # At the bottom of the Stacked Bar Graph. Bar color is blue.
            plt.barh('투표율', voting[0], color='b')
            # At the second bottom of the Stacked Bar Graph. Bar color is green
            plt.barh('투표율', voting[1], left=voting[0], color='g')
            # At the third bottom of the Stacked Bar Graph. Bar color is red.
            plt.barh('투표율', voting[2], left=sum(voting[:2]), color='r')
            # At the fourth bottom of the Stacked Bar Graph. Bar color is cyan.
            plt.barh('투표율', voting[3], left=sum(voting[:3]), color='c')
            # At the fifth bottom of the Stacked Bar Graph. Bar color is magenta.
            plt.barh('투표율', voting[4], left=sum(voting[:4]), color='m')
            # Settings label
            plt.legend(president_vote.index,    # Setting label's name
                       loc='center left',       # Label's location
                       bbox_to_anchor=(1,0.5))  # Detailed location of label
            # Set the x axis label of the stacked bar graph.
            plt.xlabel('트윗 수')
            # Show stacked bar graph.
            plt.show()

        # Base Stacked Bar Graph
        else :
            plt.figure(figsize=(9,3))
            # At the bottom of the Stacked Bar Graph. 
            plt.barh('키워드', df['Count'][0])
            # At the second bottom of the Stacked Bar Graph.
            plt.barh('키워드', df['Count'][1], left=df['Count'][0])
            # At the third bottom of the Stacked Bar Graph.
            plt.barh('키워드', df['Count'][2], left=sum(df['Count'][:2]))
            # At the fourth bottom of the Stacked Bar Graph.
            plt.barh('키워드', df['Count'][3], left=sum(df['Count'][:3]))
            # At the fifth bottom of the Stacked Bar Graph.
            plt.barh('키워드', df['Count'][4], left=sum(df['Count'][:4]))
            # At the top of the Stacked Bar Graph.
            plt.barh('키워드', df['Count'][5], left=sum(df['Count'][:5]))
            plt.barh('키워드', df['Count'][6], left=sum(df['Count'][:6]))
            plt.barh('키워드', df['Count'][7], left=sum(df['Count'][:7]))
            plt.barh('키워드', df['Count'][8], left=sum(df['Count'][:8]))
            plt.barh('키워드', df['Count'][9], left=sum(df['Count'][:9]))

            # Set a titles on a Stacked Bar Graph.
            plt.title("키워드 사용횟수")
            # Settings label
            plt.legend(df["index"],            # Setting label's name
                       loc='center left',      # Label's location
                       bbox_to_anchor=(1,0.5)) # Detailed location of label
            # Set the y axis label of the stacked bar graph.
            plt.xlabel('트윗 수')
            # Show stacked bar graph. 
            plt.show()      

    # ----------------------------------------------------------------------------------------------
    # Pie Graph visualization using 'KEYWORD_COUNT' data.
    # ----------------------------------------------------------------------------------------------
    def piegraph(self, tweetData, base_analysis):
        # Create data frame using 'keyword_count'
        df=pd.DataFrame(list(tweetData.values()),list(tweetData.keys()), columns=['Count'])
        # Sort data frames in descending order by 'Count' value
        df=df.sort_values(['Count'], ascending=False)
        # Sum of the remaining values except for 1st to 5th.
        etc=df['Count'][10:len(df)].sum()
#        df.loc["ETC",:]=df['Count'][10:len(df)].sum()
        # Index resets.
        df=df.reset_index()
        # Eliminate remaining values except 'ETC', 1st to 5th.
        df=df.drop(df.index[10:])
        # Index Setting.
        df=df.set_index("index")
        # Change 'Count' type to 'int' type
        df=df['Count'].astype('int')
        # Index resets.
        df=df.reset_index()

        # Total sum of 'Count'
        count_sum=int(df["Count"].sum())
        # List containing the percentage of each 'Count'
        countPer=[]
        # Append the percentage of each 'Count' to countPer
        for i in range(len(df)):
            countPer.append("%.1f%%" % float(df['Count'][i]/count_sum*100))      

        # List containing each 'Count' value and its percentage.
        result=[]
        # Store each 'Count' value and its percentage.
        for i in range(len(df)):
            result.append(str(df['Count'][i])+'\n'+countPer[i])


        # Analysis Pie Graph
        if base_analysis==1:
            # Save the number of times the names of the candidates.
            countlist=[tweetData['문재인'],tweetData['홍준표'],tweetData['안철수'],tweetData['유승민'],tweetData['심상정']]
            # Save candidates' names.
            candidate=['문재인','홍준표','안철수','유승민','심상정']
            # Total sum of 'countlist'
            count_sum2=(countlist[0]+countlist[1]+countlist[2]+countlist[3]+countlist[4])
            # Create data frame using 'countlist','candidate'
            df2=pd.DataFrame(countlist,candidate, columns=['Tweet Count'])
            df2=df2.sort_values(['Tweet Count'], ascending=False)
            # Index resets.
            df2=df2.reset_index()
            # Index Setting.
            df2=df2.set_index("index")
            # Index resets.
            df2=df2.reset_index()
            # Set 'Tweet Count' column to 'data'.
            data = df2["Tweet Count"]
            # List containing the percentage of each 'countlist'
            countPer2=[]
            # Append the percentage of each 'countlist' to countPer2
            for i in range(len(df2)):
                countPer2.append("%.1f%%" % float(df2["Tweet Count"][i]/count_sum2*100))      

            # List containing each 'countlist' value and its percentage.
            result2=[]
            # Store each 'countlist' value and its percentage.
            for i in range(len(df2)):
                result2.append(str(df2["Tweet Count"][i])+'\n'+countPer2[i])


            # Settings subplots.
            fig, ax = plt.subplots(figsize=(6, 3),                   # Subplots's size
                                   subplot_kw=dict(aspect="equal"))  # Automatically set x, y for SubPlots
            # Settings pie graph.
            wedges, texts = ax.pie(data,                             # The wedge sizes.
                                   wedgeprops=dict(width=0.5),       # Setting width
                                   startangle=120,                   # rotates the start of the pie chart by angle degrees counterclockwise from the x-axis.
                                   counterclock=False) 
            # Setting the box style
            bbox_props = dict(boxstyle="square", # Box style.
                              fc="w",            # Box's color
                              ec="k",            # Box edge's color
                              lw=0.72)           # Box edge's width
            # Show text, arrow, box on graph
            kw = dict(xycoords='data',                  # The coordinate system that xy is given in. default = 'data'
                      textcoords='data',                # Annotation point and text position default is value of xycoords
                      arrowprops=dict(arrowstyle="-"),  # Setting the arrows style
                      bbox=bbox_props,                  # Setting the box
                      zorder=0,                         # Order of the drawing
                      va="center")                      # Vertical alignment

            # Apply box and arrow to Pie Graph
            for i, p in enumerate(wedges):
                # Calculation to Angle
                ang = (p.theta2 - p.theta1)/2. + p.theta1
                # Change degree to radian.
                y = np.sin(np.deg2rad(ang))
                # Change degree to radian.
                x = np.cos(np.deg2rad(ang))
                # Decide left and right through the sign
                horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
                # Setting a arrows angle
                connectionstyle = "angle,angleA=0,angleB={}".format(ang)
                # Apply angle and style of arrow
                kw["arrowprops"].update({"connectionstyle": connectionstyle})
                # Create pie Graph
                ax.annotate(result2[i],                               # The text of the annotation.
                            xy=(x, y),                                # The point (x,y) to annotate.
                            xytext=(1.35*np.sign(x), 1.4*y),          # The position (x,y) to place the text at.
                            horizontalalignment=horizontalalignment,  # Return the horizontal alignment as string.
                            **kw)                                     # Apply to text, arrow, box's data
                # Set a titles on a Pie Graph.
                ax.set_title("Tweet Count on a Pie Graph")

            # Settings label
            plt.legend(df2["index"],             # Setting label's name
                       loc='center left',        # Label's location
                       bbox_to_anchor=(1.3,0.7)) # Detailed location of label


            df3=pd.DataFrame(voting, president_vote.index,columns=['투표율'])
            df3=df3.sort_values(['투표율'], ascending=False)
            # Index resets.
            df3=df3.reset_index()
            # Index Setting.
            df3=df3.set_index("index")
            # Index resets.
            df3=df3.reset_index()
            # Set 'Tweet Count' column to 'data'.
            data = df3["투표율"]

   
            # Settings Compare data to subplots.
            fig, ax = plt.subplots(figsize=(6, 3),                   # Subplots's size
                                   subplot_kw=dict(aspect="equal"))  # Automatically set x, y for SubPlots
            # Candidates for comparative data.
            candidate = president_vote.index
            # Vote rate of comparison data.
            data = voting
            # Settings pie graph.
            wedges, texts = ax.pie(data,                             # The wedge sizes.
                                   wedgeprops=dict(width=0.5),       # Setting width
                                   startangle=120,                   # rotates the start of the pie chart by angle degrees counterclockwise from the x-axis.
                                   counterclock=False)         
            # Setting the box style
            bbox_props = dict(boxstyle="square", # Box style.
                              fc="w",            # Box's color
                              ec="k",            # Box edge's color
                              lw=0.72)           # Box edge's width
            # Show text, arrow, box on graph
            kw = dict(xycoords='data',                  # The coordinate system that xy is given in. default = 'data'
                      textcoords='data',                # Annotation point and text position default is value of xycoords
                      arrowprops=dict(arrowstyle="-"),  # Setting the arrows style
                      bbox=bbox_props,                  # Setting the box
                      zorder=0,                         # Order of the drawing
                      va="center")                      # Vertical alignment


            # Total sum of 'voting' 
            count_sum3=(voting[0]+voting[1]+voting[2]+voting[3]+voting[4])
            # List containing the percentage of each 'countlist'
            countPer3=[]
            # Append the percentage of each 'voting' to countPer3
            for i in range(len(df2)):
                countPer3.append("%.1f%%" % float(voting[i]/count_sum3*100))          
            # List containing each 'voting' value and its percentage.
            result3=[]
            # Store each 'voting' value and its percentage.
            for i in range(len(df2)):
                result3.append(str(voting[i])+'\n'+countPer3[i])

            # Apply box and arrow to Pie Graph
            for i, p in enumerate(wedges):
                # Calculation to Angle
                ang = (p.theta2 - p.theta1)/2. + p.theta1
                # Change degree to radian.
                y = np.sin(np.deg2rad(ang))
                # Change degree to radian.
                x = np.cos(np.deg2rad(ang))
                # Decide left and right through the sign
                horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
                # Setting a arrows angle
                connectionstyle = "angle,angleA=0,angleB={}".format(ang)
                # Apply angle and style of arrow
                kw["arrowprops"].update({"connectionstyle": connectionstyle})
                # Create pie Graph
                ax.annotate(result3[i],                               # The text of the annotation.
                            xy=(x, y),                                # The point (x,y) to annotate.
                            xytext=(1.35*np.sign(x), 1.4*y),          # The position (x,y) to place the text at.
                            horizontalalignment=horizontalalignment,  # Return the horizontal alignment as string.
                            **kw)                                     # Apply to text, arrow, box's data
                # Set a titles on a Pie Graph.
                ax.set_title("Voting Rate on a Pie Graph")

            # Settings label
            plt.legend(candidate,                # Setting label's name
                       loc='center left',        # Label's location
                       bbox_to_anchor=(1.3,0.7)) # Detailed location of label
            # Show pie graph.
            plt.show()

        # Base Pie Graph
        else:
            # Settings to subplots.
            fig, ax = plt.subplots(figsize=(6, 3),                   # Subplots's size
                                   subplot_kw=dict(aspect="equal"))  # Automatically set x, y for SubPlots
            # Tweet Counts for data.
            data=df["Count"]
            # Settings pie graph.
            wedges, texts = ax.pie(data,                             # The wedge sizes.
                                   wedgeprops=dict(width=0.5),       # Setting width
                                   startangle=-40)                   # rotates the start of the pie chart by angle degrees counterclockwise from the x-axis.   

            bbox_props = dict(boxstyle="square", # Box style.
                              fc="w",            # Box's color
                              ec="k",            # Box edge's color
                              lw=0.72)           # Box edge's width

            kw = dict(xycoords='data',                  # The coordinate system that xy is given in. default = 'data'
                      textcoords='data',                # Annotation point and text position default is value of xycoords
                      arrowprops=dict(arrowstyle="-"),  # Setting the arrows style           
                      bbox=bbox_props,                  # Setting the box
                      zorder=0,                         # Order of the drawing
                      va="center")                      # Vertical alignment

            # Apply box and arrow to Pie Graph
            for i, p in enumerate(wedges):
                # Calculation to Angle
                ang = (p.theta2 - p.theta1)/2. + p.theta1
                # Change degree to radian.
                y = np.sin(np.deg2rad(ang))
                # Change degree to radian.
                x = np.cos(np.deg2rad(ang))
                # Decide left and right through the sign
                horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
                # Setting a arrows angle
                connectionstyle = "angle,angleA=0,angleB={}".format(ang)
                # Apply angle and style of arrow
                kw["arrowprops"].update({"connectionstyle": connectionstyle})
                # Create pie Graph
                ax.annotate(result[i],                                # The text of the annotation.
                            xy=(x, y),                                # The point (x,y) to annotate.
                            xytext=(1.35*np.sign(x), 1.4*y),          # The position (x,y) to place the text at.
                            horizontalalignment=horizontalalignment,  # Return the horizontal alignment as string.
                            **kw)                                     # Apply to text, arrow, box's data
                # Set a titles on a Pie Graph.
                ax.set_title("상위 10위 키워드")
            # Settings label
            plt.legend(df["index"],              # Setting label's name
                       loc='center left',        # Label's location
                       bbox_to_anchor=(1.3,0.7)) # Detailed location of label
            # Show pie graph.
            plt.show()
