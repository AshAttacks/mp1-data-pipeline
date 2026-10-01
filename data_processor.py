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
        raise ValueError(f'Method {method} not supported. Must be "iqr" or "zscore".')
    

def process_data(df, config):
    """Apply the processing steps enabled in the configuration."""

    if config == True:
        df = remove_duplicates(df)
        df = handle_missing(df)
        df = remove_outliers(df)
        return df
    else:
        pass

    pass


def create_cleaning_report(df_before, df_after):
    """Return a dictionary summarizing the cleaning results."""
    rows_before = len(df_before)
    rows_after = len(df_after)
    rows_removed = rows_before - rows_after
    columns_before = df_before.shape[1]
    columns_after = df_after.shape[1]
    columns_removed = columns_before - columns_after

    return {
        'rows_before': rows_before,
        'rows_after': rows_after,
        'rows_removed': rows_removed,
        'columns_before': columns_before,
        'columns_after': columns_after,
        'columns_removed': columns_removed,
    }
