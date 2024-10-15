# Python - Async
This directory contains the implementation script of Python Async related content.

## Introduction
In Python, `asyncio` is the library that allows concurrent code using `async`/`await` syntax.


## Usage
The following are sampling code.

`0-main.py`
```python
    #!/usr/bin/env python3

    import asyncio

    wait_random = __import__('0-basic_async_syntax').wait_random

    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
```


`1-main.py`
```python
    #!/usr/bin/env python3
    '''
    Test file for printing the correct output of the wait_n coroutine
    '''
    import asyncio

    wait_n = __import__('1-concurrent_coroutines').wait_n

    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
```


`2-main.py`
```python
    #!/usr/bin/env python3

    measure_time = __import__('2-measure_runtime').measure_time

    n = 5
    max_delay = 9

    print(measure_time(n, max_delay))
```


`3-main.py`
```python
    #!/usr/bin/env python3

    import asyncio

    task_wait_random = __import__('3-tasks').task_wait_random

    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
```


`4-main.py`
```python
    #!/usr/bin/env python3

    import asyncio

    task_wait_n = __import__('4-tasks').task_wait_n

    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
```

## Run
To run the files the following approaches can be used

1. Using an executable file
    >[!Note]
    >To make the entry point executable file the following code is needed
    >```bash
    >   chmod u+x filename
    >```
    > The filename is the current main.py file you want to run.
    
```python
    ./[0-4]-main.py
```

2. Without an executable file
This approach may be the simplest one. 

```python
    python3 [0-4]-main.py
```

