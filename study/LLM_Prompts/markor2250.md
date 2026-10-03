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

test_create_new_folder



## Code Coverage Summary

File: net/gsantner/markor/activity/MainActivity.java

  Only in first dataset lines: [328, 329, 330, 331]

    Line 328: hit count 3

    Line 329: hit count 9

    Line 330: hit count 12

    Line 331: hit count 1

  Only in second dataset lines: [280, 284, 289, 290, 295, 299, 300, 301, 303, 304, 307, 308, 310, 315, 322, 323, 324, 373, 509]

    Line 280: hit count 7

    Line 284: hit count 5

    Line 289: hit count 4

    Line 290: hit count 9

    Line 295: hit count 5

    Line 299: hit count 8

    Line 300: hit count 3

    Line 301: hit count 3

    Line 303: hit count 3

    Line 304: hit count 5

    Line 307: hit count 1

    Line 308: hit count 5

    Line 310: hit count 1

    Line 315: hit count 3

    Line 322: hit count 5

    Line 323: hit count 5

    Line 324: hit count 1

    Line 373: hit count 5

    Line 509: hit count 14

----------------------------------------

File: net/gsantner/markor/activity/MarkorBaseActivity.java

  Only in second dataset lines: [37]

    Line 37: hit count 5

----------------------------------------

File: net/gsantner/markor/frontend/MarkorDialogFactory.java

  Only in second dataset lines: [984, 985, 986, 994, 999]

    Line 984: hit count 4

    Line 985: hit count 7

    Line 986: hit count 9

    Line 994: hit count 11

    Line 999: hit count 2

----------------------------------------

File: net/gsantner/markor/frontend/NewFileDialog.java

  Only in first dataset lines: [256]

    Line 256: hit count 1

  Only in second dataset lines: [59, 60, 66, 67, 68, 69, 70, 71, 72, 78, 79, 81, 82, 83, 85, 86, 88, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 107, 110, 112, 113, 114, 115, 116, 118, 119, 121, 122, 123, 124, 127, 128, 142, 144, 145, 147, 149, 152, 155, 156, 158, 170, 174, 175, 177, 178, 179, 208, 209, 212, 213, 214, 218, 220, 221, 223, 227, 231, 232, 233, 235, 236, 237, 238, 239, 242, 246, 250, 255, 257, 258]

    Line 59: hit count 3

    Line 60: hit count 4

    Line 66: hit count 4

    Line 67: hit count 4

    Line 68: hit count 4

    Line 69: hit count 5

    Line 70: hit count 3

    Line 71: hit count 3

    Line 72: hit count 2

    Line 78: hit count 6

    Line 79: hit count 5

    Line 81: hit count 4

    Line 82: hit count 6

    Line 83: hit count 3

    Line 85: hit count 5

    Line 86: hit count 4

    Line 88: hit count 2

    Line 95: hit count 2

    Line 96: hit count 7

    Line 97: hit count 5

    Line 99: hit count 5

    Line 100: hit count 5

    Line 101: hit count 5

    Line 102: hit count 5

    Line 103: hit count 5

    Line 104: hit count 5

    Line 105: hit count 5

    Line 107: hit count 6

    Line 110: hit count 3

    Line 112: hit count 4

    Line 113: hit count 7

    Line 114: hit count 4

    Line 115: hit count 3

    Line 116: hit count 10

    Line 118: hit count 9

    Line 119: hit count 4

    Line 121: hit count 4

    Line 122: hit count 5

    Line 123: hit count 14

    Line 124: hit count 4

    Line 127: hit count 4

    Line 128: hit count 1

    Line 142: hit count 4

    Line 144: hit count 7

    Line 145: hit count 2

    Line 147: hit count 4

    Line 149: hit count 4

    Line 152: hit count 3

    Line 155: hit count 4

    Line 156: hit count 1

    Line 158: hit count 5

    Line 170: hit count 4

    Line 174: hit count 4

    Line 175: hit count 3

    Line 177: hit count 6

    Line 178: hit count 5

    Line 179: hit count 15

    Line 208: hit count 10

    Line 209: hit count 4

    Line 212: hit count 9

    Line 213: hit count 6

    Line 214: hit count 7

    Line 218: hit count 11

    Line 220: hit count 2

    Line 221: hit count 1

    Line 223: hit count 2

    Line 227: hit count 2

    Line 231: hit count 4

    Line 232: hit count 8

    Line 233: hit count 8

    Line 235: hit count 6

    Line 236: hit count 12

    Line 237: hit count 3

    Line 238: hit count 3

    Line 239: hit count 1

    Line 242: hit count 6

    Line 246: hit count 3

    Line 250: hit count 3

    Line 255: hit count 6

    Line 257: hit count 1

    Line 258: hit count 1

----------------------------------------

File: net/gsantner/markor/model/AppSettings.java

  Only in second dataset lines: [856, 873, 878, 879, 896, 904, 912]

    Line 856: hit count 7

    Line 873: hit count 8

    Line 878: hit count 3

    Line 879: hit count 4

    Line 896: hit count 7

    Line 904: hit count 7

    Line 912: hit count 7

----------------------------------------

File: net/gsantner/opoc/frontend/base/GsFragmentBase.java

  Only in second dataset lines: [210]

    Line 210: hit count 2

----------------------------------------

File: net/gsantner/opoc/frontend/filebrowser/GsFileBrowserFragment.java

  Only in first dataset lines: [131, 132, 133, 290]

    Line 131: hit count 3

    Line 132: hit count 4

    Line 133: hit count 1

    Line 290: hit count 3

  Only in second dataset lines: [286, 287, 288, 383]

    Line 286: hit count 11

    Line 287: hit count 4

    Line 288: hit count 2

    Line 383: hit count 3

----------------------------------------

File: net/gsantner/opoc/frontend/filebrowser/GsFileBrowserListAdapter.java

  Only in second dataset lines: [326, 422, 423, 424, 429, 430, 485, 486, 487, 488, 489, 490, 498, 546, 547, 550, 551, 552, 554, 555, 557, 561, 565, 566, 570, 574, 576, 584, 585, 587, 590, 591, 592, 596, 597, 598, 599, 601, 603, 608, 609, 610, 611, 719, 759]

    Line 326: hit count 5

    Line 422: hit count 9

    Line 423: hit count 10

    Line 424: hit count 6

    Line 429: hit count 5

    Line 430: hit count 1

    Line 485: hit count 3

    Line 486: hit count 4

    Line 487: hit count 14

    Line 488: hit count 2

    Line 489: hit count 5

    Line 490: hit count 2

    Line 498: hit count 5

    Line 546: hit count 2

    Line 547: hit count 20

    Line 550: hit count 2

    Line 551: hit count 7

    Line 552: hit count 12

    Line 554: hit count 4

    Line 555: hit count 1

    Line 557: hit count 1

    Line 561: hit count 8

    Line 565: hit count 3

    Line 566: hit count 2

    Line 570: hit count 4

    Line 574: hit count 3

    Line 576: hit count 1

    Line 584: hit count 4

    Line 585: hit count 5

    Line 587: hit count 4

    Line 590: hit count 3

    Line 591: hit count 3

    Line 592: hit count 6

    Line 596: hit count 8

    Line 597: hit count 5

    Line 598: hit count 2

    Line 599: hit count 3

    Line 601: hit count 1

    Line 603: hit count 1

    Line 608: hit count 2

    Line 609: hit count 9

    Line 610: hit count 8

    Line 611: hit count 2

    Line 719: hit count 9

    Line 759: hit count 18

----------------------------------------

File: net/gsantner/opoc/util/GsContextUtils.java

  Only in first dataset lines: [2538, 2539, 2540, 2541]

    Line 2538: hit count 10

    Line 2539: hit count 1

    Line 2540: hit count 1

    Line 2541: hit count 1

  Only in second dataset lines: [937, 938, 939, 940, 941, 945, 958, 959, 960, 964, 965, 966, 967, 2882, 2883, 2884, 2886]

    Line 937: hit count 2

    Line 938: hit count 5

    Line 939: hit count 9

    Line 940: hit count 5

    Line 941: hit count 4

    Line 945: hit count 2

    Line 958: hit count 2

    Line 959: hit count 3

    Line 960: hit count 1

    Line 964: hit count 11

    Line 965: hit count 11

    Line 966: hit count 3

    Line 967: hit count 1

    Line 2882: hit count 2

    Line 2883: hit count 3

    Line 2884: hit count 32

    Line 2886: hit count 1

----------------------------------------

File: net/gsantner/opoc/util/GsFileUtils.java

  Only in second dataset lines: [673, 674, 675, 676, 678]

    Line 673: hit count 7

    Line 674: hit count 11

    Line 675: hit count 17

    Line 676: hit count 6

    Line 678: hit count 3

----------------------------------------

File: net/gsantner/opoc/wrapper/GsAndroidSpinnerOnItemSelectedAdapter.java

  Only in second dataset lines: [19, 20, 21, 25, 26]

    Line 19: hit count 2

    Line 20: hit count 3

    Line 21: hit count 1

    Line 25: hit count 5

    Line 26: hit count 1

----------------------------------------

File: other/de/stanetz/jpencconverter/PasswordStore.java

  Only in second dataset lines: [80, 81, 82, 83, 84, 85, 168, 179, 180, 198, 220, 221, 222, 223]

    Line 80: hit count 2

    Line 81: hit count 6

    Line 82: hit count 5

    Line 83: hit count 4

    Line 84: hit count 4

    Line 85: hit count 1

    Line 168: hit count 7

    Line 179: hit count 4

    Line 180: hit count 12

    Line 198: hit count 2

    Line 220: hit count 3

    Line 221: hit count 3

    Line 222: hit count 6

    Line 223: hit count 5

----------------------------------------



## Execution Divergence Hint

Common prefix:

Input: pljc → Back → Pass: test_create_new_folder → Start: test_create_note → Input: BYCj1LA7qW → Back → Pass: test_create_note → Start: test_create_note → Input: D8PvslM → Back



FAIL continuation:

Pass: test_create_note → Random operation: SCROLL_BOTTOM_UP → Start: test_search_note → Input: BYCj1LA7qW → Back → Pass: test_search_note → Start: test_modify_note → Input: y7Fgm2uXy → Back → Pass: test_modify_note → Start: test_create_new_folder → Input: soW9 → Input: bgw2ZoRN0m → Back → Swipe → Fail: test_create_new_folder → Start: test_create_new_folder → Input: Dy1iG5 → Input: uE6KQ → Back → Swipe → Fail: test_create_new_folder → Random operation: LONG_CLICK → Start: test_create_new_folder → Input: VcW_blcMJ → Input: uqi → Back → Swipe



## Correct Execution Path

Random operation: LONG_CLICK → Random operation: CLICK → Random operation: SCROLL_BOTTOM_UP → Random operation: LONG_CLICK → Random operation: CLICK → Random operation: LONG_CLICK → Random operation: CLICK → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Start: test_create_new_folder → Input: X0t → Input: pljc → Back → Pass: test_create_new_folder → Start: test_create_note → Input: BYCj1LA7qW → Back → Pass: test_create_note → Start: test_create_note → Input: D8PvslM → Back



## Error Execution Path

Random operation: LONG_CLICK → Random operation: CLICK → Random operation: SCROLL_BOTTOM_UP → Random operation: LONG_CLICK → Random operation: CLICK → Random operation: LONG_CLICK → Random operation: CLICK → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Start: test_create_new_folder → Input: X0t → Input: pljc → Back → Pass: test_create_new_folder → Start: test_create_note → Input: BYCj1LA7qW → Back → Pass: test_create_note → Start: test_create_note → Input: D8PvslM → Back → Pass: test_create_note → Random operation: SCROLL_BOTTOM_UP → Start: test_search_note → Input: BYCj1LA7qW → Back → Pass: test_search_note → Start: test_modify_note → Input: y7Fgm2uXy → Back → Pass: test_modify_note → Start: test_create_new_folder → Input: soW9 → Input: bgw2ZoRN0m → Back → Swipe → Fail: test_create_new_folder → Start: test_create_new_folder → Input: Dy1iG5 → Input: uE6KQ → Back → Swipe → Fail: test_create_new_folder → Random operation: LONG_CLICK → Start: test_create_new_folder → Input: VcW_blcMJ → Input: uqi → Back → Swipe



## Files to Analyze

net/gsantner/markor/activity/MainActivity.java

  Differing lines: 23



net/gsantner/markor/activity/MarkorBaseActivity.java

  Differing lines: 1



net/gsantner/markor/frontend/MarkorDialogFactory.java

  Differing lines: 5



net/gsantner/markor/frontend/NewFileDialog.java

  Differing lines: 82



net/gsantner/markor/model/AppSettings.java

  Differing lines: 7



net/gsantner/opoc/frontend/base/GsFragmentBase.java

  Differing lines: 1



net/gsantner/opoc/frontend/filebrowser/GsFileBrowserFragment.java

  Differing lines: 8



net/gsantner/opoc/frontend/filebrowser/GsFileBrowserListAdapter.java

  Differing lines: 45



net/gsantner/opoc/util/GsContextUtils.java

  Differing lines: 21



net/gsantner/opoc/util/GsFileUtils.java

  Differing lines: 5



net/gsantner/opoc/wrapper/GsAndroidSpinnerOnItemSelectedAdapter.java

  Differing lines: 5



other/de/stanetz/jpencconverter/PasswordStore.java

  Differing lines: 14



## Output Format

Provide your answer with file paths only. Sort all the files by suspicion level (highest first). One file path per line. No numbering, no explanations, no additional text, no extra punctuation.



Output: