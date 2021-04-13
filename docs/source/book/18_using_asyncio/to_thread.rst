asyncio.to_thread
=================

Сопрограмма ``asyncio.to_thread`` позволяет запустить блокирующую операцию
в потоке. 

Эта сопрограмма появилась в Python 3.9, до этого использовалась ``loop.run_in_executor``.
При этом to_thread это по сути `обертка вокруг loop.run_in_executor <https://github.com/python/cpython/blob/3.9/Lib/asyncio/threads.py>`__
с использованием ThreadPoolExecutor по умолчанию, с максимальным количеством потоков
по умолчанию:

.. code:: python

    async def to_thread(func, /, *args, **kwargs):
        """Asynchronously run function *func* in a separate thread.
        Any *args and **kwargs supplied for this function are directly passed
        to *func*. Also, the current :class:`contextvars.Context` is propogated,
        allowing context variables from the main thread to be accessed in the
        separate thread.
        Return a coroutine that can be awaited to get the eventual result of *func*.
        """
        loop = events.get_running_loop()
        ctx = contextvars.copy_context()
        func_call = functools.partial(ctx.run, func, *args, **kwargs)
        return await loop.run_in_executor(None, func_call)


.. note::

    Начиная с версии Python 3.8 значение по умолчанию для max_workers высчитывается
    так ``min(32, os.cpu_count() + 4)``.

