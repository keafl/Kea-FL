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

test_change_file_when_creating



## Code Coverage Summary

File: net/gsantner/markor/activity/DocumentEditAndViewFragment.java

  Only in second dataset lines: [247, 248]

    Line 247: hit count 4

    Line 248: hit count 2

----------------------------------------

File: net/gsantner/markor/activity/MainActivity.java

  Only in second dataset lines: [280, 284, 289, 290, 295, 299, 308, 310]

    Line 280: hit count 7

    Line 284: hit count 5

    Line 289: hit count 4

    Line 290: hit count 9

    Line 295: hit count 5

    Line 299: hit count 8

    Line 308: hit count 5

    Line 310: hit count 1

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

  Only in second dataset lines: [59, 60, 66, 67, 68, 69, 70, 71, 72, 78, 79, 81, 82, 83, 85, 86, 88, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 107, 110, 112, 113, 114, 115, 116, 118, 119, 121, 122, 123, 124, 127, 128, 130, 132, 133, 136, 139, 140, 141, 142, 144, 145, 147, 149, 152, 155, 156, 158, 170, 174, 175, 177, 178, 179, 208, 223, 227, 231, 232, 233, 235, 236, 237, 238, 239]

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

    Line 130: hit count 11

    Line 132: hit count 2

    Line 133: hit count 3

    Line 136: hit count 3

    Line 139: hit count 4

    Line 140: hit count 4

    Line 141: hit count 1

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

----------------------------------------

File: net/gsantner/markor/frontend/textview/TextViewUtils.java

  Only in second dataset lines: [822, 828]

    Line 822: hit count 3

    Line 828: hit count 2

----------------------------------------

File: net/gsantner/markor/model/AppSettings.java

  Only in second dataset lines: [856, 873, 878, 879, 896, 904, 912, 916, 917]

    Line 856: hit count 7

    Line 873: hit count 8

    Line 878: hit count 3

    Line 879: hit count 4

    Line 896: hit count 7

    Line 904: hit count 7

    Line 912: hit count 7

    Line 916: hit count 6

    Line 917: hit count 1

----------------------------------------

File: net/gsantner/opoc/frontend/filebrowser/GsFileBrowserFragment.java

  Only in second dataset lines: [383]

    Line 383: hit count 3

----------------------------------------

File: net/gsantner/opoc/frontend/filebrowser/GsFileBrowserListAdapter.java

  Only in second dataset lines: [326]

    Line 326: hit count 5

----------------------------------------

File: net/gsantner/opoc/util/GsContextUtils.java

  Only in second dataset lines: [937, 938, 939, 940, 941, 945, 958, 959, 960, 964, 965, 966, 967]

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

Random operation: SCROLL_BOTTOM_UP → Start: test_change_file_when_creating → Back → Pass: test_change_file_when_creating



FAIL continuation:

Start: test_change_file_when_creating → Back → Pass: test_change_file_when_creating → Start: test_create_note → Input: LQQ_moO86k → Back → Pass: test_create_note → Start: test_modify_note → Input: Pm7hll1ucxpQVSQTfCY76a63jmDyLu → Back → Pass: test_modify_note → Start: test_change_file_when_creating → Back → Fail: test_change_file_when_creating → Start: test_change_file_when_creating → Back



## Correct Execution Path

Random operation: SCROLL_BOTTOM_UP → Start: test_change_file_when_creating → Back → Pass: test_change_file_when_creating



## Error Execution Path

Random operation: SCROLL_BOTTOM_UP → Start: test_change_file_when_creating → Back → Pass: test_change_file_when_creating → Start: test_change_file_when_creating → Back → Pass: test_change_file_when_creating → Start: test_create_note → Input: LQQ_moO86k → Back → Pass: test_create_note → Start: test_modify_note → Input: Pm7hll1ucxpQVSQTfCY76a63jmDyLu → Back → Pass: test_modify_note → Start: test_change_file_when_creating → Back → Fail: test_change_file_when_creating → Start: test_change_file_when_creating → Back



## Files to Analyze

net/gsantner/markor/activity/DocumentEditAndViewFragment.java

  Differing lines: 2



net/gsantner/markor/activity/MainActivity.java

  Differing lines: 8



net/gsantner/markor/frontend/MarkorDialogFactory.java

  Differing lines: 5



net/gsantner/markor/frontend/NewFileDialog.java

  Differing lines: 75



net/gsantner/markor/frontend/textview/TextViewUtils.java

  Differing lines: 2



net/gsantner/markor/model/AppSettings.java

  Differing lines: 9



net/gsantner/opoc/frontend/filebrowser/GsFileBrowserFragment.java

  Differing lines: 1



net/gsantner/opoc/frontend/filebrowser/GsFileBrowserListAdapter.java

  Differing lines: 1



net/gsantner/opoc/util/GsContextUtils.java

  Differing lines: 13



net/gsantner/opoc/util/GsFileUtils.java

  Differing lines: 5



net/gsantner/opoc/wrapper/GsAndroidSpinnerOnItemSelectedAdapter.java

  Differing lines: 5



other/de/stanetz/jpencconverter/PasswordStore.java

  Differing lines: 14



## Output Format

Provide your answer with file paths only. Sort all the files by suspicion level (highest first). One file path per line. No numbering, no explanations, no additional text, no extra punctuation.



Output: