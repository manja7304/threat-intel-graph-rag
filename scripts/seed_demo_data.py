#!/usr/bin/env python3
import json
from pathlib import Path

DEMO = Path(__file__).resolve().parent.parent / "demo-data"
DEMO.mkdir(parents=True, exist_ok=True)

graph = {
    "directed": True,
    "multigraph": False,
    "graph": {},
    "nodes": [
        {"id": "IOC-1", "type": "ip", "value": "192.0.2.44"},
        {"id": "T1566", "type": "technique", "name": "Phishing"},
        {"id": "T1059", "type": "technique", "name": "Command Interpreter"},
    ],
    "links": [
        {"source": "IOC-1", "target": "T1566", "rel": "indicates"},
        {"source": "T1566", "target": "T1059", "rel": "leads_to"},
    ],
    "edges": [
        {"source": "IOC-1", "target": "T1566", "rel": "indicates"},
        {"source": "T1566", "target": "T1059", "rel": "leads_to"},
    ],
}
(DEMO / "threat_graph.json").write_text(json.dumps(graph, indent=2), encoding="utf-8")
(DEMO / "iocs.json").write_text(
    json.dumps(
        [
            {"id": "IOC-1", "type": "ip", "value": "192.0.2.44", "node_id": "IOC-1"},
            {"id": "IOC-2", "type": "domain", "value": "evil.demo", "node_id": None},
        ],
        indent=2,
    ),
    encoding="utf-8",
)
print("Seeded threat graph")
