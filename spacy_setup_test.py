"""
Author : David Pugh
Date : 16th October 2018

Test code to test if libraries are installed to allow basic NLP using spaCy are
installed and working.

- load re
- load spaCy
- load english models
- load example Text
- apply pipeline to text
- examine output
- import Textacy
- perform topic analysis
- import sentiment data
- perform sentiment analysis

Will also test to see if regex, textaCy, matplotlib are
installed for Text and Topic Analysis.


How to install matplotlib
-------------------------
https://matplotlib.org/users/installing.html
python -m pip install -U matplotlib


How to install spaCy?
---------------------
https://spacy.io
https://spacy.io/usage/

Using pip
        python -m venv .env
        source .env/bin/activate
        pip install spacy

Using Conda
        conda install -c conda-forge spacy

How to install spaCy models
---------------------------
English language models
    python -m spacy download en
    python -m spacy download en_core_web_sm
    python -m spacy download en_core_web_md
    python -m spacy download en_core_web_lg
    python -m spacy download en_vectors_web_lg

How to install Textacy
----------------------
https://chartbeat-labs.github.io/textacy/

Using pipeline
    pip install textacy[viz]
    pip install textacy[lang]

Using Conda
    conda install -c conda-forge textacy
"""

text = """
Hello Brian here are your 4 Amazon parcels. Where shall I  leave them?
They are worth £34.78. Two of them are very heavy but look exciting!
If you have any queries then write to whatru@whoru.org or see wareu.co.uk
"""

print("\nSimple Script to test that an nlp environment to perfom NLP using " +\
    "spaCy is successfully loaded on machine.\n")
input("Press Enter to continue...")

################################################################################
### regex

# Import regex
input("About to test Regex. Press Enter to continue...")
import re
print("1 - Regex successfully Loaded")

# Remove all non-word characters (everything except numbers and letters)
print(re.sub(r"[^\w\s]", '', text))
# Replace all runs of whitespace with a single dash
print(re.sub(r"\s+", '-', text))
print("Regex working ok. \n")
################################################################################
### spaCy

input("About to test spaCy. Press Enter to continue...")
# Import spaCy
import spacy
print("2 - spaCy Successfully Loaded\n")
# Load English language models
nlp_en = spacy.load('en')
print("3 - en Language Successfully Loaded")
nlp_en_cw_sm = spacy.load('en_core_web_sm')
print("4 - en_core_web_sm Language Successfully Loaded")
#nlp_en_cw_md = spacy.load('en_core_web_md')
print("5 - en_core_web_md Language Successfully Loaded")
#nlp_en_cw_lg = spacy.load('en_core_web_lg')
print("6 - en_core_web_lg Language Successfully Loaded")
#nlp_en_vc_lg = spacy.load('en_vectors_web_lg')
print("7 - en_vectors_web_lg Language Successfully Loaded")

# Import support functions
from spacy.lang.en.stop_words import STOP_WORDS

from spacy.tokens import Doc

doc = nlp_en(text)
print("8 - spaCy Doc created\n\nText Outputs:\n")
print([token.text for token in doc])

print("\nLemma Outputs:\n")
print([token.lemma_ for token in doc])

print("\nPOS Outputs:\n")
print([token.pos_ for token in doc])

print("\nBasic spaCy installation working ok.\n")


################################################################################
### Textacy

input("About to test Textacy. Press Enter to continue...")

import textacy
print("8 - Textacy Successfully Loaded\n")

print("Textacy quick look:")
print(textacy.text_utils.KWIC(text, 'heavy', window_width=35))

### Topic Analysis
vectorizer = textacy.Vectorizer(
    tf_type='linear', apply_idf=True, idf_type='smooth', norm='l2',
    min_df=1, max_df=0.95)

print("\nTextacy Doc")
terms_list = list(textacy.Doc(text).to_terms_list(ngrams=1, \
                                named_entities=True, as_strings=True))

print(terms_list)

doc_term_matrix = vectorizer.fit_transform(terms_list)

model = textacy.tm.TopicModel('nmf', n_topics=2)
model.fit(doc_term_matrix)
doc_topic_matrix = model.transform(doc_term_matrix)

print("\nTopic Analysis\n")
for topic_idx, top_terms in model.top_topic_terms(vectorizer.id_to_term):
    print('topic', topic_idx, ':', ', '.join(top_terms))

### Topic Analysis
plt = model.termite_plot(doc_term_matrix, vectorizer.id_to_term,
                   topics=-1,  n_terms=25, sort_terms_by='seriation')

import matplotlib.pyplot as plt
print("\nPlotting Termite Plot - close it to continue!\n")
plt.show()

### Sentiment Analysis
def emotional_valence(text):
    nlp = spacy.load("en")
    doc = nlp(text)
    return textacy.lexicon.emotional_valence(doc)

import textacy.lexicon_methods as lm
scores = lm.emotional_valence(doc)
values = ['%s :%.3f'%(k,scores[k]) for k in sorted(scores.keys())]
print('%s :\n\t%s'%(text,'\n\t'.join(values)))
