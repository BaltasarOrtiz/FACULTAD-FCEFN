**Guia para el desarrollo del Trabajo Final** 

**Introducción**.  
Durante el desarrollo de la materia compiladores, muchos de los conceptos son entregados en forma de conocimientos, esta tarea se realiza mediante diversos recursos educativos como: videos, simulaciones de Compi, ejercicios de codificación, entre otros. El instrumento educativo denominado trabajo final de la materia compiladores  tiene por objeto  ir más allá de la información suministrada, es un instrumento pensado para ayudar a reforzar  los conocimientos adquiridos y que finalmente se alcance la comprensión. Considerando la comprensión no como un estado de posesión sino como un estado de capacitación. Cuando entendemos algo, no sólo tenemos información sino que somos capaces de hacer ciertas cosas con ese conocimiento.  
La temática a tratar es investigar sobre la generación de compiladores con Coco/R,  este es un generador de compiladores, que toma una gramática atribuida de un lenguaje de programación y genera un escáner y un analizador para este lenguaje.

**Desarrollo el trabajo**  
El trabajo se divide en dos partes 

**Parte 1\. Exploración bibliográfica y estudio de COCO/R** 

**Objetivos**

* **Comprender los fundamentos de la construcción de compiladores con COCO/R:** Adquirir conocimientos sólidos sobre los conceptos clave como análisis léxico, sintáctico, semántico y generación de código.  
* **Dominar la herramienta COCO/R:** Aprender a utilizar todas las funcionalidades de COCO/R para definir gramáticas, generar analizadores léxicos y sintácticos, y personalizar la salida.  
* **Identificar las mejores prácticas:** Descubrir las técnicas y estrategias para construir compiladores utilizando COCO/R.  
* **Explorar casos de uso:** Conocer ejemplos de aplicaciones reales de COCO/R y cómo se han utilizado para construir compiladores para diferentes lenguajes.

### **Actividades Sugeridas**

**Revisión de la documentación oficial de COCO/R [link](https://ssw.jku.at/Research/Projects/Coco/):**

* Manual de usuario: Familiarizarte con la sintaxis, las opciones de configuración y las características avanzadas de COCO/R. [https://ssw.jku.at/Research/Projects/Coco/Doc/UserManual.pdf](https://ssw.jku.at/Research/Projects/Coco/Doc/UserManual.pdf)  
* Tutoriales: Buscar tutoriales en línea que guíen paso a paso en la creación de compiladores simples **.** [https://ssw.jku.at/Research/Projects/Coco/Tutorial/](https://ssw.jku.at/Research/Projects/Coco/Tutorial/)

       **Actividades Complementarias para el estudio de COCO/R ( OPCIONAL)**

* Libros de texto: Consultar libros sobre construcción de compiladores y lenguajes formales.  
* Artículos científicos: Buscar artículos que describen investigaciones y aplicaciones relacionadas con COCO/R.  
* Foros y comunidades en línea: Participar en foros como Stack Overflow o comunidades de desarrollo para resolver dudas y compartir experiencias.  
* Uso de la Inteligencia Artificial Generativa siguiendo las pautas de su uso definidas por la cátedra , debiendo obligatoriamente hacer una bitácora de los prompts utilizados que entregará en la evaluación de las actividades de la parte 1\.

**Evaluacion Parte 1**  
La evaluación consiste de una parte oral y una parte escrita**.**   
**Parte oral.**   
Consiste en explicar el funcionamiento del proyecto TASTE que es presentado en  tutorial   
Fecha tentativa: 19/10/2026

* [https://ssw.jku.at/Research/Projects/Coco/Tutorial/](https://ssw.jku.at/Research/Projects/Coco/Tutorial/)

**Parte** **escrita**   
Consiste en la presentación del informe de las actividades desarrolladas. La siguiente es una guía para elaborar el informe lo cual no indica que taxativamente deben desarrollar cada uno de los puntos aquí presentados sino que es una guía. Cada estudiante y/o grupo puede adoptar la estructura que deseen.

| 1.1 Introducción a Coco/R Historia y desarrollo: Breve reseña histórica y principales características. Arquitectura de Coco/R: Explicar cómo funciona internamente, desde la definición de la gramática hasta la generación del código. Primeros pasos: Instalación y configuración de Coco/R. Creación de un simple analizador léxico. Generación del código y compilación. Análisis de la salida del compilador generado. 1.2 Conceptos fundamentales de compiladores relacionados con Coco/R Análisis léxico: Expresiones regulares: Introducir las expresiones regulares y cómo se utilizan en Coco/R para definir tokens. Autómatas finitos: Explicar la relación entre las expresiones regulares y los autómatas finitos, y cómo Coco/R los implementa. Análisis sintáctico: Gramáticas formales: Introducir las gramáticas libres de contexto y su representación en Coco/R (BNF). Árboles sintácticos: Explicar cómo se construyen los árboles sintácticos y cómo se utilizan en la fase semántica. Descenso recursivo: Mostrar cómo Coco/R genera automáticamente un analizador sintáctico descendente recursivo a partir de la gramática. Tabla de símbolos: Estructura y organización: Explicar cómo se implementa una tabla de símbolos en un compilador generado por Coco/R. Operaciones: Mostrar cómo se realizan operaciones de inserción, búsqueda y actualización en la tabla de símbolos. Generación de código: Código intermedio: Explicar los diferentes tipos de código intermedio y cómo se genera a partir del árbol sintáctico. Código máquina: Introducir los conceptos básicos de generación de código máquina. Relación con Coco/R: Mostrar cómo Coco/R puede ser utilizado para generar código intermedio y cómo se puede extender para generar código máquina.  |
| :---- |

Fecha tentativa : 20/10/2026  
**Parte 2 \- Desarrollo de un estudio de caso usando COCO/R**

**Objetivo**  
Desarrollar un compilador para un  lenguaje de programación  con COCO/R, a propuesta del grupo.  
.

**Actividades**

* **Búsqueda, selección o construcción de caso de estudio.**   
  Para esta tarea se debe considerar un lenguaje de programación pequeño y simple. Puede ser propuesto o puede obtenerse de la información sobre lenguajes generados por COCO/R.   
* **Ejecución y pruebas**  
  Una vez obtenido el compilador, se debe elaborar un juego de programas de prueba y ejecutarlos para demostrar el funcionamiento del mismo

**Nota.** Se sugiere el uso de la Inteligencia Artificial Generativa en el desarrollo de esta tarea, en caso de hacerlo mencionar el uso de la misma en el informe de la tarea. Se deben seguir la pautas para el uso de la inteligencia artificial generativa.

**Evaluación Parte 2**  
Consiste de evaluaciones parciales y una evaluación final integrativa   
Las evaluaciones parciales son encuentros donde los grupos presentan sus avances de forma oral  y están planificados para los días.  
Evaluación parcial 13/10/2026.  
Evaluación parcial 19/10/2026  
Evaluación parcial 26/10/2026.  
Evaluación parcial 2/11/2026

La evaluación final integrativa consiste de una parte oral y una parte escrita**.**   
**Parte oral.**   
Cada grupo defiende el trabajo realizado con la ayuda de una presentación o slides  
**Parte Escrita**  
La evaluación consiste de una presentación escrita de los pasos que se siguieron para implementar el compilador utilizando COCO/R**.**   
**Fecha tentativa** 10/11/2026

**INFORME FINAL**

Se deben integrar los dos informes para consolidar los mismo en un solo informe final que debe tener en la portada **la foto del estudiante o los estudiantes** (si trabajan en grupo)  y luego subir el informe a la carpeta personal del drive. Si trabajan el grupo es el mismo informe solo que tiene que estar subidos en la carpeta personal de cada estudiante.

**Pautas de evaluación parte 2**  
Para la nota final se tendrán en cuenta los siguientes ítems :

* Redaccion y presentacion del informe final   
* Presentación en la defensa oral ( slides y exposición )  
* Complejidad del tema abordado  
* Uso de la IA y reporte de cómo se utilizó (cumplimiento de las pautas )  
* Entregables (código, documento de diseño, interfaces, manuales de uso, etc)  
*  Anexos  
* Video explicativo sobre en que consiste el trabajo y como se desarrollo  
* Otros items que la cátedra considere necesarios por la circunstancias del cursado deba considerar

 