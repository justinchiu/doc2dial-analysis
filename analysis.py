import json
from pathlib import Path
import numpy as np
import streamlit as st

with Path("doc2dial_dial_train.json").open() as f:
    dials = json.load(f)
with Path("doc2dial_doc.json").open() as f:
    docs = json.load(f)

domain = st.radio("Domain", dials["dial_data"].keys())

keys = list(dials["dial_data"][domain].keys())

example_num = st.number_input("Example number", min_value=0, max_value=len(keys), value=0)

key1 = keys[example_num]
dom1_dials = dials["dial_data"][domain][key1]
dom1_doc = docs["doc_data"][domain][key1]

dial = dom1_dials[example_num]
turns = dial["turns"]
for turn in turns:
    speaker = turn["role"]
    da = turn["da"]
    references = turn["references"]
    utterance = turn["utterance"]

    st.write(utterance)
    st.write([reference["sp_id"] for reference in references])

with st.sidebar:
    st.write("Doc")
    for span_id, span in dom1_doc["spans"].items():
        st.write(span_id)
        st.write(span["text_sp"])

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
