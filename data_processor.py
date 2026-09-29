# data_processor.py
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def remove_duplicates(df):
    """Remove duplicate rows."""
    rows = len(df) # number of rows before removal
    df = df.drop_duplicates() # removed dups
    rows_left = len(df) # rows after removed dups
    rows_removed = rows - rows_left # number rows removed
    logger.debug(f'Removed {rows_removed} row(s) from dataframe.')
    return df, rows_removed


def handle_missing(df, axis="rows"):
    """Drop rows or columns containing missing values."""
    if axis == "rows":
        before = len(df)
        df.dropna()
        after = len(df)
        removed = before - after
        logger.debug(f'Removed {removed} row(s) from dataframe.')
        return df, removed
    elif axis == "columns":
        before = df.shape[1]
        df.dropna(axis=1)
        after = df.shape[1]
        removed = before - after
        logger.debug(f'Removed {removed} column(s) from dataframe.')
        return df, removed
    else:
        logger.error(f'Axis {axis} is not supported.')
        raise ValueError('Axis must be either "rows" or "columns"')


def remove_outliers(df, columns, method, threshold):
    """Remove outliers from the specified numeric columns."""
    if method not in ('iqr', 'zscore'):
        pass # to do
    pass


def process_data(df, config):
    """Apply the processing steps enabled in the configuration."""
    pass


def create_cleaning_report(df_before, df_after):
    """Return a dictionary summarizing the cleaning results."""
    pass