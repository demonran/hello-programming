import json

import aio_pika
import asyncio

async def main(loop):
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/", loop = loop
    )

    queue_name = "test"

    async with connection:
        channel: aio_pika.abc.AbstractChannel = await connection.channel()
        queue: aio_pika.abc.AbstractQueue = await channel.declare_queue(queue_name, auto_delete=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    print(message.body)
                    if data.request_id != current_id:
                        return
                    data.task
                    # json_data = json.loads(message.body)
                    # handler(json_data)

def connect_nat():
    print("执行完了")
    curl("http://sxx.com/result?task=connect_nat&status=success&request_id=current_id")
def handler(json_data):
    if json_data['step'] == 1:
        step2()
    if json_data['step'] == 2:
        step3()


def step1():
    print("创建任务1")


def step2():
    print("创建任务2")

process_table

processId, task_id next_id, rule
1,1, 2   ,status = succ
1, 2, 4
2, 1, 3
2, 3, 100
2, 100, 99

task_table
start
1 task1
2 task2
3 task3
4. task4
...
100 task100
end
@app.route("result")
def result(request_id, task, status):



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
