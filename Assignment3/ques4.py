import pandas as pd
import numpy as np

output_df=pd.DataFrame(columns=['Awards','Awards_won','Awards_nominated','Prime_awards_Nominated','Oscar_awards_Nominated','Gloden_Globe_Nominate','BAFTA_Awards_Nominated','Prime_awards_Won','Oscar_awards_Won','Gloden_Globe_Won','BAFTA_Awards_Won'])
df=pd.read_csv('movies_awards.csv')
df['Awards']=df['Awards'].str.replace(r'&','.')                                   #replacing & with .
df['Awards']=df['Awards'].str.replace(r'Another','')                              #replacing another with empty string
df=df.drop(df.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18]],axis=1)      #dropping unwanted columns
for index, row in df.iterrows():                                                  #iterating over all the rows
    wins=0
    nominations=0
    Oscar_nominations=0
    Oscar_won=0
    Golden_Globe_won=0
    Golden_Globe_nominations=0
    Primetime_nominations=0
    Primetime_won=0
    BAFTA_nominations=0
    BAFTA_won=0
    if type(row['Awards'])!=float:												  #checking if the data is not an nan
        row['Awards']=row['Awards'].split('.')                                    #spliting data by .
        for i in range(len(row['Awards'])-1):                     
            if 'win' in row['Awards'][i]:                                         #if win is presented
                wins+=int(row['Awards'][i].split()[0])                            #adding the number of wins to the wins variable
            if 'nomination' in row['Awards'][i]:								  #if nominations is presented
                nominations+=int(row['Awards'][i].split()[0])                     #adding the number of nominations to the nominations variable
            if 'Oscar' in row['Awards'][i]:										  #if Oscar and nominated is presented
                if 'Nominated' in row['Awards'][i]:
                    Oscar_nominations+=int(row['Awards'][i].split()[2])
                    nominations+=Oscar_nominations								  #adding the number of Oscar nominations and nominations to their respective variable
                if 'Won' in row['Awards'][i]:									  #if Oscar and won is presented
                    Oscar_won+=int(row['Awards'][i].split()[1])
                    wins+=Oscar_won												  #adding the number of Oscar won and wins to their respective variable
            if 'Golden Globe' in row['Awards'][i]:								  #if Golden Globe and nominated is presented
                if 'Nominated' in row['Awards'][i]:
                    Golden_Globe_nominations+=int(row['Awards'][i].split()[2])
                    nominations+=Golden_Globe_nominations						  #adding the number of Golden Globe nominations and nominations to their respective variable
                if 'Won' in row['Awards'][i]:                                     #if Golden Globe and won is presented
                    Golden_Globe_won+=int(row['Awards'][i].split()[1])
                    wins+=Golden_Globe_won                                        #adding the number of Golden Globe wins and wins to their respective variable
            if 'Primetime Emmy' in row['Awards'][i]:							  #if Primetime Emmy and nominated is presented
                if 'Nominated' in row['Awards'][i]:
                    Primetime_nominations+=int(row['Awards'][i].split()[2])
                    nominations+=Primetime_nominations 					          #adding the number of Primetime Emmy nominations and nominations to their respective variable
                if 'Won' in row['Awards'][i]:									  #if Primetime Emmy and won is presented
                    Primetime_won+=int(row['Awards'][i].split()[1])
                    wins+=Primetime_won											  #adding the number of Primetime Emmy wins and wins to their respective variable
            if 'BAFTA' in row['Awards'][i]:										  #if BAFTA and nominated is presented
                if 'Nominated' in row['Awards'][i]:
                    BAFTA_nominations+=int(row['Awards'][i].split()[2])
                    nominations+=BAFTA_nominations								  #adding the number of BAFTA nominations and nominations to their respective variable
                if 'Won' in row['Awards'][i]:									  #if BAFTA and won is presented
                    BAFTA_won+=int(row['Awards'][i].split()[1])
                    wins+=BAFTA_won												  #adding the number of BAFTA wins and wins to their respective variable
        output_df=output_df.append(pd.Series([row['Awards'],wins,nominations,Primetime_nominations,Oscar_nominations,Golden_Globe_nominations,BAFTA_nominations,Primetime_won,Oscar_won,Golden_Globe_won,BAFTA_won],index=['Awards','Awards_won','Awards_nominated','Prime_awards_Nominated','Oscar_awards_Nominated','Gloden_Globe_Nominate','BAFTA_Awards_Nominated','Prime_awards_Won','Oscar_awards_Won','Gloden_Globe_Won','BAFTA_Awards_Won']),ignore_index=True)
output_df.to_csv('ques4.csv')
print(output_df.head())
