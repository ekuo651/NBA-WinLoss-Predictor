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

def define_types(df):
    df.start_time = df.start_time.astype('str')
    df.away_team = df.away_team.astype('str')
    df.home_team = df.home_team.astype('str')
    return df
    
def schedule_cleaner(df):
    df['date'] = df['start_time'].str[:10]
    df['away'] = df['away_team'].str[5:]
    df['home'] = df['home_team'].str[5:]
    return df

def schedule_organizer(df):
    cols = ['date', 'away', 'home', 'away_team_score', 'home_team_score']
    new_df = df[cols].copy()
    return new_df

def schedule_encoder(df):
    df['game_number'] = df.index
    df.game_number = df.game_number.astype('str')
    df['game_id'] = df.game_number + df.date
    return df
    
def get_encoded_schedule(df):
    new_df = schedule_encoder(schedule_organizer(schedule_cleaner(define_types(df))))
    return new_df