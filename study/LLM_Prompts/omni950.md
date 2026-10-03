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

test_create_empty_category



## Code Coverage Summary

File: it/feio/android/omninotes/BaseActivity.java

  Only in second dataset lines: [140, 141, 144, 148, 173]

    Line 140: hit count 3

    Line 141: hit count 7

    Line 144: hit count 2

    Line 148: hit count 1

    Line 173: hit count 11

----------------------------------------

File: it/feio/android/omninotes/CategoryActivity.java

  Only in second dataset lines: [50, 60, 62, 63, 64, 66, 68, 70, 71, 72, 73, 77, 78, 79, 80, 89, 90, 91, 92, 93, 94, 95, 98, 99, 127, 128, 130, 131, 132, 133, 135, 136, 138, 139, 140, 141, 145, 151, 152, 153, 154, 155, 156, 160, 161, 164, 165, 166, 167]

    Line 50: hit count 3

    Line 60: hit count 3

    Line 62: hit count 5

    Line 63: hit count 4

    Line 64: hit count 3

    Line 66: hit count 3

    Line 68: hit count 6

    Line 70: hit count 3

    Line 71: hit count 2

    Line 72: hit count 5

    Line 73: hit count 7

    Line 77: hit count 6

    Line 78: hit count 2

    Line 79: hit count 2

    Line 80: hit count 1

    Line 89: hit count 3

    Line 90: hit count 3

    Line 91: hit count 3

    Line 92: hit count 8

    Line 93: hit count 3

    Line 94: hit count 3

    Line 95: hit count 1

    Line 98: hit count 5

    Line 99: hit count 6

    Line 127: hit count 7

    Line 128: hit count 7

    Line 130: hit count 4

    Line 131: hit count 5

    Line 132: hit count 6

    Line 133: hit count 3

    Line 135: hit count 3

    Line 136: hit count 8

    Line 138: hit count 9

    Line 139: hit count 6

    Line 140: hit count 6

    Line 141: hit count 1

    Line 145: hit count 7

    Line 151: hit count 11

    Line 152: hit count 4

    Line 153: hit count 8

    Line 154: hit count 8

    Line 155: hit count 3

    Line 156: hit count 6

    Line 160: hit count 2

    Line 161: hit count 6

    Line 164: hit count 7

    Line 165: hit count 5

    Line 166: hit count 2

    Line 167: hit count 1

----------------------------------------

File: it/feio/android/omninotes/DetailFragment.java

  Only in second dataset lines: [193, 208, 219, 220, 221, 222, 227, 230, 231, 239, 245, 281, 282, 283, 287, 288, 289, 293, 294, 295, 299, 300, 301, 302, 306, 307, 312, 314, 316, 317, 320, 323, 326, 328, 331, 332, 334, 335, 336, 339, 349, 352, 359, 377, 380, 382, 385, 386, 389, 390, 391, 393, 406, 408, 409, 412, 413, 416, 417, 420, 425, 426, 460, 462, 472, 486, 514, 519, 520, 551, 552, 554, 557, 558, 596, 599, 601, 603, 605, 607, 609, 611, 612, 615, 616, 617, 618, 619, 620, 623, 624, 626, 627, 628, 629, 630, 632, 635, 641, 657, 658, 663, 667, 669, 680, 684, 695, 708, 719, 722, 724, 727, 730, 731, 734, 790, 810, 857, 858, 859, 861, 863, 869, 870, 873, 874, 875, 877, 880, 881, 886, 894, 895, 897, 904, 907, 910, 911, 915, 919, 920, 921, 922, 924, 925, 926, 929, 993, 994, 995, 1001, 1002, 1003, 1006, 1008, 1009, 1010, 1011, 1012, 1013, 1015, 1021, 1022, 1023, 1024, 1025, 1027, 1031, 1035, 1043, 1044, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1056, 1061, 1067, 1071, 1079, 1080, 1125, 1228, 1229, 1230, 1231, 1239, 1241, 1242, 1243, 1244, 1245, 1246, 1247, 1248, 1249, 1250, 1251, 1252, 1257, 1261, 1263, 1272, 1273, 1403, 1404, 1431, 1432, 1433, 1434, 1435, 1443, 1541, 1542, 1543, 1544, 1545, 1547, 1555, 1556, 1559, 1560, 1561, 1562, 1563, 1564, 1565, 1568, 1569, 1570, 1573, 1586, 1590, 1633, 1636, 1641, 1642, 1645, 1646, 1647, 1651, 1657, 1713, 1714, 1785, 1795, 2172, 2175]

    Line 193: hit count 2

    Line 208: hit count 3

    Line 219: hit count 3

    Line 220: hit count 3

    Line 221: hit count 3

    Line 222: hit count 3

    Line 227: hit count 3

    Line 230: hit count 3

    Line 231: hit count 3

    Line 239: hit count 3

    Line 245: hit count 5

    Line 281: hit count 3

    Line 282: hit count 3

    Line 283: hit count 1

    Line 287: hit count 3

    Line 288: hit count 6

    Line 289: hit count 1

    Line 293: hit count 2

    Line 294: hit count 1

    Line 295: hit count 1

    Line 299: hit count 2

    Line 300: hit count 3

    Line 301: hit count 3

    Line 302: hit count 1

    Line 306: hit count 6

    Line 307: hit count 4

    Line 312: hit count 3

    Line 314: hit count 5

    Line 316: hit count 5

    Line 317: hit count 6

    Line 320: hit count 2

    Line 323: hit count 5

    Line 326: hit count 3

    Line 328: hit count 2

    Line 331: hit count 6

    Line 332: hit count 2

    Line 334: hit count 3

    Line 335: hit count 3

    Line 336: hit count 1

    Line 339: hit count 4

    Line 349: hit count 1

    Line 352: hit count 2

    Line 359: hit count 1

    Line 377: hit count 2

    Line 380: hit count 3

    Line 382: hit count 3

    Line 385: hit count 3

    Line 386: hit count 3

    Line 389: hit count 3

    Line 390: hit count 3

    Line 391: hit count 4

    Line 393: hit count 1

    Line 406: hit count 2

    Line 408: hit count 3

    Line 409: hit count 7

    Line 412: hit count 3

    Line 413: hit count 7

    Line 416: hit count 3

    Line 417: hit count 7

    Line 420: hit count 6

    Line 425: hit count 2

    Line 426: hit count 1

    Line 460: hit count 4

    Line 462: hit count 4

    Line 472: hit count 13

    Line 486: hit count 13

    Line 514: hit count 4

    Line 519: hit count 19

    Line 520: hit count 2

    Line 551: hit count 19

    Line 552: hit count 2

    Line 554: hit count 3

    Line 557: hit count 4

    Line 558: hit count 1

    Line 596: hit count 5

    Line 599: hit count 5

    Line 601: hit count 2

    Line 603: hit count 2

    Line 605: hit count 2

    Line 607: hit count 2

    Line 609: hit count 2

    Line 611: hit count 2

    Line 612: hit count 1

    Line 615: hit count 2

    Line 616: hit count 6

    Line 617: hit count 3

    Line 618: hit count 5

    Line 619: hit count 6

    Line 620: hit count 5

    Line 623: hit count 2

    Line 624: hit count 6

    Line 626: hit count 3

    Line 627: hit count 4

    Line 628: hit count 1

    Line 629: hit count 6

    Line 630: hit count 5

    Line 632: hit count 1

    Line 635: hit count 7

    Line 641: hit count 7

    Line 657: hit count 5

    Line 658: hit count 3

    Line 663: hit count 1

    Line 667: hit count 2

    Line 669: hit count 3

    Line 680: hit count 4

    Line 684: hit count 7

    Line 695: hit count 7

    Line 708: hit count 1

    Line 719: hit count 4

    Line 722: hit count 5

    Line 724: hit count 8

    Line 727: hit count 10

    Line 730: hit count 5

    Line 731: hit count 3

    Line 734: hit count 5

    Line 790: hit count 5

    Line 810: hit count 1

    Line 857: hit count 7

    Line 858: hit count 4

    Line 859: hit count 6

    Line 861: hit count 5

    Line 863: hit count 6

    Line 869: hit count 5

    Line 870: hit count 1

    Line 873: hit count 8

    Line 874: hit count 5

    Line 875: hit count 7

    Line 877: hit count 6

    Line 880: hit count 6

    Line 881: hit count 5

    Line 886: hit count 1

    Line 894: hit count 13

    Line 895: hit count 2

    Line 897: hit count 1

    Line 904: hit count 4

    Line 907: hit count 4

    Line 910: hit count 4

    Line 911: hit count 4

    Line 915: hit count 6

    Line 919: hit count 5

    Line 920: hit count 10

    Line 921: hit count 5

    Line 922: hit count 2

    Line 924: hit count 10

    Line 925: hit count 4

    Line 926: hit count 1

    Line 929: hit count 1

    Line 993: hit count 4

    Line 994: hit count 4

    Line 995: hit count 1

    Line 1001: hit count 4

    Line 1002: hit count 2

    Line 1003: hit count 3

    Line 1006: hit count 7

    Line 1008: hit count 12

    Line 1009: hit count 9

    Line 1010: hit count 5

    Line 1011: hit count 6

    Line 1012: hit count 12

    Line 1013: hit count 9

    Line 1015: hit count 5

    Line 1021: hit count 8

    Line 1022: hit count 8

    Line 1023: hit count 8

    Line 1024: hit count 8

    Line 1025: hit count 8

    Line 1027: hit count 1

    Line 1031: hit count 2

    Line 1035: hit count 3

    Line 1043: hit count 7

    Line 1044: hit count 7

    Line 1048: hit count 3

    Line 1049: hit count 4

    Line 1050: hit count 4

    Line 1051: hit count 6

    Line 1052: hit count 5

    Line 1053: hit count 4

    Line 1054: hit count 5

    Line 1056: hit count 6

    Line 1061: hit count 2

    Line 1067: hit count 3

    Line 1071: hit count 3

    Line 1079: hit count 2

    Line 1080: hit count 1

    Line 1125: hit count 4

    Line 1228: hit count 6

    Line 1229: hit count 6

    Line 1230: hit count 6

    Line 1231: hit count 1

    Line 1239: hit count 5

    Line 1241: hit count 6

    Line 1242: hit count 2

    Line 1243: hit count 2

    Line 1244: hit count 2

    Line 1245: hit count 2

    Line 1246: hit count 3

    Line 1247: hit count 3

    Line 1248: hit count 7

    Line 1249: hit count 5

    Line 1250: hit count 4

    Line 1251: hit count 1

    Line 1252: hit count 2

    Line 1257: hit count 3

    Line 1261: hit count 3

    Line 1263: hit count 3

    Line 1272: hit count 2

    Line 1273: hit count 1

    Line 1403: hit count 3

    Line 1404: hit count 2

    Line 1431: hit count 5

    Line 1432: hit count 5

    Line 1433: hit count 4

    Line 1434: hit count 3

    Line 1435: hit count 1

    Line 1443: hit count 1

    Line 1541: hit count 3

    Line 1542: hit count 5

    Line 1543: hit count 3

    Line 1544: hit count 3

    Line 1545: hit count 3

    Line 1547: hit count 1

    Line 1555: hit count 5

    Line 1556: hit count 5

    Line 1559: hit count 15

    Line 1560: hit count 3

    Line 1561: hit count 2

    Line 1562: hit count 5

    Line 1563: hit count 3

    Line 1564: hit count 3

    Line 1565: hit count 1

    Line 1568: hit count 3

    Line 1569: hit count 3

    Line 1570: hit count 3

    Line 1573: hit count 1

    Line 1586: hit count 8

    Line 1590: hit count 9

    Line 1633: hit count 6

    Line 1636: hit count 2

    Line 1641: hit count 2

    Line 1642: hit count 6

    Line 1645: hit count 6

    Line 1646: hit count 3

    Line 1647: hit count 6

    Line 1651: hit count 1

    Line 1657: hit count 2

    Line 1713: hit count 4

    Line 1714: hit count 2

    Line 1785: hit count 3

    Line 1795: hit count 1

    Line 2172: hit count 5

    Line 2175: hit count 1

----------------------------------------

File: it/feio/android/omninotes/ListFragment.java

  Only in second dataset lines: [264, 265, 278, 280, 286, 287, 336, 343, 348, 349, 350, 351, 352, 353, 354, 355, 359, 374, 375, 376, 377, 378, 379, 381, 459, 462, 523, 524, 527, 530, 531, 532, 534, 535, 536, 537, 539, 547, 550, 551, 921, 930, 931, 933, 937, 938, 941, 948, 954, 957, 958]

    Line 264: hit count 5

    Line 265: hit count 2

    Line 278: hit count 6

    Line 280: hit count 1

    Line 286: hit count 3

    Line 287: hit count 2

    Line 336: hit count 3

    Line 343: hit count 1

    Line 348: hit count 2

    Line 349: hit count 4

    Line 350: hit count 2

    Line 351: hit count 1

    Line 352: hit count 3

    Line 353: hit count 3

    Line 354: hit count 2

    Line 355: hit count 3

    Line 359: hit count 1

    Line 374: hit count 3

    Line 375: hit count 6

    Line 376: hit count 2

    Line 377: hit count 6

    Line 378: hit count 1

    Line 379: hit count 9

    Line 381: hit count 1

    Line 459: hit count 3

    Line 462: hit count 1

    Line 523: hit count 2

    Line 524: hit count 4

    Line 527: hit count 5

    Line 530: hit count 2

    Line 531: hit count 6

    Line 532: hit count 3

    Line 534: hit count 3

    Line 535: hit count 2

    Line 536: hit count 3

    Line 537: hit count 6

    Line 539: hit count 4

    Line 547: hit count 15

    Line 550: hit count 5

    Line 551: hit count 1

    Line 921: hit count 4

    Line 930: hit count 13

    Line 931: hit count 1

    Line 933: hit count 1

    Line 937: hit count 3

    Line 938: hit count 2

    Line 941: hit count 8

    Line 948: hit count 1

    Line 954: hit count 2

    Line 957: hit count 4

    Line 958: hit count 1

----------------------------------------

File: it/feio/android/omninotes/MainActivity.java

  Only in second dataset lines: [94, 142, 277, 278, 279, 281, 288, 289, 290, 291, 293, 300, 301, 313, 314, 315, 316, 317, 321, 322, 324, 327, 329, 330, 337, 352, 353, 354, 363, 364, 376, 377, 378, 379, 381, 393, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 514, 597, 598, 603, 604, 605]

    Line 94: hit count 3

    Line 142: hit count 3

    Line 277: hit count 5

    Line 278: hit count 2

    Line 279: hit count 3

    Line 281: hit count 1

    Line 288: hit count 2

    Line 289: hit count 5

    Line 290: hit count 7

    Line 291: hit count 2

    Line 293: hit count 2

    Line 300: hit count 5

    Line 301: hit count 2

    Line 313: hit count 5

    Line 314: hit count 2

    Line 315: hit count 4

    Line 316: hit count 5

    Line 317: hit count 1

    Line 321: hit count 5

    Line 322: hit count 2

    Line 324: hit count 4

    Line 327: hit count 8

    Line 329: hit count 4

    Line 330: hit count 5

    Line 337: hit count 1

    Line 352: hit count 2

    Line 353: hit count 1

    Line 354: hit count 1

    Line 363: hit count 5

    Line 364: hit count 7

    Line 376: hit count 3

    Line 377: hit count 3

    Line 378: hit count 2

    Line 379: hit count 2

    Line 381: hit count 1

    Line 393: hit count 1

    Line 498: hit count 4

    Line 499: hit count 4

    Line 500: hit count 4

    Line 501: hit count 4

    Line 502: hit count 4

    Line 503: hit count 3

    Line 504: hit count 5

    Line 505: hit count 6

    Line 506: hit count 1

    Line 507: hit count 3

    Line 514: hit count 1

    Line 597: hit count 6

    Line 598: hit count 1

    Line 603: hit count 6

    Line 604: hit count 10

    Line 605: hit count 1

----------------------------------------

File: it/feio/android/omninotes/NavigationDrawerFragment.java

  Only in second dataset lines: [136, 137, 139, 141, 184, 185, 189, 190, 191, 229, 230, 233, 234, 235, 236, 237, 238, 239, 240, 242]

    Line 136: hit count 5

    Line 137: hit count 4

    Line 139: hit count 3

    Line 141: hit count 1

    Line 184: hit count 4

    Line 185: hit count 1

    Line 189: hit count 4

    Line 190: hit count 4

    Line 191: hit count 1

    Line 229: hit count 3

    Line 230: hit count 5

    Line 233: hit count 18

    Line 234: hit count 4

    Line 235: hit count 5

    Line 236: hit count 6

    Line 237: hit count 1

    Line 238: hit count 5

    Line 239: hit count 4

    Line 240: hit count 2

    Line 242: hit count 1

----------------------------------------

File: it/feio/android/omninotes/async/CategoryMenuTask.java

  Only in second dataset lines: [74, 101, 102]

    Line 74: hit count 10

    Line 101: hit count 5

    Line 102: hit count 5

----------------------------------------

File: it/feio/android/omninotes/async/bus/SwitchFragmentEvent.java

  Only in second dataset lines: [26, 27, 30, 34, 35, 36, 37]

    Line 26: hit count 3

    Line 27: hit count 12

    Line 30: hit count 3

    Line 34: hit count 2

    Line 35: hit count 4

    Line 36: hit count 3

    Line 37: hit count 1

----------------------------------------

File: it/feio/android/omninotes/async/notes/NoteLoaderTask.java

  Only in second dataset lines: [44, 46]

    Line 44: hit count 4

    Line 46: hit count 4

----------------------------------------

File: it/feio/android/omninotes/databinding/ActivityCategoryBinding.java

  Only in second dataset lines: [41, 42, 43, 44, 45, 46, 47, 48, 53, 58, 64, 65, 68, 77, 78, 79, 83, 84, 85, 89, 90, 91, 95, 96, 97, 101, 102, 103, 107]

    Line 41: hit count 2

    Line 42: hit count 3

    Line 43: hit count 3

    Line 44: hit count 3

    Line 45: hit count 3

    Line 46: hit count 3

    Line 47: hit count 3

    Line 48: hit count 1

    Line 53: hit count 3

    Line 58: hit count 5

    Line 64: hit count 6

    Line 65: hit count 2

    Line 68: hit count 3

    Line 77: hit count 2

    Line 78: hit count 5

    Line 79: hit count 2

    Line 83: hit count 2

    Line 84: hit count 5

    Line 85: hit count 2

    Line 89: hit count 2

    Line 90: hit count 5

    Line 91: hit count 2

    Line 95: hit count 2

    Line 96: hit count 5

    Line 97: hit count 2

    Line 101: hit count 2

    Line 102: hit count 5

    Line 103: hit count 2

    Line 107: hit count 11

----------------------------------------

File: it/feio/android/omninotes/databinding/DrawerListItemBinding.java

  Only in second dataset lines: [33, 34, 35, 36, 37, 38, 43, 54, 55, 58, 67, 68, 69, 73, 74, 75, 79, 80, 81, 85]

    Line 33: hit count 2

    Line 34: hit count 3

    Line 35: hit count 3

    Line 36: hit count 3

    Line 37: hit count 3

    Line 38: hit count 1

    Line 43: hit count 3

    Line 54: hit count 6

    Line 55: hit count 2

    Line 58: hit count 3

    Line 67: hit count 2

    Line 68: hit count 5

    Line 69: hit count 2

    Line 73: hit count 2

    Line 74: hit count 5

    Line 75: hit count 2

    Line 79: hit count 2

    Line 80: hit count 5

    Line 81: hit count 2

    Line 85: hit count 9

----------------------------------------

File: it/feio/android/omninotes/databinding/FragmentDetailBinding.java

  Only in second dataset lines: [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 102, 113, 114, 117, 126, 127, 128, 132, 133, 134, 138, 139, 140, 144, 145, 146, 150, 151, 152, 156, 157, 158, 162, 163, 164, 168, 169, 170, 174, 175, 176, 180, 181, 182, 186, 187, 188, 191, 193, 194, 195, 199, 200, 201, 205, 206, 207, 211, 212, 213, 217]

    Line 80: hit count 2

    Line 81: hit count 3

    Line 82: hit count 3

    Line 83: hit count 3

    Line 84: hit count 3

    Line 85: hit count 3

    Line 86: hit count 3

    Line 87: hit count 3

    Line 88: hit count 3

    Line 89: hit count 3

    Line 90: hit count 3

    Line 91: hit count 3

    Line 92: hit count 3

    Line 93: hit count 3

    Line 94: hit count 3

    Line 95: hit count 3

    Line 96: hit count 3

    Line 97: hit count 1

    Line 102: hit count 3

    Line 113: hit count 6

    Line 114: hit count 2

    Line 117: hit count 3

    Line 126: hit count 2

    Line 127: hit count 5

    Line 128: hit count 2

    Line 132: hit count 2

    Line 133: hit count 5

    Line 134: hit count 2

    Line 138: hit count 2

    Line 139: hit count 5

    Line 140: hit count 2

    Line 144: hit count 2

    Line 145: hit count 5

    Line 146: hit count 2

    Line 150: hit count 2

    Line 151: hit count 5

    Line 152: hit count 2

    Line 156: hit count 2

    Line 157: hit count 5

    Line 158: hit count 2

    Line 162: hit count 2

    Line 163: hit count 5

    Line 164: hit count 2

    Line 168: hit count 2

    Line 169: hit count 5

    Line 170: hit count 2

    Line 174: hit count 2

    Line 175: hit count 5

    Line 176: hit count 2

    Line 180: hit count 2

    Line 181: hit count 5

    Line 182: hit count 2

    Line 186: hit count 2

    Line 187: hit count 4

    Line 188: hit count 2

    Line 191: hit count 3

    Line 193: hit count 2

    Line 194: hit count 5

    Line 195: hit count 2

    Line 199: hit count 2

    Line 200: hit count 5

    Line 201: hit count 2

    Line 205: hit count 2

    Line 206: hit count 4

    Line 207: hit count 2

    Line 211: hit count 2

    Line 212: hit count 5

    Line 213: hit count 2

    Line 217: hit count 21

----------------------------------------

File: it/feio/android/omninotes/databinding/FragmentDetailContentBinding.java

  Only in second dataset lines: [41, 42, 43, 44, 45, 46, 47, 48, 77, 78, 79, 83, 84, 85, 89, 90, 91, 95, 96, 97, 101, 102, 103, 107]

    Line 41: hit count 2

    Line 42: hit count 3

    Line 43: hit count 3

    Line 44: hit count 3

    Line 45: hit count 3

    Line 46: hit count 3

    Line 47: hit count 3

    Line 48: hit count 1

    Line 77: hit count 2

    Line 78: hit count 5

    Line 79: hit count 2

    Line 83: hit count 2

    Line 84: hit count 5

    Line 85: hit count 2

    Line 89: hit count 2

    Line 90: hit count 5

    Line 91: hit count 2

    Line 95: hit count 2

    Line 96: hit count 5

    Line 97: hit count 2

    Line 101: hit count 2

    Line 102: hit count 5

    Line 103: hit count 2

    Line 107: hit count 11

----------------------------------------

File: it/feio/android/omninotes/db/DbHelper.java

  Only in second dataset lines: [868, 869, 870, 871, 890, 891, 893, 894, 895, 896, 897]

    Line 868: hit count 11

    Line 869: hit count 6

    Line 870: hit count 5

    Line 871: hit count 3

    Line 890: hit count 4

    Line 891: hit count 11

    Line 893: hit count 5

    Line 894: hit count 5

    Line 895: hit count 5

    Line 896: hit count 9

    Line 897: hit count 2

----------------------------------------

File: it/feio/android/omninotes/helpers/date/DateHelper.java

  Only in second dataset lines: [113, 114]

    Line 113: hit count 2

    Line 114: hit count 3

----------------------------------------

File: it/feio/android/omninotes/models/Category.java

  Only in second dataset lines: [26, 27, 28, 29, 30, 31, 35, 36, 50, 51, 62, 63, 64, 65, 66, 79, 82]

    Line 26: hit count 2

    Line 27: hit count 5

    Line 28: hit count 4

    Line 29: hit count 4

    Line 30: hit count 4

    Line 31: hit count 1

    Line 35: hit count 2

    Line 36: hit count 1

    Line 50: hit count 7

    Line 51: hit count 1

    Line 62: hit count 5

    Line 63: hit count 4

    Line 64: hit count 4

    Line 65: hit count 4

    Line 66: hit count 1

    Line 79: hit count 8

    Line 82: hit count 5

----------------------------------------

File: it/feio/android/omninotes/models/Note.java

  Only in second dataset lines: [34, 46, 50, 51, 67, 68, 69, 102, 130, 134, 135, 140, 147, 150, 151]

    Line 34: hit count 8

    Line 46: hit count 6

    Line 50: hit count 2

    Line 51: hit count 1

    Line 67: hit count 3

    Line 68: hit count 4

    Line 69: hit count 1

    Line 102: hit count 3

    Line 130: hit count 3

    Line 134: hit count 3

    Line 135: hit count 1

    Line 140: hit count 4

    Line 147: hit count 7

    Line 150: hit count 3

    Line 151: hit count 1

----------------------------------------

File: it/feio/android/omninotes/models/ONStyle.java

  Only in second dataset lines: [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]

    Line 51: hit count 4

    Line 52: hit count 2

    Line 53: hit count 2

    Line 54: hit count 1

    Line 55: hit count 2

    Line 56: hit count 4

    Line 57: hit count 2

    Line 58: hit count 2

    Line 59: hit count 2

    Line 60: hit count 2

    Line 61: hit count 1

    Line 62: hit count 2

    Line 63: hit count 4

    Line 64: hit count 2

    Line 65: hit count 2

    Line 66: hit count 2

    Line 67: hit count 2

    Line 68: hit count 1

    Line 69: hit count 2

    Line 70: hit count 4

    Line 71: hit count 2

    Line 72: hit count 2

    Line 73: hit count 2

    Line 74: hit count 2

    Line 75: hit count 1

    Line 76: hit count 2

    Line 77: hit count 4

    Line 78: hit count 2

    Line 79: hit count 2

    Line 80: hit count 2

    Line 81: hit count 2

    Line 82: hit count 1

    Line 83: hit count 2

    Line 84: hit count 1

----------------------------------------

File: it/feio/android/omninotes/models/adapters/AttachmentAdapter.java

  Only in second dataset lines: [51, 52, 53, 56, 57, 58, 61]

    Line 51: hit count 2

    Line 52: hit count 3

    Line 53: hit count 2

    Line 56: hit count 3

    Line 57: hit count 6

    Line 58: hit count 1

    Line 61: hit count 4

----------------------------------------

File: it/feio/android/omninotes/models/adapters/CategoryBaseAdapter.java

  Only in second dataset lines: [75, 78, 79, 81, 82, 84, 85, 86, 87, 93, 95, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 115, 116, 117, 120, 125, 126, 129, 130, 131, 132, 134, 136, 138]

    Line 75: hit count 6

    Line 78: hit count 2

    Line 79: hit count 8

    Line 81: hit count 3

    Line 82: hit count 7

    Line 84: hit count 6

    Line 85: hit count 6

    Line 86: hit count 6

    Line 87: hit count 4

    Line 93: hit count 5

    Line 95: hit count 4

    Line 99: hit count 5

    Line 100: hit count 8

    Line 104: hit count 7

    Line 105: hit count 6

    Line 106: hit count 5

    Line 107: hit count 4

    Line 108: hit count 4

    Line 109: hit count 4

    Line 110: hit count 2

    Line 111: hit count 7

    Line 115: hit count 4

    Line 116: hit count 6

    Line 117: hit count 4

    Line 120: hit count 2

    Line 125: hit count 4

    Line 126: hit count 2

    Line 129: hit count 6

    Line 130: hit count 5

    Line 131: hit count 1

    Line 132: hit count 5

    Line 134: hit count 3

    Line 136: hit count 6

    Line 138: hit count 10

----------------------------------------

File: it/feio/android/omninotes/models/adapters/category/CategoryViewHolder.java

  Only in second dataset lines: [32, 33, 34, 35, 36]

    Line 32: hit count 4

    Line 33: hit count 4

    Line 34: hit count 4

    Line 35: hit count 4

    Line 36: hit count 1

----------------------------------------

File: it/feio/android/omninotes/models/views/ExpandableHeightGridView.java

  Only in second dataset lines: [37, 38, 56, 58, 60, 61, 65, 75, 76, 78, 83]

    Line 37: hit count 4

    Line 38: hit count 1

    Line 56: hit count 4

    Line 58: hit count 4

    Line 60: hit count 3

    Line 61: hit count 4

    Line 65: hit count 1

    Line 75: hit count 4

    Line 76: hit count 5

    Line 78: hit count 3

    Line 83: hit count 1

----------------------------------------

File: it/feio/android/omninotes/models/views/Fab.java

  Only in second dataset lines: [64, 67, 69, 106, 107, 108]

    Line 64: hit count 6

    Line 67: hit count 2

    Line 69: hit count 1

    Line 106: hit count 8

    Line 107: hit count 3

    Line 108: hit count 1

----------------------------------------

File: it/feio/android/omninotes/utils/AnimationsHelper.java

  Only in second dataset lines: [43, 44, 47, 48, 49, 56, 57, 58, 59, 66, 67, 76, 77, 78, 79, 80, 86, 87, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

    Line 43: hit count 3

    Line 44: hit count 3

    Line 47: hit count 4

    Line 48: hit count 4

    Line 49: hit count 4

    Line 56: hit count 4

    Line 57: hit count 5

    Line 58: hit count 8

    Line 59: hit count 8

    Line 66: hit count 8

    Line 67: hit count 8

    Line 76: hit count 8

    Line 77: hit count 6

    Line 78: hit count 8

    Line 79: hit count 8

    Line 80: hit count 8

    Line 86: hit count 3

    Line 87: hit count 3

    Line 91: hit count 4

    Line 92: hit count 35

    Line 93: hit count 14

    Line 94: hit count 14

    Line 95: hit count 3

    Line 96: hit count 4

    Line 97: hit count 5

    Line 98: hit count 3

    Line 99: hit count 2

    Line 100: hit count 1

----------------------------------------

File: it/feio/android/omninotes/utils/GeocodeHelper.java

  Only in second dataset lines: [120, 121, 122, 124]

    Line 120: hit count 4

    Line 121: hit count 2

    Line 122: hit count 4

    Line 124: hit count 1

----------------------------------------

File: it/feio/android/omninotes/utils/IntentChecker.java

  Only in second dataset lines: [77]

    Line 77: hit count 2

----------------------------------------

File: it/feio/android/omninotes/utils/KeyboardUtils.java

  Only in second dataset lines: [34, 38, 40, 42, 44, 45, 47, 50, 54, 57, 59, 64, 67, 68, 69, 70, 72, 73]

    Line 34: hit count 2

    Line 38: hit count 3

    Line 40: hit count 6

    Line 42: hit count 5

    Line 44: hit count 7

    Line 45: hit count 2

    Line 47: hit count 3

    Line 50: hit count 1

    Line 54: hit count 2

    Line 57: hit count 6

    Line 59: hit count 4

    Line 64: hit count 2

    Line 67: hit count 3

    Line 68: hit count 3

    Line 69: hit count 3

    Line 70: hit count 1

    Line 72: hit count 6

    Line 73: hit count 1

----------------------------------------

File: it/feio/android/omninotes/utils/date/DateUtils.java

  Only in second dataset lines: [193, 194, 199, 200]

    Line 193: hit count 3

    Line 194: hit count 4

    Line 199: hit count 2

    Line 200: hit count 2

----------------------------------------



## Execution Divergence Hint

Common prefix:

Random operation: CLICK → Start: test_create_empty_category → Input: 5saAYd → Back → Pass: test_create_empty_category → Start: test_behavior_setting



FAIL continuation:

Back → Pass: test_behavior_setting → Start: test_create_note_with_tag_in_content → Input: MnICx92hgQ → Input: #tag1 → Back → Pass: test_create_note_with_tag_in_content → Start: test_reduced_view → Pass: test_reduced_view → Start: test_data_setting → Back → Pass: test_data_setting → Random operation: CLICK → Start: test_create_empty_category → Input: rn1O → Back → Pass: test_create_empty_category → Start: test_create_empty_category → Input: Bo53gPT → Back → Pass: test_create_empty_category → Start: test_create_empty_category → Input: rn1O → Back → Fail: test_create_empty_category → Start: test_reduced_view → Pass: test_reduced_view → Start: test_reduced_view → Pass: test_reduced_view → Random operation: CLICK → Random operation: LONG_CLICK → Random operation: CLICK → Start: test_create_empty_category → Input: 6xj42kB



## Correct Execution Path

Random operation: CLICK → Start: test_create_empty_category → Input: 5saAYd → Back → Pass: test_create_empty_category → Start: test_behavior_setting



## Error Execution Path

Random operation: CLICK → Start: test_create_empty_category → Input: 5saAYd → Back → Pass: test_create_empty_category → Start: test_behavior_setting → Back → Pass: test_behavior_setting → Start: test_create_note_with_tag_in_content → Input: MnICx92hgQ → Input: #tag1 → Back → Pass: test_create_note_with_tag_in_content → Start: test_reduced_view → Pass: test_reduced_view → Start: test_data_setting → Back → Pass: test_data_setting → Random operation: CLICK → Start: test_create_empty_category → Input: rn1O → Back → Pass: test_create_empty_category → Start: test_create_empty_category → Input: Bo53gPT → Back → Pass: test_create_empty_category → Start: test_create_empty_category → Input: rn1O → Back → Fail: test_create_empty_category → Start: test_reduced_view → Pass: test_reduced_view → Start: test_reduced_view → Pass: test_reduced_view → Random operation: CLICK → Random operation: LONG_CLICK → Random operation: CLICK → Start: test_create_empty_category → Input: 6xj42kB



## Files to Analyze

it/feio/android/omninotes/BaseActivity.java

  Differing lines: 5



it/feio/android/omninotes/CategoryActivity.java

  Differing lines: 49



it/feio/android/omninotes/DetailFragment.java

  Differing lines: 251



it/feio/android/omninotes/ListFragment.java

  Differing lines: 51



it/feio/android/omninotes/MainActivity.java

  Differing lines: 52



it/feio/android/omninotes/NavigationDrawerFragment.java

  Differing lines: 20



it/feio/android/omninotes/async/CategoryMenuTask.java

  Differing lines: 3



it/feio/android/omninotes/async/bus/SwitchFragmentEvent.java

  Differing lines: 7



it/feio/android/omninotes/async/notes/NoteLoaderTask.java

  Differing lines: 2



it/feio/android/omninotes/databinding/ActivityCategoryBinding.java

  Differing lines: 29



it/feio/android/omninotes/databinding/DrawerListItemBinding.java

  Differing lines: 20



it/feio/android/omninotes/databinding/FragmentDetailBinding.java

  Differing lines: 69



it/feio/android/omninotes/databinding/FragmentDetailContentBinding.java

  Differing lines: 24



it/feio/android/omninotes/db/DbHelper.java

  Differing lines: 11



it/feio/android/omninotes/helpers/date/DateHelper.java

  Differing lines: 2



it/feio/android/omninotes/models/Category.java

  Differing lines: 17



it/feio/android/omninotes/models/Note.java

  Differing lines: 15



it/feio/android/omninotes/models/ONStyle.java

  Differing lines: 34



it/feio/android/omninotes/models/adapters/AttachmentAdapter.java

  Differing lines: 7



it/feio/android/omninotes/models/adapters/CategoryBaseAdapter.java

  Differing lines: 34



it/feio/android/omninotes/models/adapters/category/CategoryViewHolder.java

  Differing lines: 5



it/feio/android/omninotes/models/views/ExpandableHeightGridView.java

  Differing lines: 11



it/feio/android/omninotes/models/views/Fab.java

  Differing lines: 6



it/feio/android/omninotes/utils/AnimationsHelper.java

  Differing lines: 28



it/feio/android/omninotes/utils/GeocodeHelper.java

  Differing lines: 4



it/feio/android/omninotes/utils/IntentChecker.java

  Differing lines: 1



it/feio/android/omninotes/utils/KeyboardUtils.java

  Differing lines: 18



it/feio/android/omninotes/utils/date/DateUtils.java

  Differing lines: 4



## Output Format

Provide your answer with file paths only. Sort all the files by suspicion level (highest first). One file path per line. No numbering, no explanations, no additional text, no extra punctuation.



Output: