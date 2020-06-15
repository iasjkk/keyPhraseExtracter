import os
import pandas as pd
from key_phrase_ranking import KeyPhraseRank



def main(file):
	extractor = KeyPhraseRank()
	# load the content of the document, here document is expected to be in raw
	# format (i.e. a simple text file) and preprocessing is carried out using spacy
	extractor.load_document(file, language='en')

	# keyphrase candidate selection, in the case of TopicRank: sequences of nouns
	# and adjectives (i.e. `(Noun|Adj)*`)
	extractor.candidate_selection()

	# candidate weighting, in the case of TopicRank: using a random walk algorithm
	extractor.candidate_weighting()

	# N-best selection, keyphrases contains the 10 highest scored candidates as
	# (keyphrase, score) tuples
	keyphrases = extractor.get_n_best(n=15)
	# print(keyphrases)

	return keyphrases





if __name__ == '__main__':

	TEXT_DATA_DIR = "/home/jitendra/Test_code/keyPhraseExtracter/data/Text Contracts/"
	text_file_list = os.listdir(TEXT_DATA_DIR)

	final_output = []
	for file in text_file_list:
	    if file.endswith('.txt'):
	    	# print(os.path.join(TEXT_DATA_DIR, file))
	    	keyphrases = main(os.path.join(TEXT_DATA_DIR, file))
	    	temp_dict = {}
	    	temp_dict['File_Name'] = file
	    	temp_dict['KeyPhrases'] = [i[0].title() for i in keyphrases]
	    	temp_dict['KeyPhrases_with_Score'] = keyphrases
	    	temp_dict['Expected_Topic_Name'] = [i[0] for i in keyphrases][1].title()
	    	print(temp_dict)
	    	final_output.append(temp_dict)
	df = pd.DataFrame(final_output)
	df.to_csv('Output.csv', index=False)

# initialize keyphrase extraction model, here KeyPhraseRank
