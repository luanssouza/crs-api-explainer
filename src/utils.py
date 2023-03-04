import numpy as np
import re

import src.bucket as bc

def split_aspects(aspects: str):
    return re.findall(r"[^\,\'\[\]\s]+", aspects)

def get_sentences_aspects(movie: int, sentences: list):
    nouns = bc.read_csv("data/{0}/filtered_sentences.csv".format(movie))
    sentences_aspects = []
    for sentence in sentences:
        sentences_aspects.append(split_aspects(nouns.loc[nouns['sentences'] == sentence].values[0][1]))
    return sentences_aspects

def get_sentences(movie: int):
    return bc.read_csv("data/{0}/filtered_sentences.csv".format(movie))['sentences'].to_list()

def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1, 2) * np.linalg.norm(v2, 2))

def properties_aspects(properties, movie):
    r = []
    return r