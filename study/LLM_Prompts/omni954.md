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

test_create_note_without_category



## Code Coverage Summary

File: it/feio/android/omninotes/BaseActivity.java

  Only in second dataset lines: [128, 129, 130, 131, 134, 135, 140, 141, 144, 148, 173]

    Line 128: hit count 3

    Line 129: hit count 8

    Line 130: hit count 10

    Line 131: hit count 4

    Line 134: hit count 8

    Line 135: hit count 1

    Line 140: hit count 3

    Line 141: hit count 7

    Line 144: hit count 2

    Line 148: hit count 1

    Line 173: hit count 11

----------------------------------------

File: it/feio/android/omninotes/DetailFragment.java

  Only in second dataset lines: [193, 208, 219, 220, 221, 222, 227, 230, 231, 239, 245, 281, 282, 283, 287, 288, 289, 293, 294, 295, 299, 300, 301, 302, 306, 307, 312, 314, 316, 317, 320, 323, 326, 328, 331, 332, 334, 335, 336, 339, 349, 352, 359, 377, 380, 382, 385, 389, 390, 391, 393, 406, 408, 409, 412, 413, 416, 417, 420, 425, 426, 460, 462, 472, 486, 514, 519, 520, 551, 552, 554, 557, 558, 596, 599, 601, 603, 605, 607, 609, 611, 612, 615, 616, 617, 618, 619, 620, 623, 624, 626, 627, 628, 629, 630, 632, 635, 641, 657, 658, 663, 667, 669, 680, 684, 695, 708, 719, 722, 724, 727, 730, 731, 734, 790, 810, 857, 858, 859, 861, 863, 869, 870, 873, 874, 875, 877, 880, 881, 886, 894, 895, 897, 904, 907, 910, 911, 915, 919, 924, 925, 926, 929, 993, 994, 995, 1001, 1002, 1003, 1006, 1008, 1009, 1010, 1011, 1012, 1013, 1015, 1021, 1022, 1023, 1024, 1025, 1027, 1031, 1035, 1043, 1044, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1056, 1061, 1541, 1542, 1543, 1544, 1545, 1547, 1555, 1556, 1559, 1568, 1576, 1578, 1580, 1586, 1590, 1598, 1599, 1600, 1601, 1602, 1607, 1608, 1609, 1610, 1614, 1615, 1616, 1618, 1621, 1622, 1630, 1633, 1634, 1641, 1642, 1645, 1646, 1647, 1651, 1657, 1713, 1714, 1785, 1795, 2036, 2037, 2042, 2047, 2055, 2061, 2064, 2066, 2172, 2175]

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

    Line 919: hit count 2

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

    Line 1541: hit count 3

    Line 1542: hit count 5

    Line 1543: hit count 3

    Line 1544: hit count 3

    Line 1545: hit count 3

    Line 1547: hit count 1

    Line 1555: hit count 5

    Line 1556: hit count 5

    Line 1559: hit count 8

    Line 1568: hit count 3

    Line 1576: hit count 6

    Line 1578: hit count 16

    Line 1580: hit count 1

    Line 1586: hit count 8

    Line 1590: hit count 13

    Line 1598: hit count 6

    Line 1599: hit count 6

    Line 1600: hit count 6

    Line 1601: hit count 6

    Line 1602: hit count 6

    Line 1607: hit count 3

    Line 1608: hit count 7

    Line 1609: hit count 4

    Line 1610: hit count 4

    Line 1614: hit count 6

    Line 1615: hit count 3

    Line 1616: hit count 3

    Line 1618: hit count 1

    Line 1621: hit count 4

    Line 1622: hit count 2

    Line 1630: hit count 1

    Line 1633: hit count 6

    Line 1634: hit count 6

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

    Line 2036: hit count 2

    Line 2037: hit count 1

    Line 2042: hit count 1

    Line 2047: hit count 1

    Line 2055: hit count 6

    Line 2061: hit count 8

    Line 2064: hit count 7

    Line 2066: hit count 1

    Line 2172: hit count 5

    Line 2175: hit count 1

----------------------------------------

File: it/feio/android/omninotes/ListFragment.java

  Only in second dataset lines: [264, 265, 278, 280, 286, 287, 336, 343, 348, 349, 350, 351, 352, 353, 354, 355, 359, 374, 375, 376, 377, 378, 379, 381, 523, 524, 527, 530, 531, 532, 534, 535, 536, 537, 539, 547, 550, 551, 921, 930, 931, 933, 937, 938, 941, 948, 954, 957, 958, 1181, 1184, 1280, 1281, 1282, 1286]

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

    Line 1181: hit count 3

    Line 1184: hit count 2

    Line 1280: hit count 6

    Line 1281: hit count 7

    Line 1282: hit count 13

    Line 1286: hit count 1

----------------------------------------

File: it/feio/android/omninotes/MainActivity.java

  Only in second dataset lines: [94, 288, 289, 290, 291, 293, 300, 301, 313, 314, 315, 316, 317, 363, 364, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 514, 603, 604, 605]

    Line 94: hit count 3

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

    Line 363: hit count 5

    Line 364: hit count 7

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

    Line 603: hit count 6

    Line 604: hit count 10

    Line 605: hit count 1

----------------------------------------

File: it/feio/android/omninotes/NavigationDrawerFragment.java

  Only in second dataset lines: [106, 117, 118, 136, 137, 139, 141, 229, 230, 233, 234, 235, 236, 237, 238, 239, 240, 242]

    Line 106: hit count 2

    Line 117: hit count 3

    Line 118: hit count 1

    Line 136: hit count 5

    Line 137: hit count 4

    Line 139: hit count 3

    Line 141: hit count 1

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

File: it/feio/android/omninotes/async/UpdateWidgetsTask.java

  Only in second dataset lines: [48, 49, 50]

    Line 48: hit count 6

    Line 49: hit count 3

    Line 50: hit count 1

----------------------------------------

File: it/feio/android/omninotes/async/bus/NotesUpdatedEvent.java

  Only in second dataset lines: [34, 35, 36, 37]

    Line 34: hit count 2

    Line 35: hit count 4

    Line 36: hit count 3

    Line 37: hit count 1

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

File: it/feio/android/omninotes/async/notes/SaveNoteTask.java

  Only in second dataset lines: [37, 47, 48, 49, 50, 51, 56, 57, 58, 59, 62, 63, 66, 71, 72, 82, 86, 102, 103, 104, 106]

    Line 37: hit count 3

    Line 47: hit count 2

    Line 48: hit count 3

    Line 49: hit count 3

    Line 50: hit count 3

    Line 51: hit count 1

    Line 56: hit count 4

    Line 57: hit count 3

    Line 58: hit count 4

    Line 59: hit count 2

    Line 62: hit count 6

    Line 63: hit count 2

    Line 66: hit count 2

    Line 71: hit count 3

    Line 72: hit count 7

    Line 82: hit count 6

    Line 86: hit count 1

    Line 102: hit count 3

    Line 103: hit count 3

    Line 104: hit count 4

    Line 106: hit count 1

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

File: it/feio/android/omninotes/databinding/NoteLayoutExpandedBinding.java

  Only in second dataset lines: [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 104, 105, 106, 110, 111, 112, 116, 117, 118, 122, 123, 124, 128, 129, 130, 134, 135, 136, 140, 141, 142, 146, 147, 148, 152, 153, 154, 158, 159, 160, 164, 166]

    Line 62: hit count 2

    Line 63: hit count 3

    Line 64: hit count 3

    Line 65: hit count 3

    Line 66: hit count 3

    Line 67: hit count 3

    Line 68: hit count 3

    Line 69: hit count 3

    Line 70: hit count 3

    Line 71: hit count 3

    Line 72: hit count 3

    Line 73: hit count 3

    Line 74: hit count 3

    Line 75: hit count 1

    Line 104: hit count 2

    Line 105: hit count 5

    Line 106: hit count 2

    Line 110: hit count 2

    Line 111: hit count 5

    Line 112: hit count 2

    Line 116: hit count 2

    Line 117: hit count 5

    Line 118: hit count 2

    Line 122: hit count 2

    Line 123: hit count 5

    Line 124: hit count 2

    Line 128: hit count 2

    Line 129: hit count 4

    Line 130: hit count 2

    Line 134: hit count 2

    Line 135: hit count 5

    Line 136: hit count 2

    Line 140: hit count 2

    Line 141: hit count 5

    Line 142: hit count 2

    Line 146: hit count 2

    Line 147: hit count 5

    Line 148: hit count 2

    Line 152: hit count 2

    Line 153: hit count 5

    Line 154: hit count 2

    Line 158: hit count 2

    Line 159: hit count 5

    Line 160: hit count 2

    Line 164: hit count 3

    Line 166: hit count 17

----------------------------------------

File: it/feio/android/omninotes/db/DbHelper.java

  Only in second dataset lines: [216, 218, 220, 223, 225, 226, 227, 228, 229, 230, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 246, 247, 250, 251, 257, 262, 263, 266, 267, 268, 270, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 468, 474, 475, 482, 485, 487, 647, 648, 799, 800, 811, 814, 817, 828, 829, 832]

    Line 216: hit count 5

    Line 218: hit count 5

    Line 220: hit count 3

    Line 223: hit count 3

    Line 225: hit count 4

    Line 226: hit count 5

    Line 227: hit count 4

    Line 228: hit count 3

    Line 229: hit count 6

    Line 230: hit count 3

    Line 232: hit count 3

    Line 233: hit count 5

    Line 234: hit count 5

    Line 235: hit count 5

    Line 236: hit count 5

    Line 237: hit count 5

    Line 238: hit count 5

    Line 239: hit count 5

    Line 240: hit count 5

    Line 241: hit count 5

    Line 242: hit count 7

    Line 243: hit count 12

    Line 244: hit count 12

    Line 246: hit count 8

    Line 247: hit count 12

    Line 250: hit count 3

    Line 251: hit count 7

    Line 257: hit count 6

    Line 262: hit count 3

    Line 263: hit count 3

    Line 266: hit count 2

    Line 267: hit count 6

    Line 268: hit count 5

    Line 270: hit count 2

    Line 450: hit count 2

    Line 451: hit count 4

    Line 452: hit count 7

    Line 453: hit count 7

    Line 454: hit count 6

    Line 455: hit count 6

    Line 456: hit count 9

    Line 457: hit count 9

    Line 458: hit count 6

    Line 459: hit count 6

    Line 460: hit count 6

    Line 461: hit count 6

    Line 462: hit count 6

    Line 463: hit count 6

    Line 464: hit count 9

    Line 465: hit count 9

    Line 468: hit count 5

    Line 474: hit count 5

    Line 475: hit count 4

    Line 482: hit count 5

    Line 485: hit count 4

    Line 487: hit count 3

    Line 647: hit count 10

    Line 648: hit count 4

    Line 799: hit count 4

    Line 800: hit count 9

    Line 811: hit count 2

    Line 814: hit count 6

    Line 817: hit count 3

    Line 828: hit count 2

    Line 829: hit count 2

    Line 832: hit count 2

----------------------------------------

File: it/feio/android/omninotes/helpers/date/DateHelper.java

  Only in second dataset lines: [113, 114]

    Line 113: hit count 2

    Line 114: hit count 3

----------------------------------------

File: it/feio/android/omninotes/models/Note.java

  Only in second dataset lines: [34, 46, 50, 51, 67, 68, 69, 102, 122, 130, 134, 135, 140, 147, 150, 151]

    Line 34: hit count 8

    Line 46: hit count 6

    Line 50: hit count 2

    Line 51: hit count 1

    Line 67: hit count 3

    Line 68: hit count 4

    Line 69: hit count 1

    Line 102: hit count 3

    Line 122: hit count 3

    Line 130: hit count 3

    Line 134: hit count 3

    Line 135: hit count 1

    Line 140: hit count 4

    Line 147: hit count 2

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

File: it/feio/android/omninotes/models/adapters/NoteAdapter.java

  Only in second dataset lines: [75, 79, 81, 86, 88, 89, 90, 103, 112, 113, 114, 119, 121, 122, 123, 126, 128, 130, 134, 139, 144, 145, 146, 147, 148, 149, 150, 157, 158, 213, 214, 215, 216, 217, 218, 219, 233, 236, 239, 242, 255, 258, 305, 306, 307, 312, 317, 318, 319, 320, 321, 322, 323]

    Line 75: hit count 5

    Line 79: hit count 6

    Line 81: hit count 1

    Line 86: hit count 6

    Line 88: hit count 5

    Line 89: hit count 3

    Line 90: hit count 5

    Line 103: hit count 1

    Line 112: hit count 7

    Line 113: hit count 4

    Line 114: hit count 1

    Line 119: hit count 8

    Line 121: hit count 2

    Line 122: hit count 4

    Line 123: hit count 1

    Line 126: hit count 7

    Line 128: hit count 8

    Line 130: hit count 3

    Line 134: hit count 1

    Line 139: hit count 4

    Line 144: hit count 5

    Line 145: hit count 6

    Line 146: hit count 6

    Line 147: hit count 6

    Line 148: hit count 5

    Line 149: hit count 6

    Line 150: hit count 5

    Line 157: hit count 1

    Line 158: hit count 1

    Line 213: hit count 3

    Line 214: hit count 3

    Line 215: hit count 3

    Line 216: hit count 3

    Line 217: hit count 6

    Line 218: hit count 5

    Line 219: hit count 1

    Line 233: hit count 4

    Line 236: hit count 4

    Line 239: hit count 4

    Line 242: hit count 3

    Line 255: hit count 5

    Line 258: hit count 1

    Line 305: hit count 3

    Line 306: hit count 6

    Line 307: hit count 3

    Line 312: hit count 7

    Line 317: hit count 6

    Line 318: hit count 4

    Line 319: hit count 4

    Line 320: hit count 4

    Line 321: hit count 4

    Line 322: hit count 5

    Line 323: hit count 1

----------------------------------------

File: it/feio/android/omninotes/models/holders/NoteViewHolder.java

  Only in second dataset lines: [50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 84]

    Line 50: hit count 3

    Line 52: hit count 2

    Line 53: hit count 3

    Line 54: hit count 4

    Line 55: hit count 4

    Line 56: hit count 4

    Line 57: hit count 4

    Line 58: hit count 4

    Line 59: hit count 4

    Line 60: hit count 4

    Line 61: hit count 4

    Line 62: hit count 4

    Line 63: hit count 4

    Line 64: hit count 4

    Line 65: hit count 4

    Line 66: hit count 4

    Line 67: hit count 1

    Line 84: hit count 1

----------------------------------------

File: it/feio/android/omninotes/models/listeners/RecyclerViewItemClickSupport.java

  Only in second dataset lines: [54, 55, 57, 58, 60]

    Line 54: hit count 4

    Line 55: hit count 5

    Line 57: hit count 4

    Line 58: hit count 5

    Line 60: hit count 1

----------------------------------------

File: it/feio/android/omninotes/models/misc/DynamicNavigationLookupTable.java

  Only in second dataset lines: [58, 60, 62, 65, 66, 76, 77]

    Line 58: hit count 8

    Line 60: hit count 8

    Line 62: hit count 6

    Line 65: hit count 6

    Line 66: hit count 6

    Line 76: hit count 2

    Line 77: hit count 1

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

  Only in second dataset lines: [64, 67, 69, 82, 84, 88, 90, 106, 107, 108]

    Line 64: hit count 6

    Line 67: hit count 2

    Line 69: hit count 1

    Line 82: hit count 2

    Line 84: hit count 2

    Line 88: hit count 2

    Line 90: hit count 1

    Line 106: hit count 8

    Line 107: hit count 3

    Line 108: hit count 1

----------------------------------------

File: it/feio/android/omninotes/models/views/RecyclerViewEmptySupport.java

  Only in second dataset lines: [40, 41]

    Line 40: hit count 5

    Line 41: hit count 4

----------------------------------------

File: it/feio/android/omninotes/models/views/SquareImageView.java

  Only in second dataset lines: [39, 40]

    Line 39: hit count 4

    Line 40: hit count 1

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

  Only in second dataset lines: [34, 38, 40, 42, 44, 45, 47, 50, 54, 57, 59, 64, 67, 68, 69, 72, 73]

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

    Line 72: hit count 6

    Line 73: hit count 1

----------------------------------------

File: it/feio/android/omninotes/utils/TextHelper.java

  Only in second dataset lines: [49, 51, 52, 55, 66, 72, 75, 80, 81, 83, 84, 90, 127, 130, 133, 149, 150, 153]

    Line 49: hit count 2

    Line 51: hit count 3

    Line 52: hit count 8

    Line 55: hit count 5

    Line 66: hit count 8

    Line 72: hit count 5

    Line 75: hit count 14

    Line 80: hit count 5

    Line 81: hit count 5

    Line 83: hit count 8

    Line 84: hit count 3

    Line 90: hit count 3

    Line 127: hit count 3

    Line 130: hit count 4

    Line 133: hit count 8

    Line 149: hit count 14

    Line 150: hit count 4

    Line 153: hit count 2

----------------------------------------

File: it/feio/android/omninotes/utils/date/DateUtils.java

  Only in second dataset lines: [173, 193, 194, 199, 200, 202, 203, 204, 205, 207]

    Line 173: hit count 5

    Line 193: hit count 3

    Line 194: hit count 4

    Line 199: hit count 2

    Line 200: hit count 2

    Line 202: hit count 6

    Line 203: hit count 4

    Line 204: hit count 2

    Line 205: hit count 4

    Line 207: hit count 4

----------------------------------------



## Execution Divergence Hint

Common prefix:

Random operation: CLICK → Start: test_create_note_without_category → Input: JMWY8 → Input: test content → Back → Pass: test_create_note_without_category → Start: test_open_uncategorized_category_setting



FAIL continuation:

Back → Pass: test_open_uncategorized_category_setting → Start: test_create_note_without_category → Input: Tk8tGNP → Input: test content → Back → Pass: test_create_note_without_category → Random operation: CLICK → Start: test_check_uncategorized_notes → Pass: test_check_uncategorized_notes → Start: test_delete_category → Back → Pass: test_delete_category → Start: test_note_info → Input: 9m1LSIQMmA → Input: 07W6rjRtGMty1nffNmu → Back → Pass: test_note_info → Start: test_check_uncategorized_notes → Pass: test_check_uncategorized_notes → Start: test_create_checklist → Input: hI6ZgN3 → Input: 9KX → Back → Pass: test_create_checklist → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_create_note_with_new_category → Input: kY4RP0Hg0 → Input: test content → Input: wdapohZ → Pass: test_create_note_with_new_category → Random operation: CLICK → Start: test_create_note_with_new_category → Input: T85AAzQ2S → Input: test content → Input: tno57oUr → Pass: test_create_note_with_new_category → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_create_note_without_category → Input: EidVNp → Input: test content → Back → Pass: test_create_note_without_category → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_create_note_with_new_category → Input: 4WstGOP → Input: test content → Input: t2A → Pass: test_create_note_with_new_category → Start: test_create_note_without_category → Input: GZ4Pos1PhW → Input: test content → Back → Pass: test_create_note_without_category → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_create_note_with_new_category → Input: Ss8o → Input: test content → Input: F7M1l4 → Pass: test_create_note_with_new_category → Start: test_create_note_with_new_category → Input: vsx → Input: test content → Input: n6x → Fail: test_create_note_with_new_category → Random operation: CLICK → Start: test_create_note_without_category → Input: jVnRgTRr8N → Input: test content → Back → Pass: test_create_note_without_category → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_create_note_without_category → Input: OFxQa5E9 → Input: test content → Back → Fail: test_create_note_without_category → Start: test_create_note_without_category → Input: FUXGVZ → Input: test content → Back



## Correct Execution Path

Random operation: CLICK → Start: test_create_note_without_category → Input: JMWY8 → Input: test content → Back → Pass: test_create_note_without_category → Start: test_open_uncategorized_category_setting



## Error Execution Path

Random operation: CLICK → Start: test_create_note_without_category → Input: JMWY8 → Input: test content → Back → Pass: test_create_note_without_category → Start: test_open_uncategorized_category_setting → Back → Pass: test_open_uncategorized_category_setting → Start: test_create_note_without_category → Input: Tk8tGNP → Input: test content → Back → Pass: test_create_note_without_category → Random operation: CLICK → Start: test_check_uncategorized_notes → Pass: test_check_uncategorized_notes → Start: test_delete_category → Back → Pass: test_delete_category → Start: test_note_info → Input: 9m1LSIQMmA → Input: 07W6rjRtGMty1nffNmu → Back → Pass: test_note_info → Start: test_check_uncategorized_notes → Pass: test_check_uncategorized_notes → Start: test_create_checklist → Input: hI6ZgN3 → Input: 9KX → Back → Pass: test_create_checklist → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_create_note_with_new_category → Input: kY4RP0Hg0 → Input: test content → Input: wdapohZ → Pass: test_create_note_with_new_category → Random operation: CLICK → Start: test_create_note_with_new_category → Input: T85AAzQ2S → Input: test content → Input: tno57oUr → Pass: test_create_note_with_new_category → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_create_note_without_category → Input: EidVNp → Input: test content → Back → Pass: test_create_note_without_category → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_create_note_with_new_category → Input: 4WstGOP → Input: test content → Input: t2A → Pass: test_create_note_with_new_category → Start: test_create_note_without_category → Input: GZ4Pos1PhW → Input: test content → Back → Pass: test_create_note_without_category → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_create_note_with_new_category → Input: Ss8o → Input: test content → Input: F7M1l4 → Pass: test_create_note_with_new_category → Start: test_create_note_with_new_category → Input: vsx → Input: test content → Input: n6x → Fail: test_create_note_with_new_category → Random operation: CLICK → Start: test_create_note_without_category → Input: jVnRgTRr8N → Input: test content → Back → Pass: test_create_note_without_category → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_check_uncategorized_notes → Fail: test_check_uncategorized_notes → Start: test_create_note_without_category → Input: OFxQa5E9 → Input: test content → Back → Fail: test_create_note_without_category → Start: test_create_note_without_category → Input: FUXGVZ → Input: test content → Back



## Files to Analyze

it/feio/android/omninotes/BaseActivity.java

  Differing lines: 11



it/feio/android/omninotes/DetailFragment.java

  Differing lines: 230



it/feio/android/omninotes/ListFragment.java

  Differing lines: 55



it/feio/android/omninotes/MainActivity.java

  Differing lines: 29



it/feio/android/omninotes/NavigationDrawerFragment.java

  Differing lines: 18



it/feio/android/omninotes/async/UpdateWidgetsTask.java

  Differing lines: 3



it/feio/android/omninotes/async/bus/NotesUpdatedEvent.java

  Differing lines: 4



it/feio/android/omninotes/async/bus/SwitchFragmentEvent.java

  Differing lines: 7



it/feio/android/omninotes/async/notes/SaveNoteTask.java

  Differing lines: 21



it/feio/android/omninotes/databinding/FragmentDetailBinding.java

  Differing lines: 69



it/feio/android/omninotes/databinding/FragmentDetailContentBinding.java

  Differing lines: 24



it/feio/android/omninotes/databinding/NoteLayoutExpandedBinding.java

  Differing lines: 46



it/feio/android/omninotes/db/DbHelper.java

  Differing lines: 66



it/feio/android/omninotes/helpers/date/DateHelper.java

  Differing lines: 2



it/feio/android/omninotes/models/Note.java

  Differing lines: 16



it/feio/android/omninotes/models/ONStyle.java

  Differing lines: 34



it/feio/android/omninotes/models/adapters/AttachmentAdapter.java

  Differing lines: 7



it/feio/android/omninotes/models/adapters/NoteAdapter.java

  Differing lines: 53



it/feio/android/omninotes/models/holders/NoteViewHolder.java

  Differing lines: 18



it/feio/android/omninotes/models/listeners/RecyclerViewItemClickSupport.java

  Differing lines: 5



it/feio/android/omninotes/models/misc/DynamicNavigationLookupTable.java

  Differing lines: 7



it/feio/android/omninotes/models/views/ExpandableHeightGridView.java

  Differing lines: 11



it/feio/android/omninotes/models/views/Fab.java

  Differing lines: 10



it/feio/android/omninotes/models/views/RecyclerViewEmptySupport.java

  Differing lines: 2



it/feio/android/omninotes/models/views/SquareImageView.java

  Differing lines: 2



it/feio/android/omninotes/utils/AnimationsHelper.java

  Differing lines: 28



it/feio/android/omninotes/utils/GeocodeHelper.java

  Differing lines: 4



it/feio/android/omninotes/utils/IntentChecker.java

  Differing lines: 1



it/feio/android/omninotes/utils/KeyboardUtils.java

  Differing lines: 17



it/feio/android/omninotes/utils/TextHelper.java

  Differing lines: 18



it/feio/android/omninotes/utils/date/DateUtils.java

  Differing lines: 10



## Output Format

Provide your answer with file paths only. Sort all the files by suspicion level (highest first). One file path per line. No numbering, no explanations, no additional text, no extra punctuation.



Output: