# src/data_validator.py
import logging
import pandas as pd


logger = logging.getLogger(__name__)


def validate_dataframe(df, required_columns, numeric_columns):
    """Validate the DataFrame and return valid data.

    required_columns: a list of column names that must exist.
    numeric_columns: a list of column names whose values should be numeric.
    """
    for col in required_columns:
        if col not in df.columns:
            logger.error(f'Column {col} not in dataframe')
            raise ValueError(f"Required column {col} does not exist")

    for col in numeric_columns:
        invalid_rows = []
        for i, value in df[col].items():
            if pd.notna(value):
                try:
                    float(value)
                except ValueError:
                    # TODO: Log a warning and record this row's index.
                    logger.warning(f"Column {col} contains invalid value: {value}")
                    invalid_rows.append(i)
                    pass

        # TODO: Remove the invalid rows.
        logger.warning(f'Columns {invalid_rows} are invalid: removing them')
        df.drop(invalid_rows, axis=1, inplace=True)

        # convert to a numeric data type
        df[col] = pd.to_numeric(df[col])
    logger.debug(f'Valid columns: {len(df.columns)} | Removed Columns: {len(invalid_rows)}')

    return df