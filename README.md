# PEVAR V.1.0 (latest: Nov. 25, 2019)

## Currently run in Windows 10 (64-bit)

## Preliminaries
User must have python3, jdk (at least v8) to run -jar files, and r

### Pre-processing
In pre-processing, data inputs are needed:
`data_information.txt`\
`pedigree_file.txt`\
`whole_snp_seq.hmp.txt`\ 

Output: Group files are __currently__ stored inside the current directory.

Note: You may opt to delete `DATAFRAME.hmp.txt` upon execution of the preprocessing method.  

### Execution of Commands

`python PREPROCESS_FILES.py` </br>

`for %f in (*) do ( java -jar pevar_v1.jar %f pedigree_file.txt ) >> results_verbose.log` </br>

`python process_output.py >> results_non_verbose.txt`


Where `results_non_verbose.txt` contains the recall and precision values of the program.

