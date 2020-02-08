def define_types(df):
    df.team = df.team.astype('str')
    df.location = df.location.astype('str')
    df.opponent = df.opponent.astype('str')
    df.outcome = df.outcome.astype('str')
    return df

def box_score_cleaner(df):
    df['Team'] = df['team'].str[5:]
    df['Location'] = df['location'].str[9:]
    df['Opponent'] = df['opponent'].str[5:]
    df['Outcome'] = df['outcome'].str[8:]
    return df

def box_score_organizer(df):
    cols = ['slug', 'name', 'Team', 'Location', 'Opponent', 'Outcome',
            'seconds_played', 'made_field_goals', 'attempted_field_goals',
            'made_three_point_field_goals', 'attempted_three_point_field_goals',
            'made_free_throws', 'attempted_free_throws', 'offensive_rebounds',
            'defensive_rebounds', 'assists', 'steals', 'blocks', 'turnovers',
            'personal_fouls', 'game_score', 'date']
    new_df = df[cols].copy()
    return new_df

def get_cleaned_box_scores(df):
    new_df = box_score_organizer(box_score_cleaner(define_types(df)))
    return new_df