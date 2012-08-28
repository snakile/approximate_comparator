Approximate Comparator
======================
Approximate Comparator allows you to test the equality of Python structures without being too precise when comparing floats along the way. For example, when specifying a precision of 2 decimal digits, the sets `{3.14159, 2.718, 1.61803}` and `{3.14, 2.7182, 1.6180}` are considered "almost equal". 

It can approximate the equality of plain two floats but also of any compound/recursive data structure: lists of floats, sets of floats, dictionaries of floats, tuples of floats, lists of tuples of floats, dictionaries that map tuples of floats to lists and sets of floats, etc. It's OK if the structures contain items other than floats: The tuples `(0.3333, "third")` and `(0.33, "third")`, for instance, are consider almost equal given a precision of 2 decimal digits.

What is Approximate Comparator Good for
---------------------------------------
**Approximate Comparator is useful in unit testing:** If your application performs computations involving real numbers you might wish to avoid assertions such as:

```python
self.assertEqual(result, 0.0129475327294387001)
```

and prefer a less rigid assertion, like:

```python
assert_almost_equal(result, 0.0129)
```

Python unit testing framework provieds such functionality for plain floats, but what if you wish to test compound structrues that contain floats within them? As previously described, the Approximate Comparator provides such a general function which works not only for floats but for any two Python objects.

**The precision is customizable:** just specify the number of decimal digits to round to in the optional parameter `places`. By default, `places=7`.

Examples
--------

```python
>>> from approximate_comparator import is_almost_equal
>>> is_almost_equal(7, 7, places=3)
0: True
>>> is_almost_equal(6, 7, places=3)
1: False
>>> is_almost_equal('seven', 'seven', places=3)
2: True
>>> is_almost_equal('six', 'seven', places=3)
3: False
>>> is_almost_equal(7.1234, 7.12356, places=3)
4: True
>>> is_almost_equal(6.1234, 7.1334, places=3)
5: False
```

See the unittests for more illustrative examples.

Requirements
------------
 - The code is written in Python 2.7 and wasn't tested with other versions of Python.