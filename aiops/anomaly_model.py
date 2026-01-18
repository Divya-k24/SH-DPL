def confidence_score(df):
    df['confidence'] = df['cpu'].apply(lambda x: 'HIGH' if x > 90 else 'NORMAL')
    return df
