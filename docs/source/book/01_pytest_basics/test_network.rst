Использование pytest для тестирования сети
------------------------------------------

conftest.py

.. code:: python

    import pytest
    from netmiko import Netmiko
    import yaml


    with open("devices.yaml") as f:
        DEVICES = yaml.safe_load(f)
    DEVICES_IP = [dev["host"] for dev in DEVICES]


    def get_host(device):
        return device["host"]


    @pytest.fixture(params=DEVICES, ids=get_host, scope="session")
    def ssh_connection(request):
        with Netmiko(**request.param) as ssh:
            ssh.enable()
            yield ssh

Тесты:

.. code:: python

    import pytest


    @pytest.mark.parametrize(
        "command,check_output",
        [
            ("sh ip ospf", "routing process"),
            ("sh ip int br", "up"),
        ],
    )
    def test_ospf(ssh_connection, command, check_output):
        output = ssh_connection.send_command(command)
        assert check_output in output.lower()


    @pytest.mark.parametrize(
        "ip_address", ["192.168.100.1", "192.168.100.100"], ids=["ISP1", "ISP2"]
    )
    def test_ping(ssh_connection, ip_address):
        output = ssh_connection.send_command(f"ping {ip_address}")
        assert "success rate is 100" in output.lower()


    def test_loopback(ssh_connection):
        loopback = "Loopback0"
        output = ssh_connection.send_command("sh ip int br")
        assert loopback in output


    def test_intf(ssh_connection):
        output = ssh_connection.send_command("sh ip int br | i up +up")
        assert output.count("up") >= 4

