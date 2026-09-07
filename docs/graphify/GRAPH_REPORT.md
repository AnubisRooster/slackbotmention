# Graph Report - slackbotmention  (2026-09-07)

## Corpus Check
- Corpus is ~12,828 words - fits in a single context window. You may not need a graph.

## Summary
- 15 nodes · 16 edges · 4 communities (2 shown, 2 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- create_slack_userid_csv.py
- slackmentionbot.py
- graphify_pipeline.py
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

## Communities (4 total, 2 thin omitted)

### Community 0 - "create_slack_userid_csv.py"
Cohesion: 0.60
Nodes (4): create_csv_file_for_slack_userid_data(), U026GDM4B26 dbooker Danny Booker, start(), write_userid_list_to_csv()

### Community 1 - "slackmentionbot.py"
Cohesion: 0.60
Nodes (4): message, find_assignee_slackid_in_csv(), get_assignee_string(), read_incoming_message()

## Knowledge Gaps
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `handle_errors()` connect `handle_errors()` to `slackmentionbot.py`?**
  _High betweenness centrality (0.055) - this node is a cross-community bridge._