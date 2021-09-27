Встроенные fixture
------------------

* `capsys <https://docs.pytest.org/en/6.2.x/reference.html#std-fixture-capsys>`__
* `monkeypatch <https://docs.pytest.org/en/6.2.x/monkeypatch.html>`__
* `tmp_path <https://docs.pytest.org/en/6.2.x/tmpdir.html>`__
* `и другие <https://docs.pytest.org/en/6.2.x/fixture.html>`__

capsys
~~~~~~

.. code:: python

    from netmiko import ConnectHandler
    from paramiko.ssh_exception import AuthenticationException


    def send_show_command(device, command):
        try:
            with ConnectHandler(**device) as ssh:
                ssh.enable()
                result = ssh.send_command(command)
                return result
        except AuthenticationException as error:
            print(error)


    def test_function_return_value(capsys, first_router_wrong_pass):
        return_value = send_show_command(first_router_wrong_pass, "sh ip int br")
        correct_stdout = "Authentication fail"
        out, err = capsys.readouterr()
        assert out != "", "Сообщение об ошибке не выведено на stdout"
        assert correct_stdout in out, "Выведено неправильное сообщение об ошибке"



monkeypatch
~~~~~~~~~~~

.. code:: python

    def check_passwd(username, password, min_length=8):
        if len(password) < min_length:
            print('Пароль слишком короткий')
            return False
        elif username in password:
            print('Пароль содержит имя пользователя')
            return False
        else:
            print(f'Пароль для пользователя {username} прошел все проверки')
            return True


    def test_password_min_length(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x=None: 'user')
        monkeypatch.setattr('getpass.getpass', lambda x=None: '12345')
        assert check_passwd(min_length=3) == True


    @pytest.mark.parametrize(
        "username,password,result",
        [
            ('user', '12345', True),
            ('user', '12345user', False)
        ],
    )
    def test_check_passwd_function(monkeypatch, username, password, result):
        monkeypatch.setattr('builtins.input', lambda x=None: username)
        monkeypatch.setattr('getpass.getpass', lambda x=None: password)
        assert check_passwd(min_length=3) == result
