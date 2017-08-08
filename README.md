# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 4: Web Scraping TV Shows

## Business Case Overview

You are hired as a data science consultant by a TV production company.  They want to produce the next big hit, and want your help to figure out how to do that!

Specifically:
1. They want to be able accurately to predict the success of a show.
2. They want to know what attributes predict the success of a show (as measured by the average imdb rating).

To limit the scope, your principal has suggested that you first focus on the top 250 tv shows (http://www.imdb.com/chart/toptv/).  But this has some big drawbacks in terms of how you can generalize your findings!  You should try to expand beyond this list, but how you do that is up to you!

If you do not expand beyond this list, in your project writeup, you *must* discuss in what ways this choice of data affects your ability to draw conclusions from your findings.

**Goal:** Scrape your own data and/or use APIs in order to collect the data to best answer these two questions.

---

## Directions

In this project you will be leveraging a variety of skills. The first will be to use the web-scraping and/or API techniques you've learned to collect data on data jobs from http://www.imdb.com and/or http://api.tvmaze.com (or any data source you want to use!). Once you have collected and cleaned the data, you will use it to answer the questions.

### QUESTION 1: Predictive model

To predict rating, you will be building either a classification or regression model, using features like the genre, network, summary etc (you should choose your features!). If framing this as a regression problem, you will be estimating the average IMDB rating. You may instead choose to frame this as a classification problem, in which case you will create labels from these ratings (high vs. low, for example) according to thresholds (such as median average rating).  

Think about when it might make sense to frame this as a classification rather than regression.

You have learned a variety of new skills and models that may be useful for this problem:
- NLP
- Unsupervised learning and dimensionality reduction techniques (PCA, clustering)
- Ensemble methods and decision tree models
- SVM models

Whatever you decide to use, the most important thing is to justify your choices and interpret your results. *Communication of your process is key.*

You also must use at least two models to try to hone in on a well-performing model.

### QUESTION 2: Factors that predict success of show

Using your models, and other techniques (EDA etc.), explain which features best predict performance of a show.


### SUPER BONUS PROBLEM

Dig more deeply into the distribution of ratings for the shows.  What predicts a big difference between how men and women review the shows?

---

## Requirements

1. Scrape and prepare your own data.

2. **Create and compare at least two models**. One of the two models should be a decision tree or ensemble model. The other can be a classifier or regression of your choosing (e.g. Ridge, logistic regression, KNN, SVM, etc).

3. Prepare a polished Jupyter Notebook with your analysis for a peer audience of data scientists.
   - Make sure to clearly describe and label each section.
   - Comment on your code so that others could, in theory, replicate your work.

4. A brief writeup in an executive summary, written for a non-technical audience.
   - Writeups should be at least 500-1000 words, defining any technical terms, explaining your approach, as well as any risks and limitations.


## Keep in mind!

Despite your best efforts, sometimes you cannot produce a good model!  But you **must** try to be able to explain why!  That's part of your job.
