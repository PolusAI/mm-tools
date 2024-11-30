# run_trained_molgan_model (0.1.0)

MolGAN tool for generating small molecules

## Options

This plugin takes 7 input arguments and 2 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_data_path | Path to the input data file, Type: File, File type: input, Accepted formats: pkl, Example file: https://github.com/bioexcel/biobb_ml/raw/master/biobb_ml/test/reference/classification/ref_output_model_support_vector_machine.pkl | Input | File | File |
| input_NP_Score_path | Output ceout file (AMBER ceout), Type: File, File type: input, Accepted formats: gz, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/data/cphstats/sander.ceout.gz | Input | File | File |
| input_SA_Score_path | Output ceout file (AMBER ceout), Type: File, File type: input, Accepted formats: gz, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/data/cphstats/sander.ceout.gz | Input | File | File |
| input_model_dir | Input directory of trained models | Input | Directory | Directory |
| output_log_path | Path to the log file, Type: string, File type: output, Accepted formats: log | Input | string | string |
| output_sdf_path | Path to the output file, Type: string, File type: output, Accepted formats: sdf | Input | string | string |
| num_samples | The number of training epochs, Type: int | Input | int | int |
| output_log_path | Path to the log file | Output | File | File |
| output_sdf_path | Path to the output file | Output | File | File |
