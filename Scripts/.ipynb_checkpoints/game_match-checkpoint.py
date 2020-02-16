import pandas as pd
from datetime import *
import sys
sys.path.insert(1, '../Scripts') #path

from schedule_to_slugs import *

encoded_box_scores = pd.read_csv('../Resources/encoded_box_scores.csv')
encoded_box_scores['date'] = pd.to_datetime(encoded_box_scores['date'])

def get_game_ids(slug):
    '''Returns a list of game_ids for a player with a given slug.'''
    game_ids = encoded_box_scores[encoded_box_scores.slug == slug]['game_id'].to_list()
    return game_ids

def opponent_in_games(list_of_opponents):
    '''Returns a list of game_ids from a list of all opponents. The list contains duplicates depending on the number of players who played a given game.'''
    opponent_ids = encoded_box_scores[encoded_box_scores.slug.isin(list_of_opponents)]['game_id'].to_list()
    return opponent_ids

def common_games(game_ids, opponent_ids):
    '''Returns a list of games that the player and any opponent participated in. Contains duplicates for weighting.'''
    common_games = [value for value in opponent_ids if value in game_ids]
    return common_games

def common_games_set(game_ids, opponent_ids):
    '''Returns a list of games that the player and any opponent participated in. No duplicates.'''
    opp_ids = list(set(opponent_ids))
    common_games_set = [value for value in opp_ids if value in game_ids]
    return common_games_set

def calculate_matchup_box_scores(slug, common_games):
    '''Returns the average scores between player and all opponents.'''
    average_scores = encoded_box_scores[(encoded_box_scores.slug==slug) & (encoded_box_scores.game_id.isin(common_games))].mean()
    list_of_averages = list(average_scores[1:-2])
    return list_of_averages

def calculate_matchup_box_scores_time_limit(slug, common_games, date):
    '''Returns the average scores between player and all opponents.'''
    start_date = datetime.strptime(date, '%Y-%m-%d') - timedelta(weeks=104)   
    average_scores = encoded_box_scores[(encoded_box_scores.slug==slug) & 
                                        (encoded_box_scores.game_id.isin(common_games)) & 
                                        ((encoded_box_scores.date > start_date) & (encoded_box_scores.date < date))].mean()
    list_of_averages = list(average_scores[1:-2])
    return list_of_averages
    
def get_player_matchup_scores(slug, opponents_list, date):
    '''Returns the statistics of a player vs list of opponents prior to a certain game date.'''
    list_of_stats = calculate_matchup_box_scores_time_limit(slug, 
                                                            common_games(get_game_ids(slug), 
                                                                         opponent_in_games(opponents_list)), 
                                                            date)
    return list_of_stats
    
def matchup_per_game_id(game_id):
    stats = [get_player_matchup_scores(starter, away_lineup_slugs(game_id),get_date(game_id)) for starter in home_lineup_slugs(game_id)]
    return stats    