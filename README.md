# NYC Covid-19 data-by-modzcta Parser
Python code to parse the history of COVID-19 cases rates by modzcta prior to 8/8 from NYC DOHMH.

## Notes
Data for modzcta case rate does not exist prior to 5/18.  There is case rate data at the borough level.  I'm still looking to find case counts by modzcta, which could be converted to case rate by using the population data.

Also note that this data appears to be a cumulative case rate, which doesnt make sense to me.

Anecdotally, I've heard this data is 'funky'.  For example, some modzctas have very few people, which causes the case rate to appear significantly higher.
