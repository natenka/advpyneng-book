Абстрактные классы в стандартной библиотеке Python
--------------------------------------------------

.. tabularcolumns:: |l|L|L|L|

=================== =============== =================== ==========================================
ABC                 Inherits from   Abstract Methods    Mixin Methods
=================== =============== =================== ==========================================
Container                           __contains__
Hashable                            __hash__
Iterable                            __iter__
Iterator            Iterable        __next__            __iter__
Reversible          Iterable        __reversed__
Generator           Iterator        send, throw         close, __iter__, __next__
Sized                               __len__
Callable                            __call__
Collection          Sized,          __contains__,
                    | Iterable,       __iter__,
                    | Container       __len__

Sequence            Reversible,     __getitem__,        __contains__, __iter__, __reversed__,
                    | Collection      __len__             index, and count

MutableSequence     Sequence        __getitem__,        Inherited :class:Sequence methods and
                                    __setitem__,        append, reverse, extend, pop,
                                    __delitem__,        remove, and __iadd__
                                    __len__,
                                    insert

ByteString          Sequence        __getitem__,        Inherited :class:Sequence methods
                                      __len__

Set                 Collection      __contains__,       __le__, __lt__, __eq__, __ne__,
                                    __iter__,           __gt__, __ge__, __and__, __or__,
                                    __len__             __sub__, __xor__, and isdisjoint

MutableSet          Set             __contains__,       Inherited :class:Set methods and
                                    __iter__,           clear, pop, remove, __ior__,
                                    __len__,            __iand__, __ixor__, and __isub__
                                    add,
                                    discard

Mapping             Collection      __getitem__,        __contains__, keys, items, values,
                                    __iter__,           get, __eq__, and __ne__
                                    __len__

MutableMapping      Mapping         __getitem__,        Inherited :class:Mapping methods and
                                    __setitem__,        pop, popitem, clear, update,
                                    __delitem__,        and setdefault
                                    __iter__,
                                    __len__


MappingView         Sized                               __len__
ItemsView           MappingView,                        __contains__,
                    Set                                 __iter__
KeysView            MappingView,                        __contains__,
                    Set                                 __iter__
ValuesView          MappingView,                        __contains__, __iter__
                    Collection
Awaitable                           __await__
Coroutine           Awaitable       send, throw         close
AsyncIterable                       __aiter__
AsyncIterator       AsyncIterable   __anext__           __aiter__
AsyncGenerator      AsyncIterator   asend, athrow       aclose, __aiter__, __anext__
=================== =============== =================== ==========================================

