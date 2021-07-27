## PEVAR V.1.0 (last updated: Nov. 25, 2019)
Version 1.0 is solely the PEVAR (.jar) file, __without integration to TASSEL5__. PEVAR is already packed as a JAR executable ready to be run on a HapMap file. This is run in Windows 10 (64-bit).

### Preliminaries
User must have Python 3, Java JDK (at least v8) to run .jar files, and R.\
As of v1.0, PEVAR can only process one group at a time. Batch processing is to be implemented soon.

### Pre-processing
This process is done in the case where the whole HapMap file contains all the samples of each group. This process is strictly hardcoded to cater for the unique formatting of the provided data.

In pre-processing, the HapMap file containing the complete data set will be split into individual files, each bearing a specific group's samples.

These are the data needed:
* `whole_snp_seq.hmp.txt` - complete raw HapMap file (Example size: ~4000 samples, clustered in ~300 groups, with ~10-12 samples each)
* `data_information.txt` - csv file containing the information of the HapMap file (strictly hardcoded)
* `pedigree_file.txt` - csv file containing the groupings of the HapMap file (strictly hardcoded)

Output: Group files are __currently__ stored inside the current directory. Refreshing the folder will yield the group separated files. \
Important: If the python file will be run again, delete `DATAFRAME.hmp.txt` before executing the file. Failure to do this step will result to errors.

### Execution of Commands
Step 1: Preprocessing - Split the whole combined file into separate individual files.\
$ `python PREPROCESS_FILES.py` </br>

Step 2: Run PEVAR to all of the separated files. Append results to results_verbose.log.\
$ `for %f in (*) do ( java -jar pevar_v1.jar %f pedigree_file.txt ) >> results_verbose.log` </br>

Step 3: Process output file for readibility.\
$ `python process_output.py >> results_non_verbose.txt`

Where `results_non_verbose.txt` contains the recall and precision values of the program.

