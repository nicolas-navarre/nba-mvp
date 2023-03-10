import pandas as pd
import time

# useful link for other endpoints
# https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/endpoints
import nba_api


from nba_api.stats.static import players
from nba_api.stats.static import teams

from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints import boxscoreadvancedv2
from nba_api.stats.endpoints import boxscoretraditionalv2

import warnings
warnings.filterwarnings('ignore')


# add in any season you want. 20th century seasons are 21960, 21961,..
seasons = ['22011', '22012', '22013', '22014', '22015', '22016', '22017',
           '22018', '22019', '22020', '22021']

problem_games = []
all_teams = teams.get_teams()
all_players = players.get_players()
for season_year in seasons: 
    
    # reset game ids and points for each season.
    game_ids = pd.DataFrame()
    df_players = pd.DataFrame.from_dict(all_players)


    for team in all_teams: 
        team_name = team['full_name']
        print(team_name)
        team_id = team['id']
        # get game id of each team.
        team_games = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id).get_data_frames()[0]
        team_games = pd.DataFrame(team_games.loc[team_games['SEASON_ID'] == season_year])
        team_games = team_games[team_games['GAME_ID'].str.match('0')]
        
        game_ids = pd.concat([game_ids, team_games])
        
        # need this to not get shut out by the api
        time.sleep(0.100)
    
    # every game will be listed twice since two teams play in one game. drop the duplicates to
    # to  avoid double counting. 
    game_ids = game_ids.drop_duplicates(['GAME_ID'],keep='first')


    # initialize player points to 0 at the start of each season
    df_players['points'] = 0
    
    # just a catch all list to see if there are any data issues
    problem_games = []
    for game in game_ids['GAME_ID'].unique():
        print(game)
        try: 
            
            # get traditional box score data by game
            trad_boxscore = boxscoretraditionalv2.BoxScoreTraditionalV2(game).get_data_frames()
            
            # not needed in newer seasons but older seasons don't record plus minus
            plus_minus = trad_boxscore[1]['PTS'][0] - trad_boxscore[1]['PTS'][1]
            trad_boxscore[1].loc[trad_boxscore[1].index == 0, 'PLUS_MINUS'] = plus_minus
            trad_boxscore[1].loc[trad_boxscore[1].index == 1, 'PLUS_MINUS'] = - plus_minus
            
            # get advanced stat box score. Filter by players that played more than 20 minutes 
            adv_boxscore = boxscoreadvancedv2.BoxScoreAdvancedV2(game).get_available_data()
            adv_boxscore = boxscoreadvancedv2.BoxScoreAdvancedV2(game).get_data_frames()[0]
            adv_boxscore = adv_boxscore.dropna()
            adv_boxscore = adv_boxscore[adv_boxscore['MIN'].str.match(pat = '([2-9])')]
            adv_boxscore = adv_boxscore.loc[adv_boxscore['MIN'].str.len() > 4]
            adv_boxscore = adv_boxscore.sort_values(by = 'PIE', ascending = False)
            adv_boxscore = adv_boxscore.reset_index(drop = True)

            
            # initialize points for this game then assign points to the top three
            # data frame is sorted by PIE so first three indices are top three player
            adv_boxscore['points'] = 0
            adv_boxscore['points'][0] = 3
            adv_boxscore['points'][1] = 2
            adv_boxscore['points'][2] = 1
            
            
            # check if top player is on the winning team or not. then check if second player 
            # is on winning team or not.
            winning_team = trad_boxscore[1].loc[trad_boxscore[1]['PLUS_MINUS'] > 0, 'TEAM_ID'].unique()[0]
            if adv_boxscore['TEAM_ID'][0] != winning_team:
                adv_boxscore['points'][0] = 2
                
                if adv_boxscore['TEAM_ID'][1] == winning_team:
                    adv_boxscore['points'][1] = 3

            # add game points to season long tally.
            for i in adv_boxscore['PLAYER_NAME'].unique():
                df_players.loc[df_players['full_name'] == i, 'points'] += adv_boxscore.loc[adv_boxscore['PLAYER_NAME'] == i, 'points'].unique()[0]
                
        except:
            problem_games.append(game)
            continue
    

        # need this to not get shut out by the api
        time.sleep(0.100)
    
    df_players.to_excel(f"{season_year}_points_count.xlsx")

