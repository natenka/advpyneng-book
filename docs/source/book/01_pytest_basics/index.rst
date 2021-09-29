.. raw:: latex

   \newpage

1. Основы pytest
=================

Pytest - фреймворк для тестирования кода

Тестирование кода позволяет проверить:

* работает ли код так как нужно
* как ведет себя код в нестандартных ситуациях
* пользовательский интерфейс
* ...

Уровни тестирования

* unit - тестирование отдельных функций/классов
* intergration - тестирование взаимодействия разных частей софта друг с другом
* system - тестируется вся система, для web, например, это может быть
  тестирование от логина пользователя до выхода

Альтернативы pytest:

* `unittest <https://pymotw.com/3/unittest/index.html>`__
* `doctest <https://pymotw.com/3/doctest/index.html>`__
* `nose <https://nose.readthedocs.io/en/latest/>`__


Пример тестов с unittest:

.. code:: python

    import unittest

    class TestStringMethods(unittest.TestCase):

        def test_upper(self):
            self.assertEqual('foo'.upper(), 'FOO')

        def test_isupper(self):
            self.assertTrue('FOO'.isupper())
            self.assertFalse('Foo'.isupper())

        def test_split(self):
            s = 'hello world'
            self.assertEqual(s.split(), ['hello', 'world'])
            # check that s.split fails when the separator is not a string
            with self.assertRaises(TypeError):
                s.split(2)


    if __name__ == '__main__':
        unittest.main()


Аналогичный тест с pytest:

.. code:: python

    def test_upper():
        assert 'foo'.upper() == 'FOO'


    def test_isupper():
        assert 'FOO'.isupper() == True
        assert 'Foo'.isupper() == False


    def test_split():
        s = 'hello world'
        assert s.split() == ['hello', 'world']
        # check that s.split fails when the separator is not a string
        with pytest.raises(TypeError):
            s.split(2)



.. toctree::
   :maxdepth: 1

   basics
   basic_examples
   running_tests
   parametrized_tests
   fixture
   extra
   test_network
   test_hints
   further_reading
   ../../exercises/01_exercises.rst
