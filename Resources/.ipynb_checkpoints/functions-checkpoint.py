def checker(object):
    print(f'length : {len(object)}')
    print(type(object))
    if type(object) == list:
        print(object[:5])
    elif type(object) == dict:
        print(f'Keys: {list(object.keys())[:5]}')
        print(f'Values: {list(object.values())[:5]}')
    elif str(type(object)) == "<class 'pandas.core.frame.DataFrame'>":
        print(object.dtypes)
        print(object.describe())
    else:
        return
    