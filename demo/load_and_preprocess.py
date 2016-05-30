
from __future__ import print_function, division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#load csv
%time train = pd.read_csv(r'data/train.csv', parse_dates=['Dates'])

#Drop columns
train.drop(['Resolution'],axis=1,inplace=True)

#Some extra columns
%time train['Year'] = train.Dates.dt.year
%time train['Month'] = train.Dates.dt.month
%time train['Day'] = train.Dates.dt.day
%time train['DayOfWeek'] = train.Dates.dt.dayofweek
%time train['Hour'] = train.Dates.dt.hour

#let's get rid of the outliers
train = train[train.Y < 40]