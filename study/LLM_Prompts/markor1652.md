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

test_search_note



## Code Coverage Summary

File: net/gsantner/markor/activity/MainActivity.java

  Only in second dataset lines: [179, 180, 184]

    Line 179: hit count 4

    Line 180: hit count 4

    Line 184: hit count 2

----------------------------------------

File: net/gsantner/markor/ui/SearchOrCustomTextDialogCreator.java

  Only in second dataset lines: [130, 131, 136, 138]

    Line 130: hit count 2

    Line 131: hit count 5

    Line 136: hit count 3

    Line 138: hit count 1

----------------------------------------

File: net/gsantner/markor/ui/fsearch/FileSearchDialog.java

  Only in second dataset lines: [28, 29, 30, 31, 33, 34, 35, 37, 40, 42, 43, 44, 45, 46, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 62, 63, 86, 87, 90, 91, 92, 93, 94, 95, 105, 108, 129, 130, 131, 134, 135, 136, 139, 140, 141, 144, 147, 148, 149, 150, 153, 156, 157, 158, 159, 163, 165]

    Line 28: hit count 4

    Line 29: hit count 7

    Line 30: hit count 5

    Line 31: hit count 6

    Line 33: hit count 4

    Line 34: hit count 5

    Line 35: hit count 7

    Line 37: hit count 1

    Line 40: hit count 6

    Line 42: hit count 5

    Line 43: hit count 5

    Line 44: hit count 3

    Line 45: hit count 9

    Line 46: hit count 4

    Line 48: hit count 6

    Line 49: hit count 10

    Line 51: hit count 6

    Line 52: hit count 12

    Line 54: hit count 5

    Line 55: hit count 5

    Line 56: hit count 5

    Line 57: hit count 5

    Line 58: hit count 5

    Line 59: hit count 5

    Line 60: hit count 5

    Line 62: hit count 5

    Line 63: hit count 9

    Line 86: hit count 3

    Line 87: hit count 4

    Line 90: hit count 3

    Line 91: hit count 3

    Line 92: hit count 3

    Line 93: hit count 3

    Line 94: hit count 7

    Line 95: hit count 5

    Line 105: hit count 4

    Line 108: hit count 3

    Line 129: hit count 3

    Line 130: hit count 4

    Line 131: hit count 4

    Line 134: hit count 3

    Line 135: hit count 4

    Line 136: hit count 4

    Line 139: hit count 3

    Line 140: hit count 4

    Line 141: hit count 4

    Line 144: hit count 4

    Line 147: hit count 3

    Line 148: hit count 4

    Line 149: hit count 6

    Line 150: hit count 4

    Line 153: hit count 3

    Line 156: hit count 4

    Line 157: hit count 3

    Line 158: hit count 4

    Line 159: hit count 2

    Line 163: hit count 2

    Line 165: hit count 2

----------------------------------------

File: net/gsantner/markor/util/AppSettings.java

  Only in second dataset lines: [594, 602, 610, 618]

    Line 594: hit count 7

    Line 602: hit count 7

    Line 610: hit count 7

    Line 618: hit count 7

----------------------------------------

File: net/gsantner/opoc/android/dummy/TextWatcherDummy.java

  Only in first dataset lines: [25, 29, 54, 55]

    Line 25: hit count 1

    Line 29: hit count 1

    Line 54: hit count 4

    Line 55: hit count 1

----------------------------------------

File: net/gsantner/opoc/ui/FilesystemViewerFragment.java

  Only in second dataset lines: [375, 377, 379, 423, 425, 529, 530, 531, 540]

    Line 375: hit count 6

    Line 377: hit count 2

    Line 379: hit count 3

    Line 423: hit count 2

    Line 425: hit count 2

    Line 529: hit count 9

    Line 530: hit count 3

    Line 531: hit count 7

    Line 540: hit count 1

----------------------------------------

File: net/gsantner/opoc/util/ContextUtils.java

  Only in second dataset lines: [582]

    Line 582: hit count 8

----------------------------------------



## Execution Divergence Hint

Common prefix:

Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Start: test_search_note → Input: hi.md → Back → Pass: test_search_note → Start: test_create_note → Input: MRA6Yipe



FAIL continuation:

Back → Pass: test_create_note → Start: test_search_note → Input: hi.md → Back → Pass: test_search_note → Start: test_search_note → Input: hi.md → Back → Pass: test_search_note → Start: test_search_note → Input: hi.md → Back → Pass: test_search_note → Random operation: CLICK → Random operation: SCROLL_RIGHT_LEFT → Start: test_search_note → Input: hi.md → Back → Pass: test_search_note → Start: test_create_note → Input: h2Q3XE5VXQ → Back → Pass: test_create_note → Random operation: LONG_CLICK → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Start: test_create_note → Input: tA8E5G1j → Back → Pass: test_create_note → Random operation: CLICK → Random operation: SCROLL_LEFT_RIGHT → Start: test_back_to_root → Pass: test_back_to_root → Start: test_search_note → Input: hi.md → Back → Fail: test_search_note → Random operation: CLICK → Random operation: LONG_CLICK → Start: test_modify_note → Input: jCnb0vt9jXDmOI_yMTwcdAXh8ZwJXL → Back → Pass: test_modify_note → Start: test_search_note → Input: hi.md



## Correct Execution Path

Random operation: CLICK → Random operation: LONG_CLICK → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Start: test_search_note → Input: hi.md → Back → Pass: test_search_note → Start: test_create_note → Input: MRA6Yipe



## Error Execution Path

Random operation: CLICK → Random operation: LONG_CLICK → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Start: test_search_note → Input: hi.md → Back → Pass: test_search_note → Start: test_create_note → Input: MRA6Yipe → Back → Pass: test_create_note → Start: test_search_note → Input: hi.md → Back → Pass: test_search_note → Start: test_search_note → Input: hi.md → Back → Pass: test_search_note → Start: test_search_note → Input: hi.md → Back → Pass: test_search_note → Random operation: CLICK → Random operation: SCROLL_RIGHT_LEFT → Start: test_search_note → Input: hi.md → Back → Pass: test_search_note → Start: test_create_note → Input: h2Q3XE5VXQ → Back → Pass: test_create_note → Random operation: LONG_CLICK → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Start: test_create_note → Input: tA8E5G1j → Back → Pass: test_create_note → Random operation: CLICK → Random operation: SCROLL_LEFT_RIGHT → Start: test_back_to_root → Pass: test_back_to_root → Start: test_search_note → Input: hi.md → Back → Fail: test_search_note → Random operation: CLICK → Random operation: LONG_CLICK → Start: test_modify_note → Input: jCnb0vt9jXDmOI_yMTwcdAXh8ZwJXL → Back → Pass: test_modify_note → Start: test_search_note → Input: hi.md



## Files to Analyze

net/gsantner/markor/activity/MainActivity.java

  Differing lines: 3



net/gsantner/markor/ui/SearchOrCustomTextDialogCreator.java

  Differing lines: 4



net/gsantner/markor/ui/fsearch/FileSearchDialog.java

  Differing lines: 58



net/gsantner/markor/util/AppSettings.java

  Differing lines: 4



net/gsantner/opoc/android/dummy/TextWatcherDummy.java

  Differing lines: 4



net/gsantner/opoc/ui/FilesystemViewerFragment.java

  Differing lines: 9



net/gsantner/opoc/util/ContextUtils.java

  Differing lines: 1



## Output Format

Provide your answer with file paths only. Sort all the files by suspicion level (highest first). One file path per line. No numbering, no explanations, no additional text, no extra punctuation.



Output: