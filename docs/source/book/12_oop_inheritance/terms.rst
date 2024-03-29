Терминология
------------

Интерфейс/Протокол (Interface/Protocol)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Интерфейс - набор атрибутов и методов, которые реализуют определенное поведение. Примеры: итератор, менеджер контекста, последовательность.


Наследование (Inheritance)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Наследование - концепция ООП, которая возволяет дочернему классу использовать компоненты (методы и переменные) родительского класса.

Как правило, для наследования есть две основные причины:

* создание подтипа (interface inheritance)
* наследование для использования кода

В Python синтаксис наследования используется с абстрактными классами для наследования интерфейса/протокола.
Кроме того, синтаксис наследования используется с Mixin.

`Принцип подстановки Барбары Лисков <https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF_%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B8_%D0%91%D0%B0%D1%80%D0%B1%D0%B0%D1%80%D1%8B_%D0%9B%D0%B8%D1%81%D0%BA%D0%BE%D0%B2>`__



Агрегирование (Aggregation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Агрегация (агрегирование по ссылке) — отношение «часть-целое» между двумя равноправными объектами,
когда один объект (контейнер) имеет ссылку на другой объект. 
Оба объекта могут существовать независимо: если контейнер будет уничтожен, то его содержимое — нет.


Композиция (Composition)
~~~~~~~~~~~~~~~~~~~~~~~~

Композиция (агрегирование по значению) — более строгий вариант агрегирования, 
когда включаемый объект может существовать только как часть контейнера. 
Если контейнер будет уничтожен, то и включённый объект тоже будет уничтожен.


.. code:: python

    from jinja2 import Environment, FileSystemLoader

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('router_template.txt')


Полиморфизм (Polymorphism)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Как правило, различают два варианта полиморфизма:

1. способность функции/метода обрабатывать данные разных типов
2. один интерфейс - много реализаций. Пример: одно и то же имя метода в разных классах

Метакласс (Metaclass)
~~~~~~~~~~~~~~~~~~~~~

Метакласс - это класс экземпляры которого тоже являются классами.

Абстрактный класс (abstract class)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Абстрактный класс <https://ru.wikipedia.org/wiki/%D0%90%D0%B1%D1%81%D1%82%D1%80%D0%B0%D0%BA%D1%82%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BB%D0%B0%D1%81%D1%81>`__ - базовый класс, 
который не предполагает создания экземпляров.
Как правило, содержит абстрактные методы - методы, которые обязательно должны быть
созданы в дочерних классах.

В Python абстрактные классы часто используются для создания интерфейса/протокола.


Примесь (Mixin)
~~~~~~~~~~~~~~~

`Примесь <https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%81%D1%8C_(%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)>`__ это класс, который реализует какое-то одно ограниченное поведение (метод).

В Python примеси делаются с помощью классов. Так как в Python нет отдельного типа для примесей,
классам-примесям принято давать имена заканчивающиеся на Mixin.

