windowed
--------

.. code:: python

    more_itertools.windowed(seq, n, fillvalue=None, step=1)

.. code:: python

    In [33]: windows = more_itertools.windowed(f, 5)

    In [34]: for win in windows:
        ...:     print(win)
        ...:
    0
    1
    2
    3
    4
    ('SW1#show cdp neighbors detail\n', '-------------------------\n', 'Device ID: SW2\n', 'Entry address(es):\n', '  IP address: 10.1.1.2\n')
    5
    ('-------------------------\n', 'Device ID: SW2\n', 'Entry address(es):\n', '  IP address: 10.1.1.2\n', 'Platform: cisco WS-C2960-8TC-L,  Capabilities: Switch IGMP\n')
    6
    ('Device ID: SW2\n', 'Entry address(es):\n', '  IP address: 10.1.1.2\n', 'Platform: cisco WS-C2960-8TC-L,  Capabilities: Switch IGMP\n', 'Interface: GigabitEthernet1/0/16,  Port ID (outgoing port): GigabitEthernet0/1\n')
    7
    ('Entry address(es):\n', '  IP address: 10.1.1.2\n', 'Platform: cisco WS-C2960-8TC-L,  Capabilities: Switch IGMP\n', 'Interface: GigabitEthernet1/0/16,  Port ID (outgoing port): GigabitEthernet0/1\n', 'Holdtime : 164 sec\n')
    8
    ('  IP address: 10.1.1.2\n', 'Platform: cisco WS-C2960-8TC-L,  Capabilities: Switch IGMP\n', 'Interface: GigabitEthernet1/0/16,  Port ID (outgoing port): GigabitEthernet0/1\n', 'Holdtime : 164 sec\n', '\n')

