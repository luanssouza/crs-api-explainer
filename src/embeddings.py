from sentence_transformers import SentenceTransformer

import os

modelBERT = SentenceTransformer(os.environ.get('LANGUAGE_MODEL'))

def sentences_embeddings(sentences):
    return modelBERT.encode(sentences)