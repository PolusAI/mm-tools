# molgan (0.1.0)
MolGAN tool for generating small molecules

## Options

This plugin takes 6 input arguments    and 1 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_data_path | Path to the input data file, Type: string, File type: input, Accepted formats: pkl, Example file: https://github.com/bioexcel/biobb_ml/raw/master/biobb_ml/test/reference/classification/ref_output_model_support_vector_machine.pkl | Input | string | string |
| input_NP_Score_path | Output ceout file (AMBER ceout), Type: string, File type: input, Accepted formats: gz, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/data/cphstats/sander.ceout.gz | Input | string | string |
| input_SA_Score_path | Output ceout file (AMBER ceout), Type: string, File type: input, Accepted formats: gz, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/data/cphstats/sander.ceout.gz | Input | string | string |
| input_model_dir |  | Input | string | string |
| num_samples | The number of training epochs, Type: int | Input | int | int |
| outdir | Output collection. | Output | collection | collection |
