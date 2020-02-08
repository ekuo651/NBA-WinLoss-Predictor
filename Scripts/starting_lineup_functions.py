# Import Required Libraries
import pandas as pd
import numpy as np
import sys
sys.path.append('../Scripts')

# Make 'PLAYER_DICT'
players = pd.read_csv('../Resources/active_players.csv')
players.index = players['Lineup_name']
players.drop(columns=['Lineup_name'], inplace=True)
PLAYER_DICT = players.T.to_dict('list')

# Make 'PAST_DICT'
PAST_DICT = {'ATLANTA_HAWKS': ['ATL'],
 'BOSTON_CELTICS': ['BKN'],
 'BROOKLYN_NETS': ['BOS'],
 'CHARLOTTE_BOBCATS': ['CHB'],
 'CHARLOTTE_HORNETS': ['CHA'],
 'CHICAGO_BULLS': ['CHI'],
 'CLEVELAND_CAVALIERS': ['CLE'],
 'DALLAS_MAVERICKS': ['DAL'],
 'DENVER_NUGGETS': ['DEN'],
 'DETROIT_PISTONS': ['DET'],
 'GOLDEN_STATE_WARRIORS': ['GSW'],
 'HOUSTON_ROCKETS': ['HOU'],
 'INDIANA_PACERS': ['IND'],
 'LOS_ANGELES_CLIPPERS': ['LAC'],
 'LOS_ANGELES_LAKERS': ['LAL'],
 'MEMPHIS_GRIZZLIES': ['MEM'],
 'MIAMI_HEAT': ['MIA'],
 'MILWAUKEE_BUCKS': ['MIL'],
 'MINNESOTA_TIMBERWOLVES': ['MIN'],
 'NEW_ORLEANS_HORNETS': ['NOP'],
 'NEW_ORLEANS_PELICANS': ['NOP'],
 'NEW_YORK_KNICKS': ['NYK'],
 'OKLAHOMA_CITY_THUNDER': ['OKC'],
 'ORLANDO_MAGIC': ['ORL'],
 'PHILADELPHIA_76ERS': ['PHI'],
 'PHOENIX_SUNS': ['PHX'],
 'PORTLAND_TRAIL_BLAZERS': ['POR'],
 'SACRAMENTO_KINGS': ['SAC'],
 'SAN_ANTONIO_SPURS': ['SAS'],
 'TORONTO_RAPTORS': ['TOR'],
 'UTAH_JAZZ': ['UTA'],
 'WASHINGTON_WIZARDS': ['WAS']}


# Make 'CURR_DICT'
CURR_DICT = {'ATLANTA_HAWKS': ['ATLANTA'],
'BOSTON_CELTICS': ['BOSTON'],
 'BROOKLYN_NETS': ['BROOKLYN'],
 'CHARLOTTE_HORNETS': ['CHARLOTTE'],
 'CHICAGO_BULLS': ['CHICAGO'],
 'CLEVELAND_CAVALIERS': ['CLEVELAND'],
 'DALLAS_MAVERICKS': ['DALLAS'],
 'DENVER_NUGGETS': ['DENVER'],
 'DETROIT_PISTONS': ['DETROIT'],
 'GOLDEN_STATE_WARRIORS': ['GOLDEN STATE'],
 'HOUSTON_ROCKETS': ['HOUSTON'],
 'INDIANA_PACERS': ['INDIANA'],
 'LOS_ANGELES_CLIPPERS': ['LA CLIPPERS'],
 'LOS_ANGELES_LAKERS': ['LA LAKERS'],
 'MEMPHIS_GRIZZLIES': ['MEMPHIS'],
 'MIAMI_HEAT': ['MIAMI'],
 'MILWAUKEE_BUCKS': ['MILWAUKEE'],
 'MINNESOTA_TIMBERWOLVES': ['MINNESOTA'],
 'NEW_ORLEANS_PELICANS': ['NEW ORLEANS'],
 'NEW_YORK_KNICKS': ['NEW YORK'],
 'OKLAHOMA_CITY_THUNDER': ['OKLAHOMA CITY'],
 'ORLANDO_MAGIC': ['ORLANDO'],
 'PHILADELPHIA_76ERS': ['PHILADELPHIA'],
 'PHOENIX_SUNS': ['PHOENIX'],
 'PORTLAND_TRAIL_BLAZERS': ['PORTLAND'],
 'SACRAMENTO_KINGS': ['SACRAMENTO'],
 'SAN_ANTONIO_SPURS': ['SAN ANTONIO'],
 'TORONTO_RAPTORS': ['TORONTO'],
 'UTAH_JAZZ': ['UTAH'],
 'WASHINGTON_WIZARDS': ['WASHINGTON']}




def starter_fetcher(df, team_location):
    df.TEAM = df.TEAM.str.upper()
    df.index = df.TEAM
    df = df[['PG','SG','SF','PF','C']]
    df = df.T
    players = list(df[team_location])
    return players

def teams_fetcher(df):
    teams = list(df.TEAM.str.upper())
    return teams

def lineup_name_converter(string):
    name = PLAYER_DICT[string]
    return name

def schedule_past_team_converter(string):
    name = PAST_DICT[string]
    return name

def schedule_curr_team_converter(string):
    name = CURR_DICT[string]
    return name