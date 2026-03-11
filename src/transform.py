import pandas as pd

def transform_data(df):

    df = df.copy()

    df = df.rename(columns={
        "userId": "user_id",
        "id": "post_id"
    })

    df["title_length"] = df["title"].str.len()

    return df
