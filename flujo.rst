Control de flujo
================

Este capítulo no es más que una introducción sobre cómo hacer lo que
se puede hacer con cualquier lenguaje de programación en Python.  El
*control de flujo* es el nombre técnico de las estructuras
condicionales, los bucles y sus derivados mientras que el
*encapsulamiento* es cómo se llama a la técnica de tomar partes de
nuestro código y convertirlas en funciones.

Quiero enfatizar que esta parte, en el fondo, no tiene nada que ver
con Python. Si uno experimenta dificultades para seguir esta sección:
náuseas, mareos o desorientación espacial; recomiendo encarecidamente
tomar un curso de programación de verdad ya sea en la Universidad o
en Youtube. Ahora incluso los hay buenos.

Condicionales o sentencias if
-----------------------------

El condicional más sencillo posible es el siguiente:

.. code-block:: python

    >>> if True: print 'Verdadero'
    ...
    Verdadero

Dos cosas interesantes aquí. Hay una constante especial para
determinar verdadero, ``True``, del mismo modo que lo hay para falso
con ``False``.  Aunque se cumple la regla que se considera como falso
el 0 entero y como verdadero cualquier otro valor se enfatiza como
buena práctica que cualquier condicional debe evaluar una constante
lógica que puede tener como valor ``True`` o ``False``.

Otra peculiaridad es que no tenemos por qué pasar a la siguiente línea
si después de la condición y los dos puntos sólo queremos escribir una
línea.  De este modo estas dos sentencias son equivalentes a

.. code-block:: python

    >>> if True:
    ...     print 'Verdadero'
    ... 
    Verdadero

El intérprete, en cuanto se da cuenta que hemos escrito dos puntos,
nos cambia el símbolo de entrada a tres puntos. Esto significa que
está esperando nuestra decisión de si queremos introducir contenido en
el bloque o queremos salir de él.

Para complicar un poco más el control de flujo pasaremos de trabajar
con la consola a trabajar con scripts. Recordad que cualquier archivo
con código escrito en Python tendrá la extensión ``.py``.  Por
ejemplo:

.. literalinclude:: _static/flujo1.py
   :language: python

Vemos que la condición lógica complementaria también requiere de un
bloque de código asociado después de los dos puntos de rigor.

Vemos también varias cosas nuevas e interesantes en este programa. Uno
es el módulo ``random`` que contiene multitud de funciones específicas
para la generación de números o secuencias aleatorias de cualquier
tipo.  En este caso hemos importado la función choice, que dada una
lista (que aún no sabéis lo que es) escoge un elemento de la misma de
manera aleatoria.  De este modo, si ejecutáis el script varias veces,
algunas veces os saldrá Cara y otras veces Cruz.

.. code-block:: python

    Python 2.7 (r27:82500, Aug 07 2010, 16:54:59) [GCC] on linux2
    Type "copyright", "credits" or "license()" for more information.
    >>> ================================ RESTART ================================
    >>> 
    Cruz
    >>> ================================ RESTART ================================
    >>> 
    Cruz
    >>> ================================ RESTART ================================
    >>> 
    Cruz
    >>> ================================ RESTART ================================
    >>> 
    Cruz
    >>> ================================ RESTART ================================
    >>> 
    Cara

Aunque alguien avispado me podría decir que este programa se podía
escribir de manera mucho más eficiente ahorrándome el condicional

.. literalinclude:: _static/flujo2.py
   :language: python


Obviamente podemos introducir condiciones adicionales a la estructura
con ``elif`` y complicar un poco la estructura:

.. literalinclude:: _static/flujo3.py
   :language: python

Lo que estamos haciendo con este script es tomar tres variables,
``pos``, ``nil`` y ``neg`` que utilizaremos como contadores. La
función ``choice`` escoge entre tres valores y dependiendo de si su
valor es negativo, positivo o cero incrementa el contador
correspondiente.  En este caso la condición complementaria ``else`` no
tiene ningúna función porque las tres condiciones anteriores cubren
todo el espacio de probabilidades pero lo he dejado ahí por si alguien
tiene un ordenador que con una lógica alternativa.

Como aún no hemos visto prácticamente nada de Python cualquier
tontería nos parece novedosa.  Hay muchas cosas interesantes en este
pequeño ejemplo

* Una asignación múltiple en la primera línea

* Un bucle con condicional ``while`` en el que hemos puesto una
  condición lógica compuesta

* El operador incremento ``+=`` presente en prácticamente todos los
  lenguajes de programación excepto Matlab y Fortran.

.. admonition:: Ejercicio 1

   La sucesión de Fibonacci tiene la siguiente definición:

   .. math::

      F_{n}=\left\{ \begin{array}{cc}
      0 & n=0\\
      1 & n=1\\
      F_{n-1}+F_{n-2} & n>1\end{array}\right.

   Escribir un programa que saque por pantalla los 20 primeros
   términos de la sucesión de Fibonacci.

.. admonition:: Ejercicio 2

   Aunque los bombos y las esferas de plástico no tienen porqué ser
   imparciales se prefieren a los ordenadores para las loterías y los
   bingos. También es verdad que los generadores de números
   pseudoaleatorios tampoco son perfectos.

   Escribir un programa que sortee la primitiva, cinco extracciones de
   un conjunto de 49 números sin repetición.  Merece la pena echarle
   un vistazo a la ayuda del módulo ``random``.

Intermezzo. Listas.
-------------------

Aunque esta sección debería estar en el próximo capítulo, el destinado
a los distintos tipos que Python proporciona, es importante conocer lo
básico sobre las secuencias (la lista es un tipo de secuencia) para
entender cómo funcionan los bucles.

A diferencia de C o Fortran, en el que existen verdaderos bucles con
el ``for`` de C o el ``do`` de Fortran, en Python (al igual que en
Matlab) no existen los bucles como tal.  Lo que tenemos son iteradores
en el que asignamos a una variable el elemento siguiente de algo sobre
lo que podamos iterar.

La secuencia más común en Python es la lista, un tipo que sería algo
entre una matriz y una celda en Matlab. El literal se introduce
mediante corchetes

.. code-block:: python

   >>> a = [1,2,3,4]
   >>> print a
   [1, 2, 3, 4]

Una lista en Python es una lista de "cosas", de modo que puede
contener absolutamente cualquier valor independientemente de su tipo.

.. code-block:: python

   >>> a = [1,'hola',True]
   >>> print a
   [1, 'hola', True]

Las listas están indexadas, como cualquier cosa en Python, con la
numeración a partir de cero:

.. code-block:: python

   >>> print a[0]
   1

Una de las propiedades más curiosas y útiles a la vez de la indexación
en Python es la posibilidad de utilizar índices negativos para numerar
una secuencia desde el final. El elemento correspondiente al índice -1
será el último elemento de la secuencia

.. code-block:: python

   >>> print a[-1]
   True

Las listas son secuencias mutables, es decir que podemos cambiar
cualqiera de sus elementos por asignación

.. code-block:: python

   >>> a[-1] = False
   >>> print a
   [1, 'hola', True]

Si después de estos comandos pedís la documentación de cualquier
lista, en este caso con ``help(a)`` comprobaréis que disponemos de un
montón de métodos para manipular tanto sus elementos como el orden de
los mismos.

Veremos más sobre las listas en el siguiente capítulo. De momento ya
sabemos lo suficiente para entender el concepto de iterador.

Iteradores
----------

Quizás la función más básica que genera una lista de valores es la
función ``range``:

.. code-block:: python

   >>> print range(5)
   [0, 1, 2, 3, 4]

Vemos que se trata de una lista de valores desde cero con incremento 1
de 5 elementos.  Esta función nos permite generar un iterador tan
básico como nos es posible

.. code-block:: python

   >>> for i in range(5)
   ...     print i,
   ...
   0 1 2 3 4

Entenderemos perfectamente la diferencia entre un iterador y un bucle
con el siguiente ejemplo

.. code-block:: python

   >>> for i in range(5)
   ...     i = i**2
   ...     print i,
   0 1 4 9 16

Vemos que aunque hemos modificado la variable ``i`` dentro del bloque
correspondiente a una iteración, al entrar en la siguiente iteración,
``i`` se ha sobreescrito con el siguiente elemento de la secuencia.
Es importante tener este comportamiento en cuenta porque implica que
algunos algoritmos tal como estan publicados en C o en Fortran no
pueden ser simplemente copiados en Python. 

Podemos controlar los bucles con las sentencias ``break`` y
``continue``, por ejemplo

.. code-block:: python

   >>> for w in ['defenestrate','the','cat','now']:
   ...     if w == 'cat':
   ...         print 'No, I love cats!'
   ...         break
   ...     else:
   ...         print w
   ...
   defenestrate
   the
   No, I love cats!

En el siguiente ejemplo representamos por pantalla sólo los números
impares de la secuencia entre 0 y 9, aunque iteramos con la secuencia entera.

.. code-block:: python

   >>> for num in range(10):
   ...     if num%2 == 0:
   ...         continue
   ...     else:
   ...         print num,
   1 3 5 7 9

Esta no es ni mucho menos la manera de tratar los bucles en
Python. Los bucles en cualquier lenguaje interactivo son lentos
comparados con otros lenguajes como C o Fortran, más orientados a
obtener un buen rendimiento.  Python no es una excepción de modo que
debemos evitar iterar sobre secuencias muy largas
innecesariamente. Por ejemplo, si queremos iterar sobre sólo los
valores impares de una secuencia de números podemos filtrarla antes,
de este modo nos aseguraremos que el iterador realiza sólo los ciclos
imprescindibles.

.. code-block:: python

   >>> from itertools import ifilter
   >>> for num in ifilter(lambda x: x%2, range(10)):
   ...     print num,
   1 3 5 7 9

Para entender el ejemplo anterior necesitamos saber qué son las
funciones lambda. Llegaremos a ello poco después de entender cómo
Python reinterpreta el concepto de función.

El módulo ``itertools`` es uno de estos secretos escondidos de Python
que uno siempre se arrepiente de no haber conocido antes. Alguna de
las utilidades de este módulo, al igual que algunos de los trucos que
provienen de la programación funcional, ahorran muchas líneas de
código y aceleran el resultado significativamente.

.. important::

   Uno de los problemas de obligar a formatear el código de una
   determinada manera es el no poder dejar bloques vacíos.  Por
   ejemplo:

   .. code-block:: python

      >>> while True:
      ...    # Implement this later
      
          ^
      IndentationError: expected an indented block

   Vemos que, aunque hemos puesto el comentario precisamente donde
   debíamos se queja que no es capaz de entender el bloque de
   código. Esto es precisamente porque los comentarios no sirven para
   marcar un bloque de código; son comentarios, no código.

   Para dejar un bloque vacío contamos con la sentencia ``pass``

   .. code-block:: python

      >>> while True:
      ...     pass # Implement this later

   De este modo ya no generamos ningún error
