# Proposal

## Motivation and Purpose

Our role: Data Analysts at a consulting firm

Target Audience: Movie enthusiasts 

Millions of movies are published on a variety of channels; however, filtering excellent movies could be time-consuming. If we could provide a list of popular movies based on customers' preferences and illustrate approximation of box offices from different dimensions, they will save a large amount of time on searching for high-quality movies. To solve this challenge, we propose building a data visualization app that allows movie enthusiasts to explore the top 10 popular movies, box offices and other relevant information. Our app can be served as a great exploratory tool for people who like visualization and friendly-user-interface to extract various data at the same time with minimum efforts to select the filters.

## Description of the Data

This "movies" dataset is from the [Vega Datasets][1] collection. The data was compiled by Vega to create a repository for example data to be used in other packages as stated on the Vega Sources page.


This dataset contains 3,200 movies with 16 variables for each movie. By filtering out relevant features based on the purpose of our app, we decide to interactively visualize 7 variables of the movies that were created after 1980.


There are five descriptive attributes of a movie including the title of a movie (Title), the duration of a movie (Running_Time_min), which genre the movie belongs to (Major_Genre), MPAA-rating and the year when the movie was originally released (Release_Date).


The remaining two variables describe the popularity of a movie through ratings (IMDB_Ratings) and US gross revenue (US_Gross). The dataset contains ratings from two different sources, but we chose IMDB_Rating as it has fewer missing values than the Rotten Tomatoes rating. Additionally, we will use US Gross revenue as an approximation of the box office in North America.


## Research Questions and Usage Scenarios
### Research questions:

1. How does the US gross revenue different by movie genre?

2. What is the relationship between rating and duration of the movie?

3. What are the top 10 rated movies at the year(s) of interest (by genre)? 
### Scenario of usage:

Kate is a movie enthusiast in the U.S. and she is interested in a broad range of topics and fun facts about the movie industry in North America at different years since 1990. She has a habit to watch a popular movie every week to understand why the movie was so popular in a specific timeframe. She thinks that the best way to understand is to watch it and give her own verdict. Kate also likes studying how the movie industry is growing and changing by genre popularity and movie duration. She would like to use the gross revenue of movies as an indicator of box office and compare them across genres. As she observed more movies are extending their runtime, she would also like to find out if the runtime of a movie is correlated with rating. She could possibly discover a new trend that the highest-rated movie might not be in the same genre that has the highest gross revenue (highest box office).

With all these questions in mind, she find having a dashboard with plots and filter by genre and year is useful to answer them. When she logs on to the "movielover app", she can control the filter by genre(s) and year(s) of interest, the dashboard would then displays the following: 

- A list of top 10 rated movie titles with ranking, runtime, MPAA rating;
- A bar chart of U.S. gross revenue by genre;
- A scatterplot of U.S. gross revenue and movie runtime. 


[1]: https://github.com/vega/vega-datasets

