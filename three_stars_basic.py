# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import nba_api
import datetime
import time

from nba_api.stats.endpoints import playergamelog

from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.library.parameters import SeasonType

import nba_api.stats.library
from nba_api.stats.static import players
from nba_api.stats.static import teams

# teams = teams.get_teams()
# players = players.get_players()
# df_players = pd.DataFrame.from_dict(players)
# df_players = df_players.loc[df_players['is_active'] == True]
# df_players['points'] = 0

from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints import boxscoreadvancedv2
from nba_api.stats.endpoints import boxscoretraditionalv2

import warnings
warnings.filterwarnings('ignore')

# from nba_api.stats.static import players
# player_dict = players.get_players()

# # Use ternary operator or write function 
# # Names are case sensitive
# bron = [player for player in player_dict if player['full_name'] == 'Michael Jordan'][0]

# gamelog_bron_all = playergamelog.PlayerGameLog(player_id='893', season = SeasonAll.all)
# df_bron_games_all = gamelog_bron_all.get_data_frames()

seasons = ['22011', '22012', '22013', '22014', '22015', '22016', '22017',
           '22018', '22019', '22020', '22021']

seasons = ['22021']
seasons = ['21996', '21997', '21998', '21999', '22000', '22001', '22002',
           '22003', '22004', '22005', '22006', '22007', '22008', '22009', '22010']

problem_games = []
for season_year in seasons: 
    game_ids_21_22 = pd.DataFrame()
    all_teams = teams.get_teams()
    all_players = players.get_players()
    df_players = pd.DataFrame.from_dict(all_players)
    # df_players = df_players.loc[df_players['is_active'] == True]
    df_players['points'] = 0
    
    for team in all_teams: 
        team_name = team['full_name']
        print(team_name)
        #GSW = [x for x in teams if x['full_name'] == 'Golden State Warriors'][0]
        team_id = team['id']
        #this time we convert it to a dataframe in the same line of code
        GSW_games = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id).get_data_frames()[0]
        GSW_games = pd.DataFrame(GSW_games.loc[GSW_games['SEASON_ID'] == season_year])
        GSW_games = GSW_games[GSW_games['GAME_ID'].str.match('0')]
        
        game_ids_21_22 = pd.concat([game_ids_21_22, GSW_games])
        
        time.sleep(0.100)
        
    game_ids_solo = game_ids_21_22
    
    game_ids_solo = game_ids_solo.drop_duplicates(['GAME_ID'],keep='first')

        # Get only the players who played more than 20 mioutes
    # game_id_list = []
    df_players['points'] = 0
    problem_games = []
    for game in game_ids_solo['GAME_ID'].unique():
        print(game)
        # if game not in game_id_list:
        try: 
            trad_boxscore = boxscoretraditionalv2.BoxScoreTraditionalV2(game).get_data_frames()
            plus_minus = trad_boxscore[1]['PTS'][0] - trad_boxscore[1]['PTS'][1]
            
            trad_boxscore[1].loc[trad_boxscore[1].index == 0, 'PLUS_MINUS'] = plus_minus
            trad_boxscore[1].loc[trad_boxscore[1].index == 1, 'PLUS_MINUS'] = - plus_minus
            
            winning_team = trad_boxscore[1].loc[trad_boxscore[1]['PLUS_MINUS'] > 0, 'TEAM_ID'].unique()[0]
            
            adv_boxscore = boxscoreadvancedv2.BoxScoreAdvancedV2(game).get_available_data()
            adv_boxscore = boxscoreadvancedv2.BoxScoreAdvancedV2(game).get_data_frames()[0]
            adv_boxscore = adv_boxscore.dropna()
            adv_boxscore = adv_boxscore[adv_boxscore['MIN'].str.match(pat = '([2-9])')]
            adv_boxscore = adv_boxscore.loc[adv_boxscore['MIN'].str.len() > 4]
            adv_boxscore = adv_boxscore.sort_values(by = 'PIE', ascending = False)
            adv_boxscore = adv_boxscore.reset_index(drop = True)
            adv_boxscore['points'] = 0
            
            
            # df_players.loc[df_players['full_name'] == adv_boxscore['PLAYER_NAME'][0], 'points'] += 3
            # df_players.loc[df_players['full_name'] == adv_boxscore['PLAYER_NAME'][1], 'points'] += 2
            # df_players.loc[df_players['full_name'] == adv_boxscore['PLAYER_NAME'][2], 'points'] += 1
            
            adv_boxscore['points'][0] = 3
            adv_boxscore['points'][1] = 2
            adv_boxscore['points'][2] = 1
            
            if adv_boxscore['TEAM_ID'][0] != winning_team:
                adv_boxscore['points'][0] = 2
                
                if adv_boxscore['TEAM_ID'][1] == winning_team:
                    adv_boxscore['points'][1] = 3
            
            # if adv_boxscore['TEAM_ID'][1] == winning_team:
            #     adv_boxscore['points'][1] = 2
            # else:
            #     adv_boxscore['points'][1] = 1
                
                    
            # if adv_boxscore['TEAM_ID'][2] == winning_team:
            #     adv_boxscore['points'][2] = 1
            # else:
            #     adv_boxscore['points'][2] = 0
            for i in adv_boxscore['PLAYER_NAME'].unique():
                df_players.loc[df_players['full_name'] == i, 'points'] += adv_boxscore.loc[adv_boxscore['PLAYER_NAME'] == i, 'points'].unique()[0]
                
        except:
            problem_games.append(game)
            continue
    
    
        # trad_boxscore[1]
    
        # for i in adv_boxscore['PLAYER_NAME'].unique():
        #    df_players.loc[df_players['full_name'] == i, 'points'] += adv_boxscore.loc[adv_boxscore['PLAYER_NAME'] == i, 'points'].unique()[0]
            
        # game_id_list.append(game)
    
        time.sleep(0.100)
    
    df_players.to_excel(f"{season_year}_v4.xlsx")

