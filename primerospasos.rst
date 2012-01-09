Primeros pasos con Python
=========================

Python es un lenguaje interpretado
----------------------------------

Cuando compilamos un programa escrito en C o en Fortran generamos un
ejecutable. Para hacer funcionar ese ejecutable nos basta con muy poca
cosa; en el caso de un "hola, mundo" basta con simplemente
ejecutarlo. El sistema operativo lo considera ejecutable y simplemente
cumple sus ordenes.

Esto no sucede así en los lenguajes interpretados. El código en Python
nunca llega a traducirse a algo que el sistema operativo pueda
entender. En Python el programa termina convertido en un ensamblador
propio que una máquina virtual es capaz de entender y ejecutar. La
consecuencia principal de este método es que *es imprescindible contar
con un intérprete de Python instalado en el ordenador para poder
ejecutar código en Python*.

Esta no es hoy en día una condición demasiado severa. El único sistema
operativo mayoritario que no cuenta con un intérprete de Python
instalado por omisión es Windows. Linux, Mac OSX, Solaris y AIX entre
otros cuentan con uno, aunque algunas veces compensa instalar una
versión más actualizada que la que encontraremos en la distribución
del sistema operativo. En el caso especial de Windows bastará con
descargarse un instalador, darle doble clic y decir que sí a todo.

**Cuando ejecutamos código en Python lo lanzamos a un intérprete que es
capaz de entender este lenguaje. A diferencia de los lenguajes
estáticos como C o Fortran en el que un compilador convierte el código
de programa en un ejecutable que el sistema operativo es capaz de
entender.**

Python es un lenguaje interactivo
---------------------------------

Python dispone de una consola interactiva con la que jugaremos un poco
antes de escribir algún que otro programa.

.. only:: latex

   .. figure:: _static/consola.png
      :align: center
      :width: 10cm

      Consola de Python en la ventana de IDLE en Linux 

.. only:: html

   .. figure:: _static/consola.png
      :align: center
      :scale: 100

      Consola de Python en la ventana de IDLE en Linux
 
La manera de acceder a esta consola difiere en función del sistema
operativo. En los UNIX y derivados bastará con abrir una consola de
sistema y teclear en ella ``python``.  En Windows bastará con abrir el
programa correspondiente que seguro que se llamará *Python shell* o
algo parecido.

Una vez estemos delante del intérprete de Python podemos empezar a
jugar. En este respecto se trata de un lenguaje de programación
parecido a Matlab, de modo que podemos probar a hacer una suma sin
problemas.

.. code-block:: python

   >>> 2+2
   4

Como seguramente intentaréis hacer algo más complicado con números,
una gran parte de las funciones matemáticas básicas están en el módulo
``math``, pero ya llegaremos a ello.

Python es un lenguaje dinámico
------------------------------

En Python no hay que declarar ninguna variable. Cada variable toma el
tipo que tenga en cada caso lo que esté en el lado derecho del
operador asignación ``=``.  Esto es cierto tanto la primera vez que se
utiliza una variable como cuando se le asigna un valor a una variable
ya existente.

Esto es sencillo en el caso de Python porque es un lenguaje
interpretado: la mayoría de las asignaciones resuelven el tipo en
tiempo de ejecución, no en tiempo de compilación del mismo modo que
sucede en Matlab o Octave.

Si volvemos al intérprete:

.. code-block:: python

   >>> a = 2.3
   >>> b = 3.2
   >>> print a*b
   7.36
   >>> a = 2
   >>> print type(a)
   <type 'int'>
   >>> print a*b
   6.4
   >>> a = 'hola'
   >>> print type(a)
   <type 'str'>
   >>> print a*b
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: can't multiply sequence by non-int of type 'float'

Creo que no hace falta dedicarle un capítulo a lo que hace la
sentencia ``print``.

Obviamete, cuando intentamos multiplicar una secuencia de caracteres
por un número en coma flotante obtenemos un error claramente
identificado como *error de tipo*.

Aunque Python está lleno de sorpresas. Si vuestra intución os dice que
una operación puede ser posible a lo mejor está implementada. Qizás
parte del éxito de Python se debe a que la gente que lo ha estado
creando durante las dos últimas décadas es gente particularmente
lista. Por ejemplo... ¿Qué sucede si multiplicamos una palabra por 2?

.. code-block:: python

   >>> a = 'hola'
   >>> print 2*a
   holahola

Pues que tenemos dos veces ``'hola'``. Entonces, si tomamos la
definición de multiplicación como una secuencia de sumas...

   >>> print a+a
   holahola

Python está lleno de detalles de estos así que algunas veces es bueno
dejarse llevar por la intuición.

Python es un lenguaje orientado a objetos
-----------------------------------------

El las carreras de informática cubrir los conceptos fundamentales de
la orientación a objetos requiere una asignatura entera. De todos los
paraidgmas de programación es el más exitoso que se conoce.  Incluso
Fortran, a partir del estándar Fortran 2003, soporta la programación
orientada a objetos. Matlab era también otro lenguaje que
históricamente había ignorado la orientación a objetos pero por
soportarlo también, a su manera. La primera implementación de la
orientación a objetos de Matlab era tan deficiente que quedó en el
olvido. A la segunda consiguieron un resultado razonable gracias a
casi copiar el planteamiento de Python.

Sin embargo las metodologías de programación es una temática larga y
miserablemente olvidada dentro de los planes de estudios de las
carreras de Ingeniería así que no nos queda más remedio que dejar un
enorme hueco en este curso.

Me centraré en comentar lo más básico y fundamental de lo que es un
objeto: los atributos y los métodos.  De este modo veremos una clase
como una manera de agrupar variables, los atributos, y funciones que
operan sobre estas variables, los métodos.

Es imposible hablar de Python y no hablar sobre la orientación a
objetos porque en Python prácticamente todo es un objeto. Por ejemplo
un número complejo es un ejemplo especialmente simple.

.. code-block:: python

   >>> c = 2+3j
   >>> print c,type(c)
   (2+3j) <type 'complex'>
   >>> c.real
   2.0
   >>> c.imag
   3.0
   >>> print c*(1j)+3
   2j

Python dispone de una constante especial, ``j`` que es la unidad
imaginaria. Como en Matlab y Octave es recomendable utilizarlo como
sufijo de un número tal como se hace en el ejemplo.  Cualquier número
imaginario tiene dos atributos, su parte real y su parte imaginaria. 

Si bien la suma de un número complejo es una operación trivial (es la
suma de sus partes real e imaginaria respectivamente) la
multiplicación no lo es.  Esto significa que la clase ``complex``
tiene la operación de producto definida internamente.  Podemos ver
todos los atributos, métodos y operaciones disponibles para una clase
utilizando la función help.

.. code-block:: python

   >>> help(c)
   Help on complex object:
   
   class complex(object)
    |  complex(real[, imag]) -> complex number
    |  
    |  Create a complex number from a real part and an optional imaginary part.
    |  This is equivalent to (real + imag*1j) where imag defaults to 0.
    |  
    |  Methods defined here:
    |  
    |  __abs__(...)
    |      x.__abs__() <==> abs(x)
    |  
    |  __add__(...)
    |      x.__add__(y) <==> x+y
    |  
    |  __coerce__(...)
    |      x.__coerce__(y) <==> coerce(x, y)
    
    (...)

Esta función que aparece como __abs__() es en realidad la función
valor absoluto, de modo que estas dos operaciones:

.. code-block:: python

   >>> abs(c)
   3.605551275463989
   >>> c.__abs__()
   3.605551275463989

Son equivalentes a todos los efectos.
   
En Python todo está modularizado
--------------------------------

Esta sí es una diferencia esencial entre Matlab/Octave y Python.  En
estos lenguajes cualquier función de la biblioteca está accesible al
intérprete. Esto hace que, a medida que el número de funciones crece,
crezca también la probabilidad de conflictos.

En Python todas las bibliotecas, incluso la biblioteca estándar, están
modularizadas. Por ejemplo, si queremos calcular el seno de :math:`pi`
tendremos que importar antes el módulo que contiene tanto la función
seno como el valor de :math:`pi`

.. code-block:: python

   >>> import math
   >>> math.sin(math.pi)
   1.2246063538223773e-16

Dos puntos a tener en cuenta:

* Cada módulo es en sí un objeto.  En este caso, después de importar
  ``math``, hemos llegado a la constante :math:`pi` como un atributo
  del módulo y a la función ``sin`` como un método.

* Prácticamente la totalidad de módulos o scripts en Python importan
  algún módulo. Podemos importar módulos prácticamente en cualquier
  punto de la ejecución pero por convención se suelen importar al
  principio.

Ahora podéis pensar que para la función seno o para :math:``pi``,
tener que arrastrar el nombre ``math`` puede ser algo tedioso;
especialmente si no hay una intención especial de agrupar las
funciones de este módulo.  Si queremos importar sólo ``sin`` y ``pi``
podemos hacerlo de la siguiente manera:

.. code-block:: python

   >>> from math import sin,pi
   >>> sin(pi)
   1.2246063538223773e-16

También podéis pensar... ¿Y si tengo que importar veinticinco
funciones del módulo ``math``? ¿Tengo que escribirlas todas en la
llamada a ``import``? Evidentemente no. Podemos utilizar un *wildcard*
para importar todo el contenido del módulo y ponerlo a disposición del
programa:

.. code-block:: python

   >>> from math import *
   >>> sin(pi)
   1.2246063538223773e-16
   >>> cos(pi)
   -1.0
   >>> tan(pi)
   -1.2246063538223773e-16

Aunque esta manera de importar el contenido de los módulos es bastante
práctica porque evita olvidos no es la recomendada para producción.

Python incluye baterías, pero no cargador
-----------------------------------------

En la introducción, porque siempre es mala idea no leer la
introducción, mencioné que para programar en Python es una gran idea
acostumbrarse a utilizar un interfaz de desarrollo integrada (IDE)
como Eclipse; algo más sofisticado que IDLE.

Cuando se dice que Python incluye baterías se menciona el hecho que la
biblioteca estándar es enorme comparada con otros lenguajes de
programación, que sólo incluye funcionalidades básicas. La biblioteca
estándar de Python incluso viene con la posibilidad de generar
interfaces gráficas con ventanas en cualquier sistema operativo.

Pero Python no es Matlab ni Visual Basic en el sentido que uno debe
decidir cómo programará, gestionará y ejecutará sus scripts o
módulos. Es más, debido a que Python tiene la gran particularidad de
que **el significado de un programa depende de cómo se ha escrito** es
prácticamente imprescindible utilizar una herramienta específica.

A modo de ejemplo ejecutaremos un "Hola, mundo!" portable, es decir,
podemos seguir exactamente el mismo método en cualquier sistema
operativo.

Una vez abrimos IDLE, en el menú *archivo* seleccionamos *nueva
ventana*, lo que abrirá un editor en el que podemos escribir el
programa. Entonces en esta nueva ventana escribimos lo siguiente:

.. code-block:: python

   if __name__ == '__main__':
       print 'Hola, Mundo!'

.. only:: latex

   .. figure:: _static/editor.png
      :align: center
      :width: 10cm

      Editor para Python de IDLE en Linux 

.. only:: html

   .. figure:: _static/editor.png
      :align: center
      :scale: 100

      Editor para Python de IDLE en Linux


Justo después de escribir los dos puntos finales de la primera línea
veremos que el editor nos sitúa automáticamente a cuatro caracteres
del margen izquierdo.  El motivo puede parecer puramente estético pero
leed otra vez el programa. Hay un condicional, un ``if``, y ninguna
sentencia que termine el bloque. No hay ningún ``end`` ni corchetes
que encapsulen las sentencias ejecutables.

Lo que determina la prioridad del bloque de código es precisamente la
separación respecto al margen izquierdo. Todo lo que esté indentado
después de los dos puntos es parte del bloque ``if``. La necesidad de
utilizar una herramienta específica radica aumentar la facilidad en la
que se maneja la indentación del código.  En IDLE, por ejemplo, para
cambiarla basta con apretar el tabulador o backspace al principio de
cada línea para cambiarla.

Pero si comparamos IDLE con el IDE de Matlab seguimos echando de menos
un montón de piezas: la ayuda integrada, algo que nos permita navegar
entre los objetos, un debugger, un profiler... Parte de la gracia de
cualquier lenguaje de programación, y es también el caso de C o
Fortran, es llegar a un entorno de desarrollo con el que nos sintamos
cómodos. La comodidad es una sensación muy personal y para conseguirla
puedo ayudaros muy poco.

Ahora, en la ventana del editor, seleccionad *run* y luego *run
module* o pulsad F5. En el intérprete aparecerá un ``Hola, Mundo!``.

La parte inicial, el ``if __name__ == '__main__':`` es una convención
de Python que viene a decir que lo que hay a partir de esta línea
tiene que ejecutarse si se ejecuta el archivo ``.py``. Lo utilizaremos
otras veces y veremos de su importancia más adelante.

Python es también una calculadora
---------------------------------

El intérprete cuenta con todas las operaciones aritméticas usuales:
suma, resta, multiplicación, división...

Sólo hay que hacer un par de puntualizaciones al comportamiento del
lenguaje.  El símbolo correspondiente a la potencia es el doble
asterisco, ``**``, como en Fortran.

.. code-block:: python

   >>> 2**10
   1024

Otra diferencia es el operador *modulo* que da el residuo de la
división entrera entre dos números. En Matlab, Octave y Fortran este
operador es una función, a diferencia de C en el que se trata de un
operador.  Python comparte la convención con C al respecto

.. code-block:: python

   >>> 5%2
   1

La división tiene un comportamiento un poco particular en Python 2 y
depende del tipo de cada operador.  Si tanto el numerador como el
denominador son números enteros, el operador ``/`` corresponde a la
división entera y no a la división en coma flotante. Sin embargo, si
alguno de los dos operandos es un número en coma flotante el resultado
también lo será.

.. code-block:: python

    >>> 5/2
    2
    >>> 5.0/2
    2.5

Sin embargo este comportamiento se corregirá en Python 3 de manera que
cualquier división será la división en coma flotante.  Podemos
modificar el comportamiento de Python 2 utilizando el módulo
``__future__`` que introduce algunas de las modificaciones que
recibirá el lenguaje en el futuro

.. code-block:: python

   >>> from __future__ import division
   >>> 5/2
   2.5

Por lo demás el comportamiento respecto a las operaciones aritméticas
es el mismo e importando los módulos ``math`` y ``cmath``
conseguiremos funcionalidades equivalentes a cualquier calculadora.
Aunque aún estamos muy lejos de algo parecido a Matlab y Octave.
