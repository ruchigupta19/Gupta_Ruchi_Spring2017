![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Airbnb%20logo/Airbnb.png)
# BOSTON AIRBNB OPEN DATA ANALYSIS

In this Project, I am going to explore the Airbnb data of Boston which includes 3 files:

* listings.csv 
* calendar.csv
* reviews.csv

**listings csv** consists of details of all the listings in Boston including their price, accomodates, ratings, number of reviews, summary, name, owner name, Description, host Id and many other columns decribing details of listings.

**calendar.csv** consists of details of listings and its availability and its price.

**reviews.csv** consits of reveiws for each listing in Boston

This includes 5 analysis on Boston Airbnb open dataset with the help of which I tried to answer questions like What are the busiest times to visit Boston? busiest neighborhoods in Boston? seasonal pattern of airbnb housing price? and many more

## ANALYSIS - 1
## What causes difference in Prices of listings?

*Data Wrangling:* I have collected, cleaned and transformed data by levaraging pandas and numpy to be used for performing meaningful analysis.

```
# replacing NaN values with 0
inputDF.fillna(0, inplace=True)

#clean the data to make it float
for p in price:
    p=float(p[1:].replace(',',''))
    prices.append(p)

#exclude the listings with 0 for price,beds,bedrooms,accomodates etc
inputDF = inputDF[inputDF.bathrooms >0]
inputDF = inputDF[inputDF.bedrooms > 0]
inputDF = inputDF[inputDF.beds > 0]
inputDF = inputDF[inputDF.price  > 0]
inputDF = inputDF[inputDF.review_scores_rating  > 0]
inputDF = inputDF[inputDF.reviews_per_month > 0]
inputDF = inputDF[inputDF.accommodates  > 0]
inputDF.head()
```
Cleaned and transformed data can be accessed [here](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Output%20csv/cleaned_Data.csv)  

then I categorized different listings based upon their room type which gave the following results:
```
roomType_DF=inputDF.groupby('room_type').id.count()
```

Room Type  | Number Of Listings
------| --------  
Entire home/apt|   1393    
Private room  |   1061       
Shared room  |   52     

![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Output%20Graphs/Analysis%20-%201/Room_Type_.PNG)

I categorized different listings based upon their property type which gave the following results:
```
propertytype_DF = inputDF.groupby('property_type').id.count()
```
![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Output%20Graphs/Analysis%20-%201/Property_Type.PNG)

#### 1st Data point:
It can be concluded that people are more inclined towards listing their entire property than that of private rooms or shared rooms.It can also be seen that property type also plays an important factor. Not surprisingly, Apartment and houses take up an overwhelming majority of all listings, although we do see few instances unfamiliar residencies here and there.



