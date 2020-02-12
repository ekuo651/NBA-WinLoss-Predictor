def string_strip(df, column_name):
    df[column_name] = df[column_name].astype('str')
    df[column_name] = df[column_name].str.strip()
    return df.head(2)
    
    