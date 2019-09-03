import pandas as pd
import numpy as np

df =  pd.DataFrame(np.random.randn(5, 3), columns=list('ABC'))


def highlight_cols(s):
     color = 'grey'
     return 'background-color: %s' % color

	 
def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color
	
df2 = df.style.applymap(color_negative_red)

#df.style.applymap(highlight_cols, subset=pd.IndexSlice[:, ['B', 'C']])
df2.to_html('index.html')



#data.style



#html = (df.style.format(percent).render())



#df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

#print(data)

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