.. raw:: latex

   \newpage

17. Модули async
================

Почти все модули, которые работали в многопоточном варианте, не будут работать
с asyncio, так как они будут блокировать работу и не будут отдавать управление
циклу событий.

В этом разделе рассматриваются модули:

* asyncssh
* scrapli
* netdev

.. toctree::
   :maxdepth: 1
   :hidden:

   asyncssh
   scrapli
   netdev
   further_reading
   ../../exercises/17_exercises.rst
