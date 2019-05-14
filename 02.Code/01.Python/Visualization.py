# Visualization.py
#     Title: Visualize using normalized data
#    Author: Seo JaeIck
# Create on: 2019.05.12
# --------------------------------------------------------------------------------------------------

# import module
# --------------------------------------------------------------------------------------------------

## WordCloud

from wordcloud import WordCloud    # Using by WordCloud
import numpy as np  		   # Using by Pie Graph
import pandas as pd		   # Using by DataFrame 
import matplotlib.pyplot as plt    # Using by Graph
import matplotlib as mpl	   # Using by Korean Font


mpl.rc('font', family='nanumgothic')
mpl.rc('axes', unicode_minus=False)

vote=pd.read_csv('../initialize_president.csv', encoding="euc-kr", header=1)
vote.drop('시도명', axis=1, inplace=True)
vote.drop('투표수', axis=1, inplace=True)
president_vote=vote.iloc[1]
voting=pd.to_numeric(president_vote.values)


class Visualization:
    def base_linegraph(self, b):
        plt.plot(b.keys(),b.values())
        plt.title('Number of keywords used by date on a Line Graph')
        plt.show()

    def base_wordcloud(self, b):
        path = '/home/vi/.local/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf/NanumBarunGothicUltraLight.ttf'
        wc=WordCloud(font_path=path,background_color='white',max_words=2000)
        wc=wc.generate_from_frequencies(b)

        plt.title('WordCloud')
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.show()


    def base_bargraph(self, b):
#        df=pd.DataFrame(list(b.values()),list(b.keys()), columns=['Count'])
#        df.loc["ETC",:]=df['Count'][5:len(df)].sum()
#        df=df.reset_index()
#        df=df.set_index("index")
#        df=df.reset_index()
        plt.title('Number of keywords used by date on a Bar Graph')
        plt.bar(list(b.keys()),list(b.values()))
        plt.show()




    def analysis_bargraph(self, b):
        countlist=[b['문재인'],b['홍준표'],b['안철수'],b['유승민'],b['심상정']]
        candidate=['문재인','홍준표','안철수','유승민','심상정']
#        can_df=pd.DataFrame(countlist, df2['index'],columns=['TweetCount'])
 
        df=pd.DataFrame(countlist,candidate, columns=['Tweet Count'])
        df2=pd.DataFrame(voting, president_vote.index,columns=['Vote Count'])
        result=pd.concat([df,df2],axis=1)
        result.plot.bar()
        plt.title('Supported Ratio on a Bar Graph')
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
#        plt.bar('Count', df['Count'][5], bottom=sum(df['Count'][:5]))

    #    plt.title("Supported Ratio on a Stacked Bar Graph")
        plt.legend(df["index"], loc='center left',bbox_to_anchor=(1,0.5))


        plt.bar('Vote Count', voting[0], color='b')
        plt.bar('Vote Count', voting[1], bottom=voting[0], color='g')
        plt.bar('Vote Count', voting[2], bottom=sum(voting[:2]), color='r')
        plt.bar('Vote Count', voting[3], bottom=sum(voting[:3]), color='c')
        plt.bar('Vote Count', voting[4], bottom=sum(voting[:4]), color='m')

        plt.legend(president_vote.index,loc='center left',bbox_to_anchor=(1,0.5))
        plt.show()


    def base_piegraph(self, b):

        df=pd.DataFrame(list(b.values()),list(b.keys()), columns=['Count'])
        df.loc["ETC",:]=df['Count'][5:len(df)].sum()
        df=df.reset_index()
        df=df.drop(df.index[5:len(df)-1])
        df=df.set_index("index")
        df=df.reset_index()

        def make_autopct(values):
            def my_autopct(pct):
                total=sum(values)
                val=int((pct*total)/100.0)
                return '{v:d}\n({p:.1f}%)'.format(p=pct,v=val)
            return my_autopct

        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

        percent=make_autopct(df["Count"])
        data=df["Count"]
        candidate = df["index"]
#        date=pd.to_numeric(df["Count"])
#        result=my_autopct(df["Count"][0])
#        print(result)
        wedges, texts, autotexts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40, autopct=make_autopct(df["Count"]))        

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
            ax.annotate(percent(i), xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)
            ax.set_title("Pie Graph")

        plt.setp(autotexts, size=9, weight="bold")
        plt.legend(df["index"], loc='center left',bbox_to_anchor=(1.3,0.7))
        plt.show()


    def analysis_piegraph(self, b):

        countlist=[b['문재인'],b['홍준표'],b['안철수'],b['유승민'],b['심상정']]
        candidate=['문재인','홍준표','안철수','유승민','심상정']

        print(list(countlist))

        df=pd.DataFrame(countlist,candidate, columns=['Tweet Count'])
        df=df.reset_index()
        df=df.set_index("index")
        df=df.reset_index()
        def make_autopct(values):
            def my_autopct(pct):
                total=sum(values)
                val=int(round(pct*total/100.0))
                return '{v:d}\n({p:.1f}%)'.format(v=val,p=pct)
            return my_autopct

        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

        candidate = df["index"]
#        date=pd.to_numeric(df["Tweet Count"])
        data = df["Tweet Count"]

        wedges, texts, autotexts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40, autopct=make_autopct(countlist))        

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
            ax.annotate(make_autopct(countlist[i]), xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)
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


        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            ax.annotate(my_autopct1(voting[i]), xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)
            ax.set_title("Voting Count on a Pie Graph")

        plt.setp(texts, size=9, weight="bold")
        plt.legend(candidate, loc='center left',bbox_to_anchor=(1.3,0.7))
        plt.show()
