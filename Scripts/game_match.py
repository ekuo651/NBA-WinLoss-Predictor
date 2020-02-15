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
    average_scores = encoded_box_scores[(encoded_box_scores.slug==slug) & 
                                        (encoded_box_scores.game_id.isin(common_games)) & 
                                        (encoded_box_scores.date < date)].mean()
    list_of_averages = list(average_scores[1:-2])
    return list_of_averages
    
def get_player_matchup_scores(slug, list_of_opponents, date):
    '''Returns the statistics of a player vs list of opponents prior to a certain game date.'''
    list_of_stats = calculate_matchup_box_scores_time_limit(slug, 
                                                            common_games(get_game_ids, 
                                                                         opponent_in_games(list_of_opponents)), 
                                                            date)
    return list_of_stats
    