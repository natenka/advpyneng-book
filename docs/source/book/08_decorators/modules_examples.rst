Примеры модулей которые используют декораторы
--------------------------------------------


pytest
~~~~~~

.. code:: python

    @pytest.fixture(scope='module')
    def first_router_from_devices_yaml():
        with open('devices.yaml') as f:
            devices = yaml.safe_load(f)
            r1 = devices[0]
        return r1


click
~~~~~

.. code:: python

    @click.command()
    @click.option("--username", "-u", prompt=True)
    @click.option("--password", "-p", prompt=True, hide_input=True, confirmation_prompt=True)
    def cli(username, password):
        pass


flask
~~~~~

.. code:: python

    @main.route('/')
    def index():
        pass


    @main.route('/labs', methods=['GET', 'POST'])
    def labs():
        pass


    @main.route('/stats')
    def stats():
        pass


backoff
~~~~~~~~

.. code:: python

    @backoff.on_exception(
        backoff.expo, requests.exceptions.RequestException
    )
    def get_url(url):
        return requests.get(url)



dataclasses.dataclass
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    @dataclass
    class IPAddress:
        ip: str
        mask: int


    In [12]: ip1 = IPAddress('10.1.1.1', 28)

    In [13]: ip1
    Out[13]: IPAddress(ip='10.1.1.1', mask=28)

