approximate_comparator
======================
Approximate Comparator allows you to test the equality of Python structures without being too precise when comparing floats along the way. For example, when specifying a precision of 2 decimal digits, the sets {3.14159, 2.718, 1.61803} and {3.14, 2.7182, 1.6180} are considered "almost equal". 

It can approximate the equality of plain two floats but also for any compound/recursive data structure: lists of floats, sets of floats, dictionaries of floats, tuples of floats, lists of tuples of floats, dictionaries that map tuples of floats to lists and sets of floats, etc. It's OK if the structures contain items other than floats - (0.3333, "third") and (0.33, "third") are consider almost equal given a precision of 2 decimal digits.

The approximate comparator is useful in unit testing: If your application does computations with real numbers you might wish to avoid assertions such as:
self.assertEqual(result, 0.0129475327294387001)
and prefer a less rigid assertion, like:
assert_almost_equal(result, 0.0129)
Python unit testing framework provieds such functionality for floats, but what if you wish to test compound structrues that contain floats within them? As previously described, the approximate Comparator provides such a general function which works not only for floats but for any two Python objects.

The precision is customizable: just specify the number of decimal digits to round to in the optional parameter "places". By default, places=7.

See the unittests for illustrative examples.

Requirements
============
 - The code is written in Python 2.7. It wasn't tested with other versions of Python.
 - You need unittest in order to run the tests.