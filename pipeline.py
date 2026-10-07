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
from src.data_loaders import load_data
from src.data_processor import process_data, create_cleaning_report
from src.utils import validate_input, setup_logging

logger = logging.getLogger(__name__)

def parse_arguments():
    """Parse command-line arguments.""" # TODO: implement

    parser = argparse.ArgumentParser(description='Data Processing Pipeline')  # Parser

    parser.add_argument('--input',
                        '-i',
                        required=True,
                        help='Path to the input file')

    parser.add_argument('--config', # add required .yaml
                        '-c',
                        required=True,
                        help='Path to the configuration file')

    parser.add_argument('--output',
                        '-o',
                        required=True,
                        help='Path to the output file')

    parser.add_argument('--verbose',
                        '-v',
                        action='store_true',
                        help='Enable verbose logging',
                        default=False)

    return parser.parse_args()

def main():
    """Main pipeline function."""
      # TODO: implement
    args = parse_arguments()  # Arguments to use
    setup_logging(verbose=args.verbose)
    logger.debug(f'Arguments parsed: input={args.input}, config={args.config}, output={args.output}')

    if not validate_input(args.input):
        sys.exit(1)

    if not validate_input(args.config):
        sys.exit(1)

    try:
        data = load_data(args.input)
        config = load_data(args.config)
    except ValueError:
        sys.exit(1)

    df_original = data.copy()

    try:
        df_processed = process_data(data, config)
        logger.info(f'Processing complete: {len(df_original)} → {len(df_processed)} rows')
    except ValueError:
        sys.exit(1)

    report = create_cleaning_report(df_original, df_processed)
    print(report) # printing cleaning report

    # need to log processing results

    df_processed.to_csv(args.output, index=False) # output csv to output arg
    logger.info(f'Saved cleaned data to {args.output}')

    '''
    Parse the command-line arguments.
    Set up logging using the --verbose option.
    Log the parsed arguments at the DEBUG level.
    Validate the input file.
    Exit with status code 1 if the input file is invalid.
    '''

if __name__ == "__main__":
    main()