Автоматическое форматирование кода с Black
------------------------------------------

Black - модуль для автоматического форматирования кода Python.

Установка

```
pip install black
```

Использование:

```
black somefile_or_dir
```

Правила
~~~~~~~~~

.. code:: python

    # in:

    j = [1,
         2,
         3
    ]

    # out:

    j = [1, 2, 3]



.. code:: python

    # in:

    ImportantClass.important_method(exc, limit, lookup_lines, capture_locals, extra_argument)

    # out:

    ImportantClass.important_method(
        exc, limit, lookup_lines, capture_locals, extra_argument
    )


Волшебная запятая
~~~~~~~~~~~~~~~~~

Исключение кода из форматирования
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
