from src.rag.graph_rag import hybrid_query

def test_graph_rag():
    out = hybrid_query('ip 192.0.2.44', {})
    assert 'techniques' in out['answer'].lower() or 'T1566' in out['answer']
