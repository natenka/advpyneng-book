Абстрактные классы в стандартной библиотеке Python
--------------------------------------------------

.. tabularcolumns:: |l|L|L|L|

=================== ====================== ======================= ====================================================
ABC                 Inherits from          Abstract Methods        Mixin Methods
=================== ====================== ======================= ====================================================
Container                                  __contains__  
Hashable                                   __hash__  
Iterable                                   __iter__  
Iterator            Iterable               __next__                __iter__  
Reversible          Iterable               __reversed__  
Generator           Iterator               send, throw             close, __iter__, __next__  
Sized                                      __len__  
Callable                                   __call__  
Collection          Sized,                 __contains__,
                    Iterable,              __iter__,
                    Container              __len__  
=================== ====================== ======================= ====================================================

