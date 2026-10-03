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

test_rename_file



## Code Coverage Summary

File: net/gsantner/markor/activity/MainActivity.java

  Only in first dataset lines: [338]

    Line 338: hit count 4

  Only in second dataset lines: [179, 180, 184, 332, 333]

    Line 179: hit count 4

    Line 180: hit count 4

    Line 184: hit count 2

    Line 332: hit count 7

    Line 333: hit count 2

----------------------------------------

File: net/gsantner/markor/format/TextFormat.java

  Only in second dataset lines: [71, 74, 75, 76, 77]

    Line 71: hit count 2

    Line 74: hit count 5

    Line 75: hit count 14

    Line 76: hit count 4

    Line 77: hit count 2

----------------------------------------

File: net/gsantner/opoc/ui/FilesystemViewerAdapter.java

  Only in second dataset lines: [266, 267, 268, 270, 381, 382, 398, 401, 406, 407, 408, 411, 415, 417, 419, 420, 422, 430, 431, 432, 458, 460, 461, 462, 463]

    Line 266: hit count 3

    Line 267: hit count 2

    Line 268: hit count 2

    Line 270: hit count 1

    Line 381: hit count 6

    Line 382: hit count 4

    Line 398: hit count 3

    Line 401: hit count 1

    Line 406: hit count 2

    Line 407: hit count 8

    Line 408: hit count 4

    Line 411: hit count 6

    Line 415: hit count 4

    Line 417: hit count 8

    Line 419: hit count 6

    Line 420: hit count 2

    Line 422: hit count 8

    Line 430: hit count 4

    Line 431: hit count 5

    Line 432: hit count 2

    Line 458: hit count 3

    Line 460: hit count 4

    Line 461: hit count 4

    Line 462: hit count 9

    Line 463: hit count 2

----------------------------------------

File: net/gsantner/opoc/ui/FilesystemViewerData.java

  Only in second dataset lines: [140]

    Line 140: hit count 1

----------------------------------------

File: net/gsantner/opoc/ui/FilesystemViewerFragment.java

  Only in second dataset lines: [245, 253, 254, 255, 256, 279, 280, 282, 375, 377, 379, 443, 444, 498, 499, 500, 501, 503, 519, 520, 521, 522, 525]

    Line 245: hit count 12

    Line 253: hit count 5

    Line 254: hit count 5

    Line 255: hit count 5

    Line 256: hit count 1

    Line 279: hit count 3

    Line 280: hit count 5

    Line 282: hit count 1

    Line 375: hit count 6

    Line 377: hit count 2

    Line 379: hit count 3

    Line 443: hit count 6

    Line 444: hit count 1

    Line 498: hit count 4

    Line 499: hit count 10

    Line 500: hit count 8

    Line 501: hit count 5

    Line 503: hit count 2

    Line 519: hit count 2

    Line 520: hit count 5

    Line 521: hit count 7

    Line 522: hit count 2

    Line 525: hit count 2

----------------------------------------

File: net/gsantner/opoc/util/FileUtils.java

  Only in first dataset lines: [197, 201, 202, 205, 214, 215, 217, 221, 222, 314]

    Line 197: hit count 5

    Line 201: hit count 2

    Line 202: hit count 2

    Line 205: hit count 5

    Line 214: hit count 2

    Line 215: hit count 2

    Line 217: hit count 2

    Line 221: hit count 1

    Line 222: hit count 2

    Line 314: hit count 4

  Only in second dataset lines: [300, 305, 313, 321, 326, 534, 535, 536, 537, 542]

    Line 300: hit count 6

    Line 305: hit count 16

    Line 313: hit count 4

    Line 321: hit count 2

    Line 326: hit count 9

    Line 534: hit count 11

    Line 535: hit count 3

    Line 536: hit count 16

    Line 537: hit count 5

    Line 542: hit count 2

----------------------------------------

File: net/gsantner/opoc/util/FileWithCachedData.java

  Only in first dataset lines: [120, 121, 123]

    Line 120: hit count 3

    Line 121: hit count 5

    Line 123: hit count 4

  Only in second dataset lines: [47, 48, 50]

    Line 47: hit count 3

    Line 48: hit count 4

    Line 50: hit count 3

----------------------------------------

File: other/writeily/ui/WrRenameDialog.java

  Only in second dataset lines: [33, 43, 44, 45, 46, 47, 48, 58, 60, 61, 62, 63, 65, 66, 68, 69, 70, 71, 72, 73, 74, 75, 77, 86, 87, 91, 92, 93, 95, 96, 98, 100, 102, 108, 109, 111, 112, 114, 115, 116, 118, 119, 121, 125, 128, 132, 136, 141, 143, 147, 148, 152]

    Line 33: hit count 3

    Line 43: hit count 4

    Line 44: hit count 4

    Line 45: hit count 4

    Line 46: hit count 3

    Line 47: hit count 3

    Line 48: hit count 2

    Line 58: hit count 6

    Line 60: hit count 4

    Line 61: hit count 5

    Line 62: hit count 4

    Line 63: hit count 5

    Line 65: hit count 6

    Line 66: hit count 3

    Line 68: hit count 10

    Line 69: hit count 5

    Line 70: hit count 4

    Line 71: hit count 6

    Line 72: hit count 2

    Line 73: hit count 8

    Line 74: hit count 2

    Line 75: hit count 6

    Line 77: hit count 4

    Line 86: hit count 3

    Line 87: hit count 4

    Line 91: hit count 2

    Line 92: hit count 3

    Line 93: hit count 4

    Line 95: hit count 2

    Line 96: hit count 3

    Line 98: hit count 1

    Line 100: hit count 7

    Line 102: hit count 3

    Line 108: hit count 7

    Line 109: hit count 5

    Line 111: hit count 7

    Line 112: hit count 4

    Line 114: hit count 5

    Line 115: hit count 3

    Line 116: hit count 4

    Line 118: hit count 7

    Line 119: hit count 7

    Line 121: hit count 2

    Line 125: hit count 12

    Line 128: hit count 1

    Line 132: hit count 1

    Line 136: hit count 4

    Line 141: hit count 1

    Line 143: hit count 1

    Line 147: hit count 8

    Line 148: hit count 2

    Line 152: hit count 2

----------------------------------------



## Execution Divergence Hint

Common prefix:

Random operation: LONG_CLICK → Start: test_rename_file → Input: o38.md → Pass: test_rename_file



FAIL continuation:

Random operation: SCROLL_LEFT_RIGHT → Start: test_rename_file → Input: Mh5JneUDi.md → Pass: test_rename_file → Start: test_rename_file → Input: Kxazc3A.md → Pass: test_rename_file → Random operation: CLICK → Start: test_create_note → Input: hLPrjfj5 → Back → Pass: test_create_note → Random operation: LONG_CLICK → Random operation: SCROLL_BOTTOM_UP → Start: test_create_note → Input: __M → Back → Pass: test_create_note → Random operation: CLICK → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Random operation: LONG_CLICK → Start: test_create_note → Input: LNyvbz → Back → Pass: test_create_note → Start: test_modify_note → Input: GzrXLggJh7jSgGmHdGacs → Back → Pass: test_modify_note → Random operation: CLICK → Random operation: LONG_CLICK → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Random operation: SCROLL_BOTTOM_UP → Random operation: SCROLL_RIGHT_LEFT → Random operation: CLICK → Random operation: SCROLL_BOTTOM_UP → Random operation: CLICK → Random operation: BACK → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Start: test_rename_file → Input: yKOwesyC/.md → Fail: test_rename_file → Start: test_rename_file → Input: KQyWr7faFi/.md → Fail: test_rename_file → Random operation: SCROLL_LEFT_RIGHT → Start: test_rename_file → Input: xKlU6EADvl/.md → Fail: test_rename_file → Start: test_rename_file → Input: AtAyl/.md → Fail: test_rename_file → Start: test_rename_file



## Correct Execution Path

Random operation: LONG_CLICK → Start: test_rename_file → Input: o38.md → Pass: test_rename_file



## Error Execution Path

Random operation: LONG_CLICK → Start: test_rename_file → Input: o38.md → Pass: test_rename_file → Random operation: SCROLL_LEFT_RIGHT → Start: test_rename_file → Input: Mh5JneUDi.md → Pass: test_rename_file → Start: test_rename_file → Input: Kxazc3A.md → Pass: test_rename_file → Random operation: CLICK → Start: test_create_note → Input: hLPrjfj5 → Back → Pass: test_create_note → Random operation: LONG_CLICK → Random operation: SCROLL_BOTTOM_UP → Start: test_create_note → Input: __M → Back → Pass: test_create_note → Random operation: CLICK → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Random operation: LONG_CLICK → Start: test_create_note → Input: LNyvbz → Back → Pass: test_create_note → Start: test_modify_note → Input: GzrXLggJh7jSgGmHdGacs → Back → Pass: test_modify_note → Random operation: CLICK → Random operation: LONG_CLICK → Random operation: SCROLL_RIGHT_LEFT → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Random operation: SCROLL_BOTTOM_UP → Random operation: SCROLL_RIGHT_LEFT → Random operation: CLICK → Random operation: SCROLL_BOTTOM_UP → Random operation: CLICK → Random operation: BACK → Random operation: SCROLL_TOP_DOWN → Random operation: CLICK → Random operation: SCROLL_LEFT_RIGHT → Random operation: CLICK → Start: test_rename_file → Input: yKOwesyC/.md → Fail: test_rename_file → Start: test_rename_file → Input: KQyWr7faFi/.md → Fail: test_rename_file → Random operation: SCROLL_LEFT_RIGHT → Start: test_rename_file → Input: xKlU6EADvl/.md → Fail: test_rename_file → Start: test_rename_file → Input: AtAyl/.md → Fail: test_rename_file → Start: test_rename_file



## Files to Analyze

net/gsantner/markor/activity/MainActivity.java

  Differing lines: 6



net/gsantner/markor/format/TextFormat.java

  Differing lines: 5



net/gsantner/opoc/ui/FilesystemViewerAdapter.java

  Differing lines: 25



net/gsantner/opoc/ui/FilesystemViewerData.java

  Differing lines: 1



net/gsantner/opoc/ui/FilesystemViewerFragment.java

  Differing lines: 23



net/gsantner/opoc/util/FileUtils.java

  Differing lines: 20



net/gsantner/opoc/util/FileWithCachedData.java

  Differing lines: 6



other/writeily/ui/WrRenameDialog.java

  Differing lines: 52



## Output Format

Provide your answer with file paths only. Sort all the files by suspicion level (highest first). One file path per line. No numbering, no explanations, no additional text, no extra punctuation.



Output: