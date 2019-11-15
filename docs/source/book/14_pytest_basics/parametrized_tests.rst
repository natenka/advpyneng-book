Параметризация теста
--------------------

.. code:: python

    from check_password_function import check_passwd


    def test_password_min_length():
        assert check_passwd('nata', '12345', min_length=3)
        assert not check_passwd('nata', '12345nata', min_length=3)


Параметризация:

.. code:: python

    import pytest
    from check_password_function import check_passwd

    @pytest.mark.parametrize("username,password,min_length,result",[
        ('nata', '12345', 3, True),
        ('nata', '12345nata', 3, False)
    ])
    def test_password_min_length(username, password, min_length, result):
        assert result == check_passwd(username, password, min_length=min_length)

Пример из базового курса: https://github.com/pyneng/pyneng-online-may-aug-2019/blob/master/exercises/19_ssh_telnet/tests/test_task_19_2b.py
