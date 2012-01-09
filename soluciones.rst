Soluciones a los ejercicios propuestos
======================================

Ejercicio 1
-----------

.. literalinclude:: _static/ejercicio1.py
   :language: python

Que tiene como resultado

.. code-block:: python

   >>> 
   1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946


Ejercicio 2
-----------

El ejercicio puede resolverse con un simple vistazo a la ayuda del
módulo ``random``

.. code-block:: python

   >>> import random
   >>> random.seed()
   >>> random.sample(xrange(50),5)
   [46, 43, 38, 25, 8]
