from ggplot import *
import pandas as pd
import numpy
d= {'c1':1,'c2':2}
d1 = pd.DataFrame(data=numpy.random.randn(100),index=range(0,100))
kk = pd.read_csv("effi.csv")
print kk
m = pd.melt(kk,id_vars='Filter')
print m

print ggplot(aes(x='Filter',y='value',group='variable',shape='variable',color='variable'), data=m) + geom_point(size=100) +geom_line(size=2)+  theme(size=200)


