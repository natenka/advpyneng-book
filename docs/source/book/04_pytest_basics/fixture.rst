Fixture
-------

Fixtures - это функции, которые pytest вызывает.

scope:

* function (default)
* module
* session

Источник pyneng-online-may-aug-2019/exercises/26_oop_special_methods/conftest.py

.. code:: python

    import re
    import yaml
    import pytest
    from netmiko import ConnectHandler


    @pytest.fixture()
    def topology_with_dupl_links():
        topology = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}
        return topology


    @pytest.fixture()
    def normalized_topology_example():
        normalized_topology = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                               ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                               ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                               ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                               ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                               ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}
        return normalized_topology





Источник pyneng-online-may-aug-2019/exercises/19_ssh_telnet/conftest.py

.. code:: python

    import yaml
    import pytest
    from netmiko import ConnectHandler


    @pytest.fixture(scope='module')
    def first_router_from_devices_yaml():
        with open('devices.yaml') as f:
            devices = yaml.safe_load(f)
            r1 = devices[0]
            #options = {'timeout': 5, 'fast_cli': True}
            r1.update(options)
        return r1


    @pytest.fixture(scope='module')
    def r1_test_connection(first_router_from_devices_yaml):
        r1 = ConnectHandler(**first_router_from_devices_yaml)
        r1.enable()
        yield r1
        r1.disconnect()


    @pytest.fixture(scope='module')
    def first_router_wrong_pass(first_router_from_devices_yaml):
        r1 = first_router_from_devices_yaml.copy()
        r1['password'] = 'wrong'
        return r1


    @pytest.fixture(scope='module')
    def first_router_wrong_ip(first_router_from_devices_yaml):
        r1 = first_router_from_devices_yaml.copy()
        r1['ip'] = 'unreachable'
        return r1

