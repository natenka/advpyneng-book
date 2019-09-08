Абстрактные классы в стандартной библиотеке Python
--------------------------------------------------

.. tabularcolumns:: |l|L|L|L|

========================== ======================= ====================================================
ABC                        Abstract Methods        Mixin Methods
========================== ======================= ====================================================
:class:`Container`         ``__contains__``
:class:`Hashable`          ``__hash__``
:class:`Iterable`          ``__iter__``
:class:`Iterator`          ``__next__``            ``__iter__``
:class:`Reversible`        ``__reversed__``
:class:`Generator`         ``send``, ``throw``     ``close``, ``__iter__``, ``__next__``
:class:`Sized`             ``__len__``
:class:`Callable`          ``__call__``
:class:`Collection`        ``__contains__``,
                           ``__iter__``,
                           ``__len__``

:class:`Sequence`          ``__getitem__``,        ``__contains__``, ``__iter__``, ``__reversed__``,
                           ``__len__``             ``index``, and ``count``

:class:`MutableSequence`   ``__getitem__``,        Inherited :class:`Sequence` methods and
                           ``__setitem__``,        ``append``, ``reverse``, ``extend``, ``pop``,
                           ``__delitem__``,        ``remove``, and ``__iadd__``
                           ``__len__``,
                           ``insert``

:class:`ByteString`        ``__getitem__``,        Inherited :class:`Sequence` methods
                           ``__len__``

:class:`Set`               ``__contains__``,       ``__le__``, ``__lt__``, ``__eq__``, ``__ne__``,
                           ``__iter__``,           ``__gt__``, ``__ge__``, ``__and__``, ``__or__``,
                           ``__len__``             ``__sub__``, ``__xor__``, and ``isdisjoint``

:class:`MutableSet`        ``__contains__``,       Inherited :class:`Set` methods and
                           ``__iter__``,           ``clear``, ``pop``, ``remove``, ``__ior__``,
                           ``__len__``,            ``__iand__``, ``__ixor__``, and ``__isub__``
                           ``add``,
                           ``discard``

:class:`Mapping`           ``__getitem__``,        ``__contains__``, ``keys``, ``items``, ``values``,
                           ``__iter__``,           ``get``, ``__eq__``, and ``__ne__``
                           ``__len__``

:class:`MutableMapping`    ``__getitem__``,        Inherited :class:`Mapping` methods and
                           ``__setitem__``,        ``pop``, ``popitem``, ``clear``, ``update``,
                           ``__delitem__``,        and ``setdefault``
                           ``__iter__``,
                           ``__len__``


:class:`MappingView`                               ``__len__``
:class:`ItemsView`                                 ``__contains__``,
                                                   ``__iter__``
:class:`KeysView`                                  ``__contains__``,
                                                   ``__iter__``
:class:`ValuesView`                                ``__contains__``, ``__iter__``
                           
:class:`Awaitable`         ``__await__``
:class:`Coroutine`         ``send``, ``throw``     ``close``
:class:`AsyncIterable`     ``__aiter__``
:class:`AsyncIterator`     ``__anext__``           ``__aiter__``
:class:`AsyncGenerator`    ``asend``, ``athrow``   ``aclose``, ``__aiter__``, ``__anext__``
========================== ======================= ====================================================

