---
layout: default
title: "Software"
order: 4
---

# Software #

## TimeNorm: time expression normalization ##

I developed [timenorm](https://github.com/bethard/timenorm), a parser for normalizing time expressions initially based on synchronous context free grammars and later based on neural network models. It can recognize, for example, that if today is 2020-12-11, then "the next three weeks" should be normalized to the interval [2020-12-12T00:00, 2021-01-02T00:00).

## ClearTK: machine learning in the UIMA framework ##

I was one of the lead developers for [ClearTK](http://cleartk.github.io/cleartk/), a [UIMA](http://uima.apache.org/) based toolkit for developing natural language processing systems, which extends the UIMA API to make developing machine learning components easier.

## uimaFIT: UIMA factories, injection and testing ##

We originally developed [uimaFIT](https://uima.apache.org/uimafit.html) as part of [ClearTK](http://cleartk.github.io/cleartk/) to provide general purpose utilities for working with [UIMA](http://uima.apache.org/) components.
It was subsequently adopted into the main [UIMA](http://uima.apache.org/) distribution.

## argparse: Python command line parser ##

I was the original developer of [argparse](http://docs.python.org/library/argparse.html), a command line parsing module for Python which is now part of the Python standard library.
