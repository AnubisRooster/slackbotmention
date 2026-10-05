# Graph Report - slackbotmention  (2026-10-05)

## Corpus Check
- Corpus is ~15,058 words - fits in a single context window. You may not need a graph.

## Summary
- 35 nodes · 45 edges · 4 communities (2 shown, 2 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- create_slack_userid_csv.py
- slackmentionbot.py
- handle_errors()

## God Nodes (most connected - your core abstractions)
1. `read_incoming_message()` - 4 edges
2. `start()` - 3 edges
3. `create_csv_file_for_slack_userid_data()` - 3 edges
4. `write_userid_list_to_csv()` - 3 edges
5. `get_assignee_string()` - 3 edges
6. `find_assignee_slackid_in_csv()` - 3 edges
7. `handle_errors()` - 2 edges
8. `U026GDM4B26 dbooker Danny Booker` - 1 edges
9. `Self-contained graphify pipeline for CI. Builds a knowledge graph over this…` - 1 edges

## Surprising Connections (you probably didn't know these)
- `find_assignee_slackid_in_csv()` --calls--> `csv`  [EXTRACTED]
  slackmentionbot.py →   _Bridges community 2 → community 1_

## Import Cycles
- None detected.

## Communities (4 total, 2 thin omitted)

### Community 1 - "create_slack_userid_csv.py"
Cohesion: 0.27
Nodes (3): create_csv_file_for_slack_userid_data(), start(), write_userid_list_to_csv()

### Community 2 - "slackmentionbot.py"
Cohesion: 0.27
Nodes (3): find_assignee_slackid_in_csv(), get_assignee_string(), read_incoming_message()

## Knowledge Gaps
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `handle_errors()` connect `handle_errors()` to `slackmentionbot.py`?**
  _High betweenness centrality (0.059) - this node is a cross-community bridge._