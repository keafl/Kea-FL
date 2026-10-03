## Question

You will read an event flow including page actions and code coverage differences between correct and error executions.

Then answer:

Which files most likely contain the non-crash functional (NCF) bug?



## Rules

(0) Infer functionality from failed test case name.

(1) Only NCF bugs.

(2) Compare execution flows and identify divergence point.

    (a) Focus on last shared action → first divergence.

    (b) Coverage is supporting evidence only.

(3) Consider state inconsistency issues.

(4) Ignore random exploratory actions unless directly relevant.

(5) Focus only on files relevant to failed scenario.

(6) Exclude test/mock/third-party code.

(7) Rank by contribution to divergence behavior.

(8) Prefer simplest explanation.



## Failed Test Case

test_check_recent_file



## Code Coverage Summary

File: net/gsantner/markor/util/AppSettings.java

  Only in second dataset lines: [698]

    Line 698: hit count 2

----------------------------------------

File: net/gsantner/opoc/ui/FilesystemViewerAdapter.java

  Only in second dataset lines: [168, 170, 238, 239, 240, 241, 489, 490]

    Line 168: hit count 11

    Line 170: hit count 1

    Line 238: hit count 5

    Line 239: hit count 5

    Line 240: hit count 5

    Line 241: hit count 4

    Line 489: hit count 6

    Line 490: hit count 10

----------------------------------------



## Execution Divergence Hint

Common prefix:

Random operation: LONG_CLICK → Start: test_open_file → Back → Pass: test_open_file → Start: test_check_recent_file → Pass: test_check_recent_file



FAIL continuation:

Random operation: CLICK → Start: test_open_file → Back → Pass: test_open_file → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: LONG_CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Start: test_check_recent_file → Fail: test_check_recent_file → Start: test_stop_start → Pass: test_stop_start



## Correct Execution Path

Random operation: LONG_CLICK → Start: test_open_file → Back → Pass: test_open_file → Start: test_check_recent_file → Pass: test_check_recent_file



## Error Execution Path

Random operation: LONG_CLICK → Start: test_open_file → Back → Pass: test_open_file → Start: test_check_recent_file → Pass: test_check_recent_file → Random operation: CLICK → Start: test_open_file → Back → Pass: test_open_file → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: LONG_CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Start: test_check_recent_file → Fail: test_check_recent_file → Start: test_stop_start → Pass: test_stop_start



## Files to Analyze

net/gsantner/markor/util/AppSettings.java

  Differing lines: 1



net/gsantner/opoc/ui/FilesystemViewerAdapter.java

  Differing lines: 8



## Output Format

Provide your answer with file paths only. Sort all the files by suspicion level (highest first). One file path per line. No numbering, no explanations, no additional text, no extra punctuation.



Output: