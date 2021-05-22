import pandas as pd
import numpy as np
import os

import src.embeddings as emb
import src.utils as utils

def max_count_pairs(sentences, sentences_aspects, embeddings_asp, props_aspects):
    # max-count-pairs method to select sentences
    df = pd.DataFrame(sentences, columns=['sentence'])
    df['sim'] = 0.0
    aspects_len = len(props_aspects)
    for i, row in df.iterrows():
        aspects_emb = emb.sentences_embeddings(sentences_aspects[i])
        for j in props_aspects[0]:
            max_j = 0
            for asp_emb in aspects_emb:
                sim = utils.cosine_similarity(asp_emb, embeddings_asp['embedding'][j])
                if sim > max_j:
                    max_j = sim
            df.loc[i, 'sim'] = max_j/aspects_len
    
    return " ".join(df.sort_values(by='sim', ascending=False).head()['sentence'].to_list())

def properties_aspects(properties: list, prop_embs, aspects, embeddings):

    props_aspects = []
    for i in range(0, len(prop_embs)):
        sim = []
        for j in range(0, len(embeddings)):
            sim.append(utils.cosine_similarity(prop_embs[i], embeddings['embedding'][j]))
        df = pd.DataFrame(aspects, columns=['aspects'])
        df['sim'] = sim
        props_aspects.append(df.sort_values(by='sim', ascending=False).head().index.tolist())

    return props_aspects

def summarize(movie: int, properties: list):

    movie_dir = "{0}/{1}".format(os.environ.get('MOVIES_EMB'), movie)
        
    aspects_df = pd.read_csv(movie_dir + '/aspects.csv')

    embeddings_asp = pd.read_csv(movie_dir + '/embeddings_aspects.csv')

    for i, row in embeddings_asp.iterrows():
        embeddings_asp['embedding'][i] = np.fromstring(row['embedding'][1:-1], sep=', ')

    aspects = aspects_df['aspect'].to_list()

    prop_embs = emb.sentences_embeddings(properties)

    sentences = utils.get_sentences(movie)

    sentences_aspects = utils.get_sentences_aspects(movie, sentences)

    props_aspects = properties_aspects(properties, prop_embs, aspects, embeddings_asp)

    return max_count_pairs(sentences, sentences_aspects, embeddings_asp, props_aspects)