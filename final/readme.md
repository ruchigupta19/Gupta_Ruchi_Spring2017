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

### 1st Data point:
It can be concluded that people are more inclined towards listing their entire property than that of private rooms or shared rooms.It can also be seen that property type also plays an important factor. Not surprisingly, Apartment and houses take up an overwhelming majority of all listings, although we do see few instances unfamiliar residencies here and there.

Now analyzing the prices for different room type and property type and plotted a donut chart for the same which includes category and subcategory for all those categories and hovering on each subcategory will show mean price for each of them

```
roomProperty_DF = inputDF.groupby(['property_type','room_type']).price.mean()
```
![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Output%20Graphs/Analysis%20-%201/mean.PNG)

While plotting the same on a heat map:

![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Output%20Graphs/Analysis%20-%201/heat1.PNG)

### 2nd Data point:
This chart allows us to see all the listings' prices broken down by property type and room type. This gives us a much better understanding of the price breakdown in Boston based on property and room types. It can be analyzed that for almost all property type,prices for Entire home/apartment is the maximum.This tells us that Property type and room type plays a very important role in deciding price of a listing.

Lets see how the number of bedrooms available affects the price of a listing.

![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Output%20Graphs/Analysis%20-%201/Heat2.PNG)

### 3rd Data Point:
It can be analyzed that with the increase in the number of bedrooms price of listing increases.Although, it depends upon the neighbourhood as well.

So the analysis gives us data points that the prices of listings on Airbnb depends upon the room type, property type, number of bedrooms and neighbourhood.It can be seen that the property with type as Apartment and the listing as with type as entire house with maximum number of bedooms has highest price.Although it depends upon neighbourhood as well which is analyzed in the next analysis

Now that we've seen how property types and room types along with neighborhood can affect the listing prices, let's investigate the summary.
```
summaryDF = inputDF[['summary','price']]
summaryDF = summaryDF[pd.notnull(summaryDF['summary'])]
summaryDF = summaryDF[summaryDF['summary']!=0]
summaryDF = summaryDF.sort_values('price',ascending=[0])
top100DF = summaryDF.head(100)
top100DF.head()
```
