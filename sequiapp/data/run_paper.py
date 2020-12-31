# This Python file uses the following encoding: utf-8
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import geopandas as gpd

df_anom = pd.read_csv("Anomalies.csv", sep=',', skiprows=0)
df_anom = df_anom[ df_anom['cosecha_gruesa06'].notnull() & df_anom['cosecha_gruesa09'].notnull() & df_anom['cosecha_gruesa12'].notnull() & df_anom['cosecha_gruesa18'].notnull() ]

# Some pictures




# Spatial correlation of anomalies and yields

names = ["IMERG","SMAPL3","GLDAS","NDVI"]
years = [2006,2009,2012,2018]
months = [12, 1, 2, 3, 4]

def group(vals):
	groups = np.zeros(len(vals))
	groups[vals>0]=0
	groups[(vals>-0.15) & (vals<0)]=1
	groups[(vals>-0.3) & (vals<-0.15)]=2
	groups[(vals<-0.3)]=3
	return groups

for y in years:
    print('')
    print('YEAR: ' + str(y))
    for n in names:
        print(n + ' & ', end =" ")
        for m in months:
            yy = y if m != 12 else y-1
            aname = str(n) + "-" + str(yy) + "-" + str(m)
            cname = 'cosecha_gruesa' + str(y)[2:]
            corr, p_value = stats.kendalltau(group(df_anom[cname]),group(df_anom[aname]))
            print('{:2.2f}'.format(corr), end =" ")
            if (m==4):
                print("\\\\")
            else:
                print(' & ', end="")
        
            
# Classification

