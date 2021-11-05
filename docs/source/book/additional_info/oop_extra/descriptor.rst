Дескриптор
----------


.. code:: python

    class IPAddress:

        def __init__(self, ip, mask):
            self._ip = ip
            self._mask = mask

        @property
        def ip(self):
            return self._ip

        @ip.setter
        def ip(self, value):
            if not isinstance(value, str):
                raise TypeError('Wrong data type, expected str')
            self._ip = value

        @property
        def mask(self):
            return self._mask

        @mask.setter
        def mask(self, value):
            if not isinstance(value, int):
                raise TypeError('Wrong data type, expected int')
            self._mask = mask



.. code:: python

    class Integer:
        def __init__(self, name):
            self.name = name

        def __get__(self, instance, cls):
            return instance.__dict__[self.name]

        def __set__(self, instance, value):
            if not isinstance(value, int):
                raise TypeError('Wrong data type, expected int')
            instance.__dict__[self.name] = value

    class String:
        def __init__(self, name):
            self.name = name

        def __get__(self, instance, cls):
            return instance.__dict__[self.name]

        def __set__(self, instance, value):
            if not isinstance(value, str):
                raise TypeError('Wrong data type, expected str')
            instance.__dict__[self.name] = value

Дескриптор обязательно должен быть указан на уровне класса:

.. code:: python

    class IPAddress:
        mask = Integer('mask')
        ip = String('ip')

        def __init__(self, ip, mask):
            self._ip = ip
            self._mask = mask


    In [90]: ip1 = IPAddress('10.1.1.1', 28)

    In [96]: ip1.mask = '24'
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-96-247b3f37d10f> in <module>
    ----> 1 ip1.mask = '24'

    <ipython-input-93-5812cdd26ed1> in __set__(self, instance, value)
          8         def __set__(self, instance, value):
          9             if not isinstance(value, int):
    ---> 10                 raise TypeError('Wrong data type, expected int')
         11             instance.__dict__[self.name] = value
         12

    TypeError: Wrong data type, expected int

    In [97]: ip1.ip = 142
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-97-24102e80dc3a> in <module>
    ----> 1 ip1.ip = 142

    <ipython-input-93-5812cdd26ed1> in __set__(self, instance, value)
         20         def __set__(self, instance, value):
         21             if not isinstance(value, str):
    ---> 22                 raise TypeError('Wrong data type, expected str')
         23             instance.__dict__[self.name] = value

    TypeError: Wrong data type, expected str

Оптимизированный вариант:

.. code:: python

    class Typed:
        attr_type = object

        def __init__(self, name):
            self.name = name

        def __get__(self, instance, cls):
            return instance.__dict__[self.name]

        def __set__(self, instance, value):
            if not isinstance(value, self.attr_type):
                raise TypeError(f'Wrong data type, expected {self.attr_type}')
            instance.__dict__[self.name] = value

    class Integer(Typed):
        attr_type = int

    class String(Typed):
        attr_type = str


Замыкания вместо дескриптора для проверки типа
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    In [74]: def typed(name, attr_type):
        ...:     value = '_' + name
        ...:
        ...:     @property
        ...:     def attribute(self):
        ...:         return getattr(self, value)
        ...:
        ...:     @attribute.setter
        ...:     def attribute(self, new_value):
        ...:         if not isinstance(new_value, attr_type):
        ...:             raise TypeError(f'Wrong data type, expected {attr_type}')
        ...:         self.value = new_value
        ...:
        ...:     return attribute
        ...:

    In [75]: class IPAddress:
        ...:     ip = typed('ip', str)
        ...:     mask = typed('mask', int)
        ...:
        ...:     def __init__(self, ip, mask):
        ...:         self.ip = ip
        ...:         self.mask = mask
        ...:

    In [76]: ip1 = IPAddress('10.1.1.1', 28)

    In [77]: ip1.mask = '24'
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-77-247b3f37d10f> in <module>
    ----> 1 ip1.mask = '24'

    <ipython-input-74-4348b0de06dc> in attribute(self, new_value)
          9     def attribute(self, new_value):
         10         if not isinstance(new_value, attr_type):
    ---> 11             raise TypeError(f'Wrong data type, expected {attr_type}')
         12         setattr(self, value, new_value)
         13

    TypeError: Wrong data type, expected <class 'int'>

    In [80]: ip1.mask?
    Type:        property
    String form: <property object at 0xb4203aa4>
    Docstring:   <no docstring>


Дополнительные материалы
~~~~~~~~~~~~~~~~~~~~~~~~

* `Invoking Descriptors <https://docs.python.org/3/reference/datamodel.html#invoking-descriptors>`__
* `Descriptor HowTo Guide <https://docs.python.org/3/howto/descriptor.html>`__
