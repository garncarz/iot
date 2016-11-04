import pandas as pd

from . import crawler


def get_df():
    return pd.DataFrame.from_records(
        crawler.get_many_records(),
        columns=['datetime', 'temperature', 'humidity'],
        index='datetime',
    )
