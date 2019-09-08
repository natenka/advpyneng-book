Abstract Base Classes (ABC)
---------------------------

Иногда, при создании иерархии классов, необходимо чтобы ряд классов поддерживал 
одинаковый интерфейс, например, одинаковый набор методов.
Частично эту задачу можно решить с помощью наследования, однако далеко не всегда
дочерним классам подойдет реализация метода из родительского класса.


Абстрактный класс - это класс в котором созданы абстрактные методы - методы, которые
обязательно должны присутствовать в дочерних классах. Создавть экзепмляр абстрактного
класса нельзя, его надо наследовать и уже у дочернего класса можно создать экземпляр.
При этом экземпляр дочернего класса можно создать только в том случае, если у 
дочернего класса есть реализация всех абстрактных методов.

Базовый пример абстрактного класса:

.. code:: python

    In [1]: import abc

    In [2]: class Parent(abc.ABC):
       ...:     @abc.abstractmethod
       ...:     def get_info(self, parameter):
       ...:         """Get parameter info"""
       ...:
       ...:     @abc.abstractmethod
       ...:     def set_info(self, parameter, value):
       ...:         """Set parameter to value"""
       ...:

Нельзя создать экземпляр класса Parent:

.. code:: python

    In [3]: p1 = Parent()
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-3-0b1eb161869e> in <module>
    ----> 1 p1 = Parent()

    TypeError: Can't instantiate abstract class Parent with abstract methods get_info, set_info

Дочерний класс обязательно должен добавить свою реализацию абстрактных методов, 
иначе при создании экземпляра возникнет исключение:

.. code:: python

    In [4]: class Child(Parent):
       ...:     pass
       ...:

    In [5]: c1 = Child()
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-5-07f905b6a091> in <module>
    ----> 1 c1 = Child()

    TypeError: Can't instantiate abstract class Child with abstract methods get_info, set_info

После создания методов get_info и set_info, можно создать экземпляр класса Child:

.. code:: python

    In [6]: class Child(Parent):
       ...:     def __init__(self):
       ...:         self._parameters = {}
       ...:
       ...:     def get_info(self, parameter):
       ...:         return self._parameters.get(parameter)
       ...:
       ...:     def set_info(self, parameter, value):
       ...:         self._parameters[parameter] = value
       ...:         return self._parameters
       ...:

    In [7]: c1 = Child()

    In [8]: c1.set_info('name', 'BB-8')
    Out[8]: {'name': 'BB-8'}


Пример абстрактного класса BaseSSH:

.. code:: python

    import paramiko
    import time
    import abc


    class BaseSSH(abc.ABC):
        def __init__(self, ip, username, password):
            self.ip = ip
            self.username = username
            self.password = password
            self._MAX_READ = 10000

            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            client.connect(
                hostname=ip,
                username=username,
                password=password,
                look_for_keys=False,
                allow_agent=False)

            self._ssh = client.invoke_shell()
            time.sleep(1)
            self._ssh.recv(self._MAX_READ)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            self._ssh.close()

        def close(self):
            self._ssh.close()

        @abc.abstractmethod
        def send_command(self, command):
            """Send command and get command output"""

        @abc.abstractmethod
        def send_config_commands(self, commands):
            """Send configuration command(s)"""

Соответственно в дочерних классах обязательно должны быть методы 
send_command и send_config_commands:

.. code:: python

    class CiscoSSH(BaseSSH):
        device_type = 'cisco_ios'
        def __init__(self, ip, username, password, enable_password,
                     disable_paging=True):
            super().__init__(ip, username, password)
            self._ssh.send('enable\n')
            self._ssh.send(enable_password + '\n')
            if disable_paging:
                self._ssh.send('terminal length 0\n')
            time.sleep(1)
            self._ssh.recv(self._MAX_READ)

        def send_command(self, command):
            self._ssh.send(command + '\n')
            time.sleep(0.5)
            result = self._ssh.recv(self._MAX_READ).decode('ascii')
            return result

        def config_mode(self):
            self._ssh.send('conf t\n')
            time.sleep(0.5)
            result = self._ssh.recv(self._MAX_READ).decode('ascii')
            return result

        def exit_config_mode(self):
            self._ssh.send('end\n')
            time.sleep(0.5)
            result = self._ssh.recv(self._MAX_READ).decode('ascii')
            return result

        def send_config_commands(self, commands):
            result = self.config_mode()
            result += super().send_config_commands(commands)
            result += self.exit_config_mode()
            return result


.. toctree::
   :maxdepth: 1

   abc_standard_library
