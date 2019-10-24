cycle
~~~~~

Функция cycle создает итератор, которые возвращает элементы итерируемого объекта по кругу:

.. code:: python

    itertools.cycle(iterable)

Пример использования cycle:

.. code:: python

    from itertools import cycle


    spinner = it.cycle('\|/-')
    for _ in range(20):
        print(f'\r{next(spinner)}', end='')
        time.sleep(0.5)


