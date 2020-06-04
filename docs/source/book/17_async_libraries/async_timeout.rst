async-timeout
=============

`Установка <https://github.com/aio-libs/async-timeout>`__ 

::

    $ pip install async-timeout


Пример использования:

.. code:: python

    ssh_coroutine = asyncssh.connect('192.168.100.1', username='cisco', password='cisco')
    async with timeout(20):
        ssh = await asyncio.wait_for(ssh_coroutine, timeout=10)
        writer, reader, stderr = await ssh.open_session(
            term_type="Dumb", term_size=(200, 24))

Может использоваться в ``async with`` и ``with``.
Работает `быстрее чем ``asyncio.wait_for`` <https://stackoverflow.com/a/47004339>`__ потому что wait_for создает новую задачу.
