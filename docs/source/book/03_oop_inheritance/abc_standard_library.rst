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
========================== ====================== ======================= ====================================================

