import pandas as pd

schedule_lineup = pd.read_csv('../Resources/schedule_lineup.csv')
name_all_formats = pd.read_csv('../Resources/name_all_formats.csv')

## PART 1 : Get Lineups


def todays_games(date):
    '''Returns game_ids for a date representing all unique games.'''
    todays_games = list(set(schedule_lineup[schedule_lineup.date==date]['game_id'].to_list()))
    return todays_games

def home_team(game_id):
    '''Returns home team abbr.'''
    home_team = schedule_lineup[(schedule_lineup.game_id==game_id) & (schedule_lineup.Location =='HOME')].iat[0,2]
    return home_team

def away_team(game_id):
    '''Returns away team abbr.'''
    away_team = schedule_lineup[(schedule_lineup.game_id==game_id) & (schedule_lineup.Location =='AWAY')].iat[0,2]
    return away_team

def home_lineup(game_id):
    '''Returns a list of 5 starting players for the home team.'''
    home_row = schedule_lineup[(schedule_lineup.game_id==game_id) & (schedule_lineup.Location == 'HOME')]
    home_lineup = list(list(home_row.values)[0][3:8])
    return home_lineup

def away_lineup(game_id):
    '''Returns a list of 5 starting players for the away team.'''
    away_row = schedule_lineup[(schedule_lineup.game_id==game_id) & (schedule_lineup.Location == 'AWAY')]
    away_lineup = list(list(away_row.values)[0][3:8])
    return away_lineup


## PART 2 : Convert to Slugs

def slug_finder(team, lineup_name):
    slug = name_all_formats[(name_all_formats.Lineup_name==lineup_name) & 
                            (name_all_formats.Team==team)].iat[0,2]
    return slug   

def lineup_slug_converter(lineup, team):
    lineup_slug = [slug_finder(team, starter) for starter in lineup]
    return lineup_slug

def home_lineup_slugs(game_id):
    lineup = home_lineup(game_id)
    team = home_team(game_id)
    home_lineup_slugs = lineup_slug_converter(lineup, team)
    return home_lineup_slugs
    
def away_lineup_slugs(game_id):
    lineup = away_lineup(game_id)
    team = away_team(game_id)
    away_lineup_slugs = lineup_slug_converter(lineup, team)
    return away_lineup_slugs

def get_date(game_id):
    date = schedule_lineup[schedule_lineup.game_id==game_id].iat[0,1]
    return date
    