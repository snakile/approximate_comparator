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
The following examples use the `is_almost_equal(first, second, places=7)` function. Therefore you need to import it before running the examples:

```python
>>> from approximate_comparator import is_almost_equal
```

### A simple float comparison

```python
>>> is_almost_equal(7.1234, 7.12356, places=3)
0: True
>>> is_almost_equal(6.1234, 7.1334, places=3)
1: False
```

### Integers and strings are considered almost equal only if they're equal

```python
>>> is_almost_equal(7, 7, places=3)
2: True
>>> is_almost_equal(6, 7, places=3)
3: False
>>> is_almost_equal('seven', 'seven', places=3)
4: True
>>> is_almost_equal('six', 'seven', places=3)
5: False
```

### Flat lists

```python
>>> first = [12.1234, 21.00988, 7.4, 'hello', 42]
>>> second = [12.123456, 21.009, 7.40, 'hello', 42]
>>> is_almost_equal(first, second, places=3)
6: True
>>> is_almost_equal(first, second, places=2)
7: True
>>> is_almost_equal(first, second, places=4)
8: False
```

### Flat tuples

```python
>>> first = (12.1234, 21.00988, 7.4, 'hello', 42)
... second = (12.123456, 21.009, 7.40, 'hello', 42)
>>> is_almost_equal(first, second, places=3)
9: True
>>> is_almost_equal(first, second, places=4)
10: False
```

### Flat sets

```python
>>> first = {12.1234, 21.00988, 7.4, 'hello', 42}
... second = {12.123456, 21.009, 7.40, 'hello', 42}
>>> is_almost_equal(first, second, places=3)
11: True
>>> is_almost_equal(first, second, places=4)
12: False
```

### Flat dictionaries

```python
>>> first = {'a': 12.1234, 777.7777: 21.00988, 123.0011: 7.4, 3: 'hello', 12.09876: 42}
... second = {'a': 12.12399, 777.7778: 21.009, 123.0012: 7.4, 3: 'hello', 12.09876: 42}
>>> is_almost_equal(first, second, places=3)
13: True
>>> is_almost_equal(first, second, places=4)
14: False
```

### A dictionary which maps tuples to lists and sets

```python
>>> tuple1_a = ('abc', 7.1234, 3.14)
... tuple1_b = ('abc', 7.123, 3.14)
... tuple2_a = (10, 7.0099)
... tuple2_b = (10, 7.009911)
... tuple3_a = (7.4321, 1.2)
... tuple3_b = (7.432, 1.2)
... value1_a = [0.5555, 'x', (7.123, 123.7)]
... value1_b = [0.5555, 'x', (7.12345, 123.7)]
... value2_a = [4.9999, 3.141, 3.14]
... value2_b = [4.999, 3.1413, 3.14]
... value3_a = {1.111, 2.222}
... value3_b = {1.111, 2.22222}
... 
... dict_a = {tuple1_a: value1_a, tuple2_a: value2_a, tuple3_a: value3_a}
... dict_b = {tuple1_b: value1_b, tuple2_b: value2_b, tuple3_b: value3_b}
>>> is_almost_equal(dict_a, dict_b, places=3)
15: True
>>> is_almost_equal(dict_a, dict_b, places=2)
16: True
>>> is_almost_equal(dict_a, dict_b, places=1)
17: True
>>> is_almost_equal(dict_a, dict_b, places=4)
18: False
```

For more illustrative examples see the unit tests.

Requirements
------------
 - The code is written in Python 2.7 and wasn't tested with other versions of Python.