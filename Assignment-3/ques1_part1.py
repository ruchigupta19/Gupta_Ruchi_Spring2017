import pandas as pd

def getMonth(i):                                                     #function to get corresponding month
    if i==1:
        month="Jan"
    if i==2:
        month="Feb"
    if i==3:
        month="Mar"
    if i==4:
        month="Apr"
    if i==5:
        month="May"
    if i==6:
        month="Jun"
    if i==7:
        month="Jul"
    if i==8:
        month="Aug"
    if i==9:
        month="Sep"
    if i==10:
        month="Oct"
    if i==11:
        month="Nov"
    if i==12:
        month="Dec"
    return month

output_df=pd.DataFrame(columns=['MONTH','MONTH_NAME', 'MANHATTAN', 'NYC', 'PERCENTAGE'])         #created an output dataframe
output_df.set_index('MONTH')                                                        #Setting month as index
df=pd.read_csv('vehicle_collisions.csv')                                            #reading the dataset
df['DATE']=df['DATE'].str.replace(r'-','/')                                         #Making dates consistant
df['MONTH'],df['DAY'],df['YEAR']=df['DATE'].str.split('/',2).str		    #creating different day,month,year columns
df = df.rename(columns={'UNIQUE KEY': 'UNIQUE'})                                    #renaming the unique key column
yeardf=df[(df.YEAR == '2016') | (df.YEAR == '16')]                                  #creating a dataframe for the year 2016
mnhattendf=yeardf[yeardf.BOROUGH == "MANHATTAN"]                                    #creating a dataframe for borough,Manhattan
df1=yeardf.groupby('MONTH').UNIQUE.count()                                          #getting total number of collisions for a month in nyc
df2=mnhattendf.groupby('MONTH').UNIQUE.count()                                      #total collisions for a month in manhattan
result=pd.concat([df2, df1], axis=1)                                                #concatenating both the results
result.columns.values[1] = "NYC"                                                    #giving column names to the result
result.columns.values[0] = "MANHATTAN"
for index, row in result.iterrows():                                                #appending the new data to the dataframe created
    output_df=output_df.append(pd.Series([int(index),getMonth(int(index)),row[0],row[1],((row[0]*100)/row[1])],index=['MONTH', 'MONTH_NAME','MANHATTAN', 'NYC', 'PERCENTAGE']),ignore_index=True)                  #writing the data to the dataframe
final_output_df=output_df.sort_values(by='MONTH', ascending=1)                      #sorting the data
final_output_df=final_output_df.drop(final_output_df.columns[0],axis=1)             #dropping the undesired columns
final_output_df.to_csv('ques1_part1.csv')                                             #writing to csv
print(final_output_df.head())