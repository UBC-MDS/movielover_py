# Proposal

## Motivation and Purpose

Our role: Data Analysts at a consulting firm

Target Audience: Movie enthusiasts & Directors at Movie Production Companies

Movie enthusiasts:

Millions of movies are published on a variety of channels; however, filtering excellent movies could be time-consuming. If we could provide a list of popular movies based on customers' preference in genres and productions years, they will save a large amount of time on searching. To solve this challenge, we propose building a data visualization app that allows movie enthusiasts to visually present the top 10 ranking movies in a given year range or genre. Our app will visualize the selection process by providing a slider for the year range and dropdowns for genres. Eventually, detailed information (ranking, title, duration, MPAA ratings) of the top 10 movies will be rendered in a table format. 

Directors at Movie Production Companies:

The risk of investing in movies is similar to the risk of investing in financial assets. If we could help directors to understand the popularity and potential profits of a movie beforehand, the chance of a making profit-losing decision would be reduced drastically. To serve this purpose, we also propose adding two graphs to our app to provide comprehensive information regarding particular types of movies. Our app will illustrate the relationship between movie rating and duration through a scatter plot. Additionally, a bar chart will be provided to show revenue (in million USD) of movies from different genres in a given year range. 

## Description of the Data

This "movies" dataset is from the [Vega Datasets][1] collection. 
TBC

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

