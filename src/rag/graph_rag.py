"""NetworkX graph RAG with vector-like keyword retrieval."""

from __future__ import annotations

import json
from pathlib import Path

import networkx as nx

DEMO = Path(__file__).resolve().parent.parent.parent / "demo-data"
_GRAPH: nx.DiGraph | None = None
_IOC_INDEX: list[dict] | None = None


def _load_graph() -> nx.DiGraph:
    global _GRAPH
    if _GRAPH is None:
        _GRAPH = nx.node_link_graph(json.loads((DEMO / "threat_graph.json").read_text(encoding="utf-8")))
    return _GRAPH


def _load_iocs() -> list[dict]:
    global _IOC_INDEX
    if _IOC_INDEX is None:
        _IOC_INDEX = json.loads((DEMO / "iocs.json").read_text(encoding="utf-8"))
    return _IOC_INDEX


def hybrid_query(query: str, context: dict) -> dict:
    trace = []
    g = _load_graph()
    iocs = _load_iocs()
    q = query.lower()
    matched_iocs = [i for i in iocs if i["value"] in q or i["type"] in q]
    trace.append({"step": "vector_keyword", "matches": len(matched_iocs)})
    techniques = []
    for ioc in matched_iocs[:3]:
        node = ioc.get("node_id")
        if node and g.has_node(node):
            techniques.extend([n for n in g.neighbors(node) if str(n).startswith("T")])
    trace.append({"step": "graph_expand", "techniques": techniques})
    answer = f"Related techniques: {', '.join(sorted(set(techniques))) or 'none'} for query: {query}"
    return {"answer": answer, "trace": trace, "metadata": {"ioc_count": len(matched_iocs)}}
