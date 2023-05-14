import argparse
import json

import numpy as np
import torch
import sklearn.manifold
import transformers


def parse_arguments():
    parser = argparse.ArgumentParser(description="TSNE Visualization of Papers in ML4Code")

    parser.add_argument("json", default=False, help="the path the json containing all papers.")
    parser.add_argument("outpath", default=False, help="the target path of the visualizations papers.")
    parser.add_argument("--seed", default=0, help="The seed for TSNE.", type=int)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    tokenizer = transformers.AutoTokenizer.from_pretrained("deepset/sentence_bert")
    model = transformers.AutoModel.from_pretrained("deepset/sentence_bert")
    model.eval()

    with open(args.json) as f:
        data = json.load(f)

    print(f"Num papers: {len(data)}")

    all_embeddings = []
    for paper_info in data:
        with torch.no_grad():
            token_ids = torch.tensor([tokenizer.encode(paper_info["abstract"])][:512])
            hidden_states, _ = model(token_ids)[-2:]
            all_embeddings.append(hidden_states.mean(0).mean(0).numpy())

    np.random.seed(args.seed)
    all_embeddings = np.array(all_embeddings)
    out = sklearn.manifold.TSNE(n_components=2, metric="cosine").fit_transform(all_embeddings)

    for i, paper_info in enumerate(data):
        paper_info['tsne_embedding'] = out[i].tolist()

    with open(args.outpath, 'w') as f:
        json.dump(data, f)
