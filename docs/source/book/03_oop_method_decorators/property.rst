Декоратор property
------------------

Python позволяет создавать и изменять переменные экземпляров:

.. code:: python

    In [1]: class Robot:
       ...:     def __init__(self, name):
       ...:         self.name = name
       ...:

    In [2]: bb8 = Robot('BB-8')

    In [3]: bb8.name
    Out[3]: 'BB-8'

    In [4]: bb8.name = 'R2D2'

    In [5]: bb8.name
    Out[5]: 'R2D2'


Однако иногда нужно сделать так чтобы при изменении/установке значения переменной,
проверялся ее тип или диапазон значений, также иногда необходимо сдедать переменную
неищменяемой и сделать ее доступной только для чтения.
В некоторых языках программирования для этого используются методы get и set,
например:

.. code:: python

    In [9]: class IPAddress:
       ...:     def __init__(self, address, mask):
       ...:         self._address = address
       ...:         self._mask = int(mask)
       ...:
       ...:     def set_mask(self, mask):
       ...:         if not isinstance(mask, int):
       ...:             raise TypeError("Маска должна быть числом")
       ...:         if not mask in range(8, 32):
       ...:             raise ValueError("Маска должна быть в диапазоне от 8 до 32")
       ...:         self._mask = mask
       ...:
       ...:     def get_mask(self):
       ...:         return self._mask
       ...:

    In [10]: ip1 = IPAddress('10.1.1.1', 24)

    In [12]: ip1.set_mask(23)

    In [13]: ip1.get_mask()
    Out[13]: 23

По сравнению со стандартным синтаксисом обращения к атрибутам,
этот вариант выглядит очень громоздко. В Python есть более компактный
вариант сделать то же самое - property.

Property как правило, используется как декоратор метода и превращает метод
в переменную экземпляра с точки зрения пользователя класса.

Пример создания property:

.. code:: python

    In [14]: class IPAddress:
        ...:     def __init__(self, address, mask):
        ...:         self._address = address
        ...:         self._mask = int(mask)
        ...:
        ...:     @property
        ...:     def mask(self):
        ...:         return self._mask
        ...:

Теперь можно обращаться к mask как к обычной переменной:

.. code:: python

    In [15]: ip1 = IPAddress('10.1.1.1', 24)

    In [16]: ip1.mask
    Out[16]: 24

Один из плюсов property - переменная становится доступной только для чтения:

.. code:: python

    In [17]: ip1.mask = 30
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-17-e153170a5893> in <module>
    ----> 1 ip1.mask = 30

    AttributeError: can't set attribute

Также property позволяет добавлять метод setter, который будет отвечать 
за изменение значения переменной и, так как это тоже метод, позволяет
включить логику с проверкой или динамическим вычислением значения.
