
# convert a game_date to season year
def date_to_season(date):
    date = pd.to_datetime(date)
    if date.month <7:
        return date.year-1
    else:
        return date.year


# valid game_id's
set1 = [i for i in range(7400,7800)]
set2 = [i for i in range(7882,9112)]
set3 = [i for i in range(9215,9913)]
game_ids = set1+set2+set3

