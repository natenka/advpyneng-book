Декоратор property
------------------

Python позволяет создавать и изменять переменные экземпляров:

.. code:: python

    In [1]: class Robot:
       ...:     def __init__(self, name):
       ...:         self.name = name
       ...:

    In [2]: bb8 = Robot('BB-8')

    In [3]: bb8.name
    Out[3]: 'BB-8'

    In [4]: bb8.name = 'R2D2'

    In [5]: bb8.name
    Out[5]: 'R2D2'


Однако иногда нужно сделать так чтобы при изменении/установке значения переменной,
проверялся ее тип или диапазон значений, также иногда необходимо сделать переменную
неизменяемой и сделать ее доступной только для чтения.
В некоторых языках программирования для этого используются методы get и set,
например:

.. code:: python

    In [9]: class IPAddress:
       ...:     def __init__(self, address, mask):
       ...:         self._address = address
       ...:         self._mask = int(mask)
       ...:
       ...:     def set_mask(self, mask):
       ...:         if not isinstance(mask, int):
       ...:             raise TypeError("Маска должна быть числом")
       ...:         if not mask in range(8, 32):
       ...:             raise ValueError("Маска должна быть в диапазоне от 8 до 32")
       ...:         self._mask = mask
       ...:
       ...:     def get_mask(self):
       ...:         return self._mask
       ...:

    In [10]: ip1 = IPAddress('10.1.1.1', 24)

    In [12]: ip1.set_mask(23)

    In [13]: ip1.get_mask()
    Out[13]: 23

По сравнению со стандартным синтаксисом обращения к атрибутам,
этот вариант выглядит очень громоздко. В Python есть более компактный
вариант сделать то же самое - property.

Property как правило, используется как декоратор метода и превращает метод
в переменную экземпляра с точки зрения пользователя класса.

Пример создания property:

.. code:: python

    In [14]: class IPAddress:
        ...:     def __init__(self, address, mask):
        ...:         self._address = address
        ...:         self._mask = int(mask)
        ...:
        ...:     @property
        ...:     def mask(self):
        ...:         return self._mask
        ...:

Теперь можно обращаться к mask как к обычной переменной:

.. code:: python

    In [15]: ip1 = IPAddress('10.1.1.1', 24)

    In [16]: ip1.mask
    Out[16]: 24

Один из плюсов property - переменная становится доступной только для чтения:

.. code:: python

    In [17]: ip1.mask = 30
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-17-e153170a5893> in <module>
    ----> 1 ip1.mask = 30

    AttributeError: can't set attribute'

Также property позволяет добавлять метод setter, который будет отвечать 
за изменение значения переменной и, так как это тоже метод, позволяет
включить логику с проверкой или динамическим вычислением значения.

.. code:: python

    In [19]: class IPAddress:
        ...:     def __init__(self, address, mask):
        ...:         self._address = address
        ...:         self._mask = int(mask)
        ...:
        ...:     @property
        ...:     def mask(self):
        ...:         return self._mask
        ...:
        ...:     @mask.setter
        ...:     def mask(self, mask):
        ...:         if not isinstance(mask, int):
        ...:             raise TypeError("Маска должна быть числом")
        ...:         if not mask in range(8, 32):
        ...:             raise ValueError("Маска должна быть в диапазоне от 8 до 32")
        ...:         self._mask = mask
        ...:

    In [20]: ip1 = IPAddress('10.1.1.1', 24)

    In [21]: ip1.mask
    Out[21]: 24

    In [23]: ip1.mask = 30

    In [24]: ip1.mask = 320
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-24-8573933afac9> in <module>
    ----> 1 ip1.mask = 320

    <ipython-input-19-d0e571cd5e2b> in mask(self, mask)
         13             raise TypeError("Маска должна быть числом")
         14         if not mask in range(8, 32):
    ---> 15             raise ValueError("Маска должна быть в диапазоне от 8 до 32")
         16         self._mask = mask
         17

    ValueError: Маска должна быть в диапазоне от 8 до 32


Пример использования property для динамического получения значения:

.. code:: python

    from base_ssh import BaseSSH
    import time


    class CiscoSSH(BaseSSH):
        def __init__(self, ip, username, password, enable_password,
                     disable_paging=True):
            super().__init__(ip, username, password)
            self._ssh.send('enable\n')
            self._ssh.send(enable_password + '\n')
            if disable_paging:
                self._ssh.send('terminal length 0\n')
            time.sleep(1)
            self._ssh.recv(self._MAX_READ)
            self._cfg = None

        @property
        def cfg(self):
            if not self._cfg:
                self._cfg = self.send_show_command('sh run')
            return self._cfg


При обращении к переменной cfg первый раз, на оборудовании выполняется команда sh run
и записывается в переменную self._cfg, второй раз значение просто берется из переменной:

.. code:: python

    In [6]: r1 = CiscoSSH('192.168.100.1', 'cisco', 'cisco', 'cisco')

    In [7]: r1.cfg # тут возникает пауза
    Out[7]: 'sh run\r\nBuilding configuration...\r\n\r\nCurrent configuration : 2286 bytes\r\n!\r\nversion 15.2\r\n...'

    In [8]: r1.cfg
    Out[8]: 'sh run\r\nBuilding configuration...\r\n\r\nCurrent configuration : 2286 bytes\r\n!\r\nversion 15.2\r\n...'

В этом примере property используется для создания переменной, которая отвечает за
чтение/изменение основного IP-адреса:

.. code:: python

    import re
    import time
    from base_ssh import BaseSSH


    class CiscoSSH(BaseSSH):
        def __init__(self, ip, username, password, enable_password,
                     disable_paging=True):
            super().__init__(ip, username, password)
            self._ssh.send('enable\n')
            self._ssh.send(enable_password + '\n')
            if disable_paging:
                self._ssh.send('terminal length 0\n')
            time.sleep(1)
            self._ssh.recv(self._MAX_READ)
            self._mgmt_ip = None

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

        @property
        def mgmt_ip(self):
            if not self._mgmt_ip:
                loopback0 = self.send_show_command('sh run interface lo0')
                self._mgmt_ip = re.search('ip address (\S+) ', loopback0).group(1)
            return self._mgmt_ip

        @mgmt_ip.setter
        def mgmt_ip(self, new_ip):
            if self.mgmt_ip != new_ip:
                self.send_config_commands([f'interface lo0',
                                           f'ip address {new_ip} 255.255.255.255'])
                self._mgmt_ip = new_ip

Теперь при чтении переменной mgmt_ip считывается конфиг или читается переменная _mgmt_ip,
а при записи адрес перенастраивается на оборудовании:

.. code:: python

    In [19]: r1 = CiscoSSH('192.168.100.1', 'cisco', 'cisco', 'cisco')

    In [22]: r1.mgmt_ip
    Out[22]: '4.4.4.4'

    In [23]: r1.mgmt_ip = '10.4.4.4'

    In [24]: r1.mgmt_ip
    Out[24]: '10.4.4.4'

    In [27]: print(r1.send_show_command('sh run interface lo0'))
    sh run interface lo0
    Building configuration...

    Current configuration : 64 bytes
    !
    interface Loopback0
     ip address 10.4.4.4 255.255.255.255
    end

    R1#


.. toctree::
   :maxdepth: 1

   property_variations
