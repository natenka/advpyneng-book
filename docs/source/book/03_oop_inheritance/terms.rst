Терминология
------------

Полиморфизм 
Метакласс
ABC
Mixin


Composition
~~~~~~~~~~~

Environment has-a FileSystemLoader:

.. code:: python

    from jinja2 import Environment, FileSystemLoader

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('router_template.txt')


.. inheritance-diagram:: netmiko

