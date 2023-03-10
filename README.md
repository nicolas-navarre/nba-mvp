<h1> What if the MVP was awarded based on a 3-2-1 points system after each game? </h1>

Shout out to Leigh Ellis and the No Dunks Classic Factory for throwing this idea out there.  
&nbsp;

***Introduction***  

What if at the end of each game the three best players of the game were awarded 3,2 and 1 points and at the end of the season, the player with the most points wins the MVP. Over the years this idea has been thrown around the sub a few times and here are the most common reactions:  
&emsp; • It doesn’t work, it favors stand out players from bad teams.  
&emsp; • This would unfairly hurt players with good teammates (Steph-Klay / Durant-Westbrook).  
&emsp; • Lebron would win every year.  
&emsp; • Westbrook stat padding would be overvalued.  
&emsp; • This would make the MVP less varied.  
&emsp; • Finally, we’d see Harden was robbed.  
&emsp; • Makes sense, would negate recency and narrative bias.  
&emsp; • Any system that doesn’t give 2020-21 Derrick Rose a first-place vote is better.  
&nbsp;

***Method*** 
 
Obviously, we can’t go back and re-watch every single game, but I was interested in the idea and curious to see if people’s reactions were valid or not. So, I built a script that went through the 12,025 box scores of the games played over the last 10 seasons and picked the top three best players for each game.

To pick the best player of each game I used the NBA’s home-built Player Impact Estimate (PIE) advanced stat. I picked it because it was the only built-in all in one stat available through the nba_api, not because I think it’s the best stat. This stat sums a player’s stats and divides it by the sum of the total box score and more or less represents the stats a player was involved in. 

The player with the top PIE was awarded 3 points, followed by the second and third best PIE stats being awarded 2 and 1 points. Only players who played more than 20 minutes in the game were considered. If the player with top PIE was on the losing team and the player with the second highest PIE was on the winning team, their points were flipped. This was done to reflect that fact that the top honor almost always goes to player from the winning team in these kinds of systems.  
&nbsp;

***Results*** 
 
***2011-12***  

||||||
|:-----------|:------------|:------------|------------:|------------:|
| ***Player*** | ***Points*** | ***Votes*** |  ***Actual Top 3*** | ***Points rank*** |
| LeBron James | 120 | 1st | LeBron James | 1st
| Kevin Durant | 110 | 2nd | Kevin Durant | 2nd
| Chris Paul   | 81 | 3rd | Chris Paul | 3rd
&nbsp;

***2012-13***  

||||||
|:-----------|:------------|:------------|------------:|------------:|
| ***Player*** | ***Points*** | ***Votes*** |  ***Actual Top 3*** | ***Points rank*** |
| LeBron James | 164 | 1st | LeBron James | 1st
| Kevin Durant | 153 | 2nd | Kevin Durant | 2nd
| Tim Duncan   | 98 | 7th | Carmelo Anthony | 20th
&nbsp;
  
***2013-14***  

||||||
|:-----------|:------------|:------------|------------:|------------:|
| ***Player*** | ***Points*** | ***Votes*** |  ***Actual Top 3*** | ***Points rank*** |
| Kevin Durant | 151 | 1st | Kevin Durant | 1st
| LeBron James | 143 | 2nd | LeBron James | 2nd
| Kevin Love   | 125 | 11th | Blake Griffin | 10th
&nbsp;
  
***2014-15***  

||||||
|:-----------|:------------|:------------|------------:|------------:|
| ***Player*** | ***Points*** | ***Votes*** |  ***Actual Top 3*** | ***Points rank*** |
| Steph Curry | 128 | 1st | Steph Curry | 1st
| James Harden | 124 | 2nd | James Harden | 2nd
| Chris Paul   | 118 | 6th | LeBron James | 6th
&nbsp;
  
***2015-16***  

||||||
|:-----------|:------------|:------------|------------:|------------:|
| ***Player*** | ***Points*** | ***Votes*** |  ***Actual Top 3*** | ***Points rank*** |
| Steph Curry | 149 | 1st | Steph Curry | 1st
| LeBron James | 131 | 3rd | Kawhi Leonard | 7th
| Russell Westbrook | 128 | 4th | Lebron James | 2nd
&nbsp;
  
***2016-17***  

||||||
|:-----------|:------------|:------------|------------:|------------:|
| ***Player*** | ***Points*** | ***Votes*** |  ***Actual Top 3*** | ***Points rank*** |
| Russell Westbrook | 159 | 1st | Russell Westbrook | 1st
| James Harden | 139 | 2nd | James Harden | 2nd
| LeBron James   | 130 | 4th | Kawhi Leonard | 6th
&nbsp;
  
***2017-18***  

||||||
|:-----------|:------------|:------------|------------:|------------:|
| ***Player*** | ***Points*** | ***Votes*** |  ***Actual Top 3*** | ***Points rank*** |
| LeBron James | 152 | 2nd | James Harden | 5th
| Giannis Antetokounmpo | 125 | 6th | LeBron James | 1st
| Russell Westbrook   | 120 | 5th | Anthony Davis | 4th
&nbsp;
  
***2018-19***  

||||||
|:-----------|:------------|:------------|------------:|------------:|
| ***Player*** | ***Points*** | ***Votes*** |  ***Actual Top 3*** | ***Points rank*** |
| Giannis Antetokounmpo | 146 | 1st | Giannis Antetokounmpo | 1st
| James Harden | 131 | 2nd | James Harden | 2nd
| Nikola Vucevic   | 128 | N/A | Paul George | 10th
&nbsp;
  
***2019-20***  

||||||
|:-----------|:------------|:------------|------------:|------------:|
| ***Player*** | ***Points*** | ***Votes*** |  ***Actual Top 3*** | ***Points rank*** |
| Giannis Antetokounmpo | 135 | 1st | Giannis Antetokounmpo | 1st
| James Harden | 115 | 3rd | LeBron James | 4th
| Nikola Jokic   | 111 | 9th | James Harden | 2nd
&nbsp;
  
***2020-21***  

||||||
|:-----------|:------------|:------------|------------:|------------:|
| ***Player*** | ***Points*** | ***Votes*** |  ***Actual Top 3*** | ***Points rank*** |
| Nikola Jokic | 150 | 1st | Nikola Jokic | 1st
| Giannis Antetokounmpo | 116 | 4th | Joel Embiid | 5th
| Luka Doncic   | 105 | 6th | Steph Curry | 4th
&nbsp;
  
***2021-22***  


||||||
|:-----------|:------------|:------------|------------:|------------:|
| ***Player*** | ***Points*** | ***Votes*** |  ***Actual Top 3*** | ***Points rank*** |
| Nikola Jokic | 168 | TBD | TBD | TBD
| Giannis Antetokounmpo | 134    | TBD   | TBD | TBD
| Joel Embiid   | 133 | TBD | TBD | TBD
&nbsp;

***Conclusion***
    
9 of the last 10 MVP seasons would have also won under this system. What does that mean? Well maybe PIE isn’t such an awful stat. It also seems the current voting system follows the same results a more impartial approach would yield, which makes me think that the idea that narrative or late season bias isn’t nearly as much of a factor as we think it might be to the voters. I guess we build narratives to entertain ourselves because the most fun part of the MVP award is to debate back and forth with your mates who you think should win it. But at the end of the day, we, and the voters, know who should win and that comes through in the votes. 

The only MVP who doesn’t hold their title in this format is Harden in 2017-18 where he would end up in 5th instead. LeBron takes the top spot after carrying a fairly below average Cavs teams to 50 wins by playing in all 82 games, something we probably took for granted from LeBron at the time. Harden had a massive season of course, but played 10 fewer games, and like some of the initial concerns mentioned, Chris Paul also had a great season alongside which took some points away from Harden. 

The highest point total goes to Jokic this year, already surpassing LeBron’s legendary 12-13 season and with 2 games still to play, he could become the first to reach the 170 point mark. The guy is truly having an all-time great season so it looks like he’s poised to retain his MVP. 

A couple other points:  
&emsp; • No LeBron would not win every year  
&emsp; • No having good teammates doesn’t hurt  
&emsp; • No good players on bad teams aren’t overvalued  
&emsp; • Harden wasn’t robbed  
&nbsp;  

***Bonus*** 
   
If I remove the win condition to get 3 points from the script, Harden wins the 2014-15 MVP over Curry. Everything else stays the same. 

I only showed the top 3 for each season, but I have the point totals for all players of all seasons if anyone is interested. 

Kevin Love is the only player to appear in the top 3 and not make the playoffs. That final season in Minnesota was truly something special.

Some of the flaws related to PIE stand out when looking at Kawhi. It seems his defense went underrated by the metric despite its attempts to account for defense.
