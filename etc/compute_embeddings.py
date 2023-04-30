import argparse
import json

import numpy as np
import torch
import torch.nn.functional as F
import sklearn.manifold
import transformers


def parse_arguments():
    parser = argparse.ArgumentParser(description="TSNE Visualization of Papers in ML4Code")

    parser.add_argument("json", default=False, help="the path the json containing all papers.")
    parser.add_argument("outpath", default=False, help="the target path of the visualizations papers.")
    parser.add_argument("--seed", default=0, help="The seed for TSNE.", type=int)
    parser.add_argument("--model", default='sentence-transformers/all-MiniLM-L6-v2', help="Name of the HF model")

    return parser.parse_args()

def mean_pooling(token_embeddings, attention_mask):
    """ Mean Pooling, takes attention mask into account for correct averaging"""
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


if __name__ == "__main__":
    args = parse_arguments()
    tokenizer = transformers.AutoTokenizer.from_pretrained(args.model)
    model = transformers.AutoModel.from_pretrained(args.model)
    model.eval()

    with open(args.json) as f:
        data = json.load(f)

    print(f"Num papers: {len(data)}")

    corpus = []
    for paper_info in data:
        corpus.append(tokenizer.sep_token.join([paper_info['title'], paper_info['abstract']]))

    encoded_corpus = tokenizer(corpus, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        hidden_states = model(**encoded_corpus).last_hidden_state

    corpus_embeddings = mean_pooling(hidden_states, encoded_corpus['attention_mask'])
    corpus_embeddings = F.normalize(corpus_embeddings, p=2, dim=1)

    np.random.seed(args.seed)
    out = sklearn.manifold.TSNE(n_components=2, metric="cosine").fit_transform(corpus_embeddings)

    for i, paper_info in enumerate(data):
        paper_info['tsne_embedding'] = out[i].tolist()

    with open(args.outpath, 'w') as f:
        json.dump(data, f)
