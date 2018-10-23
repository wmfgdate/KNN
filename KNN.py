
# coding: utf-8

# In[1]:


from sklearn import datasets
#from sklearn.neighbors import KNeighborsClassifier
import numpy as np


# In[2]:


iris = datasets.load_iris()


# In[5]:


#print(iris)


# In[6]:


iris_data  = np.array(iris.data) 
iris_target= np.array(iris.target)

#print(iris_data.ndim)
#print(iris_data.shape)
#print(iris_target.ndim)
#print(iris_target.shape)
All_Data = np.column_stack((iris_data,iris_target))
                      
print(All_Data)


# In[8]:


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


# In[9]:


ref=np.row_stack((ref0,ref1,ref2))
print(ref)

