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

File: com/amaze/filemanager/adapters/RecyclerAdapter.java

  Only in second dataset lines: [516, 517, 518, 519, 523, 524, 938, 939, 940, 948, 949, 991]

    Line 516: hit count 3

    Line 517: hit count 4

    Line 518: hit count 5

    Line 519: hit count 3

    Line 523: hit count 3

    Line 524: hit count 1

    Line 938: hit count 4

    Line 939: hit count 4

    Line 940: hit count 5

    Line 948: hit count 4

    Line 949: hit count 9

    Line 991: hit count 9

----------------------------------------

File: com/amaze/filemanager/asynchronous/asynctasks/LoadFilesListTask.java

  Only in second dataset lines: [170, 171, 203, 258, 259, 264, 284, 285, 292, 299, 539, 541, 546, 547, 550, 551, 552, 554, 555, 556, 557, 560, 563, 565, 566, 567, 578, 579, 581, 582, 583, 584, 585, 586, 587, 588, 591, 593, 594]

    Line 170: hit count 4

    Line 171: hit count 1

    Line 203: hit count 7

    Line 258: hit count 4

    Line 259: hit count 6

    Line 264: hit count 4

    Line 284: hit count 3

    Line 285: hit count 1

    Line 292: hit count 6

    Line 299: hit count 2

    Line 539: hit count 5

    Line 541: hit count 2

    Line 546: hit count 5

    Line 547: hit count 11

    Line 550: hit count 2

    Line 551: hit count 8

    Line 552: hit count 3

    Line 554: hit count 3

    Line 555: hit count 4

    Line 556: hit count 4

    Line 557: hit count 9

    Line 560: hit count 4

    Line 563: hit count 1

    Line 565: hit count 2

    Line 566: hit count 6

    Line 567: hit count 1

    Line 578: hit count 2

    Line 579: hit count 6

    Line 581: hit count 6

    Line 582: hit count 5

    Line 583: hit count 12

    Line 584: hit count 6

    Line 585: hit count 2

    Line 586: hit count 2

    Line 587: hit count 4

    Line 588: hit count 6

    Line 591: hit count 3

    Line 593: hit count 2

    Line 594: hit count 2

----------------------------------------

File: com/amaze/filemanager/filesystem/HybridFile.java

  Only in second dataset lines: [188, 259, 267, 1382, 1383, 1384, 1385, 1394]

    Line 188: hit count 4

    Line 259: hit count 6

    Line 267: hit count 6

    Line 1382: hit count 5

    Line 1383: hit count 3

    Line 1384: hit count 3

    Line 1385: hit count 2

    Line 1394: hit count 1

----------------------------------------

File: com/amaze/filemanager/ui/activities/MainActivity.java

  Only in first dataset lines: [985, 992, 993, 994, 995, 996, 997, 999, 1000, 1003, 1337, 1338, 1339, 1340, 1582, 1583, 1585, 1598]

    Line 985: hit count 3

    Line 992: hit count 3

    Line 993: hit count 7

    Line 994: hit count 6

    Line 995: hit count 2

    Line 996: hit count 6

    Line 997: hit count 2

    Line 999: hit count 3

    Line 1000: hit count 1

    Line 1003: hit count 1

    Line 1337: hit count 5

    Line 1338: hit count 5

    Line 1339: hit count 5

    Line 1340: hit count 5

    Line 1582: hit count 5

    Line 1583: hit count 3

    Line 1585: hit count 3

    Line 1598: hit count 1

  Only in second dataset lines: [921, 926, 927, 930, 931, 934, 936, 937, 976, 1446, 1457, 1547]

    Line 921: hit count 8

    Line 926: hit count 3

    Line 927: hit count 5

    Line 930: hit count 3

    Line 931: hit count 4

    Line 934: hit count 4

    Line 936: hit count 2

    Line 937: hit count 2

    Line 976: hit count 1

    Line 1446: hit count 3

    Line 1457: hit count 5

    Line 1547: hit count 3

----------------------------------------

File: com/amaze/filemanager/ui/colors/ColorUtils.java

  Only in second dataset lines: [39, 54, 55, 57, 58, 63, 64, 69]

    Line 39: hit count 2

    Line 54: hit count 5

    Line 55: hit count 1

    Line 57: hit count 5

    Line 58: hit count 1

    Line 63: hit count 5

    Line 64: hit count 1

    Line 69: hit count 1

----------------------------------------

File: com/amaze/filemanager/ui/fragments/MainFragment.java

  Only in first dataset lines: [256, 1145]

    Line 256: hit count 3

    Line 1145: hit count 4

  Only in second dataset lines: [1086, 1088, 1089, 1090, 1553, 1554]

    Line 1086: hit count 5

    Line 1088: hit count 8

    Line 1089: hit count 3

    Line 1090: hit count 1

    Line 1553: hit count 3

    Line 1554: hit count 1

----------------------------------------

File: com/amaze/filemanager/ui/fragments/TabFragment.java

  Only in second dataset lines: [223, 226, 227]

    Line 223: hit count 6

    Line 226: hit count 3

    Line 227: hit count 3

----------------------------------------

File: com/amaze/filemanager/ui/views/FastScroller.java

  Only in second dataset lines: [237, 238]

    Line 237: hit count 3

    Line 238: hit count 1

----------------------------------------

File: com/amaze/filemanager/ui/views/appbar/BottomBar.java

  Only in second dataset lines: [385, 386, 513, 514, 515, 516, 517, 520, 521, 522, 523, 525, 526, 530, 533, 534, 535, 537, 538, 539, 540, 543, 544, 545, 547, 548, 549, 551, 555, 557, 558, 559, 560, 562, 563, 571, 572]

    Line 385: hit count 5

    Line 386: hit count 1

    Line 513: hit count 4

    Line 514: hit count 2

    Line 515: hit count 7

    Line 516: hit count 2

    Line 517: hit count 12

    Line 520: hit count 3

    Line 521: hit count 5

    Line 522: hit count 6

    Line 523: hit count 5

    Line 525: hit count 14

    Line 526: hit count 1

    Line 530: hit count 3

    Line 533: hit count 7

    Line 534: hit count 5

    Line 535: hit count 6

    Line 537: hit count 3

    Line 538: hit count 5

    Line 539: hit count 1

    Line 540: hit count 6

    Line 543: hit count 3

    Line 544: hit count 6

    Line 545: hit count 2

    Line 547: hit count 6

    Line 548: hit count 9

    Line 549: hit count 1

    Line 551: hit count 1

    Line 555: hit count 3

    Line 557: hit count 6

    Line 558: hit count 6

    Line 559: hit count 16

    Line 560: hit count 1

    Line 562: hit count 1

    Line 563: hit count 1

    Line 571: hit count 1

    Line 572: hit count 1

----------------------------------------

File: com/amaze/filemanager/ui/views/appbar/SearchView.java

  Only in second dataset lines: [582]

    Line 582: hit count 4

----------------------------------------

File: com/amaze/filemanager/ui/views/drawer/CustomNavigationView.java

  Only in second dataset lines: [56, 57, 59, 60, 63, 71, 72]

    Line 56: hit count 3

    Line 57: hit count 5

    Line 59: hit count 2

    Line 60: hit count 3

    Line 63: hit count 2

    Line 71: hit count 4

    Line 72: hit count 1

----------------------------------------

File: com/amaze/filemanager/ui/views/drawer/Drawer.java

  Only in second dataset lines: [749, 750, 752, 755, 763, 781, 782, 783, 789, 790, 791, 793, 794, 806, 807, 809, 810, 811, 813, 815, 819, 828, 829, 830, 850, 851, 852, 863, 955, 956]

    Line 749: hit count 3

    Line 750: hit count 2

    Line 752: hit count 1

    Line 755: hit count 3

    Line 763: hit count 6

    Line 781: hit count 8

    Line 782: hit count 4

    Line 783: hit count 3

    Line 789: hit count 4

    Line 790: hit count 2

    Line 791: hit count 8

    Line 793: hit count 5

    Line 794: hit count 3

    Line 806: hit count 3

    Line 807: hit count 4

    Line 809: hit count 9

    Line 810: hit count 4

    Line 811: hit count 4

    Line 813: hit count 3

    Line 815: hit count 16

    Line 819: hit count 5

    Line 828: hit count 6

    Line 829: hit count 5

    Line 830: hit count 2

    Line 850: hit count 9

    Line 851: hit count 2

    Line 852: hit count 3

    Line 863: hit count 2

    Line 955: hit count 3

    Line 956: hit count 1

----------------------------------------

File: com/amaze/filemanager/utils/DataUtils.java

  Only in second dataset lines: [109, 174, 175, 176, 177, 178, 179, 180, 328]

    Line 109: hit count 6

    Line 174: hit count 2

    Line 175: hit count 2

    Line 176: hit count 10

    Line 177: hit count 8

    Line 178: hit count 1

    Line 179: hit count 1

    Line 180: hit count 2

    Line 328: hit count 3

----------------------------------------

File: com/amaze/filemanager/utils/MainActivityHelper.java

  Only in first dataset lines: [328, 330, 331, 332]

    Line 328: hit count 5

    Line 330: hit count 8

    Line 331: hit count 6

    Line 332: hit count 1

  Only in second dataset lines: [263, 264, 284, 285, 290]

    Line 263: hit count 2

    Line 264: hit count 3

    Line 284: hit count 5

    Line 285: hit count 1

    Line 290: hit count 2

----------------------------------------



## Execution Divergence Hint

Common prefix:

Start: test_modify_file → Input: A.txt → Input: Sojdwf6ondER4aP_uEdYKaDkxkEmtG → Back → Input: A.txt → Back → Pass: test_modify_file → Start: test_check_recent_file → Back → Pass: test_check_recent_file



FAIL continuation:

Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: SCROLL_BOTTOM_UP → Random operation: SCROLL_RIGHT_LEFT → Random operation: CLICK → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Random operation: SCROLL_BOTTOM_UP → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Start: test_create_folder → Input: test_dO → Swipe → Pass: test_create_folder → Start: test_modify_file → Input: A.txt → Input: CvxLDAU4xSrVEOnA8hmM6QE4IoZS1_ → Back → Input: A.txt → Back → Pass: test_modify_file → Start: test_check_recent_file → Back → Pass: test_check_recent_file → Start: test_modify_file → Input: A.txt → Input: Q0Jzvjflg3LSdNIAIPrFMfcIIJe88B → Back → Input: A.txt → Back → Pass: test_modify_file → Start: test_check_recent_file → Back → Pass: test_check_recent_file → Start: test_delete_file → Swipe → Back → Swipe → Back → Pass: test_delete_file → Start: test_create_file → Input: fo5Yp.txt → Pass: test_create_file → Start: test_check_recent_file → Swipe → Back → Fail: test_check_recent_file → Random operation: CLICK → Start: test_create_file → Input: ijk9e.txt → Pass: test_create_file → Start: test_check_recent_file → Swipe → Back → Fail: test_check_recent_file → Random operation: SCROLL_BOTTOM_UP → Random operation: SCROLL_TOP_DOWN → Random operation: LONG_CLICK → Random operation: CLICK → Random operation: LONG_CLICK → Random operation: CLICK → Start: test_create_file → Input: kA1.txt → Pass: test_create_file → Start: test_check_recent_file → Swipe → Back → Fail: test_check_recent_file → Start: test_modify_file → Input: A.txt → Input: HUYWJ55 → Back



## Correct Execution Path

Random operation: SCROLL_RIGHT_LEFT → Random operation: CLICK → Start: test_modify_file → Input: A.txt → Input: Sojdwf6ondER4aP_uEdYKaDkxkEmtG → Back → Input: A.txt → Back → Pass: test_modify_file → Start: test_check_recent_file → Back → Pass: test_check_recent_file



## Error Execution Path

Random operation: SCROLL_RIGHT_LEFT → Random operation: CLICK → Start: test_modify_file → Input: A.txt → Input: Sojdwf6ondER4aP_uEdYKaDkxkEmtG → Back → Input: A.txt → Back → Pass: test_modify_file → Start: test_check_recent_file → Back → Pass: test_check_recent_file → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: SCROLL_BOTTOM_UP → Random operation: SCROLL_RIGHT_LEFT → Random operation: CLICK → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Random operation: SCROLL_BOTTOM_UP → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Start: test_create_folder → Input: test_dO → Swipe → Pass: test_create_folder → Start: test_modify_file → Input: A.txt → Input: CvxLDAU4xSrVEOnA8hmM6QE4IoZS1_ → Back → Input: A.txt → Back → Pass: test_modify_file → Start: test_check_recent_file → Back → Pass: test_check_recent_file → Start: test_modify_file → Input: A.txt → Input: Q0Jzvjflg3LSdNIAIPrFMfcIIJe88B → Back → Input: A.txt → Back → Pass: test_modify_file → Start: test_check_recent_file → Back → Pass: test_check_recent_file → Start: test_delete_file → Swipe → Back → Swipe → Back → Pass: test_delete_file → Start: test_create_file → Input: fo5Yp.txt → Pass: test_create_file → Start: test_check_recent_file → Swipe → Back → Fail: test_check_recent_file → Random operation: CLICK → Start: test_create_file → Input: ijk9e.txt → Pass: test_create_file → Start: test_check_recent_file → Swipe → Back → Fail: test_check_recent_file → Random operation: SCROLL_BOTTOM_UP → Random operation: SCROLL_TOP_DOWN → Random operation: LONG_CLICK → Random operation: CLICK → Random operation: LONG_CLICK → Random operation: CLICK → Start: test_create_file → Input: kA1.txt → Pass: test_create_file → Start: test_check_recent_file → Swipe → Back → Fail: test_check_recent_file → Start: test_modify_file → Input: A.txt → Input: HUYWJ55 → Back



## Files to Analyze

com/amaze/filemanager/adapters/RecyclerAdapter.java

  Differing lines: 12



com/amaze/filemanager/asynchronous/asynctasks/LoadFilesListTask.java

  Differing lines: 39



com/amaze/filemanager/filesystem/HybridFile.java

  Differing lines: 8



com/amaze/filemanager/ui/activities/MainActivity.java

  Differing lines: 30



com/amaze/filemanager/ui/colors/ColorUtils.java

  Differing lines: 8



com/amaze/filemanager/ui/fragments/MainFragment.java

  Differing lines: 8



com/amaze/filemanager/ui/fragments/TabFragment.java

  Differing lines: 3



com/amaze/filemanager/ui/views/FastScroller.java

  Differing lines: 2



com/amaze/filemanager/ui/views/appbar/BottomBar.java

  Differing lines: 37



com/amaze/filemanager/ui/views/appbar/SearchView.java

  Differing lines: 1



com/amaze/filemanager/ui/views/drawer/CustomNavigationView.java

  Differing lines: 7



com/amaze/filemanager/ui/views/drawer/Drawer.java

  Differing lines: 30



com/amaze/filemanager/utils/DataUtils.java

  Differing lines: 9



com/amaze/filemanager/utils/MainActivityHelper.java

  Differing lines: 9



## Output Format

Provide your answer with file paths only. Sort all the files by suspicion level (highest first). One file path per line. No numbering, no explanations, no additional text, no extra punctuation.



Output: