Mixin классы
------------

Mixin классы - это классы у которых нет данных, но есть методы.
Mixin используются для добавления одних и тех же методов в разные
классы.

С одной стороны, то же самое можно сделать с помощью наследования,
но не всегда те методы, которые нужны в разных дочерних классах,
имеют смысл в родительском.

.. code:: python

    class Shape:
        def perimeter(self):
            return self.width * 2 + self.length * 2


    class Circle(Shape):
        pass

    class Rectangle(Shape):
        pass

    class Square(Shape):
        pass

