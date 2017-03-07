# Performed analysis on NYT times data

I fetched the data from Article search API and Archive API with the help of requests library using the following code and stored them at a proper location:

```
apikey_parameter={'api-key':os.environ['auth_key'],'page':i}
time.sleep(4)                                         
response_articlesearch=requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json',params=apikey_parameter)
```

## Analysis - 1

While analyzing Article search data I first collected all the **unique section names** from all the articles and plotted a graph for the same:

![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/midterm/Question2/output/5-famous-sections.PNG)

It can be seen that the **maximum number of articles are on world's news**.So the world's news articles can be analyzed closely to get further information and deep dived into all the subsections this section have, plotted a graph for the same:

![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/midterm/Question2/output/pie-chart.PNG)

It can be seen that under world section category, **Europe subsection has the maximum number of articles**. We can deep dive into the main headlines of Europe subcategory to know more about its articles.So I fetched all the headlines for Section world and subsection Europe.

![alt tag](https://github.com/ruchigupta19/Gupta_Ruchi_Spring2017/blob/master/midterm/Question2/output/word-freq.PNG)

Hence we can see that the most talked words in the articles for Erope includes **"say,French,Talk,turkey,ireland,syria,german"**

## Analysis - 2 (Sentiment Analysis)

I performed sentiment analysis on the headlines for Europe using NaiveBayesAnalyzer and the output is recieved for each headline as follows:

```
Finland's Eurosceptic Leader Soini Says Will Step Down From Party Helm
Sentiment(classification='pos', p_pos=0.6110553027748823, p_neg=0.38894469722511693)
*****************************************************************************************
Expert Says Islamic State Has Badly Damaged Major Palmyra Monument
Sentiment(classification='neg', p_pos=0.10317982549780323, p_neg=0.8968201745021953)
*****************************************************************************************
EU, US to Recognize Each Other's Medical Site Inspections
Sentiment(classification='pos', p_pos=0.8989002428508415, p_neg=0.10109975714915861)
*****************************************************************************************
Hungarian Leader's Ally Acquires Stake in Major Media Firm
Sentiment(classification='pos', p_pos=0.7213725267227658, p_neg=0.2786274732772348)
*****************************************************************************************
Experts Find Mass Grave at Ex-Catholic Orphanage in Ireland
Sentiment(classification='pos', p_pos=0.8241633206234236, p_neg=0.17583667937657416)
*****************************************************************************************
```

Total postive counts:
97
Total negative counts:
27

### From all the articles on Europe total positive count is 97 and total negative coint of articles is 27

## Analysis -3 

In













