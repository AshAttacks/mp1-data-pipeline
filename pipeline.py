"""
Data Processing Pipeline - CLI Template

DS 3500 - MP1
"""

from src import (
    create_cleaning_report,
    load_data,
    process_data,
    save_data,
    setup_logging,
    validate_dataframe,
    validate_input,
)

import argparse
import logging
import sys

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

    # Reading in validation config

    required_columns = config['validation']['required_columns']
    numeric_columns = config['validation']['numeric_columns']

    # Original DF
    df_original = data.copy()

    try:
        df_validated = validate_dataframe(data, required_columns, numeric_columns)
    except ValueError:
        sys.exit(1)

    # log validated rows before & after
    logger.info(f'Validated dataframe rows: {len(df_validated)} | Rows before: {len(df_original)}')

    try:
        df_processed = process_data(df_validated, config)
        logger.info(f'Processing complete: {len(df_validated)} → {len(df_processed)} rows')
    except ValueError:
        sys.exit(1)

    # need to log processing results

    save_data(df_processed, args.output) # output csv to output arg
    logger.info(f'Saved cleaned data to {args.output}')

    report = create_cleaning_report(df_validated, df_processed)
    print(report)  # printing cleaning report

if __name__ == "__main__":
    main()