collections.defaultdict
------------------------

defaultdict - подкласс словаря, который вызывает указанную функцию для подстановки несуществующих значений

.. code:: python

    class collections.defaultdict(default_factory=None, /[, ...])


.. code:: python

    In [2]: from collections import defaultdict

    In [3]: data = "some very important text"

    In [4]: d = defaultdict(int)

    In [5]: d
    Out[5]: defaultdict(int, {})

    In [6]: for letter in data:
       ...:     d[letter] += 1
       ...:

    In [7]: d
    Out[7]:
    defaultdict(int,
                {'s': 1,
                 'o': 2,
                 'm': 2,
                 'e': 3,
                 ' ': 3,
                 'v': 1,
                 'r': 2,
                 'y': 1,
                 'i': 1,
                 'p': 1,
                 't': 4,
                 'a': 1,
                 'n': 1,
                 'x': 1})

    In [9]: sorted(d.items(), key=lambda x: x[-1], reverse=True)
    Out[9]:
    [('t', 4),
     ('e', 3),
     (' ', 3),
     ('o', 2),
     ('m', 2),
     ('r', 2),
     ('s', 1),
     ('v', 1),
     ('y', 1),
     ('i', 1),
     ('p', 1),
     ('a', 1),
     ('n', 1),
     ('x', 1)]


Пример использования
~~~~~~~~~~~~~~~~~~~~~~~

config_sw1.txt

::

    interface FastEthernet0/0
     switchport mode access
     switchport access vlan 10
    !
    interface FastEthernet0/1
     switchport trunk encapsulation dot1q
     switchport trunk allowed vlan 100,200
     switchport mode trunk
    !
    interface FastEthernet0/2
     switchport mode access
     switchport access vlan 20
    !
    interface FastEthernet0/3
     switchport trunk encapsulation dot1q
     switchport trunk allowed vlan 100,300,400,500,600
     switchport mode trunk


.. code:: python

    {'FastEthernet0/0': ['switchport mode access', 'switchport access vlan 10'],
     'FastEthernet0/1': ['switchport trunk encapsulation dot1q',
                         'switchport trunk allowed vlan 100,200',
                         'switchport mode trunk'],
     'FastEthernet0/2': ['switchport mode access', 'switchport access vlan 20'],
     'FastEthernet0/3': ['switchport trunk encapsulation dot1q',
                         'switchport trunk allowed vlan 100,300,400,500,600',
                         'switchport mode trunk'],
     'FastEthernet1/0': ['switchport mode access', 'switchport access vlan 20'],
     'FastEthernet1/1': ['switchport mode access', 'switchport access vlan 30'],
     'FastEthernet1/2': ['switchport trunk encapsulation dot1q',
                         'switchport trunk allowed vlan 400,500,600',
                         'switchport mode trunk']}

.. code:: python

    from pprint import pprint
    from collections import defaultdict


    def get_ip_from_cfg(filename):
        result = defaultdict(list)
        with open(filename) as f:
            for line in f:
                if line.startswith("interface"):
                    intf = line.split()[-1]
                elif line.startswith(" switchport"):
                    result[intf].append(line.strip())
        return result


    if __name__ == "__main__":
        pprint(get_ip_from_cfg("config_sw1.txt"))

