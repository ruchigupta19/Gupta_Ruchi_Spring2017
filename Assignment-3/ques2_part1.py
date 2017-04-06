import pandas as pd
import numpy as np

df=pd.read_csv('employee_compensation.csv')     #reading the csv
df = df.rename(columns={'Organization Group Code':'Organization_Group_Code','Organization Group': 'Organization_Group','Department Code': 'Department_Code','Total Compensation':'Total_Compensation'})
												#renaming the headers
df1=df.groupby(['Organization_Group','Department']).Total_Compensation.mean().to_frame()
											    #grouping data by Organization_Group and Department and calculating Total_Compensation's mean
output_df=pd.DataFrame(columns=['Organization_Group','Department','Total_Compensation'])
												#creating a new dataframe
for index, row in df1.iterrows():				#writing the data to the dataframe
    output_df=output_df.append(pd.Series([index[0],index[1],row[0]],index=['Organization_Group','Department','Total_Compensation']),ignore_index=True)
												#appending data to the dataframe
output_df = output_df.sort_values(['Organization_Group','Total_Compensation'], ascending=[True,False])
												#sorting data for each Organization_Group
output_df.to_csv('ques2_part1.csv')				#writing data to a csv
print(output_df.head())