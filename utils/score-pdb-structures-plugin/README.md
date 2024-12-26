# score_pdb_structures (0.1.0)

Fetches the PDB information from RCSB and scores PDB structures.

## Options

This plugin takes     6     input arguments and 2 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_pdbids | List of input PDBIDs to score, Type: string[], File type: input, Accepted formats: list[string] | Input | ['null', {'type': 'array', 'items': 'string'}] | ['null', {'type': 'array', 'items': 'string'}] |
| min_row | The row min inex, Type: int | Input | int | int |
| max_row | The row max inex, Type: int | Input | int | int |
| output_txt_path | Path to the text dataset file, Type: string, File type: output, Accepted formats: txt | Input | string | string |
| timeout_duration | The maximum time in seconds to wait for a response from the API before timing out, Type: int | Input | int | int |
| max_retries | The maximum number of times to retry the request in case of failure, Type: int | Input | int | int |
| output_txt_path | Path to the txt file | Output | File | File |
| output_pdbids | The selected PDB IDs | Output | {'type': 'array', 'items': 'string'} | {'type': 'array', 'items': 'string'} |
