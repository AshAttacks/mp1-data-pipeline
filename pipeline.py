"""
Data Processing Pipeline - CLI Template

DS 3500 - MP1

Usage:
    python pipeline.py --input data.csv --output clean.csv
    python pipeline.py --input data.csv --output results.json --format json --verbose
"""

import argparse
import logging
import sys
from pathlib import Path


logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()

def setup_logging(verbose=False):
    """Configure logging for the pipeline."""
    if not verbose: # TODO: implement
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.DEBUG)


def parse_arguments():
    """Parse command-line arguments.""" # TODO: implement

    parser.add_argument('--input',
                        '-i',
                        required=True,
                        help='Path to the input file')

    parser.add_argument('--output',
                        '-o',
                        required=True,
                        help='Path to the output file')

    parser.add_argument('--format',
                        help='Output format: csv or json; default is csv',
                        choices=['csv', 'json'],
                        default='csv')

    parser.add_argument('--verbose',
                        '-v',
                        action='store_true',
                        help='Enable verbose logging')


def validate_input(filepath):
    """Check whether the input path exists and is a file."""
    if not Path(filepath).is_file():  # TODO: implement
        logger.error(f"Input file does not exist: {filepath}")
        return False
    else:
        logger.info(f'Input file exists: {filepath}')
        return True 


def main():
    """Main pipeline function."""
    pass  # TODO: implement


if __name__ == "__main__":
    main()