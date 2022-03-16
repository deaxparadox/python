"""an object is an 'awaitable' object if it can be used in an 'awai' expression.
- many asyncio APIs are designed to accept awaitables"""

import asyncio

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()"
    # A coroutine object is created but not awaited
    # so it *won't run at all
    # nested()
    
    # Let's do it differently now and await it
    print(await nested())       # will print "42"

asyncio.run(main())