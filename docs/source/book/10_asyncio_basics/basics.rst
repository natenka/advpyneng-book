Сопрограммы и задачи
====================

Создание сопрограммы:

.. code:: python

    In [1]: import asyncio

    In [2]: async def main():
       ...:     print(f'Start {datetime.now()}')
       ...:     await asyncio.sleep(3)
       ...:     print(f'End   {datetime.now()}')
       ...:

    In [6]: coro = main()

    In [7]: coro
    Out[7]: <coroutine object main at 0xb449fdac>


Создать сопрограмму недостаточно для того чтобы она запускалась
параллельно с другими сопрограммами - для управления сопрограммами нужен
менеджер - event loop. Также по умолчанию в сопрограмме код выполняется последовательно
и надо явно указывать в каких местах можно переключаться - await.


Запустить сопрограмму можно несколькими способами:

* asyncio.run
* await
* asyncio.create_task
* asyncio.gather


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

Сопрограмма delay_message выводит указанное сообщение с задержкой:

.. code:: python

    In [10]: from datetime import datetime

    In [11]: async def delay_message(delay, message):
        ...:     await asyncio.sleep(delay)
        ...:     print(message)
        ...:

Для запуска сопрограммы delay_message, ее результат ожидается в сопрограмме main:

.. code:: python

    In [12]: async def main():
        ...:     print(f'Start {datetime.now()}')
        ...:     await delay_message(4, 'Hello')
        ...:     await delay_message(2, 'world')
        ...:     print(f'End   {datetime.now()}')
        ...:

    In [13]: asyncio.run(main())
    Start 2019-10-30 06:29:43.828145
    Hello
    world
    End   2019-10-30 06:29:49.835494

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

    In [42]: async def delay_message(delay, message):
        ...:     print('>>> start delay_message')
        ...:     await asyncio.sleep(delay)
        ...:     print('<<<', message)
        ...:

    In [43]: async def main():
        ...:     print(f'Start {datetime.now()}')
        ...:     task1 = asyncio.create_task(delay_message(4, 'Hello'))
        ...:     task2 = asyncio.create_task(delay_message(2, 'world'))
        ...:
        ...:     await task1
        ...:     await task2
        ...:     print(f'End {datetime.now()}')
        ...:

    In [44]: asyncio.run(main())
    Start 2019-10-30 10:18:39.489131
    >>> start delay_message
    >>> start delay_message
    <<< world
    <<< Hello
    End 2019-10-30 10:18:43.494321

При выполнении строк с созданием задач, выполнение сопрограмм уже запланировано
и цикл событий их запустит, как только появится возможность.

.. code:: python

    task1 = asyncio.create_task(delay_message(4, 'Hello'))
    task2 = asyncio.create_task(delay_message(2, 'world'))



.. code:: python
.. code:: python
.. code:: python
.. code:: python
.. code:: python
.. code:: python

