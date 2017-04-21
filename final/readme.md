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

This will give us summary and price for all the listings. I have chosen top 100 listings on the basis of price to find out what all common words are used by hosts while posting a listing on airbnb.
I have created a wordcloud for the same and to plot it I have cleaned the data by removing punctuation, unwanted characters and numbers.After that I have also removed all the stopwords.I have lemmatized it using WordNetLemmatizer from NTLK and plotted a wordcloud for the same to visualize the most common words these hosts utilized to describe their listings on AIRBNB.

![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Output%20Graphs/Analysis%20-%201/wordcloud.PNG)

### 4th Data Point:
It can be seen that unique words like home, south Boston, bedroom, floor, kitchen, restaurant, spacious, neighborhood ,located are very commonly words used when hosts are describing their homes. This is making sense because the primary purpose of airbnb is not to provide luxury hotel suites but just a convinient place to stay.Naturally hosts understand these purposes and create their summaries based on location and requirements in order to attract as many travellers as they can. So if hosts are not able to attract too many travellers then they can add these keywords to their summaries in order to attract travellers to choose their listings.

Now trying to analyze how the amenities provided by the listing is related to the price of the same.To analyze the same I have plotted two diferent wordclouds which in turn helped me to find out what extra emenities are provided by listings with higher price.
```
#Data collection
for index,row in amenitiesDFtop.iterrows():
    p = re.sub('[^a-zA-Z]+',' ', row['amenities'])
    allemenities+=p
   
#tokenizing
allemenities_data=nltk.word_tokenize(allemenities)

#lemitizing
wnl = nltk.WordNetLemmatizer() 
allemenities_data=[wnl.lemmatize(data) for data in filtered_data]
```

![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Output%20Graphs/Analysis%20-%201/amenities.PNG)

### 5th Data Point:
It can be clearly seen that listings with higher prices have extra eminities such as Air conditioning, washer/dryer, Kid friendly, Heating, hair dryer, buzzer and *Extra emenities comes with extra prices*

## Conclusion: 
It can be concluded that prices of listings depends upon following factors:

1. The type of room chosen by the traveller and mostly booking an Entire property costs maximum followed by private room and shared apartment.
2. The type of property chosen by the traveller and it can be analyzed that Townhouse and houses are the properties with maximum prices and apartments, houses take up an overwhelming majority of all listings.
3. Price of a listing also depends upon the number of bedrooms the property have and the same also depends upon the neighborhood of the property
4. the summary section is the one which helps to attract travellers and analyzed that presence of  unique words like home, south Boston, bedroom, floor, kitchen, restaurant, spacious, neighborhood ,located words tends to attract more travellers
5. with the increase in prices the eminities provided by host also increases.

## ANALYSIS - 2
## Where to Invest a Property in BOSTON to get maximum returns from Airbnb?

It has been analyzed earlier that the maximum number of listings are for Entire Home/Apartment. Lets check average prices for these listings based on room type.

```
# Average prices for each type of listing

avgPrice_DF=inputDF.groupby('room_type').price.mean()
avgPrice_DF=avgPrice_DF.reset_index()
avgPrice_DF=avgPrice_DF.rename(columns={'price':'average_Price'})
avgPrice_DF
```
Room Type  | Average Price
------| --------  
Entire home/apt|   232.322326    
Private room  |   89.505184       
Shared room  |   69.903846 

### !st Data Point: 
It clearly shows that Average Price of Entire home/Apartment is very high when compared to Private room and shared room.It can be concluded that Entire home/Apartment room type has the maximum average price which gives us a data point that after buying an Apartment, listing it as an entire Apartment on Airbnb will help to generate maximum revenue.

I have plotted Geographical Clusters to find out which area in Boston has maximum listings on Airbnb and to get a better understand of which is best neighborhood to invest a property.

```
# seggregating each type of property

home = inputDF[(inputDF.room_type == 'Entire home/apt')]
private = inputDF[(inputDF.room_type == 'Private room')]
shared = inputDF[(inputDF.room_type == 'Shared room')]

location_home = home[['latitude', 'longitude']]
location_private = private[['latitude', 'longitude']]
location_shared = shared[['latitude', 'longitude']]
```
![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Output%20Graphs/Analysis%20-%202/map.PNG)
