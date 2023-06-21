# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PSROZEuvnD5J_3up7zl2ZGf1zpfJubYf
"""

import pandas as pd
import numpy as np

df=pd.read_csv('smartphones.csv')
df

for i in df.columns:
  print(df[i].value_counts())
  print("\n")

print(df['os'].unique())
df['card'].unique()

df.processor.value_counts()

df['price']=df['price'].str.replace(',','').str.replace('₹','').astype('int')
df['price']



df['os_new']=np.where(df['card'].str.contains('Android') | df['card'].str.contains('iOS') | df['card'].str.contains('HarmonyOS'),df['card'],df['os'])
df['card_new']=np.where(df['card'].str.contains('Android') | df['card'].str.contains('iOS') | df['card'].str.contains('HarmonyOS') | df['os'].str.contains('Memory'),df['os'],df['card'])
#df['card_new']=np.where(df['card'].str.contains('Android'),df['os'],df['card'])
#df['os_new']=np.where(df['card'].str.contains('Android'),df['card'],df['os'])
df.os_new.value_counts()



print(df['os_new'].unique())
print(df['card_new'].unique())

df['bat_cap']=df['battery'].str.split(' ').str[0].str.split('\u2009').str[0].astype(str)
df['bat_speed']=df['battery'].str.split(' ').str[3].str.split('W').str[0].astype(str)
df['bat_cap']=np.where(df['bat_cap'].str.isnumeric(),df['bat_cap'],np.NaN)
df['bat_speed']=np.where(df['bat_speed'].str.isnumeric(),df['bat_speed'],np.NaN)

df['bat_cap'] = df['bat_cap'].astype(float)
df['bat_speed'] = df['bat_speed'].astype(float)

df['os_ver']=df['os_new'].str.split('v').str[1].astype(str)
df['os_ver']=np.where(df['os_ver'].str.isnumeric(),df['os_ver'],np.NaN)
df['os_ver']=df['os_ver'].astype(float)
df



df['os_type']=df['os_new'].str.split(' ').str[0].astype(str)


df

df=df.drop(['card','os'],axis=1)

df=df[df['ram'].str.contains('GB') & df['ram'].str.contains(',')]
df.ram.value_counts()



df['ram_']=df['ram'].str.split("\u2009").str[0].astype(int)
df['rom']=df['ram'].str.split("\u2009").str[1].str.split(',').str[1].astype(int)
df['ram']=df['ram_']

df

df=df.drop('ram_',axis=1)

print(df.display.value_counts())

df['inches']=df['display'].str.split(" ").str[0].astype('str')
df.inches=df.inches.apply(pd.to_numeric,errors="ignore")
df.inches.unique()



df['inches']=np.where(df['inches'].str.isnumeric(),df['inches'],np.NaN)
df['inches']=df['inches'].astype(float)
df.inches

df['refresh_rate']=df['display'].str.split(",").str[2].str.split(" ").str[1].astype('float')
df.refresh_rate

df['notch']=df['display'].str.split(",").str[2].str.split(" ").str[5]
df.notch.value_counts()

df['pixel']=df['display'].str.split(",").str[1].str.split('\u2009').str[0].astype(float) * df['display'].str.split(",").str[1].str.split('\u2009').str[2].astype(float)
df.pixel.value_counts()

df=df.drop(['display','battery'],axis=1)
df

df.card_new.value_counts()

df.camera.value_counts()

df['camera_new']=np.where(df['card_new'].str.contains('MP'),df['card_new'],df['camera'])

#df['card_new']=np.where(df['card'].str.contains('Android'),df['os'],df['card'])
#df['os_new']=np.where(df['card'].str.contains('Android'),df['card'],df['os'])
df.camera_new.value_counts()



df['p_cam']=df['camera_new'].str.split(' & ').str[0].str.split('+').str[0].str.split('\u2009').str[0]
df.p_cam=np.where(df['p_cam'].str.isnumeric(),df.p_cam,np.NaN)
df.p_cam=df.p_cam.astype(float)
df['s_cam']=df['camera_new'].str.split(' & ').str[0].str.split('+').str[1].str.split('\u2009').str[0].str.split(' ').str[1]
df.s_cam=np.where(df['s_cam'].str.isnumeric(),df.s_cam,np.NaN)
df.s_cam=df.s_cam.astype(float)
df['t_cam']=df['camera_new'].str.split(' & ').str[0].str.split('+').str[2].str.split('\u2009').str[0].str.split(' ').str[1]
df.t_cam=np.where(df['t_cam'].str.isnumeric(),df.t_cam,np.NaN)
df.t_cam=df.t_cam.astype(float)
df.p_cam.unique()

df['f_cam']=df['camera_new'].str.split(' & ').str[0].str.split('+').str[1].str.split('\u2009').str[0].str.split(' ').str[1]
df.f_cam=np.where(df['f_cam'].str.isnumeric(),df.f_cam,np.NaN)
df.f_cam=df.f_cam.astype(float)
df.f_cam

df.drop(['camera','camera_new'],axis=1,inplace=True)
df

df.processor.unique()

df['proc_type']=df['processor'].str.split(',').str[0].str.split(' ').str[0]
df['proc_version']=df['processor'].str.split(',').str[0].str.split(' ').str[1]
df['core']=df['processor'].str.split(',').str[1].str.split(' ').str[1]
df['ghz']=df['processor'].str.split(',').str[2].str.split(' ').str[1].str.split('\u2009').str[0].astype('float')

df.drop(columns=['processor'],inplace=True)

df.sim.unique()

df['5G']=np.where(df['sim'].str.contains('5G'),1,0)
df['IR Blaster']=np.where(df['sim'].str.contains('IR Blaster'),1,0)
df['NFC']=np.where(df['sim'].str.contains('NFC'),1,0)
df.drop(columns=['sim'],inplace=True)
df

df.card_new.value_counts()

df['Brand']=df['model'].str.split(' ').str[0]
df.Brand.unique()

df.drop(columns=['model','card_new','os_new'],inplace=True)
df

df.columns

neworder = ['Brand','price','rating','bat_cap','bat_speed','ram','rom','os_ver','os_type','inches','refresh_rate','notch','pixel','p_cam','s_cam','t_cam','f_cam','proc_type', 'proc_version', 'core', 'ghz', '5G',
       'IR Blaster','NFC']
df=df.reindex(columns=neworder)
df

from google.colab import files

df.to_csv('cleaneddata.csv')

files.download('cleaneddata.csv')