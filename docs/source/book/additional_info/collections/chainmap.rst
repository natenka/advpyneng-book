collections.ChainMap
--------------------

ChainMap - класс похожий на словарь для создания единого интерфейса для доступа к нескольким словарям

.. code:: python

    class collections.ChainMap(*maps)


Методы:

* ``maps``
* ``new_child(m=None, **kwargs)``
* ``parents``

.. code:: python

    In [1]: from collections import ChainMap

    In [2]: r1 = {
       ...:    "host": "192.168.100.1",
       ...:    "auth_username": "cisco",
       ...:    "auth_password": "cisco",
       ...:    "auth_secondary": "cisco",
       ...:    "platform": "cisco_iosxe",
       ...:    "timeout_socket": 15,
       ...: }

    In [3]: default_params = {
       ...:    "auth_strict_key": False,
       ...:    "timeout_socket": 5,
       ...:    "timeout_transport": 10,
       ...: }

    In [4]: scrapli_params = ChainMap(r1, default_params)

    In [5]: pprint(scrapli_params)
    ChainMap({'auth_password': 'cisco',
              'auth_secondary': 'cisco',
              'auth_username': 'cisco',
              'host': '192.168.100.1',
              'platform': 'cisco_iosxe',
              'timeout_socket': 15},
             {'auth_strict_key': False,
              'timeout_socket': 5,
              'timeout_transport': 10})

    In [6]: scrapli_params["timeout_socket"]
    Out[6]: 15

    In [7]: scrapli_params["timeout_transport"]
    Out[7]: 10

    In [8]: scrapli_params["host"]
    Out[8]: '192.168.100.1'


maps, parents
~~~~~~~~~~~~~

.. code:: python

    In [12]: scrapli_params.maps
    Out[12]:
    [{'host': '192.168.100.1',
      'auth_username': 'cisco',
      'auth_password': 'cisco',
      'auth_secondary': 'cisco',
      'platform': 'cisco_iosxe',
      'timeout_socket': 15},
     {'auth_strict_key': False, 'timeout_socket': 5, 'timeout_transport': 10}]

    In [13]: scrapli_params.parents
    Out[13]: ChainMap({'auth_strict_key': False, 'timeout_socket': 5, 'timeout_transport': 10})


``new_child``
~~~~~~~~~~~~~

.. code:: python

    In [18]: pprint(scrapli_params)
    ChainMap({'auth_password': 'cisco',
              'auth_secondary': 'cisco',
              'auth_username': 'cisco',
              'host': '192.168.100.1',
              'platform': 'cisco_iosxe',
              'timeout_socket': 15},
             {'auth_strict_key': False,
              'timeout_socket': 5,
              'timeout_transport': 10})

    In [19]: updated_info = {"host": "10.1.1.1"}

    In [20]: new_params = scrapli_params.new_child(updated_info)

    In [22]: pprint(new_params)
    ChainMap({'host': '10.1.1.1'},
             {'auth_password': 'cisco',
              'auth_secondary': 'cisco',
              'auth_username': 'cisco',
              'host': '192.168.100.1',
              'platform': 'cisco_iosxe',
              'timeout_socket': 15},
             {'auth_strict_key': False,
              'timeout_socket': 5,
              'timeout_transport': 10})

    In [23]: new_params["host"]
    Out[23]: '10.1.1.1'

    In [25]: pprint(scrapli_params)
    ChainMap({'auth_password': 'cisco',
              'auth_secondary': 'cisco',
              'auth_username': 'cisco',
              'host': '192.168.100.1',
              'platform': 'cisco_iosxe',
              'timeout_socket': 15},
             {'auth_strict_key': False,
              'timeout_socket': 5,
              'timeout_transport': 10})

