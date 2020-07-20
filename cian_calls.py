import pandas as pd
import numpy as np
import plotly.offline as pyo
import dash_html_components as html
import plotly.graph_objs as go

df= pd.read_excel('D:/Работа/jilfond/Работа_дистанционная/Аналитика/Звонки с агрегаторов/Статистика звонков за 01.01.2020 - 30.06.2020.xlsx')
df['Длительность'] = pd.to_datetime(df['Длительность'], format='%H:%M:%S')
df['time'] = pd.to_timedelta(df['Длительность'].dt.strftime('%H:%M:%S'))
mask = (df['time'] >= '00:00:30')
df1 = df.loc[mask].reset_index(drop=True)

df2 = pd.Series(df1['Входящий номер'].value_counts(), name = 'Count').to_frame()


data = [go.Histogram(x=df2['Count'], xbins=dict(start=0, end=10, size=1))]



layout = go.Layout(title = 'Распределение звонков с циан')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='D:/Работа/jilfond/Работа_дистанционная/Аналитика/Звонки с агрегаторов/звонки_циан.html' )