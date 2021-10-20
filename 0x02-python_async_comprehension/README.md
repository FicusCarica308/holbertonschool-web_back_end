![Python Logo](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpluralsight.imgix.net%2Fpaths%2Fpython-7be70baaac.png&f=1&nofb=1)
# 0x02. Python - Async Comprehension


## Learning objectives: 
### Advanced python concepts:
* How to write an asynchronous generator
* How to use async comprehensions
* How to type-annotate generators

## Tasks:

* 0-async_generator.py - A practice coroutine that will loop 10 times, each time asynchronously wait a second, then yield a random number between 0 and 10.
* 1-async_comprehension.py - A practice coroutine that will collect 10 random numbers using an async comprehensing over async_generator (from 0-async_generator), then return the 10 random numbers.
* 2-measure_runtime.py -      will execute async_comprehension four times in parallel using asyncio.gather, then return the total execution time

## Authors
Manuel Enrique Figueroa - [Github](https://github.com/FicusCarica308)

## License
Public Domain. No copy write protection.
