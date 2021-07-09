format_datasets.py 		v1.0 	09/07/2021
German Garcia Garcia 	gggsman@gmail.com

MSC in Artificial Intelligence
Final Master´s project: Applying Deep Learning Techniques to Terminology Extraction in Specific Domains
Universidad Politecnica de Madrid

The following script is a dataset format convertor that changes the format from the datasets found in
the https://github.com/LIAAD/KeywordExtractor-Datasets repository, a collection of 20 keyword extraction
dataset collection to the format needed in the system provided in the master's final project traning
system found in the following github repository.

https://github.com/3Gsman/DeepTerminologyExtraction


INSTALATION:

Python 3.8 or higher is requiered to run this program.

Not external libraries are needed.

The program needs 2 directories, it can be created running the program once or by the user, the directories needed are:

- 'not_formated_datasets': 	directory where the desired datasets from the https://github.com/LIAAD/KeywordExtractor-Datasets 
							repository should be placed.

- 'formated_datasets':		directory where the ouput with the datasets in the new format are storaged.


USAGE:

To use this script you need to paste the desired datasets from the https://github.com/LIAAD/KeywordExtractor-Datasets
repository in the 'not_formated_datasets' directory, execute the script using the console, wait until the script finish,
and get the new formated datasets files from the 'formated_datasets' directory.

The program has 3 editable variables found at the begining of the script to change the behaviour of it:

- show_info:		default value: False.	If True, prints statistical information in the console. Infotmation as
					the mean, std, max and min values of the words per abstract in the corpus, keywords pero abstract
					and words per keywords.

- suffle_datasets:	default value: False. 	If True, shuffles the abstracts in the train, test and dev set of abstracts.

- downsample_to:	default value: 0. 		If 10 or higher, downsample the dataset to the number of the variable.