import pandas as pd
import numpy as np
output_df=pd.DataFrame(columns=['BOROUGH','ONE_VEHICLE_INVOLVED','TWO_VEHICLES_INVLVED','THREE_VEHICLES_INVOLVED','MORE_VEHICLES_IVOLVED'])
output_df.set_index('BOROUGH')										#creating an output dataframe
df=pd.read_csv('vehicle_collisions.csv')			
df = df.rename(columns={'UNIQUE KEY': 'UNIQUE'})					#renaming column UNIQUE KEY
for br in df.BOROUGH.unique():                                      #looping for each borough
    onev=0
    twov=0
    threev=0
    morev=0                                                         #setting initial values to the variables
    for index, row in df.iterrows():
        if row['BOROUGH']==br:
            check=0                                                 
            if (type(row['VEHICLE 5 TYPE'])!=float):
                check+=1
            if (type(row['VEHICLE 4 TYPE'])!=float):
                check+=1
            if (type(row['VEHICLE 3 TYPE'])!=float):
                check+=1
            if (type(row['VEHICLE 2 TYPE'])!=float):
                check+=1
            if (type(row['VEHICLE 1 TYPE'])!=float):                 #checking the number of vehicles involved
                check+=1
            if check>=4:                                             #incresing the counter of more vehicles if no. is >=4
                morev+=1
            elif check==3:                                           #checking if 3 vehicles were involved
                threev+=1
            elif check==2: 											 #checking if 2 vehicles were involved
                twov+=1
            elif check==1:											 #checking if 1 vehicle was involved
                onev+=1
    output_df=output_df.append(pd.Series([br,onev,twov,threev,morev],index=['BOROUGH','ONE_VEHICLE_INVOLVED','TWO_VEHICLES_INVLVED','THREE_VEHICLES_INVOLVED','MORE_VEHICLES_IVOLVED']),ignore_index=True)
																	 #appending data to the output dataframe
output_df.to_csv('ques1_part2.csv')									 #writing data to the csv
print(output_df.head())