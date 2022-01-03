import argparse
import json
import nltk

nltk.download('omw-1.4')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim.corpora import Dictionary
from gensim.models import LdaModel



def parse_arguments():
    parser = argparse.ArgumentParser(description="Topic Model of Papers in ML4Code")

    parser.add_argument("json", default=False, help="the path the json containing all papers.")
    parser.add_argument("outpath", default=False, help="the target path of the visualizations papers.")
    parser.add_argument("--num-topics", default=20, help="The number of topics.", type=int)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    with open(args.json) as f:
        data = json.load(f)

    print(f"Num papers: {len(data)}")

    
    lemmatizer = WordNetLemmatizer()
    stopwords = set(stopwords.words('english'))
    stopwords.update(["one", "two", "using"])
    
    tokens_per_paper = []
    for paper_info in data:
        text = paper_info["title"] + " " + paper_info["abstract"].replace("<p>", " ").replace("</p>", " ") + " ".join(paper_info["tags"])
        lemmatized_tokens = [lemmatizer.lemmatize(w).lower() for w in nltk.word_tokenize(text) if w.lower() not in stopwords and w.isalpha()]
        tokens_per_paper.append(lemmatized_tokens)

    dictionary = Dictionary(tokens_per_paper)
    dictionary.filter_extremes(no_below=20, no_above=0.5)

    corpus = [dictionary.doc2bow(doc) for doc in tokens_per_paper]

    passes = 100
    iterations = 1000

    temp = dictionary[0]  # This is needed to "load" the dictionary.

    model = LdaModel(
        corpus=corpus,
        id2word=dictionary.id2token,
        chunksize=1000,
        alpha='asymmetric',
        eta='auto',
        iterations=iterations,
        num_topics=args.num_topics,
        passes=passes,
        eval_every=None
    )

    topic_tokens = []
    for topicid in range(args.num_topics):
        topic_tokens.append([dictionary.id2token[k[0]] for i, k in enumerate(model.get_topic_terms(topicid, topn=4)) if i < 2 or k[1] > 0.025])

    paper_topic_data = []
    for paper, paper_bow in zip(data, corpus):
        topic_distr = model.get_document_topics(paper_bow, minimum_probability=0)
        paper_topic_data.append({
            "key": paper["key"],
            "year": paper["year"],
            "title": paper["title"],
            "topic_distr": {t: float(p) for t, p in topic_distr}
        })

    with open(args.outpath, 'w') as f:
        json.dump({
            "topics": topic_tokens,
            "paper_data": paper_topic_data 
        }, f)
