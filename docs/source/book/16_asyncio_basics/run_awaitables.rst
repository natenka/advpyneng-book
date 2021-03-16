Запуск нескольких awaitables
============================

Тут рассматриваются функции, которые позволяют запускать несколько сопрограмм
или задач:

* asyncio.gather
* asyncio.as_completed

.. note::

    Кроме функций gather и as_completed, несколько awaitables может запускать и
    функция wait, но она рассматривается позже, в 18 разделе.
    

asyncio.gather
--------------

Функция gather запускает на выполнение awaitable объекты, которые перечислены в
последовательности ``aws``:

.. code:: python

    asyncio.gather(*aws, return_exceptions=False)

Если какие-то из объектов являются сопрограммами, они автоматически оборачиваются в задачи
и планируются на выполнение уже как объекты Task.

В данном примере функция connect_ssh якобы делает подключение к устройству по SSH
и отправляет команду. Все реальные действия пока заменены на asyncio.sleep.
В зависимости от числа, которое передается как аргумент, выполнение сопрограмм, которые
возвращает функция connect_ssh, занимает разное время.
Функция send_command_to_devices создает сопрограммы с помощью map и запускает их на
выполнение с помощью asyncio.gather:

.. code:: python

    async def connect_ssh(ip, command):
        print(f'Подключаюсь к {ip}')
        await asyncio.sleep(ip)
        print(f'Отправляю команду {command} на устройство {ip}')
        await asyncio.sleep(1)
        return f"{command} {ip}"


    async def send_command_to_devices(ip_list, command):
        coroutines = map(connect_ssh, ip_list, repeat(command))
        result = await asyncio.gather(*coroutines)
        return result

Если все объекты отработали корректно, asyncio.gather вернет список со значениями,
которые вернули объекты. Порядок значений в списке соответствует порядку объектов:

.. code:: python

    In [2]: ip_list = [5, 2, 3, 7]

    In [3]: result = asyncio.run(send_command_to_devices(ip_list, 'test'))
    Подключаюсь к 5
    Подключаюсь к 2
    Подключаюсь к 3
    Подключаюсь к 7
    Отправляю команду test на устройство 2
    Отправляю команду test на устройство 3
    Отправляю команду test на устройство 5
    Отправляю команду test на устройство 7

    In [4]: result
    Out[4]: ['test 5', 'test 2', 'test 3', 'test 7']

Если return_exceptions равно False (по умолчанию), при возникновении исключения,
оно появляется в том месте, где ожидается (await) результат asyncio.gather:

.. code:: python

    async def connect_ssh(ip, command):
        print(f'Подключаюсь к {ip}')
        await asyncio.sleep(ip)
        if ip == 3:
            raise OSError(f'Не могу подключиться к {ip}')
        print(f'Отправляю команду {command} на устройство {ip}')
        await asyncio.sleep(1)
        return f"{command} {ip}"


    In [11]: result = asyncio.run(send_command_to_devices(ip_list, 'test'))
    Подключаюсь к 5
    Подключаюсь к 2
    Подключаюсь к 3
    Подключаюсь к 7
    Отправляю команду test на устройство 2
    ---------------------------------------------------------------------------
    OSError                                   Traceback (most recent call last)
    <ipython-input-11-4c2a35eaf7cd> in <module>
    ----> 1 result = asyncio.run(send_command_to_devices(ip_list, 'test'))
    ...

    <ipython-input-1-7f470cb98776> in send_command_to_devices(ip_list, command)
         13 async def send_command_to_devices(ip_list, command):
         14     coroutines = map(connect_ssh, ip_list, repeat(command))
    ---> 15     result = await asyncio.gather(*coroutines)
         16     return result

    <ipython-input-10-5e26dce87ca7> in connect_ssh(ip, command)
          3     await asyncio.sleep(ip)
          4     if ip == 3:
    ----> 5         raise OSError(f'Не могу подключиться к {ip}')
          6     print(f'Отправляю команду {command} на устройство {ip}')
          7     await asyncio.sleep(1)

    OSError: Не могу подключиться к 3

Если return_exceptions равно True, исключение попадает в список как результат:

.. code:: python

    async def connect_ssh(ip, command):
        print(f'Подключаюсь к {ip}')
        await asyncio.sleep(ip)
        if ip == 3:
            raise OSError(f'Не могу подключиться к {ip}')
        print(f'Отправляю команду {command} на устройство {ip}')
        await asyncio.sleep(1)
        return f"{command} {ip}"


    async def send_command_to_devices(ip_list, command):
        coroutines = map(connect_ssh, ip_list, repeat(command))
        result = await asyncio.gather(*coroutines, return_exceptions=True)
        return result


    In [14]: result = asyncio.run(send_command_to_devices(ip_list, 'test'))
    Подключаюсь к 5
    Подключаюсь к 2
    Подключаюсь к 3
    Подключаюсь к 7
    Отправляю команду test на устройство 2
    Отправляю команду test на устройство 5
    Отправляю команду test на устройство 7

    In [15]: result
    Out[15]: ['test 5', 'test 2', OSError('Не могу подключиться к 3'), 'test 7']

    In [16]: result[2]
    Out[16]: OSError('Не могу подключиться к 3')

    In [17]: isinstance(result[2], Exception)
    Out[17]: True


asyncio.as_completed
--------------------

Функция as_completed запускает на выполнение awaitable объекты, которые перечислены
в последовательности aws:

.. code:: python

    asyncio.as_completed(aws, *, timeout=None)

Возвращает итератор с сопрограмами, в порядке получения результата от сопрограмм.
Функция генерирует исключение asyncio.TimeoutError, если за timeout отработали не
все сопрограмы.

Пример использования as_completed:

.. code:: python

    async def delay_print(task_name):
        delay = round(random.random() * 10, 2)
        print(f'>>> start {task_name} sleep {delay}')
        await asyncio.sleep(delay)
        print(f'<<< end   {task_name}')
        return task_name


    async def main():
        coroutines = [delay_print(f"task {i}") for i in range(1, 6)]
        for cor in asyncio.as_completed(coroutines):
            cor_result = await cor
            print(f"DONE {cor_result}")

Результаты возвращаются в порядке отрабатывания сопрограм, а не в порядке их запуска:

.. code:: python

    In [27]: asyncio.run(main())
    >>> start task 2 sleep 8.93
    >>> start task 1 sleep 0.03
    >>> start task 4 sleep 8.33
    >>> start task 5 sleep 3.43
    >>> start task 3 sleep 5.09
    <<< end   task 1
    DONE task 1
    <<< end   task 5
    DONE task 5
    <<< end   task 3
    DONE task 3
    <<< end   task 4
    DONE task 4
    <<< end   task 2
    DONE task 2

Это может быть полезно когда сразу после получения результата, надо запускать следующую
операцию. Например, в примере ниже сразу после получения результата сопрограмы, идет запись
результата в файл:

.. code:: python

    import asyncio
    import time
    from datetime import datetime
    import random


    async def connect_ssh(ip, command):
        print(f"Подключаюсь к {ip}")
        await asyncio.sleep(1)
        print(f"Отправляю команду {command}")
        await asyncio.sleep(random.random() * 10)
        print(f"Получен результат от {ip}")
        return ip, command


    async def write_to_file(filename, data):
        print(f">>> Записываю результат в файл {filename}")
        await asyncio.sleep(1)
        print(f"<<< Результат записан в файл {filename}")


    async def main():
        ip_list = ["10.1.1.1", "10.1.1.2", "10.1.1.3", "10.1.1.4"]
        coroutines = [connect_ssh(ip, "sh clock") for ip in ip_list]
        tasks = []
        for coro in asyncio.as_completed(coroutines):
            result = await coro
            tasks.append(asyncio.create_task(write_to_file(f"{result[0]}.txt", result)))
        await asyncio.gather(*tasks)


    if __name__ == "__main__":
        asyncio.run(main())
