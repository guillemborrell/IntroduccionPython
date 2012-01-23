Numpy y la clase ``array``
==========================

Un *array* es un conjunto de valores con el mismo tipo, esto es, todos
sus elementos son enteros, reales en doble precisión, complejos en
simple precisión... 

Python ya dispone de un tipo :class:`array` que sirve para almacenar
elementos de igual tipo pero no proporciona toda la artillería
matemática necesaria como para hacer operaciones de manera rápida y
eficiente. De este modo, siempre que nos refiramos a la clase
:class:`array` siempre nos referiremos a la que viene con el módulo
:mod:`numpy`

Si consultamos la documentación de :mod:`numpy` nos cuenta lo
siguiente:

Numpy proporciona:

#. Un objeto tipo array para datos homogéneos de tipo arbitrario

#. Operaciones matemáticas rápidas para dichos arrays

#. Rutinas para álgebra lineal, transformadas de Fourier y generación
   de números pseudoaleatorios.

Es, en sentido estricto, una parte mínima que permite convertir Python
en un lenguaje apto para Cálculo Numérico.

Instalar numpy
--------------

Desde el punto de vista de la instalación, :mod:`numpy` no es distinto
de cualquier otro módulo de Python. El tipo de instalación cambia
bastante en función del sistema operativo que estemos utilizando. En
Linux es recomendable instalar la versión disponible para la
distribución correspondiente. Hay también instaladores para Windows y
Mac.

Quizás lo más adecuado es instalar alguna versión empaquetada de
Python que incluya todas las librerías relacionadas con cálculo
científico como puede ser EPD (Enthought Python Distribution) o
PythonX,Y. 

Importar :mod:`numpy`
---------------------

No es demasiado recomendable hacer un ``from numpy import *``. Esto
importaría una cantidad bastante considerable de funciones y clases y,
si estamos trabajando con algún otro módulo relacionado con cálculo
numérico, es muy probable que estemos provocando un conflicto de
nombres.  En prácticamente toda la literatura sobre :mod:`numpy` se
importa como:

.. code-block:: python

   >>> import numpy as np

O lo que es lo mismo, importar todo :mod:`numpy` dentro del namespace
``np``. Esto no es más que una abreviatura de simplemente hacer

.. code-block:: python

   >>> import numpy

Los recortes de código de estos apuntes bien usarán el prefijo
:mod:`numpy` o el ``np``, sin un control especialmente
estricto. Simplemente hay que tener en cuenta que los dos nombres son
equivalentes.


La clase :class:`array`
-----------------------

La clase :class:`array` será, a partir de este momento, la herramienta
básica para los recortes, los ejercicios y los ejemplos. No podemos
hacer numérico en Python sin :class:`array`.

Para crear un array con determinados valores lo más normal es
generarlo a partir de una lista.

.. code-block:: python

   >>> a = np.array([[1,2],[3,4]],dtype='double')
   >>> print a
   [[ 1.  2.]
    [ 3.  4.]]

Acabamos de crear un array de 2 filas y 2 columnas de reales de doble
precisión. Aunque la lista de listas que hemos utilizado para crear el
array contuviera sólo números enteros (no hemos puesto ningún punto
después de cada uno de los números) el argumento ``dtype`` sirve para
especificar la precisión.

En el siguiente ejemplo crearemos un array *vacío* de números en coma
flotante de simple precisión con la función :func:`empty`

.. code-block:: python

   >>> b = np.empty([5,5],dtype=np.float32)
   >>> print b
   [[ -1.32853384e-05   1.45904930e-33   1.55866143e-33   1.55876722e-33
       1.32851727e-33]
    [  1.55863498e-33   1.72551991e-33   1.55871433e-33   1.72653965e-33
       1.55875400e-33]
    [  1.72652496e-33   1.55870110e-33   1.33484143e-33   1.72555224e-33
       1.72649557e-33]
    [  1.33462396e-33   1.72646619e-33   1.47818708e-33   1.50808284e-33
       1.27814146e-33]
    [  1.31751905e-33  -1.13159913e-05   1.47921638e-33   1.80231790e-33
       1.31749995e-33]]

Acabamos de crear un array vacío, esto significa que lo que hemos
obtenido son 25 números ordenados en 5 filas y 5 columnas de lo que
hubiera en ese preciso instante en la memoria, aunque el resultado de
esto no tenga sentido.

La función :func:`empty` es la manera más eficiente de alocatear
memoria, aunque ya sabemos que alocatear no es necesario en Python. Si
queremos generar un array y además inicializarlo con algo que tenga
sentido podemos utilizar la función :func:``zeros``

.. code-block:: python

   >>> b = np.zeros([5,5],dtype=np.float32)
   >>> print b
   [[ 0.  0.  0.  0.  0.]
    [ 0.  0.  0.  0.  0.]
    [ 0.  0.  0.  0.  0.]
    [ 0.  0.  0.  0.  0.]
    [ 0.  0.  0.  0.  0.]]

Indexación
----------

n-dimensionalidad
-----------------

Matlab
------

Es innegable que una de las inspiraciones de :mod:`numpy` es
Matlab. La idea es intentar aprovechar todo lo bueno y corregir lo que
no tiene sentido o está mal diseñado.

Uno de los grandes méritos de Matlab es el disponer de tal cantidad de
funciones para generar y manipular arrays que ha llegado a cambiar el
lenguaje en el que se comunican muchos científicos e ingenieros. Uno
incluso puede oír por ahí un *linspace* o un *meshgrid*. Como el afán
de Python es el de no reinventar la rueda podemos encontrar estas
mismas funciones con ese mismo nombre en :mod:`numpy`

La clase :class:`matrix`
------------------------

Ya hemos visto que la clase :class:`array` es más parecida a los
arrays que encontramos en C o en Fortran que a las miatrices de
Matlab; todas las operaciones aritméticas se ejecutan elemento a
elemento. 

Esto puede ser un inconveniente si nuestro cerebro ha enfermado por
culpa de Matlab y cada vez que vemos una multiplicación entre dos
arrays pensamos en la multiplicación matricial. La solución es
utilizar la clase :class:`matrix` en vez de la clase :class:`array`,
teniendo en cuenta que sólo es útil en el caso bidimensional. Esta
clase cambia los métodos correspondientes a la multiplicación y la
potencia para que sea su equivalente matricial, y no el escalar.

Podemos generar una matriz a partir de un array utilizando el método
:meth:`asmatrix`
