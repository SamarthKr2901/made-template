# Project Plan

## Title
<!-- Give your project a short title. -->
Pandemic Playtime: Analyzing Twitch Viewership Trends During COVID-19.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. Is there a correlation between the increase in Twitch viewership and the progression of the COVID-19 pandemic?
2. Whether certain game genres (e.g., multiplayer, cooperative, or single-player) gained more popularity on Twitch during the pandemic and if this correlated with pandemic-related factors.
3. Do certain demographics (e.g., age, location) engage more with gaming content during the pandemic?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
The COVID-19 pandemic and subsequent lockdowns had a profound impact on various aspects of everyone's lives, including their entertainment choices. This project analyzes the behavioral change of people as they turn to online gaming and streaming in response to the pandemic's challenges. It also allows us the gain insight into the role of online entertainment platforms, like Twitch during a time like this.

We can do this by finding a correlation between the increase in COVID cases and hours watched/streamed on Twitch before and after the pandemic. If we do find a direct correlation between the two, it would mean that people did rely more on these methods of entertainment during the pandemic.

Furthermore, a deeper insight could be gathered into which genre of games and what type of people were the most affected.  

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Twitch-game-data
* Metadata URL: https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch?select=Twitch_game_data.csv
* Data URL: https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch?select=Twitch_game_data.csv
* Data Type: CSV

200 observations per month representing the top games or categories on Twitch for that month. 
All information was taken from sullygnome.com - a twitch analytics and statistics site.

### Datasource2: WHO-COVID-19-global-data
* Metadata URL: https://covid19.who.int/data
* Data URL: https://covid19.who.int/WHO-COVID-19-global-data.csv
* Data Type: CSV

Daily cases and deaths by date reported to WHO. 
Day-to-day reports starting from 3rd January 2020 till 25th October 2023.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Exolore the Data [#1][i1]
2. Pre-process the data [#2][i2]

[i1]: https://github.com/SamarthKr2901/made-template/issues/1#issue-1983942876
[i2]: https://github.com/SamarthKr2901/made-template/issues/1#issue-1983942876
