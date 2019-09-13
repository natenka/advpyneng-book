Терминология и примеры
----------------------

Интерфейс/Протокол (Interface/Protocol)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Интерфейс - набор атрибутов и методов, которые реализуют определенное поведение. Примеры: итератор, менеджер контекста, последовательность.


Наследование (Inheritance)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Наследование реализации (implementation inheritance).

``Принцип подстановки Барбары Лисков <https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF_%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B8_%D0%91%D0%B0%D1%80%D0%B1%D0%B0%D1%80%D1%8B_%D0%9B%D0%B8%D1%81%D0%BA%D0%BE%D0%B2>``

Наследование интерфейса (interface inheritance).

В Python синтаксис наследования используется с абстрактными классами для наследования интерфейса/протокола.

Кроме того, синтаксис наследования используется с Mixin.


Композиция (Composition)
~~~~~~~~~~~~~~~~~~~~~~~~

Environment has-a FileSystemLoader:

.. code:: python

    from jinja2 import Environment, FileSystemLoader

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('router_template.txt')


Полиморфизм (Polymorphism)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Метакласс (Metaclass)
~~~~~~~~~~~~~~~~~~~~~

Абстрактный базовый класс (abstract base class)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ABC


Примесь (Mixin)
~~~~~~~~~~~~~~~

