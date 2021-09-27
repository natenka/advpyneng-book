Примеры тестов
--------------

Тут примеры тестов еще не используют fixture и параметризацию.

Тест функции
~~~~~~~~~~~~

.. code:: python

    import pytest


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


    def test_password_min_length():
        assert check_passwd('user', '12345', min_length=3) == True
        assert check_passwd('user', '123456', min_length=5) == False
        assert check_passwd('user', 'userpass', min_length=5) == False


Тест класса
~~~~~~~~~~~

.. code:: python

    import ipaddress


    class IPv4Network:
        def __init__(self, network):
            self.network = network
            self.mask = int(network.split("/")[-1])
            self.bin_mask = "1" * self.mask + "0" * (32 - self.mask)

        def hosts(self):
            net = ipaddress.ip_network(self.network)
            return [str(ip) for ip in net.hosts()]

        def __repr__(self):
            return f"Network('{self.network}')"

        def __len__(self):
            return len(self.hosts())

        def __iter__(self):
            return iter(self.hosts())

Тесты:

.. code:: python

    from collections.abc import Iterable
    import pytest
    from ex06_class_ipv4network import IPv4Network


    def test_attributes_created():
        """
        Проверяем, что у объекта есть атрибуты:
            network, mask, bin_mask
        """
        net = IPv4Network("100.7.1.0/26")
        assert getattr(net, "network", None) != None, "Атрибут не найден"
        assert getattr(net, "mask", None) != None, "Атрибут не найден"
        assert getattr(net, "bin_mask", None) != None, "Атрибут не найден"


    def test_attributes():
        """Проверяем значения атрибутов"""
        net = IPv4Network("10.1.1.0/29")
        assert net.network == "10.1.1.0/29"
        assert net.mask == 29
        assert net.bin_mask == "11111111111111111111111111111000"


    def test_hosts():
        """Проверяем работу метода hosts"""
        net = IPv4Network("100.7.1.0/26")
        assert type(net.hosts()) == list, "Метод hosts должен возвращать список"
        assert len(net.hosts()) == 62, "В данной сети должно быть 62 хоста"


    def test_repr():
        """Проверяем работу метода __repr__"""
        net = IPv4Network("192.168.1.0/26")
        assert repr(net) == "Network('192.168.1.0/26')"


    def test_len():
        """Проверяем работу метода __len__"""
        net = IPv4Network("192.168.1.0/26")
        assert len(net) == 62


    def test_iter():
        """Проверяем что IPv4Network итерируемый объект"""
        net = IPv4Network("192.168.1.0/26")
        net_iterator = iter(net)
        assert next(net_iterator) == "192.168.1.1"
        assert isinstance(net, Iterable)

