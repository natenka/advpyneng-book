generator expression (генераторное выражение)
---------------------------------------------

Генераторное выражение использует такой же синтаксис, как list comprehentions, но возвращает итератор, а не список.

Генераторное выражение выглядит точно так же, как list comprehentions, но используются круглые скобки:

.. code:: python

    In [1]: genexpr = (x**2 for x in range(10000))

    In [2]: genexpr
    Out[2]: <generator object <genexpr> at 0xb571ec8c>

    In [3]: next(genexpr)
    Out[3]: 0

    In [4]: next(genexpr)
    Out[4]: 1

    In [5]: next(genexpr)
    Out[5]: 4


Обратите внимание, что это не tuple comprehentions, а генераторное выражение.

Оно полезно в том случае, когда надо работать с большим итерируемым объектом или бесконечным итератором.

