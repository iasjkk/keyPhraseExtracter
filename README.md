# Key-Phrase Extraction from Documents

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Python3.x required packages.

```bash
pip install numpy
pip install spacy
pip install nltk
pip install scikit-learn
pip install nltk
pip install pandas
pip install logging
```
Download spacy model for English language
```bash
python3 -m spacy download en
```


## Usage

```python
from key_phrase_ranking import KeyPhraseRank

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
```

## C
