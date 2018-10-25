
# coding: utf-8

# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn import datasets
#from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[11]:


iris = datasets.load_iris()


# In[12]:


#print(iris)


# In[13]:


iris_data  = np.array(iris.data) 
iris_target= np.array(iris.target)

#print(iris_data.ndim)
#print(iris_data.shape)
#print(iris_target.ndim)
#print(iris_target.shape)
All_Data = np.column_stack((iris_data,iris_target))
                      
#print(All_Data)


# In[14]:


#S_length 花顎長度ref
#S_width  花半寬度
#P_length 花顎長度
#P_width  花半寬度
#樣本各取20個 3類共60個

ref0=np.array(All_Data[0:20])
ref1=np.array(All_Data[50:70])
ref2=np.array(All_Data[100:120])
#print(ref0)
#print("--------")
#print(ref1)
#print("--------")
#print(ref2)


# In[15]:


ref=np.row_stack((ref0,ref1,ref2))

print(ref)

print(ref[59,1])


# In[16]:


def dist(a,b):
    x0=a[0]
    x1=a[1]
    x2=a[2]
    x3=a[3]
    res=np.array([])
    for i in range(0,60):
        
        y0=b[i][0]
        y1=b[i][1]
        y2=b[i][2]
        y3=b[i][3]    
        res = np.append(res, np.sqrt( np.square(x0-y0) + np.square(x1-y1) + np.square(x2-y2) + np.square(x3-y3)  )  )
    return res
    #print(x0)
    #print(x1)
    #print(x2)
    #print(x3)
     


# In[216]:


a=np.array([5.7 ,1.8, 5.3, 1.8  ]) #1類
print(a)
print(dist(a,ref))


# In[217]:


#def Merge_sort(A):#小->大
    
#    if(A[0]>A[1]):
#        temp = A[1]
#        A[1] = A[0]
#        A[1] = temp
 
#    else:
#        A[0] = A[0]
#        A[1] = A[1]
        
#    arry=np.array([A[0],A[1]])
#    return arry        


# In[218]:


#x = np.array([4444,456,456])
#Merge_sort(x)
#x.size


# In[219]:


def Bubble(A):#小->大
    B=np.array(A)
    B_size=B.size
    #print(B_size)
    for i in range (0,B_size):
        #print('{0} {1}'.format("i=", i))
        
        for j in range (i+1,B_size):
            #print('{0} {1}'.format("j=", j))
            if(B[i]>B[j]):
                temp=B[i]
                B[i]=B[j]
                B[j]=temp

    print (B)  
    return B
x = np.array([56,18,59,45,456,44,87,11,1])
Bubble(x)    


# In[220]:


Dist_Oped=np.array(Bubble(dist(a,ref)))


# In[225]:


#D1 第1筆 跟D2每一筆 比較 找相同 
#return 哪幾筆?
                 #(D1,D2,K=找幾筆最相近)  
def Linear_Compare(D1,D2,K):
    D2_len=D2.size
    res=np.array([])
    for i in range (0,K):
        for j in range (0,D2_len):
            if(D1[i]==D2[j]):
                res = np.append(res,j)
               # ress=j
    return(res)            


# In[248]:


Data_No=Linear_Compare(Dist_Oped,dist(a,ref),10)
print(Data_No)
#找是處理前第幾筆 Data


# In[249]:


def Decide_target(Data_No,K):
    Final_Res=np.array([])
    for i in range (0,K):
        #print(int(Data_No[i]))
        x=int(Data_No[i])
        #print (ref[x,4])
        Final_Res=np.append(Final_Res,ref[x,4])
    
    print(Final_Res)
    
    
    #掃描陣列 看是哪類 累加
    y=Final_Res.size
    t0=t1=t2=0
    for j in range (0,y):
        if(int(Final_Res[j])==0):
            t0=t0+1
        elif (int(Final_Res[j])==1):
            t1=t1+1
        elif (int(Final_Res[j])==2):
            t2=t2+1
    tt=np.array([t0,t1,t2])   
    print('{0} {1}'.format("各類個數:", tt))
    
    
    
     #判斷哪類最多
    #print(tt[0])
    target=-1
    
    #print(target)
    for p in range (0,3):
        #print(tt[p])
        if( target < tt[p]):
            target=p
            
            
    return target    


# In[250]:


Decide_target(Data_No,10)

