# Python - Variable Annotations
This directory contains the implementation code of variable annotations related concepts

## Brief Reminder
Python is a dynamically-typed language. That means that variable types are dynamically set at run-time, upon assignment of a value to a variable.

* For example, in

```python
  def fn(a, b):
    return a + b
```
The types of a and b are not known at build-time, only when a and b are assigned values at run-time.

Hence, calling

```python
  fn("a", 1)
```
somewhere in your code will not raise an exception until the code is actually executed and the function is called:

```python
  >>> fn("a", 1)
  Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  TypeError: can only concatenate str (not "int") to str
```

>[!Note]
>In Python 3, type annotations do not change this. Python is still a dynamically-typed language. Type annotations serve the following purpose:
> * **Code documentation**: thanks to them, a developer reading type-annotated code (his own or someone else’s) will know exactly what type each variables is supposed to be. This helps reduce bugs and exceptions and accelerate the development cycle.
> * **Linting and validation**: code editors and continuous integration (CI) pipelines can be configured to automatically validate type-annotated code at build-time and catch bugs before they make it to production.

## Usages
The following are sample for running the code files.

`0-main.py`
```python
  #!/usr/bin/env python3
  add = __import__('0-add').add

  print(add(1.11, 2.22) == 1.11 + 2.22)
  print(add.__annotations__)
```

`1-main.py`
```python
  #!/usr/bin/env python3
  concat = __import__('1-concat').concat

  str1 = "egg"
  str2 = "shell"

  print(concat(str1, str2) == "{}{}".format(str1, str2))
  print(concat.__annotations__)
```


`2-main.py`
```python
  #!/usr/bin/env python3

  import math

  floor = __import__('2-floor').floor

  ans = floor(3.14)

  print(ans == math.floor(3.14))
  print(floor.__annotations__)
  print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
```


`3-main.py`
```python
  #!/usr/bin/env python3
  to_str = __import__('3-to_str').to_str

  pi_str = to_str(3.14)
  print(pi_str == str(3.14))
  print(to_str.__annotations__)
  print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))
```


`4-main.py`
```python
  #!/usr/bin/env python3

  a = __import__('4-define_variables').a
  pi = __import__('4-define_variables').pi
  i_understand_annotations = __import__('4-define_variables').i_understand_annotations
  school = __import__('4-define_variables').school

  print("a is a {} with a value of {}".format(type(a), a))
  print("pi is a {} with a value of {}".format(type(pi), pi))
  print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations), i_understand_annotations))
  print("school is a {} with a value of {}".format(type(school), school))
```


`5-main.py`
```python
  #!/usr/bin/env python3

  sum_list = __import__('5-sum_list').sum_list

  floats = [3.14, 1.11, 2.22]
  floats_sum = sum_list(floats)
  print(floats_sum == sum(floats))
  print(sum_list.__annotations__)
  print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))
```


`6-main.py`
```python
  #!/usr/bin/env python3

  sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list

  print(sum_mixed_list.__annotations__)
  mixed = [5, 4, 3.14, 666, 0.99]
  ans = sum_mixed_list(mixed)
  print(ans == sum(mixed))
  print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))
```


`7-main.py`
```python
  #!/usr/bin/env python3

  to_kv = __import__('7-to_kv').to_kv

  print(to_kv.__annotations__)
  print(to_kv("eggs", 3))
  print(to_kv("school", 0.02))
```


`8-main.py`
```python
  #!/usr/bin/env python3

  make_multiplier = __import__('8-make_multiplier').make_multiplier
  print(make_multiplier.__annotations__)
  fun = make_multiplier(2.22)
  print("{}".format(fun(2.22)))
```


`9-main.py`
```python
  #!/usr/bin/env python3

  element_length =  __import__('9-element_length').element_length

  print(element_length.__annotations__)
```
