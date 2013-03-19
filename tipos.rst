Tipos, o cómo programar en Python
=================================

En Python todos los tipos intrínsecos son objetos y como tales tienen
atributos y métodos. Un viaje por los tipos intrínsecos de Python es,
en el caso de no haber utilizado nunca la orientación a objetos, una
demostración práctica sobre cómo se usan objetos definidos por
terceros. De hecho, estrictamente hablando, definir nuevos tipos en
Python es utilizar un conjunto bastante limitado de las
funcionalidades de la orientación a objetos.

Ya hemos hablado de los números enteros, reales y complejos; de las
listas, los tuples y los diccionarios; sobre los que volveremos a
hablar en este capítulo. Nos faltan las cadenas de caracteres.

La clase :class:`string`
------------------------

Aunque las cadenas de caracteres no son un tipo demasiado importante
en el Cálculo son la sustancia de multitud de algoritmos. Sólo veremos
lo más básico de esta clase que, en muchos sentidos, no es más que una
cadena de caracteres.

.. note::

  Una diferencia importante entre Python 2 y Python 3 es que en la
  en el primero existen diferencias entre las codificaciones de
  caracteres. No es lo mismo un caracter ASCII de uno latin1 o de uno
  UTF-8. La codificación es una caraceterística propia de algunos
  tipos de cadenas de caracteres. Esto cambia en Python 3, todas las
  cadenas de caracteres son Unicode, en este caso UTF-8. Esto implica
  que incluso los archivos de código en Python serán unicode y que uno
  puede utilizar tildes y caracteres localizados para escribir
  comentarios.

  El soporte para Unicode es esencial en lo que respecta a
  internacionalización y nos incumbe a nosotros puesto que no siempre
  querremos utilizar inglés para todo.

Para introducir una cadena de caracteres podemos utilizar bien
comillas simples o comillas dobles.

.. code-block:: python 

  >>> a = 'string'
  >>> b = "string"

o bien podemos crear cadenas de caracteres vacías

.. code-block:: python

  >>> c = ''
  >>> d = str()

Las cadenas de caracteres, como hemos visto anteriormente, soportan
algunas operaciones aritméticas como la suma y la multiplicación;
obviamente reinterpretadas como secuencia de caracteres.

Una de las operaciones más habituales con caracteres es la de
reconocer secuencias. Para ello contamos con la función :func:`find` y
la sentencia ``in``.

.. code-block:: python

  >>> 'r' in 'string'
  True
  >>> str('string').find('r')
  2

Uno de los pocos motivos por el que queremos un string en Cálculo
Numérico es para manipular archivos que contienen datos y sus
nombres. Por ejemplo, numerarlos:

.. code-block:: python

  >>> for i in range(10):
  ...     'datafile'+str(i).zfill(3)+'.dat'
  'datafile000.dat'
  'datafile001.dat'
  'datafile002.dat'
  'datafile003.dat'
  'datafile004.dat'
  'datafile005.dat'
  'datafile006.dat'
  'datafile007.dat'
  'datafile008.dat'
  'datafile009.dat'

.. important::

  Este es un buen ejemplo para introducir el concepto de
  *pythonic*. En Python, como en cualquier lenguaje de programación,
  hay infinitas maneras de implementar algo. Especialmente si el
  lenguaje es muy extenso y es poco estricto en lo que a sintaxis se
  refiere. Este es precisamente el caso de Python.

  En el ejemplo anterior hemos creado una cadena de caracteres
  utilizando el operador aritmético suma para concatenar
  caracteres. Aunque esto sea perfectamente correcto y leíble no es el
  modo más *pythonic* de llegar al objetivo. Es *unpythonic*

  Este adjetivo se suele utilizar para implementaciones que, en vez de
  utilizar alguna funcionalidad lateral del lenguaje, como por ejemplo
  el comportamiento de un operador aritmético cuando se aplica a
  cadenas de caracteres, utiliza un método más leíble y mejor
  documentado.

  Esta distinción es completamente subjetiva y sólo puede utilizarse
  cuando ya se cuenta con una sólida experiencia programando en
  Python.

  Un ejemplo de lo que es o no *pythonic* es optar por utilizar de
  manera casi obsesiva los métodos de los tipos más usuales como
  :class:`str`, :class:`list` o :class:`dict`. Estas clases están
  implementadas enteramente en C y utilizar sus métodos suele ser más
  eficiente que implementar el algoritmo nosotros mismos.

Podemos proponer una implementación más convencional de lo anterior
utilizando el método :meth:`join` de la clase :class:`str`

.. code-block:: python

  >>> for i in range(10):
  ...     str().join(['datafile',str(i).zfill(3),'.dat'])
  ... 
  'datafile000.dat'
  'datafile001.dat'
  'datafile002.dat'
  'datafile003.dat'
  'datafile004.dat'
  'datafile005.dat'
  'datafile006.dat'
  'datafile007.dat'
  'datafile008.dat'
  'datafile009.dat'

Otra posibilidad bastante útil es la de completar cadenas de
caracteres dando formato a sus argumentos al igual que hacemos con el
comando ``print`` en C.  Por ejemplo:

.. code-block:: python

  >>> for i in range(10):
  ...     'datafile%03i.dat'%(i)
  ... 
  'datafile000.dat'
  'datafile001.dat'
  (...)

Lo que viene después del símbolo de porcentaje es un tuple en el que
podemos alinear todos los argumentos que tenga la cadena de
caracteres. Aunque, otra vez, hay una manera mucho más *pythonic* de
hacer exactamente lo mismo, mediante la función :func:`format` de
cualquier cadena de caracteres

  >>> for i in range(10):
  ...     'datafile{:03d}.dat'.format(i)
  ... 
  'datafile000.dat'
  'datafile001.dat'
  (...)

.. tip::

  Hay un buen tutorial sobre la manera de escribir cadenas de
  caracteres con formato en la documentación estándar del lenguaje

Empezamos a ver que si buceamos un poco por entre la documentación de
Python podemos llegar a escribir código perfectamente leíble,
eficiente y bonito.

.. code-block:: python

  >>> from random import choice
  >>> for i in range(10):
  ...     'Lanzamiento {}, me ha salido {}'.format(i,choice(['Cara','Cruz']))
  ... 
  'Lanzamiento 0, me ha salido Cruz'
  'Lanzamiento 1, me ha salido Cara'
  'Lanzamiento 2, me ha salido Cruz'
  'Lanzamiento 3, me ha salido Cara'
  'Lanzamiento 4, me ha salido Cara'
  'Lanzamiento 5, me ha salido Cruz'
  'Lanzamiento 6, me ha salido Cruz'
  'Lanzamiento 7, me ha salido Cara'
  'Lanzamiento 8, me ha salido Cara'
  'Lanzamiento 9, me ha salido Cruz'

Esto nos llevaría un buen rato en cualquier otro leguaje que no fuera
Python, incluso en Matlab.

Literal
.......

Hay múltiples maneras de definir una cadena de caracteres directamente
sin necesidad de hacer una llamada a la clase :class:`str`. Podemos
utilizar bien las comillas simples o las comillas dobles
indistintamente o cuando necesitemos alguno de los dos caracteres
dentro. Por ejemplo, si necesitamos una comilla simple dentro de una
cadena de caracteres:

.. code-block:: python

  >>> print "I'm afraid that was the funniest practical joke"
  I'm afraid that was the funniest practical joke

O viceversa, si necesitamos algunas comillas dobles podemos introducir
los caracteres entre comillas simples.

También disponemos del control de carro con los caracteres especiales
usuales como

.. code-block:: python

  >>> print "I am a whale!\n'______'"
  I am a whale!
  '______'

Pero si lo que realmente queremos es introducir una cadena de
caracteres con más de una línea tenemos un literal específico para
ello

.. code-block:: python

  >>> print """I have seen {}
  ... elephants hanging
  ... on a spider web""".format('MILLIONS!!!')
  I have seen MILLIONS!!!
  elephants hanging
  on a spider web

También en este caso podemos utilizar comillas simples o dobles.

Intermezzo. Archivos y la clase :class:`file`
---------------------------------------------

En Cálculo Numérico utilizamos esencialmente números. Las cadenas de
caracteres nos sirven para poder expresar texto, normalmente
datos. Estos datos suelen terminar en archivos que contienen, oh
sorpresa, caracteres.

El problema es que de momento no tenemos ni idea de cómo abrir, leer,
escribir y cerrar un archivo.  Para ello necesitamos conocer la clase
:class:`file` que casi siempre instanciaremos a partir de la función
:func:`open` de la librería estándar.

.. note::

  Soy un usuario de Linux desde hace ya un montón de años. Algunos de
  los ejemplos de este libro rezuman cultura UNIX por todos los poros
  y uno puede pensar que Python es un juguetito de los que utilizamos
  esta familia de sistemas operativos.

  Esto no es verdad en absoluto. Los desarrolladores de Python han
  hecho un importante esfuerzo para abstraer prácticamente cualquier
  función del sistema operativo en el que estemos trabajando. Muchas
  de las utilidades para no tener que depender del SO están en los
  módulos :mod:`os`, :mod:`sys` y :mod:`shutil`. Aunque no hemos
  hablado sobre la librería estándar empezaré a utilizarlos aquí para
  que los ejemplos funcionen en cualquier sistema operativo.

.. important::

  La manera usual de ejecutar Python en sistemas UNIX es llamarlo
  desde una consola. Esta manera de funcionar tiene implicaciones
  importantes porque entonces el intérprete cargará ese directorio
  como camino para acceder a los archivos mediante la localización
  relativa.

  En Windows lo más normal es ejecutar un script desde la interfaz
  gráfica. El comportamiento del intérprete será cargar el directorio
  en el que se encuentre el script para que el mismo pueda acceder al
  entorno a partir de su posición relativa.

.. note::

  SAGE es un bicho raro en lo que respecta a archivos porque se trata
  de una aplicación web.

Para cargar una instancia de un objeto :class:`file` basta con
utilizar la función :func:`open`, para la que no tenemos que importar
ningún módulo

.. code-block:: python

  >>> fh = open('tipos.rst','r')

El segundo argumento se refiere a los permisos con los que abrimos el
archivo, en este caso con permisos de sólo lectura. A partir de ahí ya
disponemos de todos los elementos necesarios para leer el archivo.

.. code-block:: python

  >>> print fh.readline()
  Tipos, o cómo programar en Python
  
  >>> print fh.readline()
  =================================

En este caso la variable ``fh`` dipone de los métodos necesarios tanto
para leer línea a línea o devolver cada una de las líneas del archivo
como una lista o para leerlo byte a byte en un estilo más parecido a
C.

La misma clase que nos permite escribir archivos también nos permite
leerlos, siempre que se trate de texto.

Al final debemos acordarnos de cerrar el archivo para no ir perdiendo
memoria por ahí.

.. code-block:: python

  >>> fh.close()

Formato binario
...............

Uno puede leer y escribir números como si fuera texto, uno es libre de
hacerlo, pero es una estupidez de un tamaño tan estremecedor que
debería estar tipificado como delito con pena de cárcel. Si uno quiere
guardar números, como una matriz o una ristra de datos, lo mejor es
guardarlo en formato binario del mismo modo que el sistema lo
representa en memoria. Es sin duda la manera más eficiente de
hacerlo.

Esto es independiente de cómo se abra, se lea, o se cierre el
archivo. El archivo no es distinto, lo único que cambia es su
contenido.

Esto abre una casuística sobre cómo representar los números y los
metadatos asociados como las dimensiones o la precisión. Por suerte
:mod:`numpy` y los módulos :mod:`pickle` y :mod:`cpickle` harán el
trabajo sucio por nosotros.

La clase :class:`list`
----------------------

Ya hemos hablado sobre las listas pero es importante que les demos un
segundo vistazo.

Lo más importante que debemos saber de una lista es que **no es un
array**. No es una buena idea hacer operaciones aritméticas sobre los
elementos de una lista porque son una secuencia de elementos que no
necesariamente tienen el mismo tipo. Python lo sabe y se va a negar
porque no puede multiplicar una letra por un número en coma flotante.

Sin embargo las listas son quizás el tipo más utilizado en Python
porque son una manera muy eficiente de operar sobre listas de
cosas. 

.. code-block:: python

  >>> l = str('this is a list of words').split()
  >>> print l
  ['this', 'is', 'a', 'list', 'of', 'words']
  >>> l.extend('that I extend now'.split())
  >>> print l
  ['this', 'is', 'a', 'list', 'of', 'words', 'that', 'I', 'extend', 'now']

Indexación
..........

Ya hemos visto cómo funcionan los subíndices

.. code-block:: python

  >>> l.index('list')
  3
  >>> l[3]
  'list'

Lo que aún no sabemos hacer es seleccionar una secuencia dentro de la
lista a partir de los índices. Ahí debemos pararnos un instante porque
si se entiende bien a la primera no se albergarán dudas al respecto en
un futuro.

Cuando en vez de refernrnos a un elemento nos referimos a una
secuencia dentro de la lista, un *slice*, no nos referimos a los
índices sino a los intervalos que hay entre los elementos. Esto
significa que el primer elemento, el de índice 0, corresponde al
*slice* 0-1. El tercer elemento, de índice 2, corresponde al *slice*
2-3.

.. code-block:: python

  >>> l[0:1]
  ['this']
  >>> l[2:3]
  ['a']
  >>> l[9:10]
  ['now']

Aunque podemos acceder al último elemento tal como se muestra en el
ejemplo, disponemos de un atajo para no tener que saber cómo de larga
es la lista que mejora si recordamos que podemos utilizar índices
negativos:

.. code-block:: python

  >>> l[:1]
  ['this']
  >>> l[-1:]
  ['now']
 
La cosa se puede complicar. Supongamos que queremos los elementos
entre el tercero y el antepenúltimo

.. code-block:: python

  >>> l[2:-2]
  ['a', 'list', 'of', 'words', 'that', 'I']

Y que encima los queremos en el órden inverso

.. code-block:: python

  >>> l[-2:2:-1]
  ['extend', 'I', 'that', 'words', 'of', 'list']

Supongo que con esto es suficiente

Cualquier objeto que disponga de la función :func:`__getitem__` puede
indexarse y si dispone también de la función :func:`__getslice__`
podremos también obtener secuencias.  Hay un montón de clases que
disponen de estos dos métodos como :class:`str`, :class:`tuple` o, la
que más nos interesa a nosotros, :class:`array`

Comprehension expressions
.........................

Algunas veces queremos generar una lista a través de una secuencia y
una condición más o menos compleja que no se reduce a alguno de los
métodos de una lista.  Por ejemplo obtener de la lista de palabras
anterior y por orden las palabras que contienen la letra *o*. Podemos
hacerlo mediante un bucle.

.. code-block:: python

  >>> for w in l:
  ...     if 'o' in w:
  ...         s.append(w)
  ... 
  >>> print s
  ['of', 'words', 'now']

O podemos generar directamente la lista con un *comprehension*

.. code-block:: python

  >>> s = [w for w in l if 'o' in w]
  >>> print s
  ['of', 'words', 'now']

La sintaxis de estas sentencias generadoras es prácticamente la frase
en inglés: la palabra para cada palabra en la lista si la letra está
en la palabra. Sencillo.

También nos permite empezar a utilizar la sintaxis de Python como
auténticos profesionales.

.. code-block:: python

  >>> print str(' ').join([w.capitalize() for w in l])
  'This Is A List Of Words That I Extend Now'

