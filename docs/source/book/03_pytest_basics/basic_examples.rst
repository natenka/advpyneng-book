Примеры тестов
--------------

Тест функции
~~~~~~~~~~~~

.. code:: python

    def check_passwd(username, password, min_length=8, check_username=True):
        if len(password) < min_length:
            print('Пароль слишком короткий')
            return False
        elif check_username and username in password:
            print('Пароль содержит имя пользователя')
            return False
        else:
            print(f'Пароль для пользователя {username} прошел все проверки')
            return True

.. code:: python

    In [3]: check_passwd('nata', '12345', min_length=3)
    Пароль для пользователя nata прошел все проверки
    Out[3]: True

    In [4]: check_passwd('nata', '12345nata', min_length=3)
    Пароль содержит имя пользователя
    Out[4]: False

    In [5]: check_passwd('nata', '12345nata', min_length=3, check_username=False)
    Пароль для пользователя nata прошел все проверки
    Out[5]: True

    In [6]: check_passwd('nata', '12345nata', min_length=3, check_username=True)
    Пароль содержит имя пользователя
    Out[6]: False

Тест класса
~~~~~~~~~~~

.. code:: python

    import ipaddress


    class IPv4Network:
        def __init__(self, network):
            self._net = ipaddress.ip_network(network)
            self.address = str(self._net.network_address)
            self.mask = self._net.prefixlen
            self.allocated = tuple()

        def hosts(self):
            return tuple([str(ip) for ip in self._net.hosts()])

        def allocate(self, ip):
            self.allocated += (ip,)

        def unassigned(self):
            return tuple([ip for ip in self.hosts() if ip not in self.allocated])

.. code:: python

    import pytest
    import task_1_1
    from common_functions import check_class_exists, check_attr_or_method


    def test_class_created():
        '''Проверяем, что класс создан'''
        check_class_exists(task_1_1, 'IPv4Network')


    def test_attributes_created():
        '''
        Проверяем, что у объекта есть атрибуты:
            address, mask, broadcast, allocated
        '''
        net = task_1_1.IPv4Network('100.7.1.0/26')
        check_attr_or_method(net, attr='address')
        check_attr_or_method(net, attr='mask')
        check_attr_or_method(net, attr='broadcast')
        check_attr_or_method(net, attr='allocated')
        assert net.allocated == tuple(), "По умолчанию allocated должен содержать пустой кортеж"

    def test_methods_created():
        '''
        Проверяем, что у объекта есть методы:
            allocate, unassigned
        '''
        net = task_1_1.IPv4Network('100.7.1.0/26')
        check_attr_or_method(net, method='allocate')
        check_attr_or_method(net, method='unassigned')

    def test_return_types():
        '''Проверяем работу объекта'''
        net = task_1_1.IPv4Network('100.7.1.0/26')
        assert type(net.hosts()) == tuple, "Метод hosts должен возвращать кортеж"
        assert type(net.unassigned()) == tuple, "Метод unassigned должен возвращать кортеж"


    def test_address_allocation():
        '''Проверяем работу объекта'''
        net = task_1_1.IPv4Network('100.7.1.0/26')
        assert len(net.hosts()) == 62, "В данной сети должно быть 62 хоста"
        assert net.broadcast == '100.7.1.63', "Broadcast адрес для этой сети 100.7.1.63"

        net.allocate('100.7.1.45')
        net.allocate('100.7.1.15')
        net.allocate('100.7.1.60')

        assert len(net.hosts()) == 62, "Метод hosts должен возвращать все хосты"
        assert len(net.allocated) == 3, "Переменная allocated должна содержать 3 хоста"
        assert len(net.unassigned()) == 59, "Метод unassigned должен возвращать на 3 хоста меньше"

