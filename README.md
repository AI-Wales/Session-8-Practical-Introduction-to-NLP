# Fuzzy Logic - Introduction-to-NLP
Practical workshop on NLP pipelines with a few examples.

Presented by David Pugh and Rob Bretton

We will introduce the concepts of NLP and show some basic Python code that can help process text ready for more advanced analysis. We will then introduce some libraries that can help with this, as well as start to model text in more advanced ways, We will use spaCy as a key library to demonstrate how to build custom processing pipelines and even throw in some topic and semantic modelling. Throughout we will hopefully see how powerful modern NLP libraries can be - but also how difficult interpreting language can be.

And all demonstrated using the psychodelic Welsh wonder lyrics of the [Super Furry Animals](http://www.superfurry.com). 

At the end we will show how you can use this to build some basic but powerful language processing products.

This is a practical introduction - there will be plenty of code, tips and examples and it's designed to give you the basic knowledge, tools and direction to be able to go off and explore this subject yourself. There will be a mix of theory, concepts and code workthroughs during the session - to follow along with the code, just download this repository to your computer, open up Anaconda navigator and open Jupyter notebooks. Just open each notebook as required. The notebooks are designed so that you can work through them at your own pace in your own time when - we will be going through a lot of content during the workshop and showing lots of practical code and to get the most out of it you will want to work through much of this in your own time with your own text. 


## To be able to use these notebooks you will need to have installed Anaconda and got a Python data science environment set up on your laptop. 

Refer to [Getting Started](https://github.com/AI-Wales/Getting-Started) for instructions on how to do this.

You will also need a few specific packages installed.  Install these by opening Anaconda Navigator, clicking on Environments, select the environmnet you are using (e.g., root), select the arrow and 'open terminal'.

In the command prompt that opens, type the following commands to install spaCy and its English language models:


```
conda install -c conda-forge spacy
```

```
python -m spacy download en
```

See the [spaCy](https://spacy.io) documents.

We also use [textaCy](https://chartbeat-labs.github.io/textacy/). This is installed using

```
conda install -c conda-forge textacy
```

### Other useful libraries we use:
The nltk library

```
conda install -c anaconda nltk
```

WordCloud for visually viewing common words

```
conda install -c conda-forge wordcloud
```


Pob lwc and SFAok!!!
