"""Streamlit graph visualization."""

import json
from pathlib import Path

import networkx as nx
import streamlit as st

DEMO = Path(__file__).resolve().parent.parent.parent / "demo-data"


def main():
    st.title("Threat Intel Graph")
    g = nx.node_link_graph(json.loads((DEMO / "threat_graph.json").read_text(encoding="utf-8")))
    st.write(f"Nodes: {g.number_of_nodes()}, Edges: {g.number_of_edges()}")
    st.json(list(g.nodes(data=True))[:20])


if __name__ == "__main__":
    main()
