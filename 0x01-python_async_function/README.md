![Python Logo](https://www.pngall.com/wp-content/uploads/2016/05/Python-Logo-Free-Download-PNG.png)
# 0x01. Python - Async


## Learning objectives: 
### Advanced python concepts:
* async and await syntax
* How to execute an async program with asyncio
* How to run concurrent coroutines
* How to create asyncio tasks
* How to use the random module


## Tasks:

* 0-basic_async_syntax.py - An asynchronous coroutine named wait_random that takes in an integer argument called max_delay. Waits for a random
    delay between 0 and max_delay returning the final delay.

* 1-concurrent_coroutines.py - Imports wait_random from 0-basic_async_syntax.py then uses an async routine called wait_n that takes in 2 int arguments to
    call it and concurrently based on what is passed to the function. More in documentation...

* 2-measure_runtime.py - A that measures the total execution time for wait_n() from 1-concurrent_coroutines.py
* 3-tasks.py - a function called task_wait_random that takes an integer called max_delay and returns a asyncio.Task.
* 4-tasks.py - second iteration of 3-tasks.py that is identical to 1-concurrent_coroutines.py using 3-tasks.py task_wait_random() function

## Authors
Manuel Enrique Figueroa - [Github](https://github.com/FicusCarica308), [LinkedIn](https://www.linkedin.com/in/manuel-figueroa-292216215)

## License
Public Domain. No copy write protection.
