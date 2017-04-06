import pandas as pd
import numpy as np

df=pd.read_csv('employee_compensation.csv')     #reading the csv
df = df.rename(columns={'Organization Group Code':'Organization_Group_Code','Organization Group': 'Organization_Group','Department Code': 'Department_Code','Total Compensation':'Total_Compensation'})
												#renaming the headers
df1=df.groupby(['Organization_Group','Department']).Total_Compensation.mean().to_frame()
											    #grouping data by Organization_Group and Department and calculating Total_Compensation's mean
df1=df1.reset_index()
												#reseting the index
df1 = df1.sort_values(['Organization_Group','Total_Compensation'], ascending=[True,False])
												#sorting data for each Organization_Group
df1.to_csv('ques2_part1.csv')				    #writing data to a csv
print(df1.head())