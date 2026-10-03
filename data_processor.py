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

    if method == 'iqr':
        q1 = df[columns].quantile(.25)
        q3 = df[columns].quantile(.75)
        iqr = q3 - q1
        lower_bound = q1 - threshold * iqr
        upper_bound = q3 + threshold * iqr

        return df[(df[columns] >= lower_bound) & (df[columns] <= upper_bound)]

    elif method == 'zscore':
        z_score = abs(df[columns] - df[columns].mean()) / df[columns].std()
        return df[z_score <= threshold].all(axis=1)

    else:
        raise ValueError(f'Method {method} not supported. Must be "iqr" or "zscore".')


def process_data(df, config):
    """Apply the processing steps enabled in the configuration."""

    if config['processing']:
        df = remove_duplicates(df)
        df = handle_missing(df)
        df = remove_outliers(df, config['columns'], config['method'], config['threshold'])
        return df

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
