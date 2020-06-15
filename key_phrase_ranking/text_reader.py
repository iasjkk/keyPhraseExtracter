"""Readers for the keyphraseExtractor."""

import spacy

from key_phrase_ranking.sent_structures import Document


class Reader(object):
    def read(self, path):
        raise NotImplementedError


class RawTextReader(Reader):
    """Reader for raw text."""

    def __init__(self, language='en'):
        """Constructor for RawTextReader.

        Args:
            language (str): language of text to process.
        """

        self.language = language

    def read(self, text, **kwargs):
        """Read the input file and use spacy to pre-process.

        Args:
            text (str): raw text to pre-process.
            max_length (int): maximum number of characters in a single text for
                spacy, default to 1,000,000 characters (1mb).
            spacy_model (model): an already loaded spacy model.
        """

        spacy_model = kwargs.get('spacy_model', None)

        if spacy_model is not None:
            # spacy_model = fix_spacy_for_french(spacy_model)
            spacy_doc = spacy_model(text)
        else:
            max_length = kwargs.get('max_length', 10**6)
            nlp = spacy.load(self.language,
                             max_length=max_length,
                             disable=['ner', 'textcat', 'parser'])
            nlp.add_pipe(nlp.create_pipe('sentencizer'))
            # nlp = fix_spacy_for_french(nlp)
            spacy_doc = nlp(text)

        sentences = []
        for sentence_id, sentence in enumerate(spacy_doc.sents):
            sentences.append({
                "words": [token.text for token in sentence],
                "lemmas": [token.lemma_ for token in sentence],
                # FIX : This is a fallback if `fix_spacy_for_french` does not work
                "POS": [token.pos_ or token.tag_ for token in sentence],
                "char_offsets": [(token.idx, token.idx + len(token.text))
                                     for token in sentence]
            })

        doc = Document.from_sentences(sentences,
                                      input_file=kwargs.get('input_file', None),
                                      **kwargs)

        return doc

