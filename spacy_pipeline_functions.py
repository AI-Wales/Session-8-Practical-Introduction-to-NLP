"""
October 2018
David Pugh

Functions to allow custom pipelines in spaCy.
These can be called as functions or added as part of the spaCy pipeline, e.g.,

nlp_custom.add_pipe(remove_stopwords, name='rem_stpw', after = 'tagger')


nlp_custom.add_pipe(remove_parts, name='rem_parts, after = 'tagger')

SpaCy pipelines only accept functions with a doc as a parameter. To use the
remove_parts function with paramters other than the default, override them in
a custom function:

def custom_remove_parts(doc):
    return remove_parts(doc, stop=True, punct=True, num=False, digit=False, currency=False, url=True, email=False)


nlp_custom.add_pipe(custom_remove_parts, name='rm_sw_punct_urls', after = 'tagger')
nlp_custom.add_pipe(remove_whitespace_entities, name='rm_ws_ent', after = 'ner')

"""


import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.tokens import Doc

def remove_parts(doc, stop=True, punct=True, space = True, num=True, digit=True,currency=True, url=True, email=True):
    """
    Selectively removes tags from a spaCy document based on

    Parameters
    ----------
    doc :       spaCy Doc   document to filter
    stop:       bool        indicates if stopwords will be removed
    punct:      bool        indicates if stopwords will be removed (e.g., . , ! ?)
    space:      bool        indicates if spaces will be removed
    num:        bool        indicates if number like will be removed (e.g., 2, two, 10e3)
    digit:      bool        indicates if digits will be removed (e.,g 2)
    currency:   bool        indicates if currency symbols will be removed (e.g., €)
    url:        bool        indicates if urls will be removed (e.g., bbc.co.uk)
    email:      bool        indicates if emails will be removed (e.g., whoaru@myself.com)

    Returns
    -------
    filtered spaCy document
    """

    token_pos = [None]

    for t in doc:
        if stop == True:
            if t.is_stop != False: token_pos.append(t.i)
        if punct == True:
            if t.is_punct != False: token_pos.append(t.i)
        if space == True:
            if t.is_space != False: token_pos.append(t.i)
        if num == True:
            if t.like_num != False: token_pos.append(t.i)
        if digit == True:
            if t.is_digit != False: token_pos.append(t.i)
        if currency == True:
            if t.is_currency != False: token_pos.append(t.i)
        if url == True:
            if t.like_url != False: token_pos.append(t.i)
        if email == True:
            if t.like_email != False: token_pos.append(t.i)

    doc = Doc(doc.vocab, words=[t.text for i, t in enumerate(doc) if i not in token_pos])
    return doc

def remove_whitespace_entities(doc):
  """
  Removes whitespaces and newlines classed as named entities.
  Add this to pipeline after the 'ner' step

  Parameters
  ----------
  doc : spaCy document

  Returns
  -------
  spaCy doc

  """
  doc.ents = [ent for ent in doc.ents if (ent.text != ' ') and (ent.text != '\n')  ]
  return doc


def remove_stopwords(doc):
  """
  removes stopwords from a spaCy doc

  The returned document will be stripped of any named entities, parser, so perform this
  step after the tagger.
  Parameters
  ----------
  doc : spaCy document

  Returns
  -------
  spaCy doc
  """
  token_pos = [None]
  [token_pos.append(t.i) for t in doc if t.is_stop != False]
  doc = Doc(doc.vocab, words=[t.text for i, t in enumerate(doc) if i not in token_pos])
  return doc

def remove_punctuation(doc):
    """
    removes punctuation from a spaCy doc

    The returned document will be stripped of any named entities, so perform this
    step before 'ner'
    Parameters
    ----------
    doc : spaCy document

    Returns
    -------
    spaCy doc
    """
    token_pos = [None]
    [token_pos.append(t.i) for t in doc if t.is_punct != False]
    doc = Doc(doc.vocab, words=[t.text for i, t in enumerate(doc) if i not in token_pos])
    return doc
