# AIRPLANE CRASHES AND FATALITIES ANALYSIS #

This Analysis is done on the public dataset **AIRPLANE CRASHES AND FATALITIES SINCE 1908**.My data consists of 5268 observations and 13 variables and it represents the full history of airplanes crashes throughout the world:

1. Date - The date on which the flight crashed.
2. Time - The time at which flight crashed.
3. Location - Location of the crash
4. Operator - The name of the flight operator
5. Flight - Flight Number of the airplane that crashed
6. Route - The Route of the flight
7. Type - The type of flight carrier
8. Registration - Description unavailable. This variable wouldn’t be used for analysis.
9. cn.In - Description unavailable.
10. Aboard - The number of passenger on board
11. Fatalities - The number of deaths
12. Ground - Description unavailable.
13. Summary - Brief summary of the reason for the crash.

I have added few more columns to the original dataset for further Analysis.

## ANALYSIS -1 ##

## Worst year for Aviation Industry?

Analysis-1 is based on total Statistics of the dataset which explains the following facts:

* [planes crashed per year](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Analysis1Outputs/planesCrashedPerYear_DF.csv)
* [people aboard per year during crashes](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Analysis1Outputs/pplAboardPerYear_DF.csv)
* [people dead per year during crashes](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Analysis1Outputs/pplDeadPerYear_DF.csv)
* [people survived per year during crashes](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Analysis1Outputs/pplSurvivedPerYear_DF.csv)

*Note: I have taken top 50 records in each category to plot these graphs.*

![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Analysis1Graphs/conbine.jpg)

[Click here for individual graphs](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/tree/master/final/Analysis1Graphs)

It can be analyzed that the maximum number of planes were crashed in the year 1972 and the number was 104.
Next analysis shows us total number of people aboard and the maximum number of people abored in those planes which were crashed was 3643 in the year 1989.
From these people aboard the year in which maximum people died was 1972 as that year suffered from maximum fatalities i.e. 2937 and the year in which maximum number of people survived these plane crashes was 1999 and the number was 1788.

**All these factors will help us to find out which year was the worst year for aviation industry.**

To find out worst year of Aviation Industry I merged all 4 Dataframes :

```
mergeDF1=pd.merge(planesCrashedPerYear_Output_DF,pplAboardPerYear_Output_DF,on='Year')
mergeDF2=pd.merge(pplDeadPerYear_Output_DF,pplSurvivedPerYear_Output_DF,on='Year')
mergeDF3=pd.merge(mergeDF1,mergeDF2,on='Year')
mergeDF3.head()
```
Year  | Crashes  | Aboard  | Fatalities  | Survived
------| -------- | ------- | ----------  | --------
1972  |   104    | 3635    |2937         |698
1968  |   96     | 2928    |2156         |772
1989  |   95     | 3643    |2293         |1360
1967  |   91     | 2339    |1789         |550
1979  |   89     | 2457    |  2011       |446

I have started analyzing the same by adding new columns i.e **Fatalities_Percent** and **Survival_Percent** and same has been calculated as follows:

```
mergeDF3['Fatalities_Percent'] = (mergeDF3['Fatalities']*100)/mergeDF3['Aboard']
mergeDF3['Survival_Percent'] = (mergeDF3['Survived']*100)/mergeDF3['Aboard']
```
Year  | Crashes  | Aboard  | Fatalities  | Survived | Fatalities_Percent | Survival_Percent
------| -------- | ------- | ----------  | -------- | ------------------ | ----------------
1972  |   104    | 3635    |2937         |698       |80.797799	         | 19.202201
1968  |   96     | 2928    |2156         |772       |73.633880	         |26.366120
1989  |   95     | 3643    |2293         |1360      |62.942630	         |37.331869
1967  |   91     | 2339    |1789         |550       |76.485678	         |23.514322
1979  |   89     | 2457    |  2011       |446       |81.847782	         |18.152218

Next step was to give all the crashes a **Crash_Score** and I assigned score=.5 for every crash. 
I have assigned a **Fatalities_Score** and a **Survival_Score** by assigning score =.5 for every Fatalities_Percent and Survival_Percent

```
mergeDF3['Crash_Score'] = mergeDF3['Crashes']*.5
mergeDF3['Fatalities_Score'] = mergeDF3['Fatalities_Percent']/2
mergeDF3['Survival_Score'] = mergeDF3['Survival_Percent']/2
```

Year  | Crashes  | Aboard  | Fatalities_Percent | Survival_Percent | Crash_Score | Fatalities_Score|Survival_Score
------| -------- | ------- | ------------------ | ---------------- | -----------|-------|------
1972  |   104    | 3635    |80.797799	         | 19.202201        | 52.0|
1968  |   96     | 2928    |73.633880	         |26.366120         | 48.0|
1989  |   95     | 3643    |62.942630	         |37.331869         | 47.5|
1967  |   91     | 2339    |76.485678	         |23.514322         | 45.5|
1979  |   89     | 2457    |81.847782	         |18.152218         | 44.5|
