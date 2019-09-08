Абстрактные классы в стандартной библиотеке Python
--------------------------------------------------

.. tabularcolumns:: |l|L|L|L|

========================== ====================== ======================= ====================================================
ABC                        Inherits from          Abstract Methods        Mixin Methods
========================== ====================== ======================= ====================================================
:class:`Container`                                ``__contains__``
:class:`Hashable`                                 ``__hash__``
:class:`Iterable`                                 ``__iter__``
:class:`Iterator`          :class:`Iterable`      ``__next__``            ``__iter__``
:class:`Reversible`        :class:`Iterable`      ``__reversed__``
:class:`Generator`         :class:`Iterator`      ``send``, ``throw``     ``close``, ``__iter__``, ``__next__``
:class:`Sized`                                    ``__len__``
:class:`Callable`                                 ``__call__``
:class:`Collection`        :class:`Sized`,        ``__contains__``,
                           :class:`Iterable`,     ``__iter__``,
                           :class:`Container`     ``__len__``

:class:`Sequence`          :class:`Reversible`,   ``__getitem__``,        ``__contains__``, ``__iter__``, ``__reversed__``,
                           :class:`Collection`    ``__len__``             ``index``, and ``count``

:class:`MutableSequence`   :class:`Sequence`      ``__getitem__``,        Inherited :class:`Sequence` methods and
                                                  ``__setitem__``,        ``append``, ``reverse``, ``extend``, ``pop``,
                                                  ``__delitem__``,        ``remove``, and ``__iadd__``
                                                  ``__len__``,
                                                  ``insert``

:class:`ByteString`        :class:`Sequence`      ``__getitem__``,        Inherited :class:`Sequence` methods
                                                  ``__len__``

:class:`Set`               :class:`Collection`    ``__contains__``,       ``__le__``, ``__lt__``, ``__eq__``, ``__ne__``,
                                                  ``__iter__``,           ``__gt__``, ``__ge__``, ``__and__``, ``__or__``,
                                                  ``__len__``             ``__sub__``, ``__xor__``, and ``isdisjoint``

:class:`MutableSet`        :class:`Set`           ``__contains__``,       Inherited :class:`Set` methods and
                                                  ``__iter__``,           ``clear``, ``pop``, ``remove``, ``__ior__``,
                                                  ``__len__``,            ``__iand__``, ``__ixor__``, and ``__isub__``
                                                  ``add``,
                                                  ``discard``

:class:`Mapping`           :class:`Collection`    ``__getitem__``,        ``__contains__``, ``keys``, ``items``, ``values``,
                                                  ``__iter__``,           ``get``, ``__eq__``, and ``__ne__``
                                                  ``__len__``

:class:`MutableMapping`    :class:`Mapping`       ``__getitem__``,        Inherited :class:`Mapping` methods and
                                                  ``__setitem__``,        ``pop``, ``popitem``, ``clear``, ``update``,
                                                  ``__delitem__``,        and ``setdefault``
                                                  ``__iter__``,
                                                  ``__len__``


:class:`MappingView`       :class:`Sized`                                 ``__len__``
:class:`ItemsView`         :class:`MappingView`,                          ``__contains__``,
                           :class:`Set`                                   ``__iter__``
:class:`KeysView`          :class:`MappingView`,                          ``__contains__``,
                           :class:`Set`                                   ``__iter__``
:class:`ValuesView`        :class:`MappingView`,                          ``__contains__``, ``__iter__``
                           :class:`Collection`
:class:`Awaitable`                                ``__await__``
:class:`Coroutine`         :class:`Awaitable`     ``send``, ``throw``     ``close``
:class:`AsyncIterable`                            ``__aiter__``
:class:`AsyncIterator`     :class:`AsyncIterable` ``__anext__``           ``__aiter__``
:class:`AsyncGenerator`    :class:`AsyncIterator` ``asend``, ``athrow``   ``aclose``, ``__aiter__``, ``__anext__``
========================== ====================== ======================= ====================================================

