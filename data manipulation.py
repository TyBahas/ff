
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# In[2]:


directory = 'C:/Users/bahasty/Desktop/ff/scores'
pd.set_option('display.max_rows', 500)


# In[3]:


#weekly score parser
def WeekParser (xlsx, sheetnum):
    sheet = pd.read_excel(xlsx, 'Sheet'+str(sheetnum))
        
    team1 = sheet.head(22)
    team2 = sheet.tail(23)

    #team 1 formatting
    team1name = team1.columns[0]
    team1 = team1[[team1name,'Unnamed: 6']]
    team1['Team'] = team1name
    team1['Week'] = week
    team1 = team1.drop(team1.index[[0,1,2,12,13,14,15,21]])
    team1.columns = ['Position','Points','Team','Week']
    team1 = team1[['Team','Week','Position','Points']]
    team1 = team1.groupby(['Team','Week','Position']).sum()

    #team 2 formatting
    team2name = team2[team1name].values[0]        
    team2 = team2[[team1name,'Unnamed: 6']]
    team2['Team'] = team2name
    team2['Week'] = week
    team2 = team2.reset_index()
    team2 = team2.drop(team2.index[[0,1,2,3,13,14,15,16,22]])    
    team2.columns = ['index','Position','Points','Team','Week']
    team2 = team2[['Team','Week','Position','Points']]
    team2 = team2.groupby(['Team','Week','Position']).sum()
    
    frames = [team1,team2]
    final = pd.concat(frames)
    return final
    
        


# In[4]:


#creates empty dataframe
columns = ['Team','Week','Position','Points']
dataframe = pd.DataFrame(columns=columns)

#iterate over files in scores directory
x = 1
for filename in os.listdir(directory):
    xlsx = pd.ExcelFile(directory+'/'+filename)
    week = os.path.basename(filename)
    week = week[:-5]    
    sheetnum = 1
    
    
    while sheetnum < 7:
        final = WeekParser(xlsx,sheetnum)
        
        if x == 1:
            dataframe = final            
            x = x+1
        else:
            frames = [dataframe,final]
            dataframe = pd.concat(frames)
        
        sheetnum = sheetnum+1
    


# In[88]:



############################################
#week over week output  ready for Google ChartPaste
############################################

df_weekly = dataframe.unstack(level=-1)
df_weekly = df_weekly.reset_index()
df_weekly.columns = df_weekly.columns.droplevel()
df_weekly.columns = ['Team','Week','BN','DEF','K','QB','R/W/T','RB','TE','WR']
df_weekly['String'] = '[\'' + df_weekly['Team'].map(str)+'\',\''+ df_weekly['Week'].map(str) +'\',' + df_weekly['BN'].map(str) +','+ df_weekly['DEF'].map(str)+','+ df_weekly['K'].map(str)+','+ df_weekly['QB'].map(str)+','+ df_weekly['R/W/T'].map(str)  +','+ df_weekly['RB'].map(str)  +','+ df_weekly['TE'].map(str)  +','+ df_weekly['WR'].map(str)+'],'     
df_weekly.to_csv('weekly.csv', index=False)


# In[89]:



############################################
#total output ready for Google Chart Paste
############################################

df_sum = dataframe.groupby(['Team','Position']).sum()
df_sum = df_sum.round(2)
df_sum = df_sum.reset_index()
df_sum.columns = ['Team','Position','Total']
df_sum = df_sum.pivot(index='Team', columns='Position', values='Total')
df_sum = df_sum.reset_index()
df_sum['String'] = '[\'' + df_sum['Team'].map(str) +'\',' + df_sum['BN'].map(str) +','+ df_sum['DEF'].map(str)+','+ df_sum['K'].map(str)+','+ df_sum['QB'].map(str)+','+ df_sum['R/W/T'].map(str)  +','+ df_sum['RB'].map(str)  +','+ df_sum['TE'].map(str)  +','+ df_sum['WR'].map(str)+'],'     
df_sum.to_csv('sum.csv', index=False)


# In[90]:



############################################
#position averages overall
############################################

df_avg = dataframe.groupby(['Team','Position']).mean()
df_avg = df_avg.round(2)
df_avg = df_avg.reset_index()
df_avg.columns = ['Team','Position','Average']
df_avg = df_avg.pivot(index='Team', columns='Position', values='Average')
df_avg = df_avg.reset_index()
df_avg['String'] = '[\'' + df_avg['Team'].map(str) +'\',' + df_avg['BN'].map(str) +','+ df_avg['DEF'].map(str)+','+ df_avg['K'].map(str)+','+ df_avg['QB'].map(str)+','+ df_avg['R/W/T'].map(str)  +','+ df_avg['RB'].map(str)  +','+ df_avg['TE'].map(str)  +','+ df_avg['WR'].map(str)+'],'     
df_avg.to_csv('average.csv', index=False)


# In[162]:



############################################
#League data for scatter plot
############################################
#formatting data
league = pd.read_csv('C:/Users/bahasty/Desktop/ff/league/league.csv')
league = league.drop(league.index[[0,1,5,9,13]])   
league['divRank'] = league.Rank.str.slice(0,1)
league['overallRank'] = league.Rank.str.split(pat='[(|)]', expand=True)[1]
league = league[['Team','Stk','For','Against','divRank','overallRank']]

#scatter output
scatter =league[['Team','For','Against']]
scatter = scatter.pivot(index='For', columns='Team', values='Against')
scatter = scatter.reset_index()
scatter['String'] = '[' + scatter['For'].map(str)+','+ scatter['3 Dollar Steak'].map(str) +','+ scatter['Bronny Football'].map(str) +','+ scatter['Calrissian Colts'].map(str)+','+ scatter['Charlottesville Kaepernicks'].map(str)+','+ scatter['Icebox'].map(str)+','+ scatter['Mahom-osexuals'].map(str)+','+ scatter['Optimize'].map(str)+','+ scatter['Scruffy Nerfherders'].map(str)+','+ scatter['THE ROBERTSONS'].map(str)+','+ scatter['The Eastwatch Ice Dragons'].map(str)+','+ scatter['buckfutt fc (Alex)'].map(str)+','+ scatter['buckfutt fc (Ryan)'].map(str)+'],'    
scatter['String'] = scatter['String'].str.replace('nan','NaN')
scatter.to_csv('scatter.csv', index=False)


# In[211]:



x = dataframe.reset_index()
x = x.loc[x['Position'] != 'BN']
x = x.groupby(['Team','Week']).sum()
x = x.reset_index()
mean = x.groupby(['Team']).mean()
team_mean = mean.reset_index()
#std = x.groupby['Team'][['Points']].std()
#std
mean = team_mean['Points'].mean()
std = team_mean['Points'].std()
std



team_mean['STD'] = std
team_mean['Mean'] = mean
team_mean['Z-score'] = (team_mean['Points'] - team_mean['Mean'] )/ team_mean['STD']
team_mean

