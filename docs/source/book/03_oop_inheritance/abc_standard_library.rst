Абстрактные классы в стандартной библиотеке Python
--------------------------------------------------

.. tabularcolumns:: |l|L|L|

========================== ======================= ====================================================
ABC                        Abstract Methods        Mixin Methods
========================== ======================= ====================================================
``Container``                              ``__contains__``
``Hashable``                               ``__hash__``
``Iterable``                               ``__iter__``
``Iterator``        ``__next__``            ``__iter__``
``Reversible``      ``__reversed__``
``Generator``       ``send``, ``throw``     ``close``, ``__iter__``, ``__next__``
``Sized``           ``__len__``
``Callable``        ``__call__``
``Collection``      ``__contains__``,
                    ``__iter__``,
                    ``__len__``

``Sequence``        ``__getitem__``,        ``__contains__``, ``__iter__``, ``__reversed__``,
                    ``__len__``             ``index``, and ``count``

``MutableSequence`` ``__getitem__``,        Inherited :class:`Sequence` methods and
                    ``__setitem__``,        ``append``, ``reverse``, ``extend``, ``pop``,
                    ``__delitem__``,        ``remove``, and ``__iadd__``
                    ``__len__``,
                    ``insert``

``ByteString``      ``__getitem__``,        Inherited :class:`Sequence` methods
                    ``__len__``

``Set``             ``__contains__``,       ``__le__``, ``__lt__``, ``__eq__``, ``__ne__``,
                    ``__iter__``,           ``__gt__``, ``__ge__``, ``__and__``, ``__or__``,
                    ``__len__``             ``__sub__``, ``__xor__``, and ``isdisjoint``

``MutableSet``      ``__contains__``,       Inherited :class:`Set` methods and
                    ``__iter__``,           ``clear``, ``pop``, ``remove``, ``__ior__``,
                    ``__len__``,            ``__iand__``, ``__ixor__``, and ``__isub__``
                    ``add``,
                    ``discard``

``Mapping``         ``__getitem__``,        ``__contains__``, ``keys``, ``items``, ``values``,
                    ``__iter__``,           ``get``, ``__eq__``, and ``__ne__``
                    ``__len__``

``MutableMapping``  ``__getitem__``,        Inherited :class:`Mapping` methods and
                    ``__setitem__``,        ``pop``, ``popitem``, ``clear``, ``update``,
                    ``__delitem__``,        and ``setdefault``
                    ``__iter__``,
                    ``__len__``


``MappingView``                             ``__len__``
``ItemsView``                               ``__contains__``,
                                            ``__iter__``
``KeysView``                                ``__contains__``,
                                            ``__iter__``
``ValuesView``                              ``__contains__``, ``__iter__``
                    
``Awaitable``       ``__await__``
``Coroutine``       ``send``, ``throw``     ``close``
``AsyncIterable``   ``__aiter__``
``AsyncIterator``   ``__anext__``           ``__aiter__``
``AsyncGenerator``  ``asend``, ``athrow``   ``aclose``, ``__aiter__``, ``__anext__``
========================== ======================= ====================================================

