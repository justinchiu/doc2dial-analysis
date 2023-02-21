import json
from pathlib import Path
import numpy as np
import streamlit as st

with Path("doc2dial_dial_train.json").open() as f:
    dials = json.load(f)
with Path("doc2dial_doc.json").open() as f:
    docs = json.load(f)

dmv_keys = list(dials["dial_data"]["dmv"].keys())

key1 = dmv_keys[0]
dmv1_dials = dials["dial_data"]["dmv"][key1]
dmv1_doc = docs["doc_data"]["dmv"][key1]

dial = dmv1_dials[0]
turns = dial["turns"]
for turn in turns:
    speaker = turn["role"]
    da = turn["da"]
    references = turn["references"]
    utterance = turn["utterance"]

    st.write(utterance)
    for reference in references:
        st.write(reference["sp_id"])

def doc_dial_lengths(dials, docs):
    dial_lens = []
    for domain, domdials in dials.items():
        domdocs = docs[domain]
        for docname, dials in domdials.items():
            for dial in dials:
                dialtext = " ".join([
                    f'{turn["role"]}: {turn["utterance"]}'
                    for turn in dial["turns"]
                ])
                dial_lens.append(len(dialtext.strip().split()))

    doc_lens = []
    for domain, domdocs in docs.items():
        for doc in domdocs.values():
            title = doc["title"]
            text = doc["doc_text"]
            doc_lens.append(len(title.split()) + len(text.split()))

    print(np.min(dial_lens), np.mean(dial_lens), np.max(dial_lens))
    print(np.min(doc_lens), np.mean(doc_lens), np.max(doc_lens))


doc_dial_lengths(dials["dial_data"], docs["doc_data"])
