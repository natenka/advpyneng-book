Примеры тестов
--------------

Тут примеры тестов еще не используют fixture и параметризацию.

Тест функции
~~~~~~~~~~~~

.. code:: python

    import ipaddress


    def check_ip(ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

Тесты

.. code:: python

    from basics_01_check_ip import check_ip


    def test_check_ip_correct_10_1_1_1():
        assert (
            check_ip("10.1.1.1") == True
        ), "При правильном IP, функция должна возвращать True"


    def test_check_ip_correct_180_10_1_1():
        assert (
            check_ip("180.10.1.1") == True
        ), "При правильном IP, функция должна возвращать True"


    def test_check_ip_wrong_octet():
        assert (
            check_ip("10.400.1.1") == False
        ), "При неправильном IP, функция должна возвращать False"


    def test_check_ip_wrong_number_of_octets():
        assert (
            check_ip("10.1.1") == False
        ), "При неправильном IP, функция должна возвращать False"


Тест класса
~~~~~~~~~~~

.. code:: python

    import ipaddress


    class IPAddress:
        def __init__(self, ip, mask):
            self.ip = ip
            self.mask = mask

        def __int__(self):
            int_ip = int(ipaddress.ip_address(self.ip))
            return int_ip

        def __str__(self):
            return f"{self.ip}/{self.mask}"

        def __repr__(self):
            return f"IPAddress('{self.ip}', {self.mask})"

        def __lt__(self, second_ip):
            if type(second_ip) != IPAddress:
                raise TypeError(f"'<' not supported between instances of 'IPAddress'"
                                f" and '{type(second_ip).__name__}'")
            return (int(self), self.mask) < (int(second_ip), second_ip.mask)

        def __le__(self, second_ip):
            if type(second_ip) != IPAddress:
                raise TypeError(f"'<=' not supported between instances of 'IPAddress'"
                                f" and '{type(second_ip).__name__}'")
            return (int(self), self.mask) <= (int(second_ip), second_ip.mask)

        def __eq__(self, second_ip):
            # print("eq", self, second_ip)
            if type(second_ip) != IPAddress:
                raise TypeError(f"'==' not supported between instances of 'IPAddress'"
                                f" and '{type(second_ip).__name__}'")
            return (int(self), self.mask) == (int(second_ip), second_ip.mask)



Тесты:

.. code:: python

    from class_ipaddress import IPAddress
    import pytest


    def test_ipaddress_attrs():
        ip1 = IPAddress("10.1.1.1", 25)
        assert ip1.ip == "10.1.1.1"
        assert ip1.mask == 25


    def test_ipaddress_str_repr():
        ip1 = IPAddress("10.1.1.1", 25)
        assert str(ip1) == "10.1.1.1/25"
        assert repr(ip1) == "IPAddress('10.1.1.1', 25)"


    def test_ipaddress_int():
        ip1 = IPAddress("10.1.1.1", 25)
        assert int(ip1) == 167837953


    def test_ipaddress_cmp_basic():
        ip1 = IPAddress("10.2.1.1", 25)
        ip2 = IPAddress("10.10.1.1", 25)
        assert ip1 < ip2
        assert ip2 > ip1
        assert ip1 != ip2
        assert not ip1 == ip2
        assert ip1 <= ip2
        assert ip2 >= ip1


    def test_ipaddress_cmp_mask():
        ip1 = IPAddress("10.2.1.1", 24)
        ip2 = IPAddress("10.2.1.1", 25)
        assert ip1 < ip2
        assert ip2 > ip1
        assert ip1 != ip2
        assert not ip1 == ip2
        assert ip1 <= ip2
        assert ip2 >= ip1


    def test_ipaddress_cmp_equal():
        ip1 = IPAddress("10.2.1.1", 24)
        ip2 = IPAddress("10.2.1.1", 24)
        assert ip1 == ip2


    def test_ipaddress_cmp_raise():
        ip1 = IPAddress("10.2.1.1", 24)
        ip2 = 100
        with pytest.raises(TypeError):
            ip1 == ip2

