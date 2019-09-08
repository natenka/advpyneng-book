Абстрактные классы в стандартной библиотеке Python
--------------------------------------------------

.. tabularcolumns:: |l|L|L|L|

.. list-table:: ABC
   :widths: 5, 5, 15
   :header-rows: 1
   :class: longtable

   * - ABC
     - Абстрактные методы
     - Mixin Methods
   * - Container
     -  __contains__
     -
   * - Hashable
     - __hash__
     -
   * - Iterable
     - __iter__
     - 
   * - Iterator    
     - __next__       
     - __iter__
   * - Reversible  
     - __reversed__
     - 
   * - Generator   
     - send, throw
     - close, __iter__, __next__
   * - Sized       
     - __len__
     - 
   * - Callable    
     - __call__
     - 
   * - Collection  
     - __contains__, __iter__, __len__
     - 
   * - Sequence    
     - __getitem__, __len__        
     - __contains__, __iter__, __reversed__, index, count
   * - MutableSequence
     - __getitem__, __setitem__,
      | __delitem__, __len__, insert
     - Inherited Sequence methods and append, reverse, extend, pop, remove, __iadd__
   * - ByteString  
     - __getitem__, __len__
     - Inherited Sequence methods
   * - Set         
     - __contains__, __iter__, __len__
     - __le__, __lt__, __eq__, __ne__, __gt__, __ge__, __and__, __or__, __sub__, __xor__, isdisjoint
   * - MutableSet  
     - __contains__, __iter__, __len__, add, discard
     - Inherited Set methods and clear, pop, remove, __ior__, __iand__, __ixor__, and __isub__
   * - Mapping     
     - __getitem__, __iter__, __len__
     - __contains__, keys, items, values, get, __eq__, __ne__
   * - MutableMapping
     - __getitem__, __setitem__, __delitem__, __iter__, __len__
     - Inherited Mapping methods and pop, popitem, clear, update, setdefault
   * - MappingView
     - 
     - __len__
   * - ItemsView                           
     - 
     - __contains__,  __iter__
   * - KeysView                            
     - 
     - __contains__,  __iter__
   * - ValuesView                          
     - 
     - __contains__,  __iter__
   * - Awaitable   
     - __await__
     - 
   * - Coroutine   
     - send, throw
     - close
   * - AsyncIterable
     - __aiter__
     - 
   * - AsyncIterator
     - __anext__      
     - __aiter__
   * - AsyncGenerator
     - asend, athrow
     - aclose, __aiter__, __anext__

