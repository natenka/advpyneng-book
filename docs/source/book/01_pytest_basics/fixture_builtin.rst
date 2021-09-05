Встроенные fixture
------------------

capsys
~~~~~~

.. code:: python

    import pytest
    import task_19_2a
    import sys
    sys.path.append('..')

    from common_functions import check_function_exists


    def test_functions_created():
        check_function_exists(task_19_2a, 'send_config_commands')


    def test_function_return_value(capsys, r1_test_connection,
                                   first_router_from_devices_yaml):
        test_commands = [
            'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
        ]
        correct_return_value = r1_test_connection.send_config_set(test_commands)
        return_value = task_19_2a.send_config_commands(
            first_router_from_devices_yaml, test_commands)
        # проверяем возвращаемое значение
        assert return_value != None, "Функция ничего не возвращает"
        assert type(return_value) == str, "Функция должна возвращать строку"
        assert return_value == correct_return_value, "Функция возвращает неправильное значение"

        # по умолчанию, verbose должно быть равным True
        # и на stdout должно выводиться сообщение
        correct_stdout = f'{r1_test_connection.host}'
        out, err = capsys.readouterr()
        assert out != '', "Сообщение об ошибке не выведено на stdout"
        assert correct_stdout in out, "Выведено неправильное сообщение об ошибке"

        # проверяем, что с verbose=False вывода в stdout нет
        return_value = task_19_2a.send_config_commands(
            first_router_from_devices_yaml, test_commands, verbose=False)
        correct_stdout = ''
        out, err = capsys.readouterr()
        assert out == correct_stdout,\
                "Сообщение об ошибке не должно выводиться на stdout, когда verbose=False"


tmpdir
~~~~~~~~

.. code:: python

    import pytest
    import task_20_2
    import sys
    sys.path.append('..')

    from common_functions import check_function_exists



    def test_functions_created():
        check_function_exists(task_20_2, 'send_show_command_to_devices')


    def test_function_return_value(three_routers_from_devices_yaml,
                                   r1_r2_r3_test_connection, tmpdir):
        command = 'sh ip int br'
        out1, out2, out3 = [r.send_command(command) for r in r1_r2_r3_test_connection]
        dest_filename = tmpdir.mkdir("test_tasks").join("task_20_2.txt")

        return_value = task_20_2.send_show_command_to_devices(
            devices=three_routers_from_devices_yaml,
            command=command, filename=dest_filename, limit=3)
        assert return_value == None, "Функция должна возвращать None"

        dest_file_content = dest_filename.read().strip()

        # проверяем, что вывод с каждого устройства есть в файле
        assert out1.strip() in dest_file_content, "В итоговом файле нет вывода с первого устройства"
        assert out2.strip() in dest_file_content, "В итоговом файле нет вывода со второго устройства"
        assert out3.strip() in dest_file_content, "В итоговом файле нет вывода с третьего устройства"

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


    def add_user_to_users_file(user, users_filename='users.txt'):
        while True:
            passwd = input(f'Введите пароль для пользователя {user}: ')
            if check_passwd(user, passwd):
                break
        with open(users_filename, 'a') as f:
            f.write(f'{user},{passwd}\n')

