Introducción
============

*Estaría bien que por una vez leyerais la introducción, aunque todos
sabemos que nadie se lee nunca la introducción de nada.*

¿Qué es Python?
---------------

Python es un lenguaje de programación interpretado e
interactivo de propósito general. Es, hasta cierto punto, comparable
con otros lenguajes de programación de dominio específico que podemos
encontrar dentro del ámbito de la Ingeniería como Matlab, Octave, R,
SPSS o IDL.

Se trata también de un lenguaje de programación relativamente moderno
y en constante, aunque moderada, renovación. Fue creado por Guido van
Rossum en el año 1991 tomando prestadas muchas de las buenas ideas
presentes en los lenguajes de programación que conocía. A diferencia
de lo que viene siendo habitual, en vez de reinventar cada idea
simplemente las incorporó de manera que tuvieran sentido.

Aunque la mente de un holandés suele ser un sitio bastante complicado
y retorcido consiguió crear un lenguaje sencillo, intuitivo y fácil de
aprender. Difícilmente se es más productivo con cualquier otro
lenguaje de cuanto se es programando en Python. De hecho se suele
decir: la vida es corta, por eso programo en Python. Quizás el único
lenguaje comparable a Python en ese sentido es Ruby, que curiosamente
nació de la mente de un japonés; también un sitio habitualmente
complicado y retorcido.

Python gozaba de cierta popularidad dentro del mundo UNIX porque se le
consideraba una alternativa razonable a Perl, el que era por aquel
entonces el lenguaje de scripting para programación de sistemas por
antonomasia. La explosión de Python llegó entre los años 2003 y 2007
con el auge de las aplicaciones web y posteriormente con la nube.  Es
uno de los cuatro lenguajes oficiales de Google y toda la
infraestructura de Youtube está programada en Python. Permite a los
desarrolladores de arquitecturas de servicios utilizar el mismo
lenguaje para la aplicación (para lo que también se ha venido
utilzando PHP, como en el caso de Facebook), para el middleware y
para la gestión de los equipos.  Si bien Java es el lenguaje de las
aburridas consultorías de sistemas y de las mastodónticas
multinacionales, Python es el lenguaje de las startups de Silicon
Valley.

Más o menos mientras ganaba en popularidad entre los futuros empleados
de Google, en algunos sectores del cálculo científico se lo veia como
una más que prometedora alternativa a Matlab. Matlab es en el fondo un
lenguaje de programación mediocre que sirve para juntar funciones
realmente útiles. Python debía recorrer el sentido contrario: es un
lenguaje de programación singularmente atractivo para el que, hace
unos años, no había un contexto científico. Ni siquiera se diseñó
pensando en el Cálculo Numérico.

Jim Hugunin puso la primera piedra del castillo, Numeric. No era más
que una clase para poder tratar arrays n-dimensionales en Python y
algunas rutinas numéricas pero tenía serios problemas de velocidad en
comparación con Matlab.  También había ciertos problemas de
fragmentación, cada centro de investigación desarrollaba sus propias
bibliotecas de cálculo y las compartía, pero no había ningún lugar
donde poder poner las cosas en común. El punto de no retorno llegó el
año 2007 con numpy y scipy. Finalmente Python contaba con los bloques
básicos para hacer Cálculo Numérico, todos los usuarios usaban el
mismo y sabían dónde compartir sus desarrollos.

En enero de 2012, momento en el que escribo estas líneas, Python
cuenta con una colección de recursos para Ciencia equivalente a la de
Matlab, incluso superior en campos como la visualización o el cálculo
simbólico. Y la gran mayoría de estos recursos son libres y gratuitos,
sin problemas de royalties o de abogados que intenten defender la
propiedad intelectual de sus clientes.

En resumen: Python es el futuro.

Documentación
-------------

Uno de los motivos del éxito de Python es la gran cantidad de
documentación de calidad que existe sobre el lenguaje y sus
bibliotecas, empezando por la documentación oficial que encontraremos
tanto en la página web http://python.org como en los instaladores para
cualquier sistema operativo.

Hay dos documentos que es importante retener en la memoria. El primero
es el tutorial, de poco más de 100 páginas, que introduce la mayoría
de los elementos esenciales del lenguaje. Obviamente en tan pocas
páginas no es posible entrar en profundidad con todos los detalles y
matices del lenguaje pero es una guía casi imprescindible si uno
quiere programar en Python y no sabe cómo.

El segundo documento es mucho más extenso: la documentación de la
librería estándar. Python es, como veremos, un lenguaje
modular. Algunos de estos módulos se consideran parte de cualquier
distribución al igual que en C tenemos la función ``malloc`` o en
Fortran la función ``allocate``. Todo lo que se documenta como parte
de la librería estándar está disponible en cualquier instalación de
Python independientemente del sistema operativo y de la arquitectura
de procesador.

El entorno de desarrollo en Matlab
----------------------------------

Python es un lenguaje de programación con todas las letras tal como lo
es C, Fortran o Java. Al igual que estos lenguajes y a diferencia de
Matlab no existe un entorno de desarrollo "oficial". Aunque en cada
instalación de Python viene un pequeño editor llamado idle no es ni
mucho menos el más recomendable.

En mi caso tengo dos elecciones personales: Emacs y Eclipse. Lo más
normal es que si no os habéis peleado largas horas de vuestra vida con
un Linux ni siquiera os suene la palabra emacs pero sí es probable que
os suene eclipse.

Eclipse es un entorno de desarrollo originalmente pensado para Java
pero que fue tornandos en agnóstico respecto al lenguaje de
programación. Existe una extensión bastante popular llamada pydev que
convierte a Eclipse en un entorno de desarrollo completo para Python,
con gestor de proyectos y debugger. Es una elección muy interesante en
el momento en el que uno se plantea realizar un proyecto realmente
grande con Python. Pero para manejar los pequeños scripts que
escribiremos en este curso cualquier cosa vale, incluso idle.

Hay centenares de entornos de desarrollo para Python, incluso algunos
están pensados para parecerse lo máximo posible al entorno de Matlab
como spyder.  Os recomiendo que visitéis la wiki del proyecto Python
donde encontraréis una lista actualizada de todos los entornos de
desarrollo para Python, tanto libres como comerciales.

SAGE
----

Sage es un notebook parecido al que encontramos en entornos como Maple
o Mathematica basado en Python. Fue creado por William Stein para
cubrir sus necesidades como docente e investigador en Matemáticas. Uno
podría considerar SAGE como un proyecto paralelo y casi independiente
de Python pero nos permite utilizar Python en la nube a través del
navegador. De este modo no utilizaremos ninguna funcionalidad
específica de SAGE sino que accederemos al intérprete de Python a
través del notebook de forma interactiva y "en la nube".

Utilizaré SAGE como soporte de este curso para ver de manera
interactiva el resultado de bloques de código escrito en Python, pero
esto no significa en absoluto que la manera óptima de escribir un
programa en Python sea con SAGE.  Se trata de una herramienta
puramente docente.

El objetivo es dejar un notebook público en http://picachu.dmt.upm.es
para que quien lo desee pueda crear, modificar y compartir su trabajo
en Python con todos los participantes del grupo.

Python 3
--------

Python está en la actualidad migrando de versión. Aunque la mayoría
del código escrito en Python sigue las especificaciones de la versión
2 hace ya un tiempo que uno puede descargar y utilizar la
versión 3. Algunos cambios importantes entre versiones son fáciles de
migrar, como por ejemplo el comando ``print`` que pasa a ser una
función. Incluso podemos pedir al intérprete de Python 2 que nos avise
si alguna parte de nuestro código tendrá problemas con Python 3.

Este hecho descubre la pregunta de cuándo se hará necesario empezar a
escribir código para Python 3. La respuesta es que no depende de
nosotros. Cuando uno escribe en Python utiliza muchas librerías
adicionales que no siempre están disponibles aún para Python 3. En el
momento en el que todas las dependencias de nuestro trabajo ya
ejecuten sobre Python 3 probablemente sólo tengamos que cambiar de un
intérprete a otro.
