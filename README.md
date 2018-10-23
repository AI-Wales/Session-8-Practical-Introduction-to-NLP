# Fuzzy Logic - Introduction-to-NLP
Practical workshop on NLP pipelines with a few examples.

Presented by David Pugh and Rob Bretton

We will introduce the concepts of NLP and show some basic Python code that can help process text ready for more advanced analysis. We will then introduce some libraries that can help with this, as well as start to model text in more advanced ways, We will use spaCy as a key library to demonstrate how to build custom processing pipelines and even throw in some topic and semantic modelling. Throughout we will hopefully see how powerful modern NLP libraries canbe - but also how difficult interpreting language can be.

And all demonstrated using the psychodelic Welsh wonder lyrics of the [Super Furry Animals](http://www.superfurry.com). 

At the end we will show how you can use this to build some basic but powerful language processing products.


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

