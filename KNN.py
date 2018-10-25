
# coding: utf-8

# In[45]:


get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn import datasets
#from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt


# In[46]:


iris = datasets.load_iris()


# In[47]:


#print(iris)


# In[53]:


iris_data  = np.array(iris.data) 
iris_target= np.array(iris.target)

#print(iris_data.ndim)
#print(iris_data.shape)
#print(iris_target.ndim)
#print(iris_target.shape)
All_Data = np.column_stack((iris_data,iris_target))
                      
#print(All_Data)


# In[54]:


#S_length 花顎長度ref
#S_width  花半寬度
#P_length 花顎長度
#P_width  花半寬度
#樣本各取20個 3類共60個

ref0=np.array(All_Data[0:19])
ref1=np.array(All_Data[50:69])
ref2=np.array(All_Data[100:119])
#print(ref0)
#print("--------")
#print(ref1)
#print("--------")
#print(ref2)


# In[55]:


ref=np.row_stack((ref0,ref1,ref2))
#print(ref)


# In[51]:


def dist(a,b):
    x0=a[0]
    x1=a[1]
    x2=a[2]
    x3=a[3]
    
    y0=b[0]
    y1=b[1]
    y2=b[2]
    y3=b[3]    
    
    print(x0)
    print(x1)
    print(x2)
    print(x3)
    return np.sqrt(np.square(x0-y0)+np.square(x1-y1)+
                   np.square(x2-y2)+np.square(x3-y3))
     


# In[52]:


a=np.array([4.9 ,2.4, 3.3, 1.  ]) #1類
print(a)
print(dist(ref[]))

