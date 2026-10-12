## Cleaning Command Line Description:

The `pipeline.py` file is the end-to-end general organizer and processor that imports modules, defines parser arguments and 
establishes the order of runs based on the command prompt commands. This program allows the user to input data and process 
based on their own configuration rules all in one. Outputted data files have a wide range of processing 
from removing duplicates, outliers, and more. Data is loaded, validated, cleaned according to the rules in 
`config/config.yaml`, and saved to `output/`. The modules live in `src/`, and `pipeline.py` coordinates them.

Limited action is required from the user as the pipeline utilizes modules that will identify file types, 
and import according to those types.

Below are high level steps on the actions taken by this pipeline. 

## Data Movement:

1. Establishes parser arguments into a variable 
2. Validates and loads inputs and configs provided by the user 
3. Validates & processes the data being imported 
4. Saves processed data & exports as a CSV
5. Prints cleaning report

## Data Organization:


```text
mp1-data-pipeline/
├── requirements.txt
├── config/
│   └── config.yaml
├── output/
├── src/
│   ├── __init__.py
│   ├── data_loaders.py
│   ├── data_output.py
│   ├── data_processor.py
│   ├── data_validator.py
│   └── utils.py
├── fixtures/
│   ├── sample.csv
│   ├── sample.json
│   ├── sample.yaml
│   └── sample_data.csv
├── .gitignore
├── pipeline.py
└── README.md
```

## Module Responsibilities:

- `__init__.py`
  - Re-exports modules for conciseness in pipeline.py
- `data_loaders.py`
  - Loads data from multiple datatypes
- `data_output.py`
  - Saves and outputs csv after processing
- `data_processor.py`
  - Removes duplicates, handles missing values and removes outliers
- `data_validator.py`
  - Validates data by confirming required columns are present and 
  columns being processed are numeric. If rows include non-numeric values
  they are removed.
- `utils.py`
  - Configures logging formats and validates inputs filepaths

## Example Command:

```bash 
python pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose
```
## Example output:

```text
17:13:30 DEBUG    __main__ — Arguments parsed: input=fixtures/sample_data.csv, config=config/config.yaml, output=output/clean.csv
17:13:30 INFO     src.utils — Input file validated: fixtures/sample_data.csv
17:13:30 INFO     src.utils — Input file validated: config/config.yaml
17:13:30 INFO     src.data_loaders — Loaded CSV file: fixtures/sample_data.csv (100 rows)
17:13:30 INFO     src.data_loaders — Loaded YAML file: config/config.yaml
17:13:30 WARNING  src.data_validator — Row 94 contains invalid value: not_available
17:13:30 WARNING  src.data_validator — Row 95 contains invalid value: error
17:13:30 WARNING  src.data_validator — Rows [94, 95] are invalid: removing them
17:13:30 DEBUG    src.data_validator — Valid rows: 98 | Removed Rows: 2
17:13:30 INFO     __main__ — Validated dataframe rows: 98 | Rows before: 100
17:13:30 DEBUG    src.data_processor — Remove Duplicates: Removed 2 row(s) from dataframe.
17:13:30 DEBUG    src.data_processor — Remove Missing: Removed 2 row(s) from dataframe.
17:13:30 DEBUG    src.data_processor — Method iqr initiated with threshold 1.5. | Upper 106.625 | Lower 43.625 | 2 row(s) removed.
17:13:30 INFO     __main__ — Processing complete: 98 → 92 rows
17:13:30 DEBUG    src.data_output — Saved DF as CSV with 92 rows at output/clean.csv
17:13:30 INFO     __main__ — Saved cleaned data to output/clean.csv
{'rows_before': 98, 'rows_after': 92, 'rows_removed': 6, 'columns_before': 5, 'columns_after': 5, 'columns_removed': 0}
```