def correlate(df):
    df['incident'] = df['cpu'].apply(lambda x: 'CPU_ISSUE' if x > 90 else 'NORMAL')
    return df
