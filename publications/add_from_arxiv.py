#! /usr/bin/env python3

import argparse
import arxiv
import re
import os
import textwrap


def _first_non_stopword(title: str) -> str:
    for word in re.split(r"\W", title.lower()):
        if word in ("a", "an", "the", "is", "are", "what", "who", "your"):
            continue
        return word
    raise ValueError(f'The title seems to have only stopwords! "{title}"')


def _author_lastname(author_name: str) -> str:
    return author_name.split(" ")[-1].lower()


def get_info(paper_id: str, out_dir: str) -> None:
    client = arxiv.Client()
    search = arxiv.Search(id_list=[paper_id])
    paper = next(client.results(search))

    summary = (
        paper.summary.replace("\n\n", "@@--@@")
        .replace("\n", " ")
        .replace("@@--@@", "\n\n")
    )

    tmpl = textwrap.dedent(
        f"""\
        ---
        layout: publication
        title: "{paper.title}"
        authors: {", ".join(a.name for a in paper.authors)}
        conference:
        year: {paper.published.year}
        additional_links:
          - {{name: "ArXiV", url: "https://arxiv.org/abs/{paper_id}"}}
        tags: ["TODO"]
        ---
        {summary}
        """
    )

    filename = f"{_author_lastname(paper.authors[0].name)}{paper.published.year}{_first_non_stopword(paper.title)}.markdown"
    with open(os.path.join(out_dir, filename), "w") as f:
        f.write(tmpl)

    print(f"Output at: {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("paper_id", help="The id of the paper to retrieve.")
    parser.add_argument("out_path", help="The path to output the file.")
    args = parser.parse_args()

    get_info(args.paper_id, args.out_path)
