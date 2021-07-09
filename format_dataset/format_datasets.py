# File: 		format_datasets.py 		v1.0 	09/07/2021
# Author:		German Garcia Garcia	gggsman@gmail.com
# Description:	The following script is a dataset format convertor that changes the format from the datasets 
# 				found in the https://github.com/LIAAD/KeywordExtractor-Datasets repository, a collection of
#				20 keyword extraction dataset collection to the format needed in the system provided in the
#				master's final project traning system found in the following github repository.
# Github:		https://github.com/3Gsman/DeepTerminologyExtraction


show_info = False 			# Toggle it to obtain information about the datasets in the console
suffle_datasets = False		# Toggle it to suffle the datasets
downsample_to = 0			# Select the number of samples wanted in the dataset. Set it as 0 or -1 to disable the option

import os
import statistics
import random
import sys
import codecs

if not os.path.exists('not_formated_datasets'):
    os.makedirs('not_formated_datasets')

datasets = os.listdir('not_formated_datasets/')

if len(datasets) < 1:
	print("ERROR: not_formated_datasets directory is empty")
	sys.exit()

try:
	datasets.remove('.DS_Store')
except:
	pass 

filenames_list = []
abstracts_list = []
keywords_list = []
datasets_list = []
datasets_error = []
for dataset in datasets:
  
  save_dataset = True

  try:
	  path_abstracts, dirs_abstracts, files_abstracts = next(os.walk("not_formated_datasets/"+dataset+"/docsutf8")) 
	  path_keys, dirs_keys, files_keys = next(os.walk("not_formated_datasets/"+dataset+"/keys")) 

	  if show_info:
		  print("")
		  print('_____________' + dataset.upper() + '_____________')
		  print("")

		  file_count_abstracts = len(files_abstracts)
		  print("Abstracts number:", file_count_abstracts)
		  file_count_keys = len(files_keys)
		  print("Keys number:", file_count_keys)
		  print("")

	  filenames = []
	  abstracts = []
	  keywords = []

	  for item in files_keys:

	    path_abs = "not_formated_datasets/"+dataset+"/docsutf8/"+item[:-4]+".txt"
	    file_abs = open(path_abs, "rt", encoding="utf8")
	    data_abs = file_abs.read()
	    data_abs = data_abs.replace('\t','')
	    data_abs = data_abs.replace('\n','. ')
	    path_key = "not_formated_datasets/"+dataset+"/keys/"+item

	    file_key = open(path_key, "rt", encoding="utf8")	    
	    data_key = file_key.read()
	    data_key = data_key.replace('\t','')
	    words_key = data_key.split()

	    lines_key = data_key.split('\n')
	    lines_key = [x for x in lines_key if x != '']

	    filenames.append(item[:-4])
	    abstracts.append(data_abs)
	    keywords.append(lines_key)

	  if show_info:  
	  	print("_____Words per abstract_____")

	  words_per_abstract = []
	  for item in abstracts:
	    words_per_abstract.append(len(item.split()))

	  if show_info:  
		  print('Media:', statistics.mean(words_per_abstract))
		  print('STD:', statistics.stdev(words_per_abstract))
		  print('Min:', min(words_per_abstract))
		  print('Max:', max(words_per_abstract))
		  print('')

		  print("_____Keywords per abstract_____")

	  keywords_per_abstract = []
	  for item in keywords:
	    keywords_per_abstract.append(len(item))

	  if show_info:  
		  print('Media:', statistics.mean(keywords_per_abstract))
		  print('STD:', statistics.stdev(keywords_per_abstract))
		  print('Min:', min(keywords_per_abstract))
		  print('Max:', max(keywords_per_abstract))
		  print('')

		  print("_____Words per keywords_____")

	  words_per_keyword = []
	  for item in keywords:
	    for keyword in item:
	      words_per_keyword.append(len(keyword.split()))

	  if show_info:  
		  print('Media:', statistics.mean(words_per_keyword))
		  print('STD:', statistics.stdev(words_per_keyword))
		  print('Min:', min(words_per_keyword))
		  print('Max:', max(words_per_keyword))
		  print("______________________________")
		  print("")
		  print("")

	  datasets_list.append(dataset)

	  print("Dataset loaded suscessfully " + dataset)

  except:
  	print("ERROR: Wrong dataset format " + dataset)
  	datasets_error.append(dataset)
  	save_dataset = False

  if downsample_to > 0:
  	filenames = filenames[:downsample_to]
  	abstracts = abstracts[:downsample_to]
  	keywords = keywords[:downsample_to]

  if save_dataset:	
	  filenames_list.append(filenames)
	  abstracts_list.append(abstracts)
	  keywords_list.append(keywords)

for it in range(len(abstracts_list)):
	lower_abstracts = []
	for item in abstracts_list[it]:
	  item = item.replace('.',' .')
	  item = item.replace(',',' ,')
	  item = item.replace('"','')
	  item = item.replace('(','')
	  item = item.replace(')','')
	  item = item.replace(':',' :')
	  item = item.replace('?','')
	  lower_abstracts.append(item.lower())

	lower_keywords = []
	for item in keywords_list[it]:
	  temp = []
	  for word in item:
	    temp.append(word.lower())
	  temp = list(set(temp))
	  lower_keywords.append(temp)


	formated_keywords = []

	for keywords_lst in lower_keywords:
	  formated_keywords_per_abstract = []
	  for item in keywords_lst:

	    words = item.split()

	    keyword_formated = ''
	    if len(words) > 1:
	      keyword_formated = words[0] + 'B-KEY'

	      for f in range(len(words)-1):
	        keyword_formated = keyword_formated + ' ' + words[f+1] + 'I-KEY'
	    
	    elif len(words) == 1:
	      keyword_formated = words[0] + 'B-KEY'
	    
	    else:
	      keyword_formated = "NO_KEYWORDS"

	    formated_keywords_per_abstract.append(keyword_formated)

	  formated_keywords.append(formated_keywords_per_abstract)

	preformated_abstracts = lower_abstracts

	for i in range(len(preformated_abstracts)):
	  for j in range(len(lower_keywords[i])):
	    preformated_abstracts[i] = preformated_abstracts[i].replace(' '+lower_keywords[i][j]+' ',' '+formated_keywords[i][j]+' ')
	    	  
	if suffle_datasets:
		random.shuffle(preformated_abstracts)

	full_data_length = len(preformated_abstracts)
	middle_index = full_data_length//2
	train_list = preformated_abstracts[:middle_index]
	half_list = preformated_abstracts[middle_index:]
	half_list_length = len(half_list)
	quarter_index = half_list_length//2
	test_list = half_list[:quarter_index]
	valid_list = half_list[quarter_index:]

	dirName = 'formated_datasets/'+datasets[it]

	try:
		os.makedirs(dirName)
		print('Directory: ',dirName," created")
	except:
		pass

	output_path = 'formated_datasets/'+datasets[it]+'/'

	with codecs.open(output_path+"train.txt", "w", "utf-8-sig") as f:

		for item in train_list:
		  abstract_list = item.split()

		  for word in abstract_list:

		    if word[-5:] == 'B-KEY':
		       f.write(word[:-5] + '\tB-KEY\n')
		    
		    elif word[-5:] == 'I-KEY':
		      f.write(word[:-5] + '\tI-KEY\n')

		    else:
		      f.write(word + '\tO\n')
		  
		  f.write('\n')


	with codecs.open(output_path+"test.txt", "w", "utf-8-sig") as f:

		for item in test_list:
		  abstract_list = item.split()

		  for word in abstract_list:

		    if word[-5:] == 'B-KEY':
		       f.write(word[:-5] + '\tB-KEY\n')
		    
		    elif word[-5:] == 'I-KEY':
		      f.write(word[:-5] + '\tI-KEY\n')

		    else:
		      f.write(word + '\tO\n')
		  
		  f.write('\n')


	with codecs.open(output_path+"dev.txt", "w", "utf-8-sig") as f:

		for item in valid_list:
		  abstract_list = item.split()

		  for word in abstract_list:

		    if word[-5:] == 'B-KEY':
		       f.write(word[:-5] + '\tB-KEY\n')
		    
		    elif word[-5:] == 'I-KEY':
		      f.write(word[:-5] + '\tI-KEY\n')

		    else:
		      f.write(word + '\tO\n')
		  
		  f.write('\n')

print("__________ Script execution completed __________")
