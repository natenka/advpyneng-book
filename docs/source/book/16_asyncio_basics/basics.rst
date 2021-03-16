Сопрограммы и задачи
====================

Создание сопрограммы (coroutine):

.. code:: python

    import asyncio

    async def main():
        print(f'Start {datetime.now()}')
        await asyncio.sleep(3)
        print(f'End   {datetime.now()}')


    In [6]: coro = main()

    In [7]: coro
    Out[7]: <coroutine object main at 0xb449fdac>


Как и с генераторами, различают:

* функцию сопрограмму - функция, которая создается с помощью ``async def``
* объект сопрограмму - объект, который возвращается при вызове функции сопрограммы

Создать сопрограмму недостаточно для того чтобы она запускалась
параллельно с другими сопрограммами - для управления сопрограммами нужен
менеджер - event loop. Также по умолчанию в сопрограмме код выполняется последовательно
и надо явно указывать в каких местах можно переключаться - await.


Запустить сопрограмму можно несколькими способами:

* asyncio.run
* await
* asyncio.create_task


asyncio.run
-----------

Функция asyncio.run запускает сопрограмму и возвращает результат:

.. code:: python

    asyncio.run(coro, *, debug=False)

Функция asyncio.run всегда создает новый цикл событий и закрывает его в конце.
В идеале, функция asyncio.run должна вызываться в программе только один раз и использоваться
как основная точка входа.
Эту функцию нельзя вызвать, когда в том же потоке запущен другой цикл событий.

Запуск с помощью asyncio.run:

.. code:: python

    In [8]: asyncio.run(coro)
    Start 2019-10-30 06:36:03.396389
    End   2019-10-30 06:36:06.399606


    In [9]: asyncio.run(main())
    Start 2019-10-30 06:46:22.162731
    End   2019-10-30 06:46:25.166902

await
-----

Второй вариант запуска сопрограммы - ожидание ее результата в другой сопрограмме
с помощью ``await``.

Сопрограмма delay_print выводит указанное сообщение с задержкой:

.. code:: python

    In [2]: from datetime import datetime

    In [3]: async def delay_print(delay, task_name):
       ...:     print(f'>>> start {task_name}')
       ...:     await asyncio.sleep(delay)
       ...:     print(f'<<< end   {task_name}')
       ...:

Для запуска сопрограммы delay_print, ее результат ожидается в сопрограмме main:

.. code:: python

    In [4]: async def main():
       ...:     print(f'Start {datetime.now()}')
       ...:     await delay_print(4, 'task1')
       ...:     await delay_print(2, 'task2')
       ...:     print(f'End   {datetime.now()}')
       ...:

    In [5]: asyncio.run(main())
    Start 2021-03-16 09:54:42.163949
    >>> start task1
    <<< end   task1
    >>> start task2
    <<< end   task2
    End   2021-03-16 09:54:48.172434

Обратите внимание на время выполнения main - в данном случае сопрограммы выполнились
последовательно и суммарное время 6 секунд.

asyncio.create_task
-------------------

Еще один вариант запуска сопрограммы - это создание задачи (task).
Обернуть сопрограмму в задачу и запланировать ее выполнение можно с помощью функции
asyncio.create_task. Она возвращает объект Task, который можно ожидать с await, как
и сопрограммы.

.. code:: python

    asyncio.create_task(coro)

Функция asyncio.create_task позволяет запускать сопрограммы одновременно, так как
создание задачи означает для цикла, что надо запустить эту сопрограмму при первой
возможности.

Пример создания задач:

.. code:: python

    In [6]: async def delay_print(delay, task_name):
       ...:     print(f'>>> start {task_name}')
       ...:     await asyncio.sleep(delay)
       ...:     print(f'<<< end   {task_name}')
       ...:

    In [7]: async def main():
       ...:     print(f'Start {datetime.now()}')
       ...:     task1 = asyncio.create_task(delay_print(4, 'task1'))
       ...:     task2 = asyncio.create_task(delay_print(2, 'task2'))
       ...:
       ...:     await asyncio.sleep(1)
       ...:     print("Все задачи запущены")
       ...:
       ...:     await task1
       ...:     await task2
       ...:     print(f'End   {datetime.now()}')
       ...:

    In [8]: asyncio.run(main())
    Start 2021-03-16 09:58:10.817222
    >>> start task1
    >>> start task2
    Все задачи запущены
    <<< end   task2
    <<< end   task1
    End   2021-03-16 09:58:14.821104

При выполнении строк с созданием задач, выполнение сопрограмм уже запланировано
и цикл событий их запустит, как только появится возможность.
При этом обе сопрограммы уже будут работать и await уже только ждет их результат.

Что именно использовать await или create_task для запуска сопрограмм, зависит от
ситуации. Некоторые действия внутри функции должны выполняться последовательно,
некоторые могут выполняться параллельно.

Например, если есть две сопрограмы get_command_output и parse_command_output:

.. code:: python

    async def get_command_output(device_ip, show_command):
        print(f">>> Start get_command_output {device_ip}")
        await asyncio.sleep(1)
        print(f"<<< End  get_command_output  {device_ip}")


    async def parse_command_output(output):
        print(">>> Start parse_command_output")
        await asyncio.sleep(1)
        print("<<< End parse_command_output")


Внутри функции, которая должна получить вывод команды и распарсить его,
эти функции надо вызывать последовательно, не параллельно, поэтому используется await:

.. code:: python

    async def get_and_parse_show_command(device, command):
        print(f"### Start get_and_parse_show_command {device}")
        output = await get_command_output(device, command)
        parsed_data = await parse_command_output(output)
        print(f"### End   get_and_parse_show_command {device}")

При этом саму функцию get_and_parse_show_command можно запускать параллельно
для разных устройств, поэтому используем create_task.

.. code:: python

    async def main():
        print(f'Start {datetime.now()}')
        tasks = [asyncio.create_task(get_and_parse_show_command(ip, "sh ip int br"))
                 for ip in ["10.1.1.1", "10.2.2.2", "10.3.3.3"]]
        results = [await t for t in tasks]
        print(f'End {datetime.now()}')

    In [15]: asyncio.run(main())
    Start 2021-03-16 10:29:24.280408
    ### Start get_and_parse_show_command 10.1.1.1
    >>> Start get_command_output 10.1.1.1
    ### Start get_and_parse_show_command 10.2.2.2
    >>> Start get_command_output 10.2.2.2
    ### Start get_and_parse_show_command 10.3.3.3
    >>> Start get_command_output 10.3.3.3
    <<< End  get_command_output  10.1.1.1
    >>> Start parse_command_output
    <<< End  get_command_output  10.2.2.2
    >>> Start parse_command_output
    <<< End  get_command_output  10.3.3.3
    >>> Start parse_command_output
    <<< End parse_command_output
    ### End   get_and_parse_show_command 10.1.1.1
    <<< End parse_command_output
    ### End   get_and_parse_show_command 10.2.2.2
    <<< End parse_command_output
    ### End   get_and_parse_show_command 10.3.3.3
    End 2021-03-16 10:29:26.286659

