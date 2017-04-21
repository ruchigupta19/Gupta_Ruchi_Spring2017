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
## WHAT CAUSES DIFFERENCE IN PRICES OF LISTINGS?

*Data Wrangling:* I have collected, cleaned and transformed **listings.csv** data by levaraging pandas and numpy to be used for performing meaningful analysis.

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
## WHERE TO INVEST A PROPERTY IN BOSTON TO GET MAXIMUM RETURNS FROM AIRBNB?

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

### 1st Data Point: 
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
where,

1. Blue circles indicates Entire Apartment/home listings 
2. red circle indicates private room listings 
3. green indicates shared listings

It can be seen that Wealthier neighborhoods, mainly South End, north end, Fenway park and back bay have a higher proportion of listings for an entire apartment while Less central and poorer neighborhoods have a disproportionate number of listings from multi-unit listers.For example, Allston, there are only listings with private room. 

### 2nd Data Point:
this analysis gives us another data point that Wealthier neighborhoods should be chosen for property investment. 

Analyzing data on Entire Apartments/home to find the right location to invest property.
```
# grouping neighbourhood by number of listings

neighbourhood_DF=home.groupby('neighbourhood_cleansed').id.count()
```

```
# grouping neighbourhood by average price of listings

neighbourhoodPrice_DF=home.groupby('neighbourhood_cleansed').price.mean()
```
```
#Merging above two dataframes

mergeDF=pd.merge(neighbourhood_DF,neighbourhoodPrice_DF,on='neighbourhood_cleansed')
mergeDF.head()
```

neighbourhood_cleansed	|Number_Of_Listings	|Average_Price
------------------------|-------------------|-------------
South End	|165	|245.290909
Back Bay	|157	|280.006369
Jamaica Plain	|125	|211.160000
Fenway	|113	|240.398230
Beacon Hill	|101	|255.178218

visualizing the frequency of listings on the basis of neighbourhood where room type is entire apartment

![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Output%20Graphs/Analysis%20-%202/niighborhood_freq.PNG)

### 3rd Data Point:
It can be noticed that the maximum number of listings for entire apartment for Boston on Airbnb is in South End area followed by back bay and Jamaica plain.So these area become potential neighbourhood to invest a property

Exploring the relationship between price and neighbourhood

![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Output%20Graphs/Analysis%20-%202/price_n_neighborhood.PNG)

It can be analyzed that the maximum price is reached for Back Bay and soutn end.

Now lets visualize average price of these listings on the basis of neighbourhood where room type is entire apartment

![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Output%20Graphs/Analysis%20-%202/neighborhood_average_Price.PNG)

### 4th Data Point:
By analyzing the number of listings and prices per neighborhood, we can get a clearer understanding of how accurate the average price is per neighborhood. The neighorhoods with a lot of listings (such as South End & Back Bay), we can expect a more accurate average prices. However, neighborhoods with less than 100 listings might have relatively inaccurate average prices due to presence of outliers. Looking at the analysis done so far, one might conclude that certain neighborhoods are more 'expensive' than others.

For next analysis I have compiled a list of keywords for differnt neighborhoods in Boston which should be included while writing description about the listing on Airbnb.

```
#function to clean the data and compile a list of most common words
def cleanData(neighbrhood_name,descrip):
    p = re.sub('[^a-zA-Z]+',' ', descrip)
    cmn_words=['The','I','Boston','room']
    descrip_data=nltk.word_tokenize(p)
    filtered_data=[word.lower() for word in descrip_data if word not in cmn_words if word not in stopwords.words('english')] 
    wnl = nltk.WordNetLemmatizer() 
    counts=Counter([wnl.lemmatize(data) for data in filtered_data])
    commn_words=[]
    for w in counts.most_common(5):
        commn_words.append(w[0])
    return ' '.join(commn_words)
```

```
#calling function and adding returned data to dataframe
for a in summ.items():
    top5words=cleanData(a[0],a[1])
    final_DF_neighbrhood=final_DF_neighbrhood.append(pd.Series([a[0],top5words],index=['neighborhood','top 5 words in description']),ignore_index=True)
```

neighborhood	|top 5 words in description
----------------|------------------------------------
Roslindale	|roslindale minute guest house neighborhood
Jamaica Plain	|jamaica walk minute neighborhood bedroom
Mission Hill	|apartment bed bedroom walk medical
Longwood Medical Area	|longwood bathroom access kitchen medical
Bay Village	|walk bay bed arlington bedroom

Click here to have a look at [complete list](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Output%20csv/top_words_description.csv)

### 5th Data Point:
I can be observed that for neighborhood "South Boston Waterfront" major words include seaport, "Hyde Park" includes quiet, "East Boston" includes airport, downtown, station and chinatown includes theatre.All these observations shows that these words are unique to a particular neighborhood which gives us another data point that while listing the property on airbnb these words should definitely be included to attract travellers.

## Conclusion: 
After combining all the data points collected from above analysis it can be concluded that:

1. Invest a property in a wealthy neighborhood and according to this analysis that neighborhood should be 'Back Bay' and 'South End' as they have maximum number of listings and average prices in these neighborhood is fairly high.
2. After buying an Apartment, listing an entire Apartment on Airbnb will help to generate maximum revenue.
3. While listing the property on AirBnB, keywords describing the area should be added in order to gain the attention of travellers

It needs to be analyzed that how prices of listings vary with seasons which constitutes the next analysis in which I tried to find out how prices vary according to season,month,week,day

## ANALYSIS - 3
## SEASONAL PATTERN OF PRICES

*Data Wrangling:* I have collected, cleaned and transformed **calendar.csv** data by levaraging pandas and numpy to be used for performing meaningful analysis.

```
#replacing NaN values with 0
calendarDF.fillna(0, inplace=True)
calendarDF = calendarDF[calendarDF.price != 0]
```

```
#Extracting prices from the table
price = calendarDF['price']
prices=[]

for p in price:
    p = re.sub('[^0-9.]+','', p)
    prices.append(float(p))
```

Cleaning of data has been done and added new columns namely Year,Month and Day by splitting date.I analyzed the data by group it on the basis of Year and Month to see the trend of prices.

```
yearDF=calendarDF.groupby(['Year','Month']).price.mean()
```
Data can be accessed from [here](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Output%20csv/year_month_data.csv)

It can be seen that the data is available from September 2016 to September 2017 and when average prices are analyzed maximum rates for the listings were in the month of september.Visualizing the same for a better understanding.

![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Output%20Graphs/Analysis%20-%203/trend.PNG)

### 1st Data Point:
It can be clearly seen that the maximum average price for listings were in the month of september and October 2016 and the reason is because of good weather and Massachussetts' best time to observe fall colors.Fall Colors in Massachusetts attracts a lot of visitors which makes September and October peak months for Airbnb hosts. 

To analyze the data further, I have extracted name of the day from given date and checked weather it was a holiday and what is the reason for that holiday using datetime, clendar and holidays modules of python.

```
calendarDF.fillna(0, inplace=True)
us_holidays = holidays.US()
```
```
for index,row in calendarDF.iterrows():
    sdate = datetime.date(int(row['Year']),int(row['Month']),int(row['Day']))
    vall=date(int(row['Year']),int(row['Month']),int(row['Day'])) in us_holidays
    calendarDF.set_value(index,'day_Name',calendar.day_name[sdate.weekday()])
    calendarDF.set_value(index,'holiday',vall)
    calendarDF.set_value(index,'us_holidays_name',us_holidays.get(sdate))
```

Output data consisting days and holidays information can be accessed [here]()

Added 3 new columns Day_Name, Holiday and us_holiday_name which counsits of name of the day, boolean value for "is it a holiday?" and reason for the holiday respectively.

Trying to find a trend of avergae prices for a week

```
#calculating Average price for each day

dayDF=calendarDF.groupby('day_Name').price.mean()
```
day_Name	|Average_Price|	day_num
-----------|-------------|---------
Monday	|195.809561	|1
Tuesday|	195.173842|	2
Wednesday|	195.418228	|3
Thursday|	198.073112	|4
Friday|	203.121167	|5
Saturday|	203.408387|	6
Sunday	|198.219764|	7

It can be seen that the average price of listings increases on weekends and are usual on weekdays.Lets plot it to get a better understanding

![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Output%20Graphs/Analysis%20-%203/trend_week.PNG)

### 2nd Data Point
It can be seen that the prices are fairly high for the weekends than that of weekdays.Now we need to dig in into Sept 2016 and oct 2016 data to find the reason behind increase in Average prices. 

Analyzing all the holidays

```
#checking which holiday has maximum listings

holidayDF=calendarDF.groupby('us_holidays_name').listing_id.count()
```
![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Output%20Graphs/Analysis%20-%203/listing%20holidays.PNG)

It can be seen that the maximum number of listings is for thanksgiving which can be reasoned as its a very popular holiday.Lets dig in further to find which holiday has the maximum average price.

```
holidayPriceDF=calendarDF.groupby('us_holidays_name').price.mean()
```
us_holidays_name	|price
-----------------|--------------
Columbus Day	|237.838101
Veterans Day	|205.283324
Thanksgiving	|200.077407
Christmas Day	|198.380805
Independence Day|	197.900737
Christmas Day (Observed)|	196.901139
New Year's Day	|191.555994
Memorial Day	|190.034305
Labor Day|	189.907829
New Year's Day (Observed)	|183.823384

### 3rd Data Point:

It can be observed that the maximum average price of listings is for **columbus day** and that mean Columbus day is the busiest US long weekend holiday for Boston.

Lets dig in into september 2016 and october 2016 data to find the reason for increase in average prices.

```
#analyzing data of september and october

checkHolidaysDF=calendarDF[(calendarDF['Year'] == '2016') & ((calendarDF['Month'] == '09') |(calendarDF['Month'] == '10'))]
checkHolidaysDF=checkHolidaysDF.groupby(['Year','Month','holiday']).price.mean()
```
Year	|Month|	holiday|	price
-------|-------|--------|---------
2016	|09	|False|	252.677308
2016	|10	False	|233.264468
2016	|10	True	|237.838101

```
#analyzing longweekednd holiday days

columbusDF=calendarDF[(calendarDF['Year'] == '2016') & (calendarDF['Month'] == '10' ) & ((calendarDF['Day'] == '08') | (calendarDF['Day'] == '09') | (calendarDF['Day'] == '10'))]
columbusDF.groupby('Month').price.mean()
```
Output: 244.633573

```
#analyzing rest of the days

NocolumbusDF=calendarDF[(calendarDF['Year'] == '2016') & (calendarDF['Month'] == '10' ) & ((calendarDF['Day'] != '08') | (calendarDF['Day'] != '09') | (calendarDF['Day'] != '10'))]
NocolumbusDF.groupby('Month').price.mean()
```

Output:  233.416248

### 4th Data Point:

It can be analyzed that on a long weekend the average price is 244.63 while for the whole month the average price was 233.Hence, this suggests that the price of listings increses with the presence of long weekend.

analyzing data from date 5th of October to date 13th of October which includes both long weekend and normal workdays
```
octDF=calendarDF[(calendarDF['Year'] == '2016') & (calendarDF['Month'] == '10' )& ((calendarDF['Day'] == '05' )| (calendarDF['Day'] == '06' )| (calendarDF['Day'] == '07' )| (calendarDF['Day'] == '08' )| (calendarDF['Day'] == '09' )| (calendarDF['Day'] == '10' )| (calendarDF['Day'] == '10' )| (calendarDF['Day'] == '11' )| (calendarDF['Day'] == '12' )| (calendarDF['Day'] == '13' ))]
octDF=octDF.groupby('Day').price.mean()
```

![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/final/Output%20Graphs/Analysis%20-%203/days%20average%20price.PNG)

hence its can be seen that Long weekends have higher prices of listings which gives us another data point that price of a listing increases with the presence of Long weekend.

