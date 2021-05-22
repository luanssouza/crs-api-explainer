import pandas as pd
import numpy as np
import os
import re

def split_aspects(aspects: str):
    return re.findall(r"[^\,\'\[\]\s]+", aspects)

def get_sentences_aspects(movie: int, sentences: list):
    nouns = pd.read_csv("{0}/{1}/filtered_sentences.csv".format(os.environ.get('MOVIES_SENT'), movie))
    sentences_aspects = []
    for sentence in sentences:
        sentences_aspects.append(split_aspects(nouns.loc[nouns['sentences'] == sentence].values[0][1]))
    return sentences_aspects

def get_sentences(movie: int):
    return pd.read_csv("{0}/{1}/filtered_sentences.csv".format(os.environ.get('MOVIES_EMB'), movie))['sentences'].to_list()

def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1, 2) * np.linalg.norm(v2, 2))

def properties_aspects(properties, movie):
    r = []
    return r