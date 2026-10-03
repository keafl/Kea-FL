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

test_search_does_not_show_archived_notes



## Code Coverage Summary

File: it/feio/android/omninotes/ListFragment.java

  Only in first dataset lines: [1456, 1457, 1458, 1460, 1461, 1690, 1691, 1693, 1694, 1699, 1700, 1701, 1702, 1705, 1706, 1707, 1708, 1710, 1711, 1713]

    Line 1456: hit count 6

    Line 1457: hit count 3

    Line 1458: hit count 4

    Line 1460: hit count 12

    Line 1461: hit count 1

    Line 1690: hit count 7

    Line 1691: hit count 3

    Line 1693: hit count 3

    Line 1694: hit count 6

    Line 1699: hit count 3

    Line 1700: hit count 3

    Line 1701: hit count 3

    Line 1702: hit count 3

    Line 1705: hit count 3

    Line 1706: hit count 3

    Line 1707: hit count 3

    Line 1708: hit count 3

    Line 1710: hit count 4

    Line 1711: hit count 3

    Line 1713: hit count 2

  Only in second dataset lines: [679, 689, 690, 693, 694, 695, 696, 703, 714, 722, 723, 727, 847]

    Line 679: hit count 5

    Line 689: hit count 4

    Line 690: hit count 6

    Line 693: hit count 7

    Line 694: hit count 7

    Line 695: hit count 4

    Line 696: hit count 2

    Line 703: hit count 14

    Line 714: hit count 4

    Line 722: hit count 4

    Line 723: hit count 2

    Line 727: hit count 2

    Line 847: hit count 1

----------------------------------------

File: it/feio/android/omninotes/MainActivity.java

  Only in first dataset lines: [142]

    Line 142: hit count 3

----------------------------------------

File: it/feio/android/omninotes/async/notes/NoteProcessor.java

  Only in first dataset lines: [33, 34, 35, 39, 40, 41, 47, 51, 52, 53, 54, 55, 61, 62, 67, 68]

    Line 33: hit count 2

    Line 34: hit count 6

    Line 35: hit count 1

    Line 39: hit count 5

    Line 40: hit count 11

    Line 41: hit count 1

    Line 47: hit count 6

    Line 51: hit count 4

    Line 52: hit count 10

    Line 53: hit count 4

    Line 54: hit count 1

    Line 55: hit count 2

    Line 61: hit count 4

    Line 62: hit count 1

    Line 67: hit count 6

    Line 68: hit count 1

----------------------------------------

File: it/feio/android/omninotes/async/notes/NoteProcessorArchive.java

  Only in first dataset lines: [31, 32, 33, 38, 39]

    Line 31: hit count 3

    Line 32: hit count 3

    Line 33: hit count 1

    Line 38: hit count 5

    Line 39: hit count 1

----------------------------------------

File: it/feio/android/omninotes/db/DbHelper.java

  Only in first dataset lines: [231, 501, 502, 503]

    Line 231: hit count 4

    Line 501: hit count 4

    Line 502: hit count 5

    Line 503: hit count 1

----------------------------------------

File: it/feio/android/omninotes/models/NavigationItem.java

  Only in first dataset lines: [58]

    Line 58: hit count 3

----------------------------------------

File: it/feio/android/omninotes/models/adapters/NavDrawerAdapter.java

  Only in first dataset lines: [95, 96, 97]

    Line 95: hit count 9

    Line 96: hit count 5

    Line 97: hit count 8

----------------------------------------

File: it/feio/android/omninotes/models/adapters/NoteAdapter.java

  Only in first dataset lines: [275, 276, 277, 278]

    Line 275: hit count 10

    Line 276: hit count 3

    Line 277: hit count 1

    Line 278: hit count 1

----------------------------------------

File: it/feio/android/omninotes/models/misc/DynamicNavigationLookupTable.java

  Only in first dataset lines: [61]

    Line 61: hit count 7

----------------------------------------



## Execution Divergence Hint

Common prefix:

Random operation: CLICK → Random operation: SCROLL_LEFT_RIGHT → Random operation: SCROLL_BOTTOM_UP → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes



FAIL continuation:

Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: SCROLL_BOTTOM_UP → Random operation: CLICK → Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes → Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes → Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes → Start: test_create_note_for_archive → Input: PK1NFn → Back → Pass: test_create_note_for_archive → Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes → Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes → Start: test_behavior_setting → Back → Pass: test_behavior_setting → Start: test_data_setting → Back → Pass: test_data_setting → Start: test_create_note_for_archive → Input: ybRO77I → Back → Pass: test_create_note_for_archive → Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes → Start: test_create_note_for_archive → Input: tkRMFlCd → Back → Pass: test_create_note_for_archive → Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes → Start: test_reduced_view → Pass: test_reduced_view → Random operation: LONG_CLICK → Start: test_archive_note_removes_from_main_list → Pass: test_archive_note_removes_from_main_list → Start: test_search_does_not_show_archived_notes → Fail: test_search_does_not_show_archived_notes → Start: test_reduced_view → Pass: test_reduced_view → Start: test_search_does_not_show_archived_notes → Fail: test_search_does_not_show_archived_notes → Start: test_reduced_view



## Correct Execution Path

Random operation: CLICK → Random operation: SCROLL_LEFT_RIGHT → Random operation: SCROLL_BOTTOM_UP → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes



## Error Execution Path

Random operation: CLICK → Random operation: SCROLL_LEFT_RIGHT → Random operation: SCROLL_BOTTOM_UP → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes → Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: SCROLL_BOTTOM_UP → Random operation: CLICK → Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes → Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes → Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes → Start: test_create_note_for_archive → Input: PK1NFn → Back → Pass: test_create_note_for_archive → Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes → Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes → Start: test_behavior_setting → Back → Pass: test_behavior_setting → Start: test_data_setting → Back → Pass: test_data_setting → Start: test_create_note_for_archive → Input: ybRO77I → Back → Pass: test_create_note_for_archive → Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes → Start: test_create_note_for_archive → Input: tkRMFlCd → Back → Pass: test_create_note_for_archive → Start: test_search_does_not_show_archived_notes → Pass: test_search_does_not_show_archived_notes → Start: test_reduced_view → Pass: test_reduced_view → Random operation: LONG_CLICK → Start: test_archive_note_removes_from_main_list → Pass: test_archive_note_removes_from_main_list → Start: test_search_does_not_show_archived_notes → Fail: test_search_does_not_show_archived_notes → Start: test_reduced_view → Pass: test_reduced_view → Start: test_search_does_not_show_archived_notes → Fail: test_search_does_not_show_archived_notes → Start: test_reduced_view



## Files to Analyze

it/feio/android/omninotes/ListFragment.java

  Differing lines: 33



it/feio/android/omninotes/MainActivity.java

  Differing lines: 1



it/feio/android/omninotes/async/notes/NoteProcessor.java

  Differing lines: 16



it/feio/android/omninotes/async/notes/NoteProcessorArchive.java

  Differing lines: 5



it/feio/android/omninotes/db/DbHelper.java

  Differing lines: 4



it/feio/android/omninotes/models/NavigationItem.java

  Differing lines: 1



it/feio/android/omninotes/models/adapters/NavDrawerAdapter.java

  Differing lines: 3



it/feio/android/omninotes/models/adapters/NoteAdapter.java

  Differing lines: 4



it/feio/android/omninotes/models/misc/DynamicNavigationLookupTable.java

  Differing lines: 1



## Output Format

Provide your answer with file paths only. Sort all the files by suspicion level (highest first). One file path per line. No numbering, no explanations, no additional text, no extra punctuation.



Output: