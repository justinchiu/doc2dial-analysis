import json
from pathlib import Path
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
import pdb; pdb.set_trace()
