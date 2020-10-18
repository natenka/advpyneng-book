Декоратор staticmethod
----------------------

Статический метод - это метод, который не привязан к состоянию 
экземпляра или класса. Для создания статического метода 
используется декоратор staticmethod.

Преимущества использования staticmethod:

* Это подсказка для тех, кто читает код, которая указывает на то, 
  что метод не зависит от состояния экземпляра класса.

Большинству методов для работы нужна ссылка на экземпляр,
поэтому как первый аргумент используется self.
Однако иногда бывают методы, которые никак не связаны с
экземпляром и зависят только от аргументов.
Как правило, в таком случае можно даже вынести метод из класса
и сделать его функцией.
Если же метод логически связан с работой класса, но работает одинаково 
независимо от состояния экземпляров, метод декорируют декоратором staticmethod,
чтобы указать это явно.

.. code:: python

    import time
    from textfsm import clitable
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

        @staticmethod
        def _parse_show(command, command_output,
                       index_file='index', templates='templates'):
            attributes = {'Command': command,
                          'Vendor': 'cisco_ios'}
            cli_table = clitable.CliTable(index_file, templates)
            cli_table.ParseCmd(command_output, attributes)
            return [dict(zip(cli_table.header, row)) for row in cli_table]

        def send_show_command(self, command, parse=True):
            command_output = super().send_show_command(command)
            if not parse:
                return command_output
            return self._parse_show(command, command_output)


.. code:: python

    In [6]: r1 = CiscoSSH('192.168.100.1', 'cisco', 'cisco', 'cisco')

    In [7]: r1.send_show_command('sh ip int br')
    Out[7]:
    [{'intf': 'Ethernet0/0',
      'address': '192.168.100.1',
      'status': 'up',
      'protocol': 'up'},
     {'intf': 'Ethernet0/1',
      'address': '192.168.200.1',
      'status': 'up',
      'protocol': 'up'},
     {'intf': 'Ethernet0/2',
      'address': '19.1.1.1',
      'status': 'up',
      'protocol': 'up'},
     {'intf': 'Ethernet0/3',
      'address': '192.168.230.1',
      'status': 'up',
      'protocol': 'up'},
     {'intf': 'Loopback0',
      'address': '10.4.4.4',
      'status': 'up',
      'protocol': 'up'},
     {'intf': 'Loopback90',
      'address': '90.1.1.1',
      'status': 'up',
      'protocol': 'up'}]

