from __future__ import print_function, division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
%matplotlib inline

#load csv
%time train = pd.read_csv(r'data/train.csv', parse_dates=['Dates'])
%time test = pd.read_csv(r'data/train.csv', parse_dates=['Dates'])
%time sample = pd.read_csv(r'data/sampleSubmission.csv')

#Enrichment function
def enrich(df):
    # Some extra columns
    df['Hour'] = df.Dates.dt.hour
    df['Year'] = df.Dates.dt.year
    df['Month'] = df.Dates.dt.month
    df['DayOfWeek'] = df.Dates.dt.dayofweek
    df['Day'] = df.Dates.dt.day
   
%time enrich(train)
%time enrich(test)

