# autodock_vina_filter (0.1.0)

Filters results of the AutoDock Vina software.

## Options

This plugin takes     11     input arguments and 5 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_log_path | Path to the log file, Type: string, File type: output, Accepted formats: log, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/reference/vina/ref_output_vina.log | Input | File | File |
| input_log_paths | Path to the log files, Type: string, File type: output, Accepted formats: log, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/reference/vina/ref_output_vina.log | Input | File[] | File[] |
| docking_score_cutoff | Cutoff threshold for filtering docking scores, Type: float | Input | float | float |
| max_num_poses_per_ligand | Maximum number of poses per initial ligand, Type: int | Input | int | int |
| max_num_poses_total | Maximum number of poses total, Type: int | Input | int | int |
| input_txt_path | Experimental binding free energy data file (if any) | Input | File | File |
| rescore | Use True if autodock vina was run with --rescore | Input | boolean | boolean |
| input_ligand_pdbqt_path | Path to the input PDBQT ligands, Type: string, File type: input, Accepted formats: pdbqt, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/data/vina/vina_ligand.pdbqt | Input | {'type': 'array', 'items': {'type': 'array', 'items': 'File'}} | {'type': 'array', 'items': {'type': 'array', 'items': 'File'}} |
| output_ligand_pdbqt_path | Path to the output PDBQT ligand files, Type: string, File type: output, Accepted formats: pdbqt, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/reference/vina/ref_output_vina.pdbqt | Input | string | string |
| input_receptor_pdbqt_path | Path to the input PDBQT receptors, Type: string, File type: input, Accepted formats: pdbqt, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/data/vina/vina_ligand.pdbqt | Input | {'type': 'array', 'items': {'type': 'array', 'items': 'File'}} | {'type': 'array', 'items': {'type': 'array', 'items': 'File'}} |
| output_receptor_pdbqt_path | Path to the output PDBQT receptor files, Type: string, File type: output, Accepted formats: pdbqt, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/reference/vina/ref_output_vina.pdbqt | Input | string | string |
| output_ligand_pdbqt_path | Path to the output PDBQT file | Output | File[] | File[] |
| output_receptor_pdbqt_path | Path to the output PDBQT file | Output | File[] | File[] |
| docking_scores | Estimated Free Energies of Binding | Output | {'type': 'array', 'items': 'float'} | {'type': 'array', 'items': 'float'} |
| experimental_binding_data | Experimental binding data (if any) | Output | ['null', {'type': 'array', 'items': 'float'}] | ['null', {'type': 'array', 'items': 'float'}] |
| experimental_dGs | Experimental binding free energy dG values (if any) | Output | ['null', {'type': 'array', 'items': 'float'}] | ['null', {'type': 'array', 'items': 'float'}] |
