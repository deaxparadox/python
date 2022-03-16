# import asyncio
# import time 

# async def table1():
#     for i in range(1,11):
#         print(1*i)
#         await asyncio.sleep(1)

# async def table2():
#     for i in range(1,11):
#         print(2*i)
#         await asyncio.sleep(1)

# # async def main():
# #     task1 = asyncio.create_task(table1())
# #     task2 = asyncio.create_task(table2())
# #     await task1
# #     await task2    

# def main():
#     loop = asyncio.get_event_loop()
#     tasks = [
#         loop.create_task(table1()),
#         loop.create_task(table2()),
#     ]
#     loop.run_until_complete(asyncio.wait(tasks))
#     loop.close()
        
    
# if __name__ == "__main__":
#     # asyncio.run(main())
#     main()

import asyncio, time 

async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')