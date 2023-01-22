Дополнительные возможности
--------------------------

pytest.raises
~~~~~~~~~~~~~

.. code:: python

    import ipaddress
    import pytest


    def check_ip(ip):
        if type(ip) != str:
            raise TypeError("Function only works with strings")
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False


    def test_check_ip_raises_1():
        with pytest.raises(TypeError):
            check_ip(100)


    def test_check_ip_raises_3():
        with pytest.raises(TypeError) as error:
            check_ip(100)
        assert "strings" in str(error.value)


    def test_check_ip_raises_4():
        with pytest.raises(TypeError, match="st.+ngs"):
            check_ip(100)
