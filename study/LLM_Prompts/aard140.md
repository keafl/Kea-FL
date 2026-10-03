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

test_filter_words



## Code Coverage Summary

File: itkach/aard2/Application.java

  Only in second dataset lines: [255, 256]

    Line 255: hit count 5

    Line 256: hit count 1

----------------------------------------

File: itkach/aard2/ArticleCollectionActivity.java

  Only in second dataset lines: [404, 405, 406, 408, 409, 411, 412, 413, 414, 574, 575, 576, 577]

    Line 404: hit count 3

    Line 405: hit count 3

    Line 406: hit count 4

    Line 408: hit count 3

    Line 409: hit count 3

    Line 411: hit count 4

    Line 412: hit count 3

    Line 413: hit count 2

    Line 414: hit count 1

    Line 574: hit count 5

    Line 575: hit count 3

    Line 576: hit count 3

    Line 577: hit count 1

----------------------------------------

File: itkach/aard2/ArticleFragment.java

  Only in second dataset lines: [223, 224, 225, 227, 228, 229, 230]

    Line 223: hit count 3

    Line 224: hit count 3

    Line 225: hit count 3

    Line 227: hit count 3

    Line 228: hit count 3

    Line 229: hit count 2

    Line 230: hit count 1

----------------------------------------

File: itkach/aard2/ArticleWebView.java

  Only in second dataset lines: [564, 565, 566]

    Line 564: hit count 2

    Line 565: hit count 3

    Line 566: hit count 1

----------------------------------------

File: itkach/aard2/BlobDescriptorList.java

  Only in second dataset lines: [123, 124, 126, 127, 128, 130, 286, 287, 288]

    Line 123: hit count 11

    Line 124: hit count 13

    Line 126: hit count 3

    Line 127: hit count 3

    Line 128: hit count 5

    Line 130: hit count 1

    Line 286: hit count 3

    Line 287: hit count 2

    Line 288: hit count 1

----------------------------------------

File: itkach/aard2/BlobDescriptorListAdapter.java

  Only in second dataset lines: [57, 75]

    Line 57: hit count 3

    Line 75: hit count 3

----------------------------------------

File: itkach/aard2/BlobDescriptorListFragment.java

  Only in second dataset lines: [188, 189, 190, 192, 239, 240, 241, 246, 255]

    Line 188: hit count 4

    Line 189: hit count 5

    Line 190: hit count 5

    Line 192: hit count 2

    Line 239: hit count 3

    Line 240: hit count 3

    Line 241: hit count 3

    Line 246: hit count 3

    Line 255: hit count 4

----------------------------------------

File: itkach/aard2/MainActivity.java

  Only in second dataset lines: [142, 158]

    Line 142: hit count 3

    Line 158: hit count 4

----------------------------------------



## Execution Divergence Hint

Common prefix:

Random operation: LONG_CLICK → Start: test_lookup_word → Input: kf → Pass: test_lookup_word → Start: test_lookup_word → Input: w → Pass: test_lookup_word → Start: test_filter_words → Input: w → Pass: test_filter_words



FAIL continuation:

Random operation: LONG_CLICK → Start: test_favorite_word → Start: test_lookup_word → Input: - → Pass: test_lookup_word → Start: test_filter_words → Input: w → Pass: test_filter_words → Start: test_lookup_word → Input: - → Pass: test_lookup_word → Start: test_filter_words → Input: ~ → Pass: test_filter_words → Start: test_filter_words → Input: w → Pass: test_filter_words → Random operation: LONG_CLICK → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: BACK → Start: test_filter_words → Input: ~ → Pass: test_filter_words → Start: test_filter_words → Input: - → Fail: test_filter_words → Start: test_lookup_word → Input: MN



## Correct Execution Path

Random operation: LONG_CLICK → Start: test_lookup_word → Input: kf → Pass: test_lookup_word → Start: test_lookup_word → Input: w → Pass: test_lookup_word → Start: test_filter_words → Input: w → Pass: test_filter_words



## Error Execution Path

Random operation: LONG_CLICK → Start: test_lookup_word → Input: kf → Pass: test_lookup_word → Start: test_lookup_word → Input: w → Pass: test_lookup_word → Start: test_filter_words → Input: w → Pass: test_filter_words → Random operation: LONG_CLICK → Start: test_favorite_word → Start: test_lookup_word → Input: - → Pass: test_lookup_word → Start: test_filter_words → Input: w → Pass: test_filter_words → Start: test_lookup_word → Input: - → Pass: test_lookup_word → Start: test_filter_words → Input: ~ → Pass: test_filter_words → Start: test_filter_words → Input: w → Pass: test_filter_words → Random operation: LONG_CLICK → Random operation: CLICK → Random operation: SCROLL_TOP_DOWN → Random operation: BACK → Start: test_filter_words → Input: ~ → Pass: test_filter_words → Start: test_filter_words → Input: - → Fail: test_filter_words → Start: test_lookup_word → Input: MN



## Files to Analyze

itkach/aard2/Application.java

  Differing lines: 2



itkach/aard2/ArticleCollectionActivity.java

  Differing lines: 13



itkach/aard2/ArticleFragment.java

  Differing lines: 7



itkach/aard2/ArticleWebView.java

  Differing lines: 3



itkach/aard2/BlobDescriptorList.java

  Differing lines: 9



itkach/aard2/BlobDescriptorListAdapter.java

  Differing lines: 2



itkach/aard2/BlobDescriptorListFragment.java

  Differing lines: 9



itkach/aard2/MainActivity.java

  Differing lines: 2



## Output Format

Provide your answer with file paths only. Sort all the files by suspicion level (highest first). One file path per line. No numbering, no explanations, no additional text, no extra punctuation.



Output: