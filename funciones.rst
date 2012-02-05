Definición de funciones, encapsulamiento y módulos
==================================================

Aunque Python es estrictamente un lenguaje orientado a objetos tiene
todas las piezas necesarias para utilizar el paradigma procedimental,
también llamado "código spaghetti con funciones para que quien lo lea
no se atragante".

Python, al igual que Matlab, no diferencia entre funciones y
subrutinas pero al igual que fortran pasa siempre los argumentos por
referencia. Esto significa que si cambiamos alguno de los argumentos
de entrada lo estaremos cambiando de verdad, no una hipotética copia
hecha en tiempo de ejecución, así que cuidadín.

La función más sencilla que podemos definir es es la función vacía sin
argumentos:

.. code-block:: python

   >>> def none():
   ...     pass

Es una función que no recibe ningún argumento, no hace nada y no
devuelve ningún argumento de salida.

Duck Typing
-----------

Construyamos una función un poco más complicada.

.. code-block:: python

   >>> from math import sqrt
   >>> def rms(a):
   ...     return sqrt(a**2.mean())

En esta vemos todas las piezas necesarias para definir una función de
verdad. Recibe un argumento, *a*, realiza un cálculo con este mismo
argumento y devuelve un resultado a la salida. Ahora intentmos
llamarla desde el intérprete:

   >>> rms([1,2,3,4])
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "<stdin>", line 2, in rms
   TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'

Este ejemplo nos sirve para introducir el concepto de *duck
typing*. Cuando hemos definido la función func:`rms` y hemos definido el
argumento *a* no hemos especificado ningún tipo.  Declarar los
argumentos de entrada y de salida es algo obligatorio en, por ejemplo,
Fortran y C. En cambio en Matlab no es necesario porque la mayoría de
las variables tienen el mismo tipo, una matriz.  En cambio Python es
un lenguaje orientado a objetos así que, estrictamente hablando, tiene
infinitos tipos posibles. Sin embargo al definir la función no se nos
pide que declaremos de qué tipo es. Encima en el cuerpo de la
función asumimos que el argumento de entrada 'a' se puede elevar al
cuadrado y dispone del método :meth:`mean`. ¡Y nadie nos avisa de lo
mucho que podemos cagarla con esto!

Este es el concepto de *duck typing*. Uno puede hacer lo que le dé la
real gana dentro de cualquier bloque de función, o en un método, y es
responsable de lo que haya dentro. Y si da un error es culpa del
programador.  Este comportamiento no implica que Python sea un
lenguaje menos formal.  Si en un lenguaje donde tenemos que declarar
el tipo de todos los argumentos nos equivocamos llamando una función
nos avisará en tiempo de compilación. Pero como Python es un lenguaje
interpretado la decisión ha sido dejar que estos errores simplemente
sucedan en tiempo de ejecución.

En el caso de la función anterior nosotros, como programadores,
definimos la función :func:`rms`, por Root Mean Square, por la raíz cuadrada
de cualquier tipo que pueda elevarse al cuadrado y disponga del método
:meth:`mean()`.

Afortunadamente, por si nos equivocamos y pasamos a :func:`rms` algo que
no cuadra, el sistema de excepciones de Python es excelente. Quizás el
mejor que uno pueda encontrar. Si nos fijamos en el mensaje de error
vemos que es perfectamente explicativo: *no puedo elevar al cuadrado
una lista de enteros*.  Entonces llegamos a la conclusión que la
función func:`rms` está diseñada para funcionar con un tipo que no es la
lista y que dispone del método :meth:`mean`, como por ejemplo un
:class:`array`.

.. code-block:: python

   >>> from numpy import array
   >>> rms(array([1,2,3,4,5,6],dtype='double')
   3.8944404818493075

.. note::

   Acabamos de utilizar la clase :class:`array` del módulo :mod:`numpy`. Es
   una clase esencial para el Cálculo Numérico en Python así que le
   dedicaremos un capítulo entero más adelante.

Docstrings
----------

Si no hay pistas sobre los tipos en las cabeceras tendremos que
documentar convenientemente cada función. Lo más sencillo es utilizar
una cadena de texto con soporte para salto de línea justo después de
la definición de la cabecera

.. literalinclude:: _static/func1.py
   :language: python


Ahora utilizamos la función :func:`help` para ver qué pinta tiene en
la consola

.. code-block:: python

   >>> help(rms)
   Help on function rms in module func1:

   rms(a)
       Computes the root mean square of *a*, which is a numpy array. The
       result is a double constant.

Python disponde de excelentes herramientas para tratar la
documentación incluida en el código. Disponemos de herramientas
capaces de crear manuales a partir de dicha documentación, formatos
propios para redactarla e incluso podemos introducir notación
matemática en LaTeX para describir algoritmos.

La herramienta en la que está redactado esta documentación, Sphinx, es
de gran ayuda cuando cualquier proyecto empieza a crecer de verdad
para mantener todo bien ordenado y documentado.

Módulos
-------

Podemos utilizar los módulos para ordenar las funciones que vayamos
escribiendo de manera eficaz. Tomemos como ejemplo el siguiente
archivo llamado ``means.py`` que contiene la definición de varias
medias posibles:

.. literalinclude:: _static/means.py
   :language: python

Quizás la manera más efectiva de gestionar colecciones de funciones es
la siguiente:

.. code-block:: python

   >>> import means
   >>> help(means)
   Help on module means:

   NAME
       means
   
   FILE
       /home/guillem/intropy/_static/means.py
   
   FUNCTIONS
       cmc(a)
           Computes the cubic root mean cube of *a*, which is a numpy array.
           The result is a double constant.
       
       nmn(a, n)
           Computes the nth root mean nth power of *a*, which is a numpy array.
           The result is a double constant.
       
       rms(a)
           Computes the root mean square of *a*, which is a numpy array. The
           result is a double constant.
       
       sqrt(...)
           sqrt(x)
           
           Return the square root of x.

Esto implica que podemos utilizar el nombre del módulo, :mod:`means`,
como prefijo del espacio de nombres:

.. code-block:: python

   >>> from numpy import array
   >>> means.cmc(array([1,2,3,4,5,6],dtype="double"))
   4.1888593641200274

Y todo esto gratis sólo por haber ordenado las distintas funciones
dentro del mismo archivo.

Intermezzo. Tuples
------------------

Ya concemos un tipo básico de secuencia, la lista.  Es el momento de
conocer otro: el tuple.

Podemos hacernos una idea intuitiva de qué es si analizamos la
asignación múltiple. Cuando escribo lo siguiente:

.. code-block:: python

   >>> a = 2

Asigno el literal *número entero 2* a la variable *a*. Podemos
complicar un poco la asignación haciendo dos a la vez

.. code-block:: python

   >>> a,b = 1,2

Acabo de realizar una asignación múltiple. En este caso la variable
*a* contendrá el número entero 1 y la variable *b* el número
entero 2. Podemos utilizar también la siguiente sintaxis:

.. code-block:: python

   >>> (a,b) = (1,2)

A todos los efectos esta sentencia ejecutable es idéntica a la
anterior. La única diferencia es que en la anterior hemos utilizado la
sintaxis reservada a las asignaciones múltiples mientras que en este
caso hemos utilizado una variable *doble*. Y es precisamente este
concepto de variable múltiple el que nos sirve para entender el
*tuple*.

El tuple es una secuencia *inmutable* que se puede utilizar, a todos
los efectos, como una secuencia de variables de longitud arbitraria.

El hecho que no sea inmutable diferencia el tuple de la lista. Sólo
podemos cambiar el tuple, no podemos cambiar ninguno de sus elementos
independientemente.  Como demostración:

.. code-block:: python 

   >>> a = (1,2,False)
   >>> a[2] = True
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'tuple' object does not support item assignment

.. important::

   Un tuple **no** sirve para lo mismo que una lista. Un tuple sirve
   para concatenar variables sin que haya una relación formal entre
   ellas. Las listas son para conjuntos ordenados de elementos que,
   tengan o no el mismo tipo, estan relacionados conceptualmente.

Los tuples se indexan igual que las listas, utilizando corchetes. No
sólo no se pueden cambiar los elementos de un tuple sino que tampoco
se pueden sustraer o añadir más elementos.

Funciones que retornan varias variables
---------------------------------------

Gracias al concepto de tuple una función que retorna varias variables
no es más que una función que retorna un tuple

.. code-block:: python

   >>> def something(a):
   ...     return (a,a**2,a**3)
   ...
   >>> a,squarea,cubea = something(3)
   >>> print cubea
   27
   >>> (a,squarea,cubea) = something(2)
   >>> print cubea
   8
   >>> a = something(4)
   >>> print a
   (4, 16, 64)

Funciones con argumentos por omisión
------------------------------------

Podemos definir argumentos opcionales con un valor por omisión con la
siguiente notación

.. code-block:: python

   >>> def something(a,b=2)
   ...     return(a,a**b,a**(b+1))
   ...
   >>> a,squarea,cubea = something(3)
   >>> print cubea
   27
   >>> a,squarea,cubea = something(3,1)
   >>> print cubea
   9

Empaquetar y desempaquetar argumentos
-------------------------------------

Podemos empaquetar argumentos de una función utilizando un tuple y el
operador asterisco. Por ejemplo, si una función debe recibir dos
argumentos podemos pasarle un único argumento doble y desempaquetarlo
con el asterisco

.. code-block:: python

   >>> a,squarea,cubea = something(*(3,1))
   ... print cubea
   9

Podemos también desempaquetar argumentos con el operador doble
asterisco (``**``) y un diccionario pero como no sabemos qué es un
diccionario vamos a por otro *intermezzo*.

Intermezzo. Diccionarios.
-------------------------

Hemos visto ya dos tipos distintos de tipos derivados: las listas y
los tuples. Los primeros sirven para almacenar conjuntos ordenados de
valores en los que el orden cuenta y los segundos sirven para juntar
valores de manera inmutable.

En la programación moderna se ha popularizado una manera de almacenar
datos de tipo *key-value*. En las listas y los tuples podemos acceder
a cada valor a través de un índice, en el caso de Python numerado
desde el cero.  El índice es, de manera natural, un número
entero. Esta no es la manera necesariamente más adecuada para nombrar
un valor, por ejemplo cuando una lista contiene números enteros y
podemos confundir fácilmente el índice con el contenido.

El almacenamiento *key-value* asigna una clave a cada valor que
contiene el tipo derivado, de manera que forman una pareja. La
impliementación de esta estrategia en Python es el diccionario.

.. code-block:: python

   >>> d = {1 : 1, 'dos': 2, 3: [1,2,3]}
   >>> print d
   {1: 1, 3: [1, 2, 3], 'dos': 2}
   >>> d['cuatro'] = 2.443
   >>> print d
   {'cuatro': 2.443, 1: 1, 3: [1, 2, 3], 'dos': 2}
   >>> for key in d.iterkeys():
   ...     print d[key]
   ... 
   2.443
   1
   [1, 2, 3]
   2


Vemos que los diccionarios son mutables, podemos eliminar o añadir más
parejas clave-valor. La manera de acceder a un valor a través de la
clave es la misma que utilizaríamos si fuera el índice de una lista o
un tuple, con la diferencia que este no es necesariamente un entero.

El ejemplo anterior no es muy bueno porque da un rodeo por las claves
para iterar sobre los valores. Una manera un poco más efectiva de
hacerlo es utilizando el método :meth:`itervalues`

.. code-block:: python

   >>> for value in d.itervalues():
   ...     print value
   ... 
   2.443
   1
   [1, 2, 3]
   2

.. warning::

   En los diccionarios, como en cualquier almacenamiento *key-value*,
   el orden en el que realmente están almacenadas las parejas no se no
   se considera relevante. Si creamos un diccionario introduciendo las
   parejas en un orden dado puede ser que Python lo cambie por
   cualquier motivo que se puede escapar a nuestra comprensión.

De vuelta al empaquetado y desempaquetado de argumentos
-------------------------------------------------------

Ahora que ya sabemos lo básico sobre los diccionarios podemos volver
al tema que traíamos entre manos. El problema de pasar argumentos con
el tuple y el operador ``*`` es que quizás no queremos introducir
todos los argumentos en una llamada donde algunos de los argumentos
tienen un valor por omisión.

Os pongo un ejemplo

.. code-block:: python

   >>> def dummy(a,b=2,c=3,d=4):
   ...    print a,c
   ...    print b,d
   ... 
   >>> dummy(1)
   1 3
   2 4

¿Cómo conseguimos llamar la función anterior sólo mencionando los
agumentos ``a`` y ``d``? Pues con los diccionarios y el operador
``**`` es tan sencillo como lo siguiente

.. code-block:: python

   >>> dummy(1,**{'d':123})
   1 3
   2 123
   >>> dummy(**{'a':321,'d':123})
   321 3
   2 123

.. note::

   En la función anterior el argumento ``a`` es imprescindible. Sea
   cual sea la manera en la que escojamos introducir ese argumento no
   nos lo podemos olvidar o recibiremos un error.

Funciones *lambda*
------------------

Una función *lambda* es una estructura que *en tiempo de ejecución*
convierte una variable en una función con argumentos. Aunque algunos
habrán visto este tipo de estructuras por primera vez en Matlab con
los *function handles*, expresados por el símbolo ``@``, las funciones
*lambda* son un invento de los años cincuenta.

De hecho son un invento del primer lenguaje interpretado de la
historia, *lisp* que es casi contemporáneo a Fortran y fue el primer
lenguaje que utilizaba el paradigma funcional.  *Lisp* tuvo un gran
arranque y se convirtió rápidamente en el lenguaje por excelencia en
la investigación en inteligencia artificial pero como nunca se enseñó
demasiado en las universidades cayó un poco en el olvido.

El paradigma funcional sigue vivo en algunos lenguajes de programación
modernos como Scheme o Haskell, incluso Python adopta algunas de las
herramientas propias de la programación funcional.

La estructura de una función *lambda* en Python conserva la forma que
tenía en *lisp*:

.. code-block:: python

  >>> square = lambda x: x*x
  >>> print square(3)
  9

Si necesitamos más de una variable

.. code-block:: python

  >>> prod = lambda x,y: x*y
  >>> print prod(3,4)
  12

Las funciones *lambda* son muy útiles para definir funciones cortas
que sólo usaremos una vez.

Programación funcional
----------------------

Python no sigue el paradigma funcional pero reinterpreta algunas de
sus características más útiles como son las funciones :func:`map` y
:func:`reduce`

La primera aplica una función dada a todos los elementos de una lista
o secuencia y nos devuelve una lista con el resultado

.. code-block:: python

  >>> print map(lambda x:x[0]*x[1],[(1,2),(2,3),(3,4),(4,5)])
  [2, 6, 12, 20]

O podemos empezar a utilizar los módulos de la librería estándar para
empezar a contestarnos preguntas que siempre quisimos formular.
¿Cuánto suman cada una de las combinaciones con repetición de dos
elementos de los números del 1 al 4?

