def what_is_this(thing):
    print(f'length : {len(thing)}')
    print(type(thing))
    if type(thing) == list:
        print(thing[:5])
    elif type(thing) == dict:
        print(f'Keys: {list(thing.keys())[:5]}')
        print(f'Values: {list(thing.values())[:5]}')
    elif str(type(thing)) == "<class 'pandas.core.frame.DataFrame'>":
        print(thing.dtypes)
        print(thing.describe())
    else:
        return
def calculate_endtime(df):
    import pandas as pd
    df.start_time = pd.to_datetime(df.start_time)
    df['end_time'] = df.start_time - pd.Timedelta(value=1, unit='day')
    return df
    
def define_types(df):
    df.start_time = df.start_time.astype('str')
    df.end_time = df.end_time.astype('str')
    df.away_team = df.away_team.astype('str')
    df.home_team = df.home_team.astype('str')
    return df
    
def schedule_cleaner(df):
    df['date1'] = df['start_time'].str[:10]
    df['date2'] = df['end_time'].str[:10]
    df['away'] = df['away_team'].str[5:]
    df['home'] = df['home_team'].str[5:]
    return df

def schedule_organizer(df):
    cols = ['date1', 'date2', 'away', 'home', 'away_team_score', 'home_team_score']
    new_df = df[cols].copy()
    return new_df

def schedule_encoder(df):
    df['game_id'] = df.index+1
    df.game_id = df.game_id.astype('str')
    return df
    
def organize_and_encode_schedule(df):
    new_df = schedule_encoder(schedule_organizer(schedule_cleaner(define_types(calculate_endtime(df)))))
    return new_df

def verify_integers(df):
    df.fillna(0, inplace=True)
    df.away_team_score = df.away_team_score.astype('int')
    df.home_team_score = df.home_team_score.astype('int')
    return df

def calculate_spread(df):
    df['spread'] = abs(df.away_team_score-df.home_team_score)
    return df

def get_spread(df):
    new_df = calculate_spread(verify_integers(df))
    return new_df

def get_encoded_schedule(df):
    new_df = get_spread(organize_and_encode_schedule(df))
    return new_df