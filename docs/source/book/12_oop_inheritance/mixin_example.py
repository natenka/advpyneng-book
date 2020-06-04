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
                if value.__doc__:
                    value = value.__doc__
                print(f"{name:25}{str(value):<20}")


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
        """Переходит в конфигурационный режим"""
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
        """Отправляет команды в конфигурационном режиме"""
        result = self.config_mode()
        result += super().send_config_commands(commands)
        result += self.exit_config_mode()
        return result


if __name__ == "__main__":
    r1 = CiscoSSH('192.168.100.1', 'cisco', 'cisco', 'cisco')
    r1.attributes()


