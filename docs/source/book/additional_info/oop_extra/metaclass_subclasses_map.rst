
.. code:: python

    import paramiko
    import time


    CLASS_MAPPER_BASE = {}

    class Base(type):
        def __init__(cls, clsname, bases, methods):
            super().__init__(clsname, bases, methods)
            if hasattr(cls, 'device_type'):
                CLASS_MAPPER_BASE[cls.device_type] = cls


    class BaseSSH(metaclass=Base):
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

        def send_show_command(self, command):
            self._ssh.send(command + '\n')
            time.sleep(2)
            result = self._ssh.recv(self._MAX_READ).decode('ascii')
            return result

        def send_config_commands(self, commands):
            if isinstance(commands, str):
                commands = [commands]
            for command in commands:
                self._ssh.send(command + '\n')
                time.sleep(0.5)
            result = self._ssh.recv(self._MAX_READ).decode('ascii')
            return result


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


    class JuniperSSH(BaseSSH):
        device_type = 'juniper'
        def __init__(self, ip, username, password, enable_password,
                     disable_paging=True):
            pass


