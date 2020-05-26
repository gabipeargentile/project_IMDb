#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# ## IMDB Movies

# In[2]:


database = pd.read_csv("IMDb_movies.csv", sep = ",")
database["date_published"] = pd.to_datetime(database["date_published"])
database.head(15)


# ### Informações das colunas 

# In[3]:


database.info()


# In[4]:


list(database.columns)


# ### Limpando a base de dados
# - reviews_from_users 
# - reviews_from_critics
# 
# Queremos excluir da base de dados a parte que não possui nota dos críticos nem dos expectadores e algumas colunas que não farão parte do escopo do projeto.

# In[5]:


df1 = database[(database["reviews_from_critics"].notnull()) & (database["reviews_from_users"].notnull())]
df1.reset_index(drop = True, inplace = True)  ## resetando o indice das linhas
df1.drop(columns = ["usa_gross_income", "writer"], axis = "columns", inplace = True) ## excluindo colunas
df1


# In[6]:


database2 = database[(database["reviews_from_critics"].isnull()) | (database["reviews_from_users"].isnull())]
A = database.shape[0]
B = database2.shape[0]
print("O número de linhas inicial é:",  database.shape[0])
print("O número de linhas retiradas é:",  database2.shape[0])
print("O número de linhas restante é:",  A - B)


# In[7]:


df1.shape


# ## IMDB Ratings

# In[8]:


df2 = pd.read_csv("IMDb_ratings.csv", sep = ",")
df2.drop(["total_votes", "votes_10", "votes_9", "votes_8",
                "votes_7", "votes_6","votes_5", "votes_4", "votes_3",
                "votes_2", "votes_1", "us_voters_votes", "us_voters_rating",
                "non_us_voters_rating", "non_us_voters_votes"], axis = "columns", inplace = True)

# total_votes já está no IMDb Movies

df2


# ### Juntando as duas base de dados com merge

# In[9]:


left = df1
right = df2
df = left.merge(right, on='imdb_title_id')
df.head(15)


# In[40]:


df.shape


# ### Exportando pro Excel

# In[11]:

df.dropna(inplace=True)
df.to_csv("base_de_dados.csv", sep = ";", index = False) ## não salva o indice 

