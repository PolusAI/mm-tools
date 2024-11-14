# config_tag_pdb (0.1.0)

Returns a dictionary of the given arguments as a JSON-encoded string.

## Options

This plugin takes     2     input arguments and 1 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| pdb_id | RSCB PDB code | Input | string | string |
| filter | Array of groups to be kept. If value is None or False no filter will be applied. All the possible values are defined in the https://www.wwpdb.org/documentation/file-format | Input | string | string |
| output_config_string | A dictionary of the given arguments as a JSON-encoded string. | Output | string | string |
