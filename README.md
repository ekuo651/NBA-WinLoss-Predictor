# NBA Predictor 
![Python](https://camo.githubusercontent.com/de59e8e9b410aa0b9479b114040c06468ef33cfc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d76332e362b2d626c75652e737667) 

## A statistical look into NBA Starting Line Matchups

The sports betting market has been on the rise due to a recent wave of changes to legislation. On the whole, the industry is expected to grow by ____ in the next ___ years. In order to capitalize on the expected growth, we are using machine learning to predict outcomes in NBA regular season games. 

Since the strength of a team is heavily dependent upon them having star players, we decided to take a player centric approach in predicting matchups. Our training set is comprised of player advanced stats, usage stats and average box scores. The average box scores are calculated by equally weighing the scores from each individual game a home team starter and away team starter were in for a lookback period of 2 years.  

## **Table of Contents**
1. [Data Extraction](#data-extraction)
1. [Data Transformation](#data-transformation)
1. [Data Hosting](#data-on-the-cloud)
1. [Machine Learning Models](#machine-learning-models)
1. [Conclusions](#conclusions)

## **Data Extraction**

There is no shortage of collected statistics in most major league sports; the NBA is no exception. However, much of the data is either not in an easily usable format or behind a paywall. For our dataset, we needed the following:

> Current Starting Lineup (ESPN)

> Current & Historical Game Schedule (Basketball Reference)

> Historical Starting Lineups (Basketball Reference)

> Historical Player Usage Stats (NBA Stats)

> Historical Individual Player Box Scores (Basketball Reference)

We were able to aggregate it from Basketball Reference, NBA Stats and ESPN using the ```basketball-reference-web-scraper```, ```BeautifulSoup``` and ```selenium```.

**Basketball Reference**

Individual player box scores from 2013-present were available via the  ```basketball-reference``` client. This dataset includes an entry per player per game for over 7 years. In the regular season, each of 30 teams plays 82 games, which means that there are 1,230 games for each regular season. Additionally, there are roughly 70 playoff games each season, depending on how long each team lasts in a 7 game series. For each game, there are roughly 11 players per team who see minutes on the court. Therefore, the player box scores was estimated to be ***approximately 200,200 rows of data*** ([1,230 +70] games * 11 players per team * 2 teams * 7 years). This took approximately 40 minutes to scrape using the API client. Code can be found in the `Data Extraction/clean_data_scrape.ipynb` notebook.

Historical starting lineups were available on the basketball-reference.com website, but not availabe through their API client. Using `BeautifulSoup` ...
>## ***JEN, THIS IS ALL YOU***

Advanced stats were available though the API client (`Data Extraction/...`)
>## ***JEN, THIS IS ALSO ALL YOU***

Historical game schedules were obtained using the `basketball-reference` client as well. Code can be found in the `Data Extraction/season_schedules.ipynb` notebook.

A list of active players were also obtained using the `basketball-reference` client. Code can be found in `Data Extraction/active_players.ipynb`.







**NBA Stats**

Usage statistics were scraped from the NBA stats page. 

`Data Extraction/get_stats_nba_id.ipynb`
>## ***RAY, THIS IS ALL YOU***



**ESPN Depth Charts**

>## ***JEN, THIS IS ALL YOU***
---
## **Data Transformation**

**A Unique Identifier**

Since we needed to calculate box scores of head to head matchup between starters on the two teams, we needed a way to uniquely identify each game. After scraping the NBA schedule, we cleaned the data and assigned each game a unique ```game_id```.

**Connecting the Data Sets**

Since the box score data, usage data, historical starting lineup and current starting lineup data were from 3 different sources, we had to find a way to link them all together. 

**Head to Head Stats by Starting Lineup**

`schedule_lineup.py`\
`game_match.py`\
`game_matching.ipynb`

---

## **Data on the Cloud**
As part of a way to use use our models for day to day predictions, we hosted our datasets on the cloud. 
>## ***JEN, THIS IS ALL YOU***


## **Machine Learning Models**

## **Conclusions**




#### Web Pages:
- https://stats.nba.com
- http://www.espn.com/nba/depth
- https://www.basketball-reference.com

#### Web Scraping Libraries: 

- `BeautifulSoup` with `urllib`
- `Selenium`
- `Basketball Reference Web Scraper`


213D09D33BFB50023A778BB827749905D326C5E14BB51ACCBE8FA4DDC45660