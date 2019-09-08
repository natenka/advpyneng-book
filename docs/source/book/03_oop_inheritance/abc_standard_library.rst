Абстрактные классы в стандартной библиотеке Python
--------------------------------------------------

.. tabularcolumns:: |l|L|L|L|

================== ================== ========================================
ABC                Abstract Methods   Mixin Methods
================== ================== ========================================
Container          __contains__  
Hashable           __hash__  
Iterable           __iter__  
Iterator           __next__            __iter__  
Reversible         __reversed__  
Generator          send, throw         close, __iter__, __next__  
Sized              __len__  
Callable           __call__  
Collection         __contains__,
                   __iter__,
                   __len__  

Sequence           __getitem__,        __contains__, __iter__, __reversed__,
                   __len__             index, and   count  

MutableSequence    __getitem__,        Inherited Sequence methods and
                   __setitem__,        append, reverse, extend,  pop,
                   __delitem__,        remove,  __iadd__  
                   __len__,
                   insert  
================== =================== =======================================

