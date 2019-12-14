#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install nba_api')


# In[2]:


def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict   


# In[3]:


import pandas as pd


# In[50]:


import matplotlib.pyplot as plt
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 12
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size


# In[7]:


from nba_api.stats.static import teams


# In[8]:


nba_teams = teams.get_teams()


# In[9]:


nba_teams[0:3]


# In[12]:


dict_nba_teams = one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_teams)
df_teams.head()


# In[29]:


df_wizards=df_teams[df_teams['city']=='Washington']
df_wizards


# In[32]:


id_wizards=df_wizards[['id']].values[0][0]
id_wizards


# In[33]:


from nba_api.stats.endpoints import leaguegamefinder


# In[34]:


gamefinder=leaguegamefinder.LeagueGameFinder(team_id_nullable=id_wizards)
gamefinder.get_json()


# In[35]:


games=gamefinder.get_data_frames()[0]
games.head()


# In[41]:


games_won = games [games ['PLUS_MINUS'] >= 0.0]
games_lost = games [games ['PLUS_MINUS'] < 0.0]


# In[51]:


fig, ax = plt.subplots()

games_won.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_lost.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["won", "lost"])
plt.show()


# In[ ]:




