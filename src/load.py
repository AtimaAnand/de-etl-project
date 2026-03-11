from sqlalchemy import create_engine

def load_data(df):

    engine = create_engine("sqlite:///etl_data.db")

    df.to_sql(
        "posts",
        engine,
        if_exists="replace",
        index=False
    )
