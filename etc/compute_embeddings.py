import argparse
import json
from timeit import default_timer as timer
from datetime import date

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
    parser.add_argument("--model", default='sentence-transformers/all-MiniLM-L6-v2', help="The name of the HF model")
    parser.add_argument("--save_emb", action='store_true', help="Save embeddings in CSV for Tensorboard Projector")

    return parser.parse_args()

def mean_pooling(token_embeddings, attention_mask):
    """ Mean Pooling, takes attention mask into account for correct averaging"""
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

def main(args):
    tokenizer = transformers.AutoTokenizer.from_pretrained(args.model)
    model = transformers.AutoModel.from_pretrained(args.model)
    model.eval()

    with open(args.json) as f:
        data = json.load(f)

    print(f"Num papers: {len(data)}")

    corpus = []
    for paper_info in data:
        corpus.append(tokenizer.sep_token.join([paper_info['title'], paper_info['abstract']]))

    batch_size = 4
    all_embeddings=[]
    start = timer()
    for i in range(0, len(corpus), batch_size):
        encoded_batch = tokenizer(corpus[i:min(i+batch_size, len(corpus))], padding=True, truncation=True, return_tensors='pt')
        with torch.no_grad():
            hidden_state = model(**encoded_batch).last_hidden_state
            all_embeddings.append(mean_pooling(hidden_state, encoded_batch['attention_mask']))

    all_embeddings = torch.cat(all_embeddings, dim=0)
    all_embeddings = F.normalize(all_embeddings, p=2, dim=1)
    print(f"elapsed {timer()-start:.1f}s")

    if args.save_emb:
        filename = f"{args.model.replace('/', '_')}-{date.today().strftime('%d.%m.%y')}"
        np.savetxt(f"{filename}-emb.tsv", all_embeddings, delimiter="\t")
        import csv
        with open(f"{filename}-meta.tsv", 'w', newline='') as csvfile:
            w = csv.writer(csvfile, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
            w.writerow(["year", "key", "title"])
            for paper in data:
                w.writerow([paper["year"], paper["key"], paper["title"]])

    np.random.seed(args.seed)
    out = sklearn.manifold.TSNE(n_components=2, metric="cosine").fit_transform(all_embeddings)

    for i, paper_info in enumerate(data):
        paper_info['tsne_embedding'] = out[i].tolist()

    with open(args.outpath, 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    args = parse_arguments()
    main(args)
