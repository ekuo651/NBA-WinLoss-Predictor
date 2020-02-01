# **Project Proposal**
Using machine learning to predict NBA matchps. 

## **Roadmap**
1. [Data Scraping](#Data-Scraping)
1. [Organizing Data](#Data-Organization)
1. [Algorithms](#Processing-Data)
1. [Visualization & Presentation](#Visualization-&-Presentations)
1. [Hosting](#AWS)


## **Data Scraping**

>**Theoretically ...**
1. Use beautifulsoup to extract past basketball statistics \
 [Webscraping NBA Stats](!https://towardsdatascience.com/web-scraping-nba-stats-4b4f8c525994)\
 [Webscraper library](!https://pypi.org/project/basketball-reference-web-scraper/)

1. Use beautifulsoup to intermitently upload new stats as new league games are played

1. Use beautifulsoup to continously extract player news data from a variety of sources

>**But if it doesn't work ...**

1. Manually upload past basketball statistics

2. Drop the updating aspect (this would be disappointing)

3. Don't use the news

---

## **Data Organization**

>**Theoretically ...**
1. Structure historic data and put it into a database

1. Update the database

1. Write schema and views to access data

1. Link database with Python (likely using AWS), but open to exploring how to access PostgreSQL remotely

1. Index news data

>**But if it doesn't work ...**[]
1. We should be able to do this

1. We should be able to do this

1. We should be able to do this

1. We can use CSV's, which is what I did in Project 1, but it would be nice to improve upon this

1. Don't use the news
---
## **Processing Data**

**Primary Goal**

Build a generalizable TensorFlow model that uses classification, regression or reinforcement learning to predict the outcome of NBA games and use Keras Tuner to optimize the hyperparameters for the neural net.

**Secondary Goal** 

Incorporate live news sentiment analysis as a data stream to feed into neural net.

---
## **Visualization & Presentation**

It would be ideal to have an auto updating dashboard for this project. I would like to explore using Tableau or coding this in PyViz if possible.

---
## **AWS**

Host the project on AWS.






## **If this all doesn't work ...**
 SimFin 
