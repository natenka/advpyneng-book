Mixin классы
------------

Mixin классы - это классы у которых нет данных, но есть методы.
Mixin используются для добавления одних и тех же методов в разные
классы.

В Python примеси делаются с помощью классов. Так как в Python нет отдельного типа 
для примесей, классам-примесям принято давать имена заканчивающиеся на Mixin.

С одной стороны, то же самое можно сделать с помощью наследования обычных классов,
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

.. code:: python

    import time
    import inspect
    from base_ssh import BaseSSH


    class SourceCodeMixin:
        @property
        def sourcecode(self):
            return inspect.getsource(self.__class__)


    class AttributesMixin:
        @property
        def attributes(self):
            # data attributes
            for name, value in self.__dict__.items():
                print(f"{name:25}{str(value):<20}")
            # methods
            for name, value in self.__class__.__dict__.items():
                if not name.startswith('__'):
                    print(f"{name:25}{str(value):<20}")


.. code:: python

    In [1]: from mixin_example import CiscoSSH

    In [2]: r1 = CiscoSSH('192.168.100.1', 'cisco', 'cisco', 'cisco')

    In [3]: r1.attributes
    ip                       192.168.100.1
    username                 cisco
    password                 cisco
    _MAX_READ                10000
    _ssh                     <paramiko.Channel 0 (open) window=8161 -> <paramiko.Transport at 0xb36a412c (cipher aes128-cbc, 128 bits) (active; 1 open channel(s))>>
    config_mode              <function CiscoSSH.config_mode at 0xb36a15cc>
    exit_config_mode         <function CiscoSSH.exit_config_mode at 0xb36a1614>
    send_config_commands     <function CiscoSSH.send_config_commands at 0xb36a165c>


    In [4]: print(r1.sourcecode)
    class CiscoSSH(SourceCodeMixin, AttributesMixin, BaseSSH):
        def __init__(self, ip, username, password, enable_password,
                     disable_paging=True):
            super().__init__(ip, username, password)
            self._ssh.send('enable\n')
            self._ssh.send(enable_password + '\n')
            if disable_paging:
                self._ssh.send('terminal length 0\n')
            time.sleep(1)
            self._ssh.recv(self._MAX_READ)

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

