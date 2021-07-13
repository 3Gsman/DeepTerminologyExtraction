keyphrase_extractor.py 	v1.0 	09/07/2021
German Garcia Garcia	gggsman@gmail.com

MSC in Artificial Intelligence
Final Master´s project: Applying Deep Learning Techniques to Terminology Extraction in Specific Domains
Universidad Politecnica de Madrid

The following script is an automatic terminology or keyphrase extractor that given a text
input returns the text itself with the keywords on it highlighted and a list of them,
the model has been trained using the system provided in the following github repository.

https://github.com/3Gsman/DeepTerminologyExtraction


INSTALATION: 

Python 3.8 or higher is requiered to run this program.

This program uses the FLAIR library: https://github.com/flairNLP/flair, it can be download
using pip with the following command: pip3 install flair
The version used in this work is flair==0.8.0.post1

Using this program requires 2 files:

- input.txt: 	A plain text file where the user writes the input to be processed by the model

- model.pt: 	The model file, due storage constrains, github do not let upload large files 
				to the platform. You can access to this file in the following google drive link:
				https://drive.google.com/file/d/1Y4VQxkBZnzMVLnFwhkJowphoQdthRcl-/view?usp=sharing
				or contact with the author, German Garcia in the following email: gggsman@gmail.com
				Then, move the model file to the working directory with the rest of the files.

USAGE:

To use this program you only need to execute the python script on the console once the installation 
steps are completed. Write the desired input that you want to extract the keywords from, wait until 
the execution finish, and obtain the result in the 'output.txt' file. The structure of the output file
has 3 sections, the text input, the text input with the keywords highlighted and the list of the keywords.

