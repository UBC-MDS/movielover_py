
# Proposal

## Motivation and Purpose

Our role: Data Analysts at a consulting firm

Target Audience: Movie enthusiasts

Millions of movies are published on a variety of channels; however, filtering excellent movies could be time-consuming. If we could provide a list of popular movies based on customers' preferences and illustrate approximation of box offices from different dimensions, they will save a large amount of time on searching for high-quality movies. To solve this challenge, we propose building a data visualization app that allows movie enthusiasts to explore and compare trends in box offices and movie duration over time. Our app can be served as a great exploratory tool for people who like visualization and friendly-user-interface to extract various data at the same time with minimum efforts to select the filters.

## Description of the Data

This "movies" dataset is from the [Vega Datasets][1] collection. The data was compiled by Vega to create a repository for example data to be used in other packages as stated on the Vega Sources page.

This dataset contains 3,200 movies with 16 variables for each movie. By filtering out relevant features based on the purpose of our app, we decide to interactively visualize 7 variables of the movies that were created after 1980. A detailed exploratory analysis of the data wrangling can be found [here](https://github.com/UBC-MDS/movielover_py/blob/improvements/src/movies_analysis_py.ipynb).

After we wrangled the data, it has six features including:

* `Title`: The title of a movie (Title)
* `Running Time min`: the duration of a movie in minutes
* `Major Genre`: which genre the movie belongs to
* `Year`: when the movie was originally released
* `US_Revenue`: which is considered as the box office
* `IMDB Rating`: Rating of each movie
* `MPAA Rating`: It contains 6 categorie (R, PG_13, G, NC-17, PG, and Not Rated)

The dataset contains ratings from two different sources, but we chose IMDB_Rating as it has fewer missing values than the Rotten Tomatoes rating (it has only 2321 observation VS. IMDB_Rating has 2988 examples.). Additionally, the dataset contains US Gross revenue (as an approximation of the box office) in North America, hence users who are interested in box office information might find our dashboard useful. can explore. Given that our data is in resonable size, the dashboard can be quickly loaded and maintain a good user experience.

## Research Questions and Usage Scenarios

### Research questions

1. How does the US gross revenue different by movie genre?

2. What is the relationship between rating and duration of the movie?

3. How does the US box office (US gross revenue) by genre(s) change over the year(s)?

### Scenario of usage

Kate is a movie enthusiast in the U.S. and she is interested in a broad range of topics and fun facts about the movie industry in North America at different years from 1990 to 2016. Kate likes studying how the movie industry is growing and changing by genre popularity and movie duration. With more online movie streaming platforms available to the general public, would the growth of movie box office be dampened? She would like to use the gross revenue of movies as an indicator of box office and compare them across genres and growth in box office over time. As she observed more movies are extending their runtime, she would also like to find out if the runtime of a movie is correlated with rating. She could possibly discover a new trend that the highest-rated movie might not be in the same genre that has the highest gross revenue (highest box office).

With all these questions in mind, she find having a dashboard with plots and filter by genre and year useful to answer them. When she logs on to the "movielover app", she can control the filter by genre(s) and year(s) of interest, the dashboard would then display the following:

* A line chart of U.S. gross revenue by genre against year;
* A bar chart of U.S. gross revenue by genre;
* A scatterplot of rating and movie runtime.

[1]: https://github.com/vega/vega-datasets
