Полезные встроенные функции
---------------------------

Работа с атрибутами объекта
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Функции hasattr, getattr, delattr, setattr.

hasattr:

.. code:: python

    class Test:
        def __init__(self, name):
            self.name = name

        def method1(self):
            print("method1")


    In [7]: t1 = Test("object1")

    In [8]: hasattr(t1, "name")
    Out[8]: True

    In [9]: hasattr(t1, "test")
    Out[9]: False

    In [10]: hasattr(t1, "method1")
    Out[10]: True

getattr

.. code:: python

    In [11]: getattr(t1, "method1")
    Out[11]: <bound method Test.method1 of <__main__.Test object at 0xb5213ef8>>

    In [12]: getattr(t1, "name")
    Out[12]: 'object1'

    In [13]: getattr(t1, "test")
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-13-200257dcfffb> in <module>
    ----> 1 getattr(t1, "test")

    AttributeError: 'Test' object has no attribute 'test'

    In [14]: getattr(t1, "test", None)

    In [15]: getattr(t1, "test", False)
    Out[15]: False



setattr

.. code:: python

    In [16]: setattr(t1, "test", False)

    In [17]: t1.test
    Out[17]: False


delattr

.. code:: python

    In [19]: delattr(t1, "test")

    In [20]: t1.test
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-20-8ad1d771f5eb> in <module>
    ----> 1 t1.test

    AttributeError: 'Test' object has no attribute 'test'



vars
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    class Test:
        def __init__(self, name):
            self.name = name

        def method1(self):
            print("method1")


.. code:: python

    In [22]: vars(Test)
    Out[22]:
    mappingproxy({'__module__': '__main__',
                  '__init__': <function __main__.Test.__init__(self, name)>,
                  'method1': <function __main__.Test.method1(self)>,
                  '__dict__': <attribute '__dict__' of 'Test' objects>,
                  '__weakref__': <attribute '__weakref__' of 'Test' objects>,
                  '__doc__': None})

.. code:: python

    In [23]: t1 = Test("object1")

    In [24]: vars(t1)
    Out[24]: {'name': 'object1'}


isinstance, issubclass
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    In [39]: from collections.abc import Iterator, Iterable

    In [40]: vlans = [1, 2, 3]

    In [41]: isinstance(vlans, list)
    Out[41]: True

    In [42]: isinstance(vlans, Iterable)
    Out[42]: True

    In [43]: isinstance(vlans, Iterator)
    Out[43]: False


callable
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    def summ(a, b):
        print(locals())
        return a + b


    In [36]: callable(summ)
    Out[36]: True

    In [37]: callable(Test)
    Out[37]: True

    In [38]: callable(t1)
    Out[38]: False


dir
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    class Test:
        def __init__(self, name):
            self.name = name

        def method1(self):
            print("method1")


    In [34]: dir(Test)
    Out[34]:
    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     'method1']


eval, exec
~~~~~~~~~~~~~~~~~~~~~~~~~~~

eval

.. code:: python

    In [29]: eval("10 + 5")
    Out[29]: 15

exec

.. code:: python

    upper_func = """
    def upper(string):
        return string.upper()
    """

    In [31]: exec(upper_func)

    In [32]: upper("test")
    Out[32]: 'TEST'



locals, globals
~~~~~~~~~~~~~~~~~~~~~~~~~~~

globals

.. code:: python

    In [25]: globals()
    Out[25]:
    {'__name__': '__main__',
     '__doc__': 'Automatically created module for IPython interactive environment',
     '__package__': None,
     '__loader__': None,
     '__spec__': None,
     '__builtin__': <module 'builtins' (built-in)>,
     '__builtins__': <module 'builtins' (built-in)>,
     ...

locals

.. code:: python

    def summ(a, b):
        print(locals())
        return a + b


    In [28]: summ(3, 4)
    {'a': 3, 'b': 4}
    Out[28]: 7


