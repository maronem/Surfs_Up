# Module 9 SurfsUp Challenge

### Overview and Purpose

The purpose of this analysis was to use Python and SQLAlchemy to query hawaii.sqlite database data and compile temperature and summary statistic data 
for the month of June and December. The code for this analysis was written in Jupyter Notebook and utilized Pandas to generate dataframes from the 
queried data.

### Results

* The mean temperature in June is only 4 degrees warmer than in December with the average temperatures being 74.9 and 71.0 respectively.
* While the max temps are similar in both June (85) and December (83), their minimum temperatures vary greater with a min temp of
64 deg. in June and 56 deg. in December.
* Both months have a relatively stable temperature variation with standard deviations of 3.26 and 3.74 in June and December, respectively. 

### Summary

While there is a wider temperature range in December compared to June, both have fairly stable and temperate conditions suitible for comfort while surfing 
but also staying warm enough to enjoy ice cream and have a successful business. While it can get relatively just as hot between both months, it may be show 
more success running both surf and ice cream businesses in June as the temperature is slightly more stable and has a higher minimum temperature that will 
be both more comfortable for customers looking to get out into the water to surf as well as push more people to want ice cream to cool down. Overall, these
data suggest that both surf and ice cream shop businesses are suitable year round but may see a spike in success during the summer months. 

An additional query that can be ran would be to query the precipitation during these months to see if there is a rainy season during these months as this may
drive down surfing and ice cream businesses as less people will be outside. For example, to query this for June you could run:
```
session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date)==6).all()
```

Another additional query could be to look at the temperature results seasonally in each year to see if these shops would fare best being open during certain season. This will also give a more comprehensive look at the data instead of looking at just two specific months. For example, to query spring 2022 you could run:
```
spring = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2022-03-01', Measurement.date <= '2022-05-31')
```
