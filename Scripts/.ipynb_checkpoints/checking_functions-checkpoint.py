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




def verify_entries(df_1, df_2, original_df):
    entries = len(original_df)
    entry_1 = len(df_1)
    entry_2 = len(df_2)
    if entries == entry_1 + entry_2:
        print(f'{entries} = {entry_1} + {entry_2}')
        print( "No Data Loss")
    else:
        print("Keep Scrubbing")

    
