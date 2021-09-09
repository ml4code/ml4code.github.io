import argparse
import json
import os

import nltk

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import numpy as np
import scipy

from gensim.models import TfidfModel
from gensim.corpora import Dictionary


def parse_arguments():
    parser = argparse.ArgumentParser(description="TSNE Visualization of Papers in ML4Code")

    parser.add_argument("json", default=False, help="the path the json containing all papers.")
    parser.add_argument("outdir", default=False, help="the target path of the visualizations papers.")
    parser.add_argument("--num-relwork", default=4, help="Number of related work per paper.", type=int)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    num_relworks = args.num_relwork

    with open(args.json) as f:
        data = json.load(f)

    print(f"Num papers: {len(data)}")

    lemmatizer = WordNetLemmatizer()
    stopwords = set(stopwords.words('english'))
    stopwords.update(["one", "two", "using"])

    tokens_per_paper = []
    keys = []

    for paper_info in data:
        keys.append((paper_info["key"], paper_info["title"]))
        text = paper_info["title"] + " " + paper_info["abstract"].replace("<p>", " ").replace("</p>", " ") + " ".join(paper_info["tags"])
        lemmatized_tokens = [lemmatizer.lemmatize(w).lower() for w in nltk.word_tokenize(text) if w.lower() not in stopwords and w.isalpha()]
        tokens_per_paper.append(lemmatized_tokens)

    dictionary = Dictionary(tokens_per_paper)
    dictionary.filter_extremes(no_below=2, no_above=0.5)

    corpus = [dictionary.doc2bow(line) for line in tokens_per_paper]
    model = TfidfModel(corpus)
    
    tf_idf_vectors = []
    for bow in corpus:
        vec = np.zeros(len(dictionary), dtype=np.float64)
        for i, v in model[bow]:
            vec[i] = v
        tf_idf_vectors.append(vec)
    tf_idf_vectors = np.array(tf_idf_vectors)
    
    distances = scipy.spatial.distance.cdist(tf_idf_vectors, tf_idf_vectors, metric='cosine')
    sorted_idxs = np.argsort(distances, axis=-1)[:, 1:num_relworks+1]
    
    os.makedirs(args.outdir, exist_ok=True)
    for i, (bibkey, title) in enumerate(keys):
        with open(os.path.join(args.outdir, bibkey + ".json"), "w") as f:
            json.dump([keys[j] for j in sorted_idxs[i]], f)

    