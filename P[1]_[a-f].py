import csv
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.offline import iplot, init_notebook_mode
class ex1:
    def __init__(self,data,feature):
        self.data=data
        self.feature=feature
        self.dList=self.data['index'].to_list()
    def partA(self):
        # #part a / show 10 item random
        for i in range(10):
            x=(random.randint(1,len(self.data["index"])))
            print("item",i,":")
            print(self.data.iloc[x])
        
    def plott(self,category):
        # part b
        # sns.kdeplot(data=data[category], shade=True)
        plt.hist(self.data[category])
        plt.title(category)
        plt.show()
    # part c
    def cpart(self,x,y):
        colors = np.random.rand(len(self.data["index"])) 
        sns.scatterplot(x=self.data[x], y=self.data[y],c=colors, cmap='viridis')
        # plt.plot(x=data[x], y=data[y])
        plt.title(x+"/"+y)
        plt.show()
    def partD(self):
        # missing data
        # print("sum of null value in first:",data.isnull().sum())

        for i in self.feature:
            x=data[i].to_list()
            missing_values_count =x.count("?")
            print(i," missing data:",missing_values_count)
            self.data[i]=self.data[i].replace("?",None)
            print(self.data[i].isnull().sum())
            self.data[i]=self.data[i].dropna()
            # x=self.data[i].to_list()
            # missing_values_count =x.count("?")
            # print(i," missing data:",missing_values_count)
        # محاسبه میانگین و انحراف معیار داده‌ها
        mean = np.mean(self.data)
        std_dev = np.std(self.data)
        print("mean:\n",mean,"\n \n std_dev:\n",std_dev)
        # تعیین مرزهای بازه بین‌کوادری برای تشخیص outlierها
        print("/////////////////////////////////////////////////////////////////\n outliers")
        out=["age","edu_level","gain","hours-per-week","loss" ]
        for i in out:
            Q1 = np.percentile(self.data[i], 25)
            Q3 = np.percentile(self.data[i], 75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = [x for x in self.data[i] if x < lower_bound or x > upper_bound]

            print("Outliers for",i,":", len(outliers))


# read data
data=pd.read_csv("D:/pyton1/bro/Dataset1.csv")
dList=data['index'].to_list()
print(data.head())
feature=["index",
"age",    
"job_category",
"edu",
"edu_level",
"marriage",
"job",
"rel",
"race",
"sex" ,
"gain",
"loss",
"hours-per-week",
"nationality" ,
"salary" ]   

x=ex1(data,feature)
while(True):
    print("which part?\n(a=>press'1')\n(b=>'2')\n(c=>'3')\n(d=>'4')\n(exit=>0)")
    k=input()
    if k=='1':
        print("10 random sample:\n")
        x.partA()
    elif k=='2':
        catg=int(input("which category do you want to plot:(1)age  2)job_category3)edu4)edu_level 5)marriage6)job7)rel8)race9)sex10)gain11)loss12)hours-per-week13)nationality14)salary)") )
        print(feature[catg])
        x.plott(feature[catg])
    elif k=='3':
        one=int(input("which category do you want to plot:(1)age  2)job_category3)edu4)edu_level 5)marriage6)job7)rel8)race9)sex10)gain11)loss12)hours-per-week13)nationality14)salary)") )
        two=int(input())
        x.cpart(feature[one],feature[two])
    elif k=='4':
        x.partD()
    else:
        break
