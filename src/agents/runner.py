"""Graph RAG with hybrid retrieval over STIX/MITRE demo graph."""

from __future__ import annotations

from src.rag.graph_rag import hybrid_query


def run_agent(query: str, context: dict | None = None) -> dict:
    return hybrid_query(query, context or {})
