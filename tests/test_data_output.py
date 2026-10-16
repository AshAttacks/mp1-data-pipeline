#tests/test_data_output.py

import pandas as pd

from src import save_data


def test_save_data_creates_csv(sample_df, tmp_path):
    output_path = tmp_path / "clean.csv"

    # TODO: Call save_data() and store its return value.
    # TODO: Assert that the returned path is correct.
    # TODO: Read the saved CSV with pandas.
    # TODO: Assert that its row count and column names match sample_df.
    assert save_data(sample_df, output_path) == output_path

    saved = pd.read_csv(output_path)

    assert len(saved) == len(sample_df)