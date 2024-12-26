# autodock_vina_rescore (0.1.0)

Wrapper of the AutoDock Vina software.

## Options

This plugin takes     6     input arguments and 3 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_ligand_pdbqt_path | Path to the input PDBQT ligand, Type: string, File type: input, Accepted formats: pdbqt, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/data/vina/vina_ligand.pdbqt | Input | File | File |
| input_receptor_pdbqt_path | Path to the input PDBQT receptor, Type: string, File type: input, Accepted formats: pdbqt, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/data/vina/vina_receptor.pdbqt | Input | File | File |
| local_only | Do local search only | Input | boolean | boolean |
| score_only | Do not do any conformational search; simply rescore. | Input | boolean | boolean |
| output_ligand_pdbqt_path | Path to the output PDBQT ligand, Type: string, File type: output, Accepted formats: pdbqt, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/reference/vina/ref_output_vina.pdbqt | Input | string | string |
| output_log_path | Path to the log file, Type: string, File type: output, Accepted formats: log, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/reference/vina/ref_output_vina.log | Input | string | string |
| output_ligand_pdbqt_path | Path to the output PDBQT files | Output | {'type': 'array', 'items': 'File'} | {'type': 'array', 'items': 'File'} |
| output_log_path | Path to the log file | Output | File | File |
| docking_score | Estimated Free Energy of Binding | Output | float | float |
