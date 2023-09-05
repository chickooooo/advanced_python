import time
import random
import asyncio


def time_consuming_operation_one() -> int:
    """Some time consuming task

    Returns:
        int: random number
    """
    time.sleep(1)
    return random.randint(0, 99)

def method_one():
    """Main method 1
    """
    print("start")
    # call time cosuming task
    data: int = time_consuming_operation_one()
    print(data)
    print("method 1 finished")

# calling method 1
method_one()

# console logs:
# start
# 5
# method 1 finished


print("\n")


def display_number(task: asyncio.Task[int]):
    """Display task result.

    Args:
        task (asyncio.Task[int]): scheduled task
    """
    print(task.result())

async def time_consuming_operation_two() -> int:
    """Some time consuming task (async)

    Returns:
        int: random number
    """
    time.sleep(1)
    return random.randint(0, 99)

async def method_two():
    """Main method 2 (async)
    """
    print("start")
    # schedule time consuming task
    task = asyncio.create_task(time_consuming_operation_two())
    # add completion callback
    task.add_done_callback(display_number)
    print("method 2 finished")

# run method 2 in event loop
asyncio.run(method_two())

# console logs:
# start
# method 2 finished
# 5
