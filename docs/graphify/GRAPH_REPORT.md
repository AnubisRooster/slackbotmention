# Graph Report - slackbotmention  (2026-09-21)

## Corpus Check
- Corpus is ~12,828 words - fits in a single context window. You may not need a graph.

## Summary
- 35 nodes · 42 edges · 5 communities (4 shown, 1 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- graphify_pipeline.py
- create_slack_userid_csv.py
- slackmentionbot.py
- read_incoming_message()
- handle_errors()

## God Nodes (most connected - your core abstractions)
1. `read_incoming_message()` - 4 edges
2. `start()` - 3 edges
3. `write_userid_list_to_csv()` - 3 edges
4. `create_csv_file_for_slack_userid_data()` - 2 edges
5. `handle_errors()` - 2 edges
6. `get_assignee_string()` - 2 edges
7. `find_assignee_slackid_in_csv()` - 2 edges
8. `U026GDM4B26 dbooker Danny Booker` - 1 edges
9. `Self-contained graphify pipeline for CI. Builds a knowledge graph over this…` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (5 total, 1 thin omitted)

### Community 0 - "graphify_pipeline.py"
Cohesion: 0.15
Nodes (11): graphify_analyze, graphify_build, graphify_cluster, graphify_detect, graphify_export, graphify_extract, graphify_llm, graphify_report (+3 more)

### Community 1 - "create_slack_userid_csv.py"
Cohesion: 0.24
Nodes (9): create_csv_file_for_slack_userid_data(), U026GDM4B26 dbooker Danny Booker, start(), write_userid_list_to_csv(), csv, dotenv, os, pathlib (+1 more)

### Community 2 - "slackmentionbot.py"
Cohesion: 0.33
Nodes (5): logging, re, slack_bolt, slack_bolt_adapter_socket_mode, slack_bolt_error

### Community 3 - "read_incoming_message()"
Cohesion: 0.50
Nodes (4): message, find_assignee_slackid_in_csv(), get_assignee_string(), read_incoming_message()

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `read_incoming_message()` connect `read_incoming_message()` to `slackmentionbot.py`?**
  _High betweenness centrality (0.060) - this node is a cross-community bridge._
- **Why does `handle_errors()` connect `handle_errors()` to `slackmentionbot.py`?**
  _High betweenness centrality (0.059) - this node is a cross-community bridge._