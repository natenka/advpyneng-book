Дополнительные возможности
--------------------------

pytest.raises
~~~~~~~~~~~~~

.. code:: python

    from netmiko import ConnectHandler
    import pytest


    def send_show_command(device, command):
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
        return result


    @pytest.mark.parametrize("host", ["192.168.100.5", "192.168.100.2", "192.168.100.3"])
    def test_send_show_exceptions(cisco_ios_router_common_params, host):
        device = cisco_ios_router_common_params.copy()
        device["host"] = host
        device["password"] = "sdkjfhshdkf"
        with pytest.raises(
            (
                netmiko.ssh_exception.NetmikoTimeoutException,
                netmiko.ssh_exception.NetmikoAuthenticationException,
            )
        ) as exc:
            output = send_show_command(device, "sh ip int br")

