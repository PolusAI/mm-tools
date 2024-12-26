# extract_data_csv (0.1.0)

Extract data from a CSV file

## Options

This plugin takes 6 input arguments and 2 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_csv_path | Path to the input csv file, Type: string, File type: input, Accepted formats: csv | Input | File | File |
| query | query str to search the dataset, Type: string, File type: input, Accepted formats: txt | Input | string | string |
| min_row | The row min inex, Type: int | Input | int | int |
| max_row | The row max inex, Type: int | Input | int | int |
| column_name | The name of the column to load data, Type: string, File type: input, Accepted formats: txt | Input | string | string |
| output_txt_path | Path to the txt datoutput file, Type: string, File type: output, Accepted formats: txt | Input | string | string |
| output_txt_path | Path to the txt output file | Output | File | File |
| output_data | The output data | Output | {'type': 'array', 'items': 'string'} | {'type': 'array', 'items': 'string'} |
