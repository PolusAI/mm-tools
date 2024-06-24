# extract_pdbids_drugbank_xsdata (0.1.0)

Filter Drugbank database using xsData

## Options

This plugin takes 5 input arguments and 3 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| drugbank_xml_file_path | Path to the Drugbank xml file | Input | File | File |
| smiles | List of input SMILES, Type: string[], File type: input, Accepted formats: list[string] | Input | ['null', {'type': 'array', 'items': 'string'}] | ['null', {'type': 'array', 'items': 'string'}] |
| inchi | List of input SMILES, Type: string[], File type: input, Accepted formats: list[string] | Input | ['null', {'type': 'array', 'items': 'string'}] | ['null', {'type': 'array', 'items': 'string'}] |
| inchi_keys | List of input SMILES, Type: string[], File type: input, Accepted formats: list[string] | Input | ['null', {'type': 'array', 'items': 'string'}] | ['null', {'type': 'array', 'items': 'string'}] |
| output_txt_path | Path to the text dataset file, Type: string, File type: output, Accepted formats: txt | Input | string | string |
| output_txt_path | Path to the txt file | Output | File | File |
| output_smiles | The Smiles of small molecules | Output | {'type': 'array', 'items': 'string'} | {'type': 'array', 'items': 'string'} |
| output_pdb_ids | The PDB IDs of target structures | Output | {'type': 'array', 'items': 'string'} | {'type': 'array', 'items': 'string'} |
