import asyncio

class option:
    sleep = 0.5

async def table2():
    for i in range(10):
        print(2*i)
        await asyncio.sleep(option.sleep)
        
        
async def table3():
    for i in range(3):
        print(3*i)
        await asyncio.sleep(option.sleep)

async def table4():
    for i in range(10):
        print(4*i)
        await asyncio.sleep(option.sleep)


async def table5():
    for i in range(10):
        print(5*i)
        await asyncio.sleep(option.sleep)
        
async def table6():
    for i in range(10):
        print(6*i)
        await asyncio.sleep(option.sleep)


        
# async def main1():
#     L = await asyncio.gather(
#         table2(),
#         table3(),
#     )
#     # print(L)
# asyncio.run(main1())

# async def main2():
#     task1 = asyncio.create_task(table2())
#     task2 = asyncio.create_task(table3())
#     await task1
#     await task2 
    
# asyncio.run(main2())


# async def main3():
#     # get an error
#     table2()
#     table3()
#     # right way
#    await table2()
#    await table3()

# asyncio.run(main3())



async def main4():
    '''
    1. task created before (like task, task2) the 
    awaitable function wil run wil run in concurrency 
    with await function (like tabe3), 
    2. But read of the function and task will be 
    run after the table3 in finished
    '''
    
    task = asyncio.create_task(table2())            # 
    task2 = asyncio.create_task(table4())
    
    await table3()                                                      
    await table5()
    
    # this task will run after above await function
    # task3 = asyncio.create_task(table6())
    # await task3
    await asyncio.create_task(table6())

    # await task3
    # await task                                  # task run
    # await task2                                # task2 run 
    
asyncio.run(main4())
