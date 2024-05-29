# train_molgan_model (0.1.0)

MolGAN tool for generating small molecules

## Options

This plugin takes 8 input arguments and 2 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_data_path | Path to the input data file, Type: File, File type: input, Accepted formats: pkl, Example file: https://github.com/bioexcel/biobb_ml/raw/master/biobb_ml/test/reference/classification/ref_output_model_support_vector_machine.pkl | Input | File | File |
| input_NP_Score_path | Output ceout file (AMBER ceout), Type: File, File type: input, Accepted formats: gz, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/data/cphstats/sander.ceout.gz | Input | File | File |
| input_SA_Score_path | Output ceout file (AMBER ceout), Type: File, File type: input, Accepted formats: gz, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/data/cphstats/sander.ceout.gz | Input | File | File |
| output_log_path | Path to the log file, Type: string, File type: output, Accepted formats: log | Input | string | string |
| output_model_dir | Path to the output model directory | Input | string | string |
| validation_metrics | The metrics are used during validation and testing | Input | string | string |
| num_epochs | The number of training epochs, Type: int | Input | int | int |
| save_frequency | The frequency to save the outputs, Type: int | Input | int | int |
| output_log_path | Path to the log file | Output | File | File |
| output_model_dir | Path to the output model directory | Output | Directory | Directory |
