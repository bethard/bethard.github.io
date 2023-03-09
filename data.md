---
layout: default
title: "Data"
order: 6
---
# Data #

## Time Normalization in News and Clinical Text ##

We have [annotated time expressions in a corpus of news articles and clinical notes](https://github.com/bethard/anafora-annotations/) following the Semantically Compositional Annotation Scheme for Time Normalization (SCATE). This new approach to annotating time expressions has allowed new types of machine-learning models to be trained for normalizing times, and formed the basis for a shared task in 2018.

<div class="px-5"><script src="https://bibbase.org/show?bib=http%3A%2F%2Fclulab.cs.arizona.edu%2Fpapers%2Fbethard.bib&jsonp=1&fullnames=1&groupby=&hidemenu=true&filter=title:Time%20Normalization,year:(2016|2018)"></script></div>

## Temporal Dependency Trees in Children's Stories ##

As part of the [TERENCE](http://www.terenceproject.eu/) project, we annotated a small [corpus of children's fables with temporal dependency trees](https://raw.githubusercontent.com/bethard/data-archive/master/fables-100-temporal-dependency.xml), that is, where timelines are annotated as tree-structured graphs of temporal links between events. More details about the annotation process and temporal dependency parsing models are available in:

<div class="px-5"><script src="https://bibbase.org/show?bib=http%3A%2F%2Fclulab.cs.arizona.edu%2Fpapers%2Fbethard.bib&jsonp=1&fullnames=1&groupby=&hidemenu=true&filter=title:Timelines,year:2012"></script></div>

## Re-annotated TempEval 2010 Time Expressions ##

In working with the TempEval 2010 time expression recognition task, we found that a few time expressions, such as such as *23-year*, *a few days* and *third-quarter* were missed by the annotators in the official test data. Our [re-annotated version of the TempEval time expression test data](https://raw.githubusercontent.com/bethard/data-archive/master/timex-extents.tab) can be used as a drop-in replacement to the original data. More details about the re-annotation process and reasons to use this data instead of the original are available in:

<div class="px-5"><script src="https://bibbase.org/show?bib=http%3A%2F%2Fclulab.cs.arizona.edu%2Fpapers%2Fbethard.bib&jsonp=1&fullnames=1&groupby=&hidemenu=true&filter=title:Portability,year:2011"></script></div>

## Conjoined-Event Temporal and Causal Relations ##

We annotated a small [corpus of conjoined-event temporal-causal relations](https://raw.githubusercontent.com/bethard/data-archive/master/treebank-verb-conj-anns.xml). For example, given the sentence:

> Fuel tanks had *leaked* and *contaminated* the soil.

we annotated the relations `(leaked BEFORE contaminated)` and `(leaked CAUSED contaminated)`. The corpus includes 1000 pairs of events taken from the Wall Street Journal, with each event pair assigned both a temporal and a causal relation. More details about the annotation process and models for predicting such relations are available in:

<div class="px-5"><script src="https://bibbase.org/show?bib=http%3A%2F%2Fclulab.cs.arizona.edu%2Fpapers%2Fbethard.bib&jsonp=1&fullnames=1&groupby=&hidemenu=true&filter=title:(Temporal|Causal),year:2008"></script></div>

## Verb-Clause Temporal Relations ##

We annotated a small [corpus of verb-clause temporal relations](https://raw.githubusercontent.com/bethard/data-archive/master/timebank-verb-clause.txt). For example, given the sentence:

> International Business Machines Corp. and Compaq Computer Corp. *say* the bugs will *delay* products.

we annotated the temporal relation `(say BEFORE delay)`. The corpus includes 895 such pairs, taken from the Wall Street Journal section of the [TimeBank](http://timeml.org/site/timebank/timebank.html). More details about the data and annotation process are available in:

<div class="px-5"><script src="https://bibbase.org/show?bib=http%3A%2F%2Fclulab.cs.arizona.edu%2Fpapers%2Fbethard.bib&jsonp=1&fullnames=1&groupby=&hidemenu=true&filter=title:Syntactic%20Temporal,year:2007"></script></div>

## Opinions and Opinion Holders ##

We annotated opinions and opinion holders for verbs with clausal complements in both [FrameNet data](https://raw.githubusercontent.com/bethard/data-archive/master/opinion-holder-framenet1.3.xml) and [PropBank data](https://raw.githubusercontent.com/bethard/data-archive/master/opinion-holder-propbank1.0.xml). For example, given the sentence:

> Still, Vista officials realize they're relatively fortunate.

we annotated *Vista officials* as the opinion holder, and *they're relatively fortunate* as the opinion. More details about the data and the models we built from it are available in:

<div class="px-5"><script src="https://bibbase.org/show?bib=http%3A%2F%2Fclulab.cs.arizona.edu%2Fpapers%2Fbethard.bib&jsonp=1&fullnames=1&groupby=&hidemenu=true&filter=title:opinion%20holder,year:2005"></script></div>

The corpora on which this annotation was performed have changed since this work was done, but I mostly re-aligned the data in 2016. The PropBank data should be almost identical to that used in the paper, while the FrameNet data is about 50 sentences smaller, since some of the sentences we annotated are missing in the later versions of FrameNet.
