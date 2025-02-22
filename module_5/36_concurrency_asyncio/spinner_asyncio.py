# Example is taken from Fluent Python book

# https://github.com/fluentpython/example-code-2e/blob/master/19-concurrency/spinner_async.py

import asyncio
import itertools
import time

async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        try:
            await asyncio.sleep(.1) 
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

async def slow() -> int:
    time.sleep(7)
    return 42

async def supervisor() -> int:
    spinner = asyncio.create_task(spin('thinking!'))
    print(f'spinner object: {spinner}')
    result = await slow()
    spinner.cancel()
    return result

def main() -> None:
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()
