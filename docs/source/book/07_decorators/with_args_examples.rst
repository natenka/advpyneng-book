Примеры декораторов с аргументами
---------------------------------

В Flask декораторы используются для сопоставления функция с ссылками на сайте:

.. code:: python

    url_function_map = {}

    def register(route):
        def decorator(func):
            url_function_map[route] = func
            return func
        return decorator

    @register('/')
    def func(a,b):
        return a+b

    @register('/scripts')
    def func2(a,b):
        return a+b


    In [3]: url_function_map
    Out[3]: {'/': <function __main__.func>, '/scripts': <function __main__.func2>}

А также для ограничения доступа к определенным ссылкам:

.. code:: python

    from functools import wraps


    class User:
        def __init__(self, username, permissions=None):
            self.username = username
            self.permissions = permissions

        def has_permission(self, permission):
            return permission in self.permissions


    natasha = User('nata', ['admin', 'user'])
    oleg = User('oleg', ['user'])

    current_user = natasha


    class AccessDenied(Exception):
        pass


    def permission_required(permission):
        def decorator(func):
            @wraps(func)
            def decorated_function(*args, **kwargs):
                if not current_user.has_permission(permission):
                    raise AccessDenied('You shall not pass!')
                return func(*args, **kwargs)
            return decorated_function
        return decorator


    @permission_required('admin')
    def secret_func():
        return 42


    In [77]: secret_func()
    Out[77]: 42

    In [78]: current_user = oleg

    In [79]: secret_func()
    ---------------------------------------------------------------------------
    AccessDenied                              Traceback (most recent call last)
    <ipython-input-79-23f2f66c4b3b> in <module>()
    ----> 1 secret_func()

    <ipython-input-75-240afbb2dcfe> in decorated_function(*args, **kwargs)
          4         def decorated_function(*args, **kwargs):
          5             if not current_user.has_permission(permission):
    ----> 6                 raise AccessDenied('You shall not pass!')
          7             return func(*args, **kwargs)
          8         return decorated_function

    AccessDenied: You shall not pass!


Иногда в зависимости от типа аргумента надо вызываться разные функции:

.. code:: python

    from netmiko import ConnectHandler
    import yaml
    from pprint import pprint


    def send_show_command(device, show_command):
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(show_command)
        return result

    def send_config_commands(device, config_commands):
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_config_set(config_commands)
        return result

    def send_commands(device_list, config=None, show=None):
        if show:
            return send_show_command(device_list, show)
        elif config:
            return send_config_commands(device_list, config)



    if __name__ == "__main__":
        commands = [ 'logging 10.255.255.1',
                     'logging buffered 20010',
                     'no logging console' ]
        show_command = "sh ip int br"
        with open('devices.yaml') as f:
            dev_list = yaml.safe_load(f)

        send_commands(dev_list, config=commands)
        send_commands(dev_list, show=show_command)

В стандартной библиотеке есть интересный `декоратор singledispatch <https://github.com/python/cpython/blob/3.7/Lib/functools.py#L763>`__:

.. code:: python

    from netmiko import ConnectHandler
    import yaml
    from pprint import pprint
    from functools import singledispatch
    from collections.abc import Iterable, Sequence


    @singledispatch
    def send_commands(command, device):
        print('original func')
        raise NotImplementedError('Поддерживается только список или строка')

    @send_commands.register(str)
    def _(show_command, device):
        print('Выполняем show')
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(show_command)
        return result

    @send_commands.register(Iterable)
    def _(config_commands, device):
        print('Выполняем config')
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_config_set(config_commands)
        return result

    if __name__ == "__main__":
        commands = ['logging 10.255.255.1',
                    'logging buffered 20010',
                    'no logging console' ]
        show_command = "sh ip int br"

        with open('devices.yaml') as f:
            r1 = yaml.safe_load(f)[0]

        print(send_commands(tuple(commands), r1))
        print(send_commands(show_command, r1))


