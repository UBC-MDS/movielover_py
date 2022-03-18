# Milestone 4 Reflection


### Accomplishments of dashboard deliverables

- The dashboard displays 3 intuitive illustrations, including a scatter plot, bar chart and line chart. The filtering options are straightforward to control with range slider and checklist that are common in digital forms. Therefore, massive statistical, coding knowledge or extensive industry background are not necessarily required for using the app.
- The 3 graphs are tightly linked to each other as the app supports various interactivity. It provides flexibility to present different characteristics of each selected genre.
- The usage instructions in the tip box are simple and intuitive.
- The app was deployed on Heroku. So, other users are welcome to use the app for their purpose by accessing the webserver.
- Each plot demonstrates different information of movies with minimal overlaps.


### Current Implementations

Filters:

- Slider: year range
- Checklist: movie genres

Outputs:

- Bar chart: US revenue (box offices) for different movie genres
- Scatter plot: Relationship between IMDB ratings and duration
- Line chart: Trend of US revenue (box office)


### Differences between DashPy and DashR

- DashPy allow further interactions between plots (eg. selecting a genre on bar plot would dim the other genre’s information on plots). Such interactivity could be further developed in DashR when there is more time. 
- Exporting individual plots is available in DashR but not DashPy because of the grouping of plots in one code function.  


### Limitations and Future Improvements

- Minor finetuning to the background color and overall web aesthetic design could be done (eg. aligning color themes for DashPy and DashR). 
- We agree with one of the comments from peer review that the app does not provide a list of movies based on users' genre preference. We could add multiple tabs feature to the app for more plots or tables to avoid crowding. (eg. A new tab `Top 10 movie titles` to allow user to pick a genre from dropdown filter and show a table of top 10 movie titles).
- There is a simple tips box on interactivity but for those who are not familiar with online tools, we could provide a link to a step-by-step user guide.
- DashPy can be finetuned to allow exporting individual plots instead of all three together for more flexibility.
- For future development, we may consider adding a couple of advanced graphics as optional plots, which provide more information to different users.
- To add more flexibility in filtering to the current 2 filters, we may include more filtering options, such as MPAA Ratings or Distributors.
- Our team only used several features in the data set. Perhaps, we can incorporate more features to generate more meaningful insights for movie enthusiasts.
- To extend our user pool from North America to the international market, we could include the feature Worldwide Revenue apart from US Revenue.

