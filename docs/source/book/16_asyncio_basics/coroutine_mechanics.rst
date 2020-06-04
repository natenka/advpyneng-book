Особенности работы сопрограмм
-----------------------------

`Сопрограмма <https://docs.python.org/3/reference/datamodel.html#coroutine-objects>`__ 
это `awaitable <https://docs.python.org/3/glossary.html#term-awaitable>`__ 
объект. Сопрограммы поддерживают такие методы:

* ``coroutine.send(value)``
* ``coroutine.throw(type[, value[, traceback]])``
* ``coroutine.close()``

Все эти методы не нужно вызывать напрямую, это делает цикл событий и задачи.

Аналогичные методы есть у генераторов, однако сопрограммы не поддерживают итерацию
напрямую.

send
~~~~

.. code:: python

    In [1]: async def do_thing(arg1):
       ...:     print('do_thing', arg1)
       ...:     return 42
       ...:

    In [2]: type(do_thing)
    Out[2]: function

    In [4]: my_coroutine = do_thing(4)

    In [5]: my_coroutine
    Out[5]: <coroutine object do_thing at 0xb4eea4ec>

    In [6]: type(my_coroutine)
    Out[6]: coroutine


Для инициализации сопрограммы, ей передают None с помощью метода send:

.. code:: python

    In [8]: my_coroutine.send(None)
    do_thing 4
    ---------------------------------------------------------------------------
    StopIteration                             Traceback (most recent call last)
    <ipython-input-8-d2b91152dace> in <module>
    ----> 1 my_coroutine.send(None)

    StopIteration: 42

Фактически это никогда не нужно будет делать руками, так как цикл событий
передает это автоматически.

.. code:: python

    In [12]: my_coroutine = do_thing(4)

    In [13]: try:
        ...:     my_coroutine.send(None)
        ...: except StopIteration as exc:
        ...:     print('Result:', exc.value)
        ...:
    do_thing 4
    Result: 42


throw
~~~~~

.. code:: python
