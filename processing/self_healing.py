def heal_missing_values(df):
    df['cpu'] = df['cpu'].fillna(df['cpu'].mean())
    return df
