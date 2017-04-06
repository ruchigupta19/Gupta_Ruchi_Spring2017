import pandas as pd
import numpy as np

df=pd.read_csv('employee_compensation.csv')                                                     #read csv
resltdf=df[df['Year Type']=="Calendar"]															#filtering by tear type calendar
resltdf=resltdf.groupby(['Year','Job Family','Job','Employee Identifier']).mean()				#taking mean of all columns
resltdf = resltdf.reset_index()																	#reseting index
resltdf=resltdf[resltdf['Overtime']>.05*resltdf['Salaries']]									#filtering values when Overtime is > .05 of salary
resltdf=resltdf[['Job Family','Total Benefits','Total Compensation']]                           #taking only required columns
resltdf=resltdf.groupby('Job Family').mean()													#taking avg of Total Benefits & Total Compensation acrding to Job Family
resltdf = resltdf.reset_index()
resltdf['percent total benifit']=((resltdf['Total Benefits']*100)/resltdf['Total Compensation'])#making percent column
resltdf = resltdf.sort_values(['percent total benifit'], ascending=[False])						#sorting percent values from highest to lowest
resltdf.to_csv('ques2_part2.csv')																#creating scv
print(resltdf.head())