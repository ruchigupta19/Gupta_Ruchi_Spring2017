import pandas as pd
import numpy as np

output_df=pd.DataFrame(columns=['home','away','winner','innings1','innings1_runs','innings2','innings2_runs','final_runs'])  #output dataframe
df=pd.read_csv('cricket_matches.csv')                                                                                        #reading csv
home_equals_winner=df[df.home == df.winner]                                                                                  #checking if the host team is the winner
for index, row in home_equals_winner.iterrows():                                                                             #looping over all the rows
    if row.winner==row.innings2:                                                                                             #checking if final runs are innings2 or innings1 runs
        row['final_runs']=row.innings2_runs
    elif row.winner==row.innings1:
        row['final_runs']=row.innings1_runs
    output_df=output_df.append(pd.Series([row['home'],row['away'],row['winner'],row['innings1'],row['innings1_runs'],row['innings2'],row['innings2_runs'],row['final_runs']],index=['home','away','winner','innings1','innings1_runs','innings2','innings2_runs','final_runs']),ignore_index=True)
																															 #appending data to output dataframe
finaldf=output_df.groupby(['home']).final_runs.mean()																		 #grouping by home and taking mean of final runs
finaldf.to_csv('ques3.csv')                                                                                                  #writing data to csv
print(finaldf.head())
