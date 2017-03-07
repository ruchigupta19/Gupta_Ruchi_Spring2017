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

![alt tag]




