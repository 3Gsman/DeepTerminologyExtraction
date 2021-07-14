Applying Deep Learning techniques to terminology extraction in specific domains
German Garcia Garcia	gggsman@gmail.com
14/07/2021

MSC in Artificial Intelligence
Final Master´s project: Applying Deep Learning Techniques to Terminology Extraction in Specific Domains
Universidad Politecnica de Madrid

The following GitHub repository contains the code, results and input data needed to replicate the 
experiments shown in the main document of the Final Master´s project.


ABSTRACT:

Automatic terminology extraction or automatic keyphrase extraction is a very useful subfield of natural 
language processing when it comes to synthesizing information from texts in concise terms. In this 
master's thesis, this problem is approached with a sequence labeling approach using supervised deep 
learning techniques in specific domains, using bidirectional LTSM (Long short-term memory) neural networks 
and contextual word embeddings. A statistical significance study has been carried out to verify that the 
results presented in this work are significant. The final result in the F1 score in the Inspec dataset 
is 0.5730 slightly better than the higher result of the state of the art and it offers less dispersed 
results. Additionally, in this work the variation of samples in the training set is analyzed, a program 
to convert the datasets to a sequence labelling format needed for the final system is provided and there 
is an available sample program to test the keyphrase extractor in texts given by the user.


INDEX:

- datasets folder: 		has the different datasets used during the experimentation.

- documents folder:		has two documents, the main document that presents this work and a lab 
				notebook where results and annotations can be found.

- format_dataset folder:	has an script able to change the format of given datasets to the format
				needed in the main program.

- keyphrase_extractor folder:	has an script able to highlight the keywords of a custom text given by 
				the user using the trained model.

- main_program folder:		has the Jupyter notebook with the main program that is able to run
				different experiments to train a keyword extraction model.

- results folder:		has the results and the modelsof the two main models studied in this work, 
				the one proposed by Sahrawat et ali., and the one proposed in this work.