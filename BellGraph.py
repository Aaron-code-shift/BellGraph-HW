import plotly.express as px
import csv 
import pandas as pd
import plotly.figure_factory as ff

dt = pd.read_csv('data3.csv')
fig = ff.create_distplot([dt['AvgRating'].tolist()] , ["AvgRating"] , show_hist = False)
fig.show()