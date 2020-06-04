.. raw:: latex

   \newpage

3. Classmethod, staticmethod, property
======================================

В Python есть ряд полезных встроенных декораторов, которые позволяют менять поведение
методов класса. Декораторы рассматриваются позже довольно подробно.
На данном этапе достаточно знать, что декоратор это синтаксический сахар,
который упрощает запись ``func = decorator(func)`` и позволяет писать так:

.. code:: python

    @decorator
    def func():
        pass

.. toctree::
   :maxdepth: 1

   property
   classmethod
   staticmethod
   ../../exercises/03_exercises.rst
