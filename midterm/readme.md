
# Question 1 : (45 Points)

Using Enron data-set, perform 3 analysis.
15 points per analysis

Instructions :

Enron Scandal Summary - Link to Investopedia article to get a brief summary about the what the scandal was.
The enron data-set is available at CMU Enron data 1.82 GB tgz file .
You do not need to upload this data in your repository. TA will have their own local copy of the data at ~/midterm/data/enron/maildir/*. So use this relative path for storing your data.
$ mkdir -p ~/midterm/data/enron/
$ cd ~/midterm/data/enron/
Download it manually (faster) and unzip it or use below command (slower)
$ curl -O https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tgz
You can do any analysis of your choice. A better analysis is one which gives useful information.



# Question 2 : (55 points)

Use NYT API to collect NYT data. Perform 3 analysis on the collected data.
Link to NYT developer docs : NYT API Documentation

Code	Points
Collect Data	10 Points
Storing Data	15 Points
Individual Analysis	10 Points
Instructions :

You would need to create an API key.
Use request or beautiful-soap library to download the data. (No other library or crawler allowed).
Store the data in your local machine.
Your analysis should use this downloaded data only (and not try to redownload this data again during analysis time).
There is a rate limit for downloading the data. I would suggest you to start collecting the data from day 1. You can try using multiple account to get more than 1 key.
You need to use atleast 2 API method eg: archive, Article Search. Do not use Movies Review, Semantic API.
