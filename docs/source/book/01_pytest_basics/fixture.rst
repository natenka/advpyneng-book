Fixture
-------

Fixtures это функции, которые выполняют что-то до теста и, при необходимости, после.

Два самых распространенных применения fixture:

* для передачи каких-то данных для теста
* setup and teardown

Fixture scope - контролирует как часто запускается fixture:

* function (значение по умолчанию) - fixture запускается до и после каждого теста, который использует это fixture
* class
* module - fixture запускается один раз до и после тестов в модуле, который использует это fixture
* package
* session - fixture запускается один раз в начале сессии и в конце

Запуск "после" актуален только для fixture c yield.


Полезные команды для работы с fixture:

* ``pytest --fixtures`` - показывает все доступные fixture (встроенные,
  из плагинов и найденные в тестах и conftest.py). Добавление ``-v`` показывает
  в каких файлах находятся fixture и на какой строке определена функция
* ``pytest --setup-show`` - показывает какие fixture запускаются и когда


.. toctree::
   :maxdepth: 1
   :hidden:

   fixture_custom
   fixture_builtin
   conftest
   fixture_features
   fixture_parametrization
