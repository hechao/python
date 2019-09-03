import pandas as pd
import numpy as np

#df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

df =  pd.DataFrame(np.random.randn(5, 3), columns=list('ABC'))

html = (df.style.format(percent).render())

#print(data)
# def highlight_cols(s):
    # color = 'grey'
    # return 'background-color: %s' % color

#data.style.applymap(highlight_cols, subset=pd.IndexSlice[:, ['B', 'C']])

data.style

#print(data)

#df = pd.read_clipboard(s) #Copy and paste then do this 

#df = pd.
# def to_color(x): 
    # return ["background-color: %s"%i for i in df.color] 
# df.style.apply(to_color, axis=0) 

#print(df.species)
#print(df.columns)
#df.columns

#df.style.format('${0:,.2f}')

#print(df)