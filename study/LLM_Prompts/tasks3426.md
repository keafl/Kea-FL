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

test_search_task



## Code Coverage Summary

File: com/todoroo/astrid/activity/MainActivity.kt

  Only in first dataset lines: [147]

    Line 147: hit count 3

----------------------------------------

File: com/todoroo/astrid/activity/MainActivityViewModel.kt

  Only in first dataset lines: [119, 120]

    Line 119: hit count 6

    Line 120: hit count 1

----------------------------------------

File: com/todoroo/astrid/activity/TaskEditFragment.kt

  Only in first dataset lines: [412, 413]

    Line 412: hit count 12

    Line 413: hit count 3

----------------------------------------

File: com/todoroo/astrid/activity/TaskListFragment.kt

  Only in first dataset lines: [256, 257]

    Line 256: hit count 4

    Line 257: hit count 7

  Only in second dataset lines: [253, 254, 263]

    Line 253: hit count 6

    Line 254: hit count 7

    Line 263: hit count 1

----------------------------------------

File: com/todoroo/astrid/api/SearchFilter.kt

  Only in first dataset lines: [16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 52, 53, 54, 55, 56, 57, 58, 61, 66, 73]

    Line 16: hit count 2

    Line 17: hit count 1

    Line 18: hit count 6

    Line 19: hit count 3

    Line 23: hit count 4

    Line 24: hit count 4

    Line 25: hit count 1

    Line 26: hit count 2

    Line 27: hit count 4

    Line 28: hit count 9

    Line 29: hit count 4

    Line 30: hit count 18

    Line 31: hit count 3

    Line 32: hit count 10

    Line 33: hit count 2

    Line 34: hit count 4

    Line 36: hit count 4

    Line 37: hit count 10

    Line 38: hit count 2

    Line 39: hit count 4

    Line 41: hit count 3

    Line 42: hit count 10

    Line 43: hit count 2

    Line 44: hit count 21

    Line 45: hit count 1

    Line 46: hit count 2

    Line 47: hit count 3

    Line 48: hit count 10

    Line 52: hit count 3

    Line 53: hit count 10

    Line 54: hit count 2

    Line 55: hit count 1

    Line 56: hit count 9

    Line 57: hit count 2

    Line 58: hit count 11

    Line 61: hit count 4

    Line 66: hit count 1

    Line 73: hit count 2

----------------------------------------

File: org/tasks/ui/TaskEditViewModel.kt

  Only in first dataset lines: [227, 228, 229, 231, 233, 234, 235, 236, 238, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251]

    Line 227: hit count 10

    Line 228: hit count 10

    Line 229: hit count 12

    Line 231: hit count 1

    Line 233: hit count 9

    Line 234: hit count 7

    Line 235: hit count 10

    Line 236: hit count 12

    Line 238: hit count 1

    Line 240: hit count 9

    Line 241: hit count 9

    Line 242: hit count 7

    Line 243: hit count 7

    Line 244: hit count 11

    Line 245: hit count 3

    Line 246: hit count 12

    Line 247: hit count 8

    Line 248: hit count 2

    Line 249: hit count 4

    Line 250: hit count 4

    Line 251: hit count 2

----------------------------------------

File: org/tasks/ui/TaskListViewModel.kt

  Only in first dataset lines: [149, 207]

    Line 149: hit count 1

    Line 207: hit count 20

----------------------------------------



## Execution Divergence Hint

Common prefix:

Swipe → Input: gbOfw → Pass: test_update_description → Start: test_search_task → Input: Iv → Back → Fail: test_search_task → Random operation: LONG_CLICK → Random operation: CLICK → Start: test_create_tag



FAIL continuation:

Random operation: CLICK → Random operation: SCROLL_BOTTOM_UP → Start: test_delete_task → Pass: test_delete_task → Start: test_search_task → Input: → Back → Pass: test_search_task → Start: test_change_priority → Pass: test_change_priority → Start: test_delete_task → Pass: test_delete_task → Random operation: CLICK → Start: test_delete_task → Start: test_update_description → Swipe → Input: cHnHfj → Pass: test_update_description → Random operation: CLICK → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_BOTTOM_UP → Start: test_update_description → Swipe → Input: arAsQdPNFJ → Pass: test_update_description → Start: test_delete_task → Pass: test_delete_task → Start: test_update_description → Swipe



## Correct Execution Path

Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: SCROLL_BOTTOM_UP → Random operation: CLICK → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Start: test_create_task → Input: q → Pass: test_create_task → Start: test_create_task → Input: jXL → Pass: test_create_task → Start: test_create_task → Input: Iv → Pass: test_create_task → Random operation: LONG_CLICK → Start: test_create_task → Input: Ho → Pass: test_create_task → Start: test_create_task → Input: U → Pass: test_create_task → Random operation: CLICK → Start: test_create_task → Input: Z → Pass: test_create_task → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Random operation: SCROLL_BOTTOM_UP → Random operation: CLICK → Random operation: LONG_CLICK → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Random operation: LONG_CLICK → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: SCROLL_BOTTOM_UP → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_LEFT_RIGHT → Random operation: BACK → Random operation: SCROLL_BOTTOM_UP → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Random operation: SCROLL_BOTTOM_UP → Random operation: SCROLL_RIGHT_LEFT → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Random operation: SCROLL_BOTTOM_UP → Random operation: LONG_CLICK → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Start: test_search_task → Input:   → Back → Pass: test_search_task → Random operation: SCROLL_RIGHT_LEFT → Random operation: CLICK → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_LEFT_RIGHT → Random operation: SCROLL_TOP_DOWN → Random operation: SCROLL_BOTTOM_UP → Random operation: BACK → Start: test_delete_task → Pass: test_delete_task → Start: test_update_description → Swipe → Input: J → Pass: test_update_description → Start: test_update_description → Swipe → Input: Dj → Pass: test_update_description → Start: test_create_task → Input: paR → Pass: test_create_task → Random operation: SCROLL_LEFT_RIGHT → Start: test_update_description → Swipe → Input: gbOfw → Pass: test_update_description → Start: test_search_task → Input: Iv → Back → Fail: test_search_task → Random operation: LONG_CLICK → Random operation: CLICK → Start: test_create_tag



## Error Execution Path

Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: SCROLL_BOTTOM_UP → Random operation: CLICK → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Start: test_create_task → Input: q → Pass: test_create_task → Start: test_create_task → Input: jXL → Pass: test_create_task → Start: test_create_task → Input: Iv → Pass: test_create_task → Random operation: LONG_CLICK → Start: test_create_task → Input: Ho → Pass: test_create_task → Start: test_create_task → Input: U → Pass: test_create_task → Random operation: CLICK → Start: test_create_task → Input: Z → Pass: test_create_task → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Random operation: SCROLL_BOTTOM_UP → Random operation: CLICK → Random operation: LONG_CLICK → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Random operation: LONG_CLICK → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: SCROLL_BOTTOM_UP → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_LEFT_RIGHT → Random operation: BACK → Random operation: SCROLL_BOTTOM_UP → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Random operation: SCROLL_BOTTOM_UP → Random operation: SCROLL_RIGHT_LEFT → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Random operation: SCROLL_BOTTOM_UP → Random operation: LONG_CLICK → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Start: test_search_task → Input:   → Back → Pass: test_search_task → Random operation: SCROLL_RIGHT_LEFT → Random operation: CLICK → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_LEFT_RIGHT → Random operation: SCROLL_TOP_DOWN → Random operation: SCROLL_BOTTOM_UP → Random operation: BACK → Start: test_delete_task → Pass: test_delete_task → Start: test_update_description → Swipe → Input: J → Pass: test_update_description → Start: test_update_description → Swipe → Input: Dj → Pass: test_update_description → Start: test_create_task → Input: paR → Pass: test_create_task → Random operation: SCROLL_LEFT_RIGHT → Start: test_update_description → Swipe → Input: gbOfw → Pass: test_update_description → Start: test_search_task → Input: Iv → Back → Fail: test_search_task → Random operation: LONG_CLICK → Random operation: CLICK → Start: test_create_tag → Random operation: CLICK → Random operation: SCROLL_BOTTOM_UP → Start: test_delete_task → Pass: test_delete_task → Start: test_search_task → Input:   → Back → Pass: test_search_task → Start: test_change_priority → Pass: test_change_priority → Start: test_delete_task → Pass: test_delete_task → Random operation: CLICK → Start: test_delete_task → Start: test_update_description → Swipe → Input: cHnHfj → Pass: test_update_description → Random operation: CLICK → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_BOTTOM_UP → Start: test_update_description → Swipe → Input: arAsQdPNFJ → Pass: test_update_description → Start: test_delete_task → Pass: test_delete_task → Start: test_update_description → Swipe



## Files to Analyze

com/todoroo/astrid/activity/MainActivity.kt

  Differing lines: 1



com/todoroo/astrid/activity/MainActivityViewModel.kt

  Differing lines: 2



com/todoroo/astrid/activity/TaskEditFragment.kt

  Differing lines: 2



com/todoroo/astrid/activity/TaskListFragment.kt

  Differing lines: 5



com/todoroo/astrid/api/SearchFilter.kt

  Differing lines: 38



org/tasks/ui/TaskEditViewModel.kt

  Differing lines: 21



org/tasks/ui/TaskListViewModel.kt

  Differing lines: 2



## Output Format

Provide your answer with file paths only. Sort all the files by suspicion level (highest first). One file path per line. No numbering, no explanations, no additional text, no extra punctuation.



Output: