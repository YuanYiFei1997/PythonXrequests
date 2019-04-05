import numpy as np
c=np.arange(12)
print(c)
c.shape=2,3,2
print(c)
print(np.linspace(1,10,12,endpoint=True))
print(np.logspace(0,5,6,base=2))

df=np.dtype([('name',np.str_,40),('num',np.int8),('price',np.float64)])
print(df)
products=np.array([("酱油",60,3.2),("白糖",34,2.1)],dtype=df)
print(products['name'])
np.random.seed(123)
#print(np.random.randn(10,5)) #正态分布
print(np.random.normal(0,1,[10]))