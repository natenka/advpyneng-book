Переменные класса
~~~~~~~~~~~~~~~~~

Помимо переменных экземпляра, существуют также переменные класса. Они
создаются, при указании переменных внутри самого класса, не метода:

.. code:: python

    In [1]: class CiscoSSH:
       ...:     device_type = 'cisco_ios'
       ...:
       ...:     def send_command(self, command):
       ...:         pass
       ...:

Теперь не только у класса, но и у каждого экземпляра класса будет
переменная ``device_type``:

.. code:: python

    In [2]: CiscoSSH.device_type
    Out[2]: 'cisco_ios'

    In [3]: r1 = CiscoSSH()

    In [4]: r1.device_type
    Out[4]: 'cisco_ios'

    In [5]: r2 = CiscoSSH()

    In [6]: r2.device_type
    Out[6]: 'cisco_ios'

Важный момент при использовании переменных класса, то что внутри метода
к ним все равно надо обращаться через имя класса. Для
начала, вариант обращения без имени класса:

.. code:: python

    In [7]: class CiscoSSH:
       ...:     device_type = 'cisco_ios'
       ...:
       ...:     def send_command(self, command):
       ...:         print(device_type)
       ...:

    In [8]: r1 = CiscoSSH()

    In [9]: r1.send_command()
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-9-921b8733dbee> in <module>()
    ----> 1 r1.send_command()

    <ipython-input-7-ef923c4e39d3> in send_command(self, command)
          3
          4     def send_command(self, command):
    ----> 5         print(device_type)
          6

    NameError: name 'device_type' is not defined

И правильный вариант:

.. code:: python

    In [10]: class CiscoSSH:
        ...:     device_type = 'cisco_ios'
        ...:
        ...:     def send_command(self, command):
        ...:         print(CiscoSSH.device_type)
        ...:

    In [11]: r1 = CiscoSSH()

    In [12]: r1.send_command()
    'cisco_ios'

