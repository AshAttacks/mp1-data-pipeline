# data_loaders.py
from pathlib import Path

import logging
import pandas as pd
import json
import yaml


# Do not call logging.basicConfig() here.
# Use the logging configuration from Part 1.
logger = logging.getLogger(__name__)


def load_csv(filepath):
    """Load a CSV file into a DataFrame."""
    df = pd.read_csv(filepath)
    logger.info(f'Loaded CSV file: {filepath} ({len(df)} rows)')
    return df


def load_json(filepath):
    """Load a JSON file into a Python object (dict or list)."""
    load_json = json.load(open(filepath))
    logger.info(f'Loaded JSON file: {filepath}')
    return load_json


def load_yaml(filepath):
    """Load a YAML file into a Python object."""
    load_yaml = yaml.safe_load(filepath)
    logger.info(f'Loaded YAML file: {filepath}')

    return load_yaml

def load_data(filepath):
    """Load a file based on its extension."""
    path = Path(filepath)
    suffix = Path(path).suffix
    if suffix == ".csv":
        return load_csv(path)
    elif suffix == ".json":
        return load_json(path)
    elif suffix == ".yaml":
        return load_yaml(path)
    else:
        logger.error(f'Unsupported file format: {Path(filepath).suffix}')
        raise ValueError(f'Unsupported file format: {suffix}')