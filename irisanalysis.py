import pandas as pd 
df=pd.read_csv('/home/harsha/Desktop/Python Mini Project/iris.csv')

#Statistical Information
print(df.describe())

#Non-NaN Data
missingfreedf=df.fillna('0')

#Before Binning
#Attribute 1: Sepal Length
df.hist('sepal_length','species',rwidth=0.5,color='red')
#Attribute 2: Sepal Width
df.hist('sepal_width','species',rwidth=0.5,color='blue')
#Attribute 3: Petal Length
df.hist('petal_length','species',rwidth=0.5,color='Green')
#Attribute 4: Petal Width
df.hist('petal_width','species',rwidth=0.5,color='yellow')

#Binning
df['binned']=pd.cut(df['sepal_length'],bins=10)
df['binned']=pd.cut(df['sepal_width'],bins=10)
df['binned']=pd.cut(df['petal_length'],bins=10)
df['binned']=pd.cut(df['petal_width'],bins=10)
#After Binning
#Attribute 1: Sepal Length
df.hist('sepal_length','binned',color='red')
#Attribute 2: Sepal Width
df.hist('sepal_width','binned',color='blue')
#Attribute 3: Petal Length
df.hist('petal_length','binned',color='Green')
#Attribute 4: Petal Width
df.hist('petal_width','binned',color='Yellow')
