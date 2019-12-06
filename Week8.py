#!/usr/bin/env python
# coding: utf-8

# # Week 8 NumPy and Pandas Intro

# ## 1. Numpy (Numerical Python)

# - 과학적, 수학적 데이터를 정리/처리 하기 위한 라이브러리
# - NumPy의 array class 를 ndarray 로 명명한다
# - 대규모 행렬 데이터를 효율적으로 처리하도록 설계 되어 있다.<br>
#     **<행렬이라 함은, 하나의 변수 안에 여러 값을 저장하고자 할 때 사용하는 것>**
# - NumPy는 생성할 때 크기가 고정 된다.<br>
#     **<하나의 행렬을 생성하고 이후 그 크기를 수정하면 기존의 행렬이 삭제 되고 새로운 행렬이 생성된다.>**
# - 리스트와 다르게 유연하지 못하다. 하나의 열에 같은 종류의 데이터만 입력이 가능하다.
# - 하지만 리스트와 비교하여 메모리를 덜 소모하고 계산과정에서 보다 적은 단계를 거친다.

# ## 2. Array 생성

# ### 1) Array dimension

# In[3]:


import numpy as np #이 과정을 안 해주면 밑에 다 에러 뜸.


# In[4]:


arr1d= np.array([1,2,3]) #1dimension
arr1d


# In[5]:


arr2d= np.array([(1,2,3),(4,5,6),(7,8,9)]) #2dimension
arr2d


# In[9]:


arr3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]]) #3dimension
print(arr3d)


# <img src="http://www.oreilly.com/library/view/elegant-scipy/9781491922927/assets/elsp_0105.png">

# ### 2) numpy.arange

# pythoon의 built-in functioin 중 range()와 같으나, 리스트 대신 ndarray를 반환.<br>
# half-open interval로 변수 생성(마지막 값 생략)

# In[10]:


np.arange(10)


# In[11]:


np.zeros(10) #0만 10개 있는 행렬


# In[13]:


np.zeros((2,5)) #0만으로 2*5 행렬을 만든다


# In[14]:


np.ones((2,5))


# 배열의 크기가 커지면 배열을 초기화하는데도 시간이 걸린다. 이 시간을 단축하려면 배열을 생성만 하고 특정한 값으로 초기화를 하지 않는 empty 명령을 사용한다. empty 명령으로 생선된 배열에는 기존 메모리에 저장되어 있던 값이 있으므로 배열의 원소 값을 미리 알 수 없다. <br><i>#무슨 말인 지 잘 모르겠어요...<i>

# In[15]:


np.empty(10)


# ### 3) numpy.reshape

# 행렬의 값을 바꾸지 않으면서 모양만 변환하고자 할 때

# In[16]:


np.zeros(10).reshape(2,5)


# In[17]:


np.zeros(4)


# ### 4) ndarray 속성들

# In[19]:


# "ndim" 배열의 dimension의 수를 출력
print(arr1d.ndim)


# In[20]:


#"itemsize" 배열의 byte수를 출력
arr2d.itemsize


# In[22]:


# "dtype" 배열의 data type를 출력
arr2d.dtype


# In[23]:


#"size" 배열의 원소 개수를 출력
arr2d.size


# In[25]:


#"shape"배열의 shape를 (행,열)로 출력
arr3d.shape


# ### 5) NumPy 배열 연산

# In[28]:


a2d=np.array([(1,2,3),(4,5,6),(7,8,9)])
a2d


# In[29]:


a2d+1


# In[30]:


a2d*a2d


# In[31]:


a2d1=a2d+1
a2d1<a2d


# In[32]:


a2d1>a2d


# ### 6) NumPy 배열 인덱싱, 슬라이싱

# In[34]:


index=np.arange(0,20,2)
print(index)


# In[35]:


index[5]


# Basic slice syntax is "i:j:k"<br><br>
# i=Starting index<br>
# j=Stoping index<br>
# k=Step<br>

# In[36]:


index[0:10:3]


# In[37]:


index[5:9]


# In[39]:


index[5:9]=100
index


# In[40]:


index[:]=100
index


# <i>더 고차원의 배열을 인덱싱을 하면 원소 값이 출력 되는 것이 아니라, 하나의 배열(행)을 인덱싱 한다.<i>

# In[42]:


a2d=np.array([(1,2,3),(4,5,6),(7,8,9)])
print(a2d)


# In[43]:


a2d[0] #0번째 행이 출력


# In[44]:


a2d[0,0] #왼쪽 부터 0번째 원소가 출력


# In[45]:


a2d[1]=10,11,12
a2d


# <img src = "https://www.oreilly.com/library/view/python-for-data/9781449323592/httpatomoreillycomsourceoreillyimages2172114.png" width = 300>

# In[46]:


a2d[:2,1:]


# In[47]:


a3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])


# In[48]:


a3d[1]


# In[49]:


a3d[1,1]=13
a3d


# # Pandas

# 파이썬의 가장 큰 약점으로 여겨져온 데이터 분석 및 모델링 부문을 보완해주는 것이 Pandas! 굳이 R을 사용하지 않더라도 파이썬만으로 데이터 분석 가능하게 함.

# - Convert a Python list, dict, or NumPy arrray into a Pandas data frame
# - Open a local file using Pandas (e.g. CSV, EXCEL, TXT files, and etc.) 
# - Open a remote file or database through a URL

# **Pandas의 가장 기본적인 데이터 구성**

# 1) Series <br>
# - 1차원 배열과 비슷하나, NumPy와는 다르게 안에 속하는 데이터 값이 다른 종류여도 괜찮다.

# 2) DataFrame<br>
# - 데이터 표. 데이터를 행과 열로 정리하여 2차원의 배열 형태로 정렬한 것.<br>

# In[50]:


import pandas as pd


# ## 1. Series

# In[52]:


b_w = pd.Series([12,13,14,'number'])
b_w


# In[54]:


bw2=pd.Series([1,2,3,4], index=['a','b','c','d'])
bw2


# In[55]:


bw2['a']


# In[56]:


bw2[bw2>2]


# In[57]:


bw2*2


# ## 2. 데이터 로드

# In[ ]:


요약:<br><br>
- pd.read_csv
- pandas 만의 DataFrame=table
- 0으로 시작하는 특수한 인덱스
- 각 변수의 데이터 타입 확인 가능

