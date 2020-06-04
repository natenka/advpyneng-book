pydantic
--------

pydantic использует аннотацию типов для проверки данных.

Пример создания dataclass:

.. code:: python

    In [9]: from dataclasses import dataclass

    In [10]: @dataclass
        ...: class Book:
        ...:     title: str
        ...:     price: int
        ...:

В этом случае, аннотация переменных используется для создания атрибутов, но при этом
тип данных не проверяется и все эти варианты отработают:

.. code:: python

    In [11]: book = Book('Good Omens', price=35)

    In [12]: book = Book('Good Omens', price='35')

    In [13]: book = Book('Good Omens', price='a')

При использовании декоратора dataclass из модуля pydantic, типы проверяются:

.. code:: python

    In [14]: from pydantic.dataclasses import dataclass

    In [15]: @dataclass
        ...: class Book:
        ...:     title: str
        ...:     price: int
        ...:

    In [16]: book = Book('Good Omens', price=35)

    In [17]: book = Book('Good Omens', price='35')

    In [18]: book = Book('Good Omens', price='a')
    ---------------------------------------------------------------------------
    ValidationError                           Traceback (most recent call last)
    <ipython-input-18-c21f0df3a6ac> in <module>
    ----> 1 book = Book('Good Omens', price='a')

    <string> in __init__(self, title, price)

    ~/venv/pyneng-py3-7/lib/python3.7/site-packages/pydantic/dataclasses.cpython-37m-i386-linux-gnu.so in pydantic.dataclasses._process_class._pydantic_post_init()

    ValidationError: 1 validation error for Book
    price
      value is not a valid integer (type=type_error.integer)

    In [19]: book = Book('Good Omens', price='35')

    In [20]: book.price
    Out[20]: 35


`Примеры использования pydantic <https://github.com/samuelcolvin/pydantic/tree/master/docs/examples>`__
