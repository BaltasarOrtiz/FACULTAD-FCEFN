# Trabajo Final de Compiladores — Análisis previo, investigación sobre Coco/R y propuesta de caso de estudio

**Materia:** Compiladores  
**Institución:** FCEFN  
**Grupo:** [completar con integrantes]  
**Fecha:** 29/09/2026  
**Versión:** 0.9 — documento de trabajo para discusión del grupo

---

## Resumen ejecutivo

Este documento consolida: (1) el análisis de los tres documentos de la Semana 8 que fijan las condiciones del Trabajo Final; (2) el relevamiento del compilador de referencia de la cátedra (COMPI, repositorio `compi2026_grupo`); (3) la investigación sobre el generador de compiladores Coco/R, eje de la Parte 1 del trabajo; y (4) una propuesta formal de caso de estudio para la Parte 2.

La propuesta consiste en construir, con Coco/R, el compilador de un lenguaje pequeño y declarativo —denominado provisoriamente **LPP, «lenguaje de políticas»**— con el que se describen inspecciones sobre flujos de texto generados por modelos de lenguaje (LLM). El compilador traduce cada patrón declarado en la política a un **autómata finito**, y un **motor de aplicación** ejecuta esos autómatas sobre flujos de respuesta (grabados o, opcionalmente, en vivo) disparando acciones: reportar, redactar o bloquear.

El proyecto persigue tres objetivos simultáneos: cubrir todos los conceptos y fases evaluados por la cátedra (que el grupo ya trabajó semana a semana sobre COMPI), aportar un tema de complejidad y pertinencia actuales (el uso de IA como objeto de estudio y como herramienta), y ser **escalable en alcance** para adaptarse a los cuatro hitos de evaluación parcial y a la entrega final.

---

## 1. Propósito y alcance del documento

Este documento reúne, en un único material de trabajo, los resultados de tres relevamientos realizados al inicio del Trabajo Final:

1. El análisis de los tres documentos de la Semana 8, que fijan las condiciones, los plazos y las pautas de evaluación del Trabajo Final.
2. El relevamiento del compilador de referencia de la cátedra (COMPI) sobre el repositorio del grupo (`compi2026_grupo`), cuyo estudio se viene realizando desde las actividades de las semanas anteriores.
3. La investigación sobre el generador de compiladores Coco/R y su caso de estudio canónico (el lenguaje TASTE), eje de la Parte 1 del trabajo.

Sobre esa base se presenta la propuesta formal de caso de estudio para la Parte 2, con el nivel de detalle suficiente para orientar el desarrollo posterior: qué se va a construir, con qué herramientas, en qué orden, con qué pruebas y con qué criterios de aceptación.

---

## 2. Lo que requiere la cátedra

*(Síntesis de los tres documentos de la Semana 8: «Guía para el desarrollo del Trabajo Final», «Pautas para el uso de la IA en el trabajo final de compiladores» y «Guía para la redacción del apartado Reflexiones sobre el uso de la IA generativa».)*

### 2.1 Estructura del Trabajo Final

El trabajo se divide en dos partes:

**Parte 1 — Exploración bibliográfica y estudio de Coco/R.** Sus objetivos son: comprender los fundamentos de la construcción de compiladores con Coco/R; dominar la herramienta (definición de gramáticas, generación de analizadores léxicos y sintácticos, personalización de la salida); identificar buenas prácticas; y explorar casos de uso reales. Incluye la revisión de la documentación oficial (manual de usuario y tutorial) y admite actividades complementarias opcionales: libros de texto, artículos científicos, foros y comunidades, y el uso de IA generativa sujeto a las pautas de la cátedra.

**Parte 2 — Desarrollo de un estudio de caso con Coco/R.** Objetivo: «Desarrollar un compilador para un lenguaje de programación con COCO/R, a propuesta del grupo». La consigna precisa que se debe «considerar un lenguaje de programación pequeño y simple» (propuesto por el grupo u obtenido de la información sobre lenguajes generados por Coco/R), y que «una vez obtenido el compilador, se debe elaborar un juego de programas de prueba y ejecutarlos para demostrar el funcionamiento del mismo».

### 2.2 Evaluación y fechas

| Instancia | Fecha (tentativa) | Descripción |
|---|---|---|
| Parte 2 — evaluación parcial 1 | 13/10/2026 | Presentación oral de avances |
| Parte 2 — evaluación parcial 2 | 19/10/2026 | Presentación oral de avances |
| Parte 1 — oral | 19/10/2026 | Explicar el funcionamiento del proyecto TASTE presentado en el tutorial de Coco/R |
| Parte 1 — escrita | ~20/10/2026 | Informe de las actividades desarrolladas (guía sugerida: historia y arquitectura de Coco/R, primeros pasos, análisis léxico y sintáctico, tabla de símbolos, generación de código) |
| Parte 2 — evaluación parcial 3 | 26/10/2026 | Presentación oral de avances |
| Parte 2 — evaluación parcial 4 | 02/11/2026 | Presentación oral de avances |
| Evaluación final integrativa | ~10/11/2026 | Oral con slides (defensa) + presentación escrita de los pasos seguidos para implementar el compilador con Coco/R |
| Informe final | — | Integración de ambos informes en uno solo; portada con foto del/los estudiantes; cada estudiante lo sube a su carpeta personal del Drive |
| Video explicativo | — | Video sobre en qué consiste el trabajo y cómo se desarrolló (ítem de evaluación) |

Criterios de la nota final (Parte 2):

- Redacción y presentación del informe final.
- Presentación en la defensa oral (slides y exposición).
- **Complejidad del tema abordado.**
- Uso de la IA y reporte de cómo se utilizó (cumplimiento de las pautas).
- Entregables: código, documento de diseño, interfaces, manuales de uso, etc.
- Anexos.
- Video explicativo.
- Otros ítems que la cátedra considere necesarios.

### 2.3 Uso de IA generativa: obligaciones

Resumen de las pautas que condicionan todo el trabajo:

- **Bitácora de prompts obligatoria (Parte 1):** la guía exige «obligatoriamente hacer una bitácora de los prompts utilizados». Conviene llevar el registro desde el primer día de trabajo.
- **Originalidad:** el trabajo y el compilador final deben ser propios del grupo; la IA «debe ser utilizada como una ayuda para incrementar el trabajo, no como un sustituto». No se admite copiar y pegar contenido generado sin modificación significativa ni atribución.
- **Trazabilidad:** debe documentarse dónde y cómo se usó IA (herramientas y prompts).
- **Privacidad:** no compartir información confidencial, personal o sensible (propia, de terceros o del estudio de caso) con sistemas de IA.
- **Verificación crítica:** las salidas de la IA deben evaluarse contra fuentes originales (prevención de alucinaciones y desactualización de modelos).
- **Comprensión humana:** el grupo debe poder explicar y demostrar el funcionamiento de todos los artefactos sin ayuda de la IA.
- **Formulación de prompts:** la guía recomienda la fórmula [ROL] + [CONTEXTO] + [TAREA] + [FORMATO], y dividir tareas complejas en indicaciones breves.
- **Apartado «Reflexiones sobre el uso de la IA generativa»** en el informe, con una guía de nueve puntos: motivo de incorporación de la IA; herramientas empleadas; tareas asistidas por fase del proyecto o tipo de actividad; asistencia en la construcción de los artefactos; depuración y resolución de errores (con ejemplos concretos de códigos de error y fragmentos de código); mejora de usabilidad y diseño de la herramienta; ejemplos prácticos de prompts y partes relevantes de las respuestas; contribución a la documentación; y reflexión crítica final (beneficios, necesidad de verificación permanente y casos en que la IA no ayudó o requirió mayor intervención humana).

---

## 3. El compilador de referencia: COMPI

COMPI es el compilador didáctico de la cátedra, desarrollado en C# sobre .NET con interfaz Windows Forms. El repositorio oficial es `github.com/CompiladoresExactasUNSJ/compi2026`; el grupo trabaja sobre un clon propio (`compi2026_grupo`). Compila un lenguaje imperativo pequeño, de estilo similar a un Java/Pascal reducido: clases, constantes y variables globales, métodos (por ejemplo `void Main()`), asignaciones, control de flujo (`if/else`, `while`), impresión (`write`/`writeln`) y expresiones aritméticas y relacionales.

Organización del código y su correspondencia con la materia:

| Componente | Archivo | Concepto de la materia |
|---|---|---|
| Escáner (analizador léxico) | `Scanner.cs` | Autómata finito determinista; tokens; ventana doble `token`/`laToken` (Semana 3) |
| Analizador sintáctico | `Parser.cs` | Descenso recursivo; conjunto FIRST; `Check`/`Scan`; árbol de derivación (Semana 4) |
| Acciones semánticas y atributos | (integradas en `Parser.cs`) | Gramática atribuida; atributos de entrada/salida; registro `Item` (Semana 5) |
| Tabla de símbolos | `SymTab.cs` | Ámbitos (scopes); inserción/búsqueda; `Symbol`/`Struct` (Semana 6) |
| Generación de código | `miCodGen.cs` | CIL; `System.Reflection.Emit`; máquina de pila (Semana 7) |
| Máquina virtual | `FrmContinuarMaqVirtual.cs` | Modo de ejecución paso a paso del código generado (Semana 7) |

**Observación de linaje (de utilidad para el informe):** el código de COMPI declara el namespace `at.jku.ssw.cc`, correspondiente a la tradición de la Johannes Kepler University Linz (JKU) — el mismo instituto (`ssw.jku.at`) que publica Coco/R — y utiliza la notación `(. ... .)` para acciones semánticas embebidas, propia de esa línea (Mössenböck/Wirth). En otras palabras: **COMPI es la versión escrita a mano del mismo pipeline que Coco/R genera automáticamente**. Este dato conecta las tres piezas del trabajo final (COMPI, Coco/R y TASTE) como partes de una misma tradición académica.

**Nota metodológica:** la arquitectura de COMPI es conocida por el grupo por las actividades de las semanas anteriores (seguimientos sobre `Scanner.cs`, `Parser.cs`, `miCodGen.cs`, etc.), lo que reduce el costo de aprendizaje de cualquier proyecto que reuse sus conceptos. El trabajo final, sin embargo, pide un compilador **construido con Coco/R** — es decir, generado a partir de una gramática atribuida, no escrito a mano.

---

## 4. Investigación: Coco/R

### 4.1 Historia y linaje

Coco/R es un **generador de compiladores** creado por Hanspeter Mössenböck en 1989 en la ETH Zürich (Suiza) y desarrollado y mantenido desde mediados de los años noventa en la Johannes Kepler University Linz (JKU), Austria. Las versiones actuales para C#, Java y C++ se distribuyen desde el sitio oficial del proyecto en `ssw.jku.at`. Es software de código abierto (GPL) y su ecosistema documental incluye:

- el **manual de usuario** (referencia completa del lenguaje de entrada y de las interfaces generadas);
- un **tutorial de medio día** (JMLC'06) cuyos capítulos son: Compilers, Grammars, Coco/R Overview, Scanner Specification, Parser Specification, Error Handling, LL(1) Conflicts y Case Study (el lenguaje TASTE);
- el **artículo sobre resolución de conflictos LL(1)** en analizadores de descenso recursivo (JMLC'03), que describe los mecanismos de la herramienta.

Su motivación histórica fue ofrecer una alternativa más integrada que la combinación LEX/YACC, con soporte directo de gramáticas atribuidas y análisis descendente.

> **Precisión sobre una atribución de los apuntes:** el material teórico de la materia menciona a Coco/R como «de la ETH Zúrich». La formulación correcta para el informe es: **creado en ETH Zürich (1989), desarrollado y mantenido en JKU Linz**; todos los enlaces oficiales que cita la cátedra pertenecen al sitio de JKU.

### 4.2 Arquitectura y funcionamiento

Coco/R toma una **gramática atribuida** de un lenguaje fuente y genera, para ese lenguaje, un **escáner y un analizador sintáctico**. El escáner resultante funciona como **autómata finito determinista**; el analizador es de **descenso recursivo**. El análisis es **LL(1)** y los conflictos que exceden un símbolo de lookahead se resuelven mediante dos mecanismos: lookahead múltiple o **resoluciones de conflicto definidas por el usuario** (predicados booleanos escritos en el lenguaje objetivo). La clase de gramáticas aceptadas es, por lo tanto, LL(k) para k arbitrario.

Estructura típica del archivo de gramática (el lenguaje de entrada se denomina Cocol/R):

```
COMPILER <Nombre>

CHARACTERS
  ...definición de conjuntos de caracteres...

TOKENS
  ...definición de tokens mediante expresiones regulares (con cláusulas CONTEXT y PRAGMAS opcionales)...

IGNORE
  ...caracteres ignorados (espacios, tabulaciones, fin de línea)...

COMMENTS [FROM ... TO ...] [NESTED]
  ...delimitadores de comentarios...

PRODUCTIONS
  ...producciones en EBNF con atributos <...> y acciones semánticas (. ... .)...

END <Nombre>.
```

Puntos clave del funcionamiento:

- **Tokens:** se especifican con expresiones regulares extendidas (secuencia, alternancia, repetición, conjuntos de caracteres). Coco/R construye con ellos el autómata del escáner, resolviendo ambigüedades por orden de declaración.
- **Producciones:** EBNF (secuencia, alternativas `|`, opción `[ ]`, iteración `{ }`), con **atributos** `<...>` (de entrada y de salida) y **acciones semánticas** `(. ... .)` escritas en el lenguaje objetivo.
- **El usuario completa el compilador** con clases propias —tabla de símbolos, generador de código, clase principal— cuyos métodos se invocan desde las acciones semánticas. Es exactamente el rol que cumplen `SymTab.cs` y `miCodGen.cs` en COMPI, y las clases `Tab` y `Gen` en el ejemplo TASTE.
- **Invocación:** `Coco archivo.atg` (variante C#) genera `Scanner.cs`, `Parser.cs` y componentes auxiliares, a partir de plantillas («frames») personalizables. Las interfaces generadas típicas incluyen el escáner (avance y lookahead de tokens), la clase `Token` (tipo, valor, posición) y el parser (método de arranque y manejo de errores con recuperación).
- **Manejo de errores:** el analizador generado aplica estrategias de recuperación (por ejemplo, sincronización con conjuntos de continuación) y ofrece servicios para emitir diagnósticos.

**Objetivos disponibles:** las versiones mantenidas oficialmente son C#, Java y C++ (las más recientes del sitio de JKU). Históricamente existieron también versiones para Modula-2, Oberon, Delphi y otros lenguajes. **Para este trabajo, el objetivo natural es C#**, por continuidad con el stack .NET que el grupo ya utiliza en COMPI.

### 4.3 El caso de estudio del tutorial: TASTE

TASTE es el lenguaje de ejemplo que acompaña al manual de usuario y al tutorial (descargable como `Taste.zip`, «the sources of the sample compiler (Taste) described in the user manual»). Es la pieza central de la **evaluación oral de la Parte 1** («explicar el funcionamiento del proyecto TASTE»).

Características del lenguaje:

- Mini-lenguaje de estilo imperativo, con similitudes con Modula-2/Oberon simplificados.
- Programa con declaraciones de variables **globales** y **procedimientos sin parámetros** (con variables locales).
- Dos tipos: `int` y `bool`.
- Sentencias: asignación, llamada a procedimiento, `if`/`else`, `while`, lectura (`read`) y escritura (`write`), y bloques.
- Expresiones aritméticas (`+ - * /`) y relacionales (`== < >`).

Características del compilador:

- Se especifica en `Taste.atg` (escáner + producciones con acciones semánticas) y se completa con clases auxiliares: tabla de símbolos (`Tab`: ámbitos con `OpenScope`/`CloseScope`, `Insert`/`Find`) y generador de código (`Gen`: emisión de instrucciones y parcheo de saltos).
- Es un compilador **compile-and-go**: traduce el programa a instrucciones de una **máquina de pila abstracta** (`CONST`, `LOAD`, `ADD`, `SUB`, `MUL`, `DIV`, `JMP`, `FJMP`, `CALL`, `RET`, `ENTER`, `LEAVE`, `READ`, `WRITE`, etc.) y las interpreta inmediatamente después de compilar.
- El nombre es un juego: el lenguaje «te da un *taste* (una probada)» de cómo escribir un compilador con Coco/R.

**Qué hay que poder explicar en la defensa oral (checklist de estudio):**

1. Qué genera Coco/R a partir de `Taste.atg`: un escáner (autómata finito determinista) y un analizador de descenso recursivo con las acciones semánticas embebidas.
2. Cómo se especifica el escáner: conjuntos de caracteres, tokens con expresiones regulares, comentarios (anidables), caracteres ignorados.
3. Cómo funcionan los atributos y las acciones semánticas en las producciones (por ejemplo, en la declaración de variables: obtener el tipo y el nombre y registrar el símbolo en la tabla).
4. El rol de la tabla de símbolos: ámbitos, inserción, búsqueda; cómo representa variables y procedimientos.
5. El rol del generador de código: emisión de instrucciones de la máquina de pila, manejo del contador de programa y parcheo de saltos.
6. El flujo completo «compile-and-go»: leer el programa fuente, compilarlo a instrucciones y ejecutarlas con un archivo de entrada de datos.
7. La relación conceptual con COMPI: mismo pipeline (escáner AFD + parser de descenso recursivo + tabla de símbolos + generación de código), con la diferencia de que COMPI está escrito a mano y TASTE se genera con Coco/R.

### 4.4 Aplicaciones y casos de uso documentados

Material útil para el punto «explorar casos de uso» de la Parte 1:

- **Framework de compilador para C# en el proyecto Rotor de Microsoft:** Coco/R y su mecanismo de resolución de conflictos LL(1) se usaron para construir un framework de análisis de C# (gramática atribuida de C# a la que los usuarios agregan acciones semánticas para construir compiladores, analizadores de código y otras herramientas).
- **Libro «Compiling with C# and Java» (Pat Terry):** el manual distribuido con el libro describe las extensiones de Coco/R mantenidas para ese texto, con ejemplos completos de compiladores.
- **Uso educativo extendido:** es una herramienta estándar en cursos de construcción de compiladores (el propio TASTE es un ejemplo de mini-lenguaje generable), y existen ports y variantes mantenidas por la comunidad para numerosos lenguajes objetivo.

### 4.5 Ruta de estudio para la Parte 1

1. Manual de usuario completo: estructura de una gramática, escáner, parser, atributos, acciones, conflictos LL(1) y resolutores, manejo de errores, frames, interfaces generadas.
2. Tutorial JMLC'06 (slides) y fuentes de TASTE (`Taste.zip`): recorrer `Taste.atg`, `Tab`, `Gen` y la clase principal; compilarlo mentalmente de punta a punta.
3. Libro de Pat Terry (opcional, recomendado para profundizar el objetivo C#).
4. Artículos: resolución de conflictos LL(1) (JMLC'03) y, si el tiempo lo permite, notas sobre construcción de AST con Coco/R.
5. Practicar: escribir una mini-gramática propia (por ejemplo, la del lenguaje propuesto en la sección 6) y generar el escáner y el parser antes de la primera evaluación parcial.

---

## 5. Referencia conceptual: pasarelas de LLM (Aperture) y decodificación restringida

> Esta sección cumple una única función: documentar la referencia conceptual que motiva el dominio del caso de estudio. **No forma parte de la implementación propuesta** ni se propone reproducir la arquitectura de ningún producto.

Aperture (de Tailscale) es un ejemplo real y actual de **pasarela centralizada de IA**: un proxy que se interpone entre los clientes (herramientas y agentes) y los proveedores de modelos (OpenAI, Anthropic, Google, etc.). Sus mecanismos centrales —a los efectos de este trabajo— son:

- **Intercepción del tráfico LLM a nivel HTTP:** inspecciona y enruta las peticiones por modelo, inyecta autenticación y devuelve las respuestas, incluidas las respuestas en streaming (reconstruye el flujo de eventos SSE para su procesamiento).
- **Captura de telemetría:** registra los cuerpos de peticiones y respuestas (con valores sensibles redactados), conteos de tokens de uso (entrada, salida, caché, razonamiento), duración y sesiones.
- **Reglas y observabilidad:** hooks, exportadores y sesiones permiten auditar, gobernar y actuar sobre el uso.

**Precisión técnica importante:** la granularidad de Aperture es **a nivel mensaje** (contenido HTTP y metadatos); no analiza los tokens BPE internos del modelo, y en su vocabulario «tokens» también designa credenciales de acceso y unidades de consumo.

**La línea técnica real de granularidad a nivel token** existe y es un área activa de investigación e industria: la **decodificación restringida** (*constrained decoding*). Sistemas como Outlines compilan expresiones regulares a autómatas finitos y los superponen al vocabulario del modelo para enmascarar los tokens inválidos durante la generación; marcos posteriores hacen lo mismo con gramáticas libres de contexto; el formato GBNF de llama.cpp es un ejemplo popular de gramáticas para generación restringida. Esta línea se cita en el trabajo como **trabajo relacionado** (enriquecerá el informe y la defensa), pero **no es parte del alcance de implementación propuesto**.

Lo que el caso de estudio toma de esta referencia es la **forma del dominio**: existe una práctica real de definir políticas y observabilidad sobre flujos de salida de modelos, y esa práctica involucra exactamente los objetos que este trabajo sabe construir: **expresiones formales compiladas a autómatas que actúan sobre flujos de texto**.

---

## 6. Propuesta de caso de estudio para la Parte 2

### 6.1 Objetivo y denominación

**Objetivo:** definir y desarrollar, con Coco/R, el compilador de un lenguaje pequeño y declarativo (denominado provisoriamente **LPP**, «lenguaje de políticas») que permite describir políticas de inspección sobre flujos de texto generados por modelos de lenguaje. La compilación traduce cada patrón declarado a **autómatas finitos** que codifican lo que debe detectarse, y un **motor de aplicación** ejecuta esos autómatas sobre flujos de respuesta disparando acciones declaradas por la política: **reportar**, **redactar** o **bloquear**.

Ejemplo del flujo completo:

```
política (LPP)  →  Coco/R  →  compilador LPP  →  autómatas generados  →  motor  →  decisiones sobre el flujo
```

### 6.2 Correspondencia con el programa de la materia (por qué este caso de estudio)

El proyecto fue diseñado para que cada componente del compilador ejercite un concepto ya trabajado en la cursada:

| Semana | Concepto trabajado | Componente del proyecto |
|---|---|---|
| 1 | Jerarquía de Chomsky; expresiones regulares; AFD/AFND; autómata a pila | Patrones de las políticas → AFN → AFD; relación regex–autómata hecha código |
| 2 | Fases del compilador; compilador vs. intérprete | Arquitectura general del compilador LPP + motor |
| 3 | Escáner (análisis léxico); tokens; ventana doble | Escáner del LPP generado por Coco/R; escaneo del flujo de respuesta por el motor |
| 4 | Parser (descenso recursivo); FIRST; errores | Parser del LPP generado por Coco/R; discusión de conflictos LL(1) |
| 5 | Gramática atribuida; atributos; acciones semánticas | Atributos y acciones del `lpp.atg`; traducción de patrones |
| 6 | Tabla de símbolos; ámbitos; validez semántica | Tabla de políticas/patrones/reglas; validación semántica del LPP |
| 7 | Generación de código; CIL; máquina de pila | Generación de código: emisión de los autómatas (tablas/estructuras ejecutables) |
| 8 / Trabajo final | Coco/R; TASTE | La herramienta y su caso de estudio aplicados a un lenguaje propio |

Razones adicionales:

- **Ítem «complejidad del tema abordado»** de la evaluación: el proyecto combina un lenguaje propio, un compilador generado, una fase de construcción de autómatas no trivial (AFN→AFD) y un motor de aplicación; sin depender de infraestructura pesada ni de servicios externos.
- **Temática actual:** el dominio (análisis de salidas de modelos de lenguaje) permite que el propio trabajo documente su uso de IA de manera doblemente pertinente (la IA como herramienta del grupo y como objeto de estudio).
- **Escalable:** el alcance puede ajustarse por etapas sin perder coherencia (sección 6.8).
- **Reutilización:** todo el conocimiento ya adquirido sobre COMPI (escáner AFD, parser de descenso recursivo, tabla de símbolos, generación de código) se aplica directamente; TASTE aporta el modelo de arquitectura de un compilador generado (clases `Tab` y `Gen`, VM de pila).

### 6.3 Definición del lenguaje (borrador v0.1)

**Descripción.** Un programa LPP declara políticas. Cada política tiene un ámbito de aplicación (respuesta, petición o ambas), un conjunto de patrones con nombre y un conjunto de reglas que, ante la detección de un patrón (o combinación booleana de patrones), disparan una acción.

**Gramática propuesta (EBNF, borrador sujeto a ajuste al escribir el `.atg`):**

```
Programa    = { Política } .
Política    = "politica" string "{" { Cláusula } "}" .
Cláusula    = Ámbito | Patrón | Regla .
Ámbito      = "sobre" ( "respuesta" | "peticion" | "ambas" ) "." .
Patrón      = "patron" ident "=" ExprPatrón "." .
Regla       = "regla" ident "cuando" Condición "->" Acción "." .
Condición   = Término { ( "y" | "o" ) Término } .
Término     = [ "no" ] ( "(" Condición ")" | ident ) .
Acción      = ( "reportar" | "redactar" | "bloquear" ) [ string ] .
ExprPatrón  = Secuencia { "|" Secuencia } .
Secuencia   = Unidad { Unidad } .
Unidad      = ( string | Clase | "(" ExprPatrón ")" ) [ Repetición ] .
Clase       = "[" { Carácter } "]" .
Repetición  = "?" | "*" | "+" | "x" number .
```

**Ejemplo de programa LPP:**

```
politica "proteccion-de-datos-sensibles" {
    sobre respuesta.

    patron credencial_aws = "AKIA" [A-Z0-9] x 16.
    patron tarjeta        = ("4" | "5" | "6") [0-9] x 15.
    patron inyeccion      = ("ignore" | "ignora") " las instrucciones anteriores".

    regla fuga_credencial cuando credencial_aws -> redactar "[REDACTADO]".
    regla alerta_inyeccion cuando inyeccion -> reportar "posible intento de inyeccion".
    regla bloqueo_total cuando tarjeta y no inyeccion -> bloquear "tarjeta detectada".
}
```

**Observaciones de diseño:**

- Las reglas gramaticales fueron pensadas para ser **LL(1) directas** (los conjuntos FIRST de las alternativas son disjuntos). Cualquier conflicto que aparezca al escribir la gramática definitiva se documentará y resolverá con las técnicas de la materia (transformación de gramática o resolutores de Coco/R) — ese análisis en sí mismo es material evaluable.
- **Reglas semánticas (a implementar en la fase semántica):** todo `ident` usado en una condición debe estar declarado como patrón (referencias no declaradas ⇒ error); no puede haber duplicados de políticas, patrones o reglas en el mismo ámbito; las clases de caracteres deben ser válidas y no vacías; v0.1 admite un ámbito por política; la resolución de nombres usará una tabla de símbolos con ámbitos (global y por política), replicando los conceptos de la Semana 6.
- Esta definición es un **borrador v0.1**: la especificación se congela como versión 1.0 el 13/10/2026 (primer hito), y todo agregado posterior pasa al backlog de extensiones.

### 6.4 Arquitectura del compilador propuesto

Componentes y artefactos, en orden de construcción:

1. **Especificación del lenguaje LPP** (documento): gramática léxica y sintáctica, reglas semánticas, semántica de las acciones. *Artefacto: especificación v1.0.*
2. **Gramática atribuida `lpp.atg`** para Coco/R: secciones CHARACTERS/TOKENS/IGNORE/COMMENTS + PRODUCCIONES con atributos y acciones semánticas que invocan las clases auxiliares. *Artefacto: `lpp.atg`.*
3. **Generación con Coco/R:** `Coco lpp.atg` produce el escáner y el parser del LPP. *Artefactos: `Scanner.cs`, `Parser.cs` generados (código objeto de estudio para el informe).*
4. **Clases auxiliares del compilador** (escritas por el grupo, invocadas desde las acciones semánticas): tabla de símbolos (políticas, patrones, reglas; ámbitos), verificación semántica, y generador de autómatas/código. *Artefactos: `TablaSimbolos.cs`, `VerificadorSemantico.cs`, `GeneradorAutomatas.cs` (nombres provisorios).*
5. **Fase de generación:** traducción de cada `ExprPatrón` a autómata finito y emisión del código o tablas correspondientes (ver 6.5). *Artefacto: código generado (por ejemplo `Politicas_Generadas.cs`).*
6. **Motor de aplicación:** programa de línea de comandos que carga las políticas compiladas y las aplica sobre flujos de respuesta en modo replay y, opcionalmente, en vivo (ver 6.6). *Artefacto: `Motor/` (CLI + runtime).*
7. **Corpus y suite de pruebas** (ver 6.7). *Artefactos: `corpus/*.jsonl`, pruebas automatizadas.*
8. **Documentación y trazabilidad:** manual de uso del lenguaje, guía de compilación/ejecución, bitácora de prompts, material para el informe y el video.

**Estructura de repositorio sugerida:**

```
trabajo-final-compiladores/
├── gramatica/        lpp.atg (y frames, si se personalizan)
├── compilador/       generado (Scanner.cs, Parser.cs) + clases auxiliares + main
├── motor/            runtime, CLI, modo replay/live
├── corpus/           flujos de prueba (jsonl) + resultados esperados
├── docs/             especificación, manuales, bitácora, informe
└── tests/            suite automatizada
```

### 6.5 Traducción de patrones a autómatas (diseño de la generación de código)

Esta es la pieza que materializa la Semana 1 (expresiones regulares ↔ autómatas) y la Semana 7 (generación de código):

1. **AFN (Thompson):** cada `ExprPatrón` se compila a un autómata finito no determinista usando las construcciones estándar: concatenación (secuencia), alternancia (`|`), clausura de Kleene (`*`), clausura positiva (`+`), opcional (`?`) y repetición fija (`x n`). Las clases de caracteres se expanden a conjuntos del alfabeto.
2. **AFD (construcción por subconjuntos):** el AFN se determiniza; opcionalmente se minimiza (Hopcroft) como extensión.
3. **Emisión (generación de código):** los autómatas se emiten como estructuras ejecutables —por ejemplo, tablas de transición (`int[,]`), estado inicial y estados de aceptación con su etiqueta (qué regla/acción dispara)— en un archivo C# generado, o bien serializados (JSON) para ser interpretados por el motor. La decisión de formato se documentará con su justificación en el informe (criterio: demostrar la generación de código y mantener el motor simple).
4. **Ejecución sobre flujos (matching incremental):** el motor mantiene, para cada patrón activo, su estado actual entre fragmentos consecutivos del flujo (el estado del autómata «sobrevive» entre chunks, igual que la ventana doble del escáner sobrevive entre tokens). Al alcanzar un estado de aceptación se dispara la acción de la regla correspondiente.

Casos borde que el diseño debe contemplar y documentar: coincidencias que cruzan fragmentos; coincidencias solapadas entre patrones; re-sincronización tras un casi-match (retroceso del autómata sin perder texto); acciones de redacción que modifican lo que el motor reenvía.

### 6.6 Motor de aplicación y modos de ejecución

El motor aplica las políticas compiladas sobre flujos de respuesta. Dos modos:

- **Modo `replay` (evidencia formal):** recibe un archivo de flujo grabado (fragmentos en orden, formato JSONL) y produce un archivo de resultados: qué regla se disparó, con qué acción, sobre qué posición del flujo. Es **determinista y reproducible**: es la evidencia con la que se demuestra el funcionamiento ante la cátedra y con la que se corre la suite de pruebas.
- **Modo `live` (demostración opcional):** se conecta a un endpoint compatible con la API de chat completions (por ejemplo, un servidor local de modelos) y aplica las políticas al flujo real a medida que llega. Se documenta como demostración de integración (por ejemplo, en el video), con las precauciones propias de un sistema no determinista.

Formato tentativo del archivo de flujo (JSONL):

```json
{"id":"caso-001","escenario":"fuga de credencial ficticia",
 "fragmentos":["La clave configurada es AKIA","IOSFODNN7EXAMPLE y el resto sigue igual"],
 "esperado":[{"regla":"fuga_credencial","accion":"redactar"}]}
```

### 6.7 Juego de pruebas y criterios de aceptación

En línea con la consigna («elaborar un juego de programas de prueba y ejecutarlos para demostrar el funcionamiento»), se proponen cinco suites:

1. **Escáner y parser del LPP:** programas válidos (deben compilar sin errores) y programas inválidos (deben producir los diagnósticos esperados con línea/columna).
2. **Análisis semántico:** referencias a patrones no declarados, duplicados, clases inválidas; cada caso con su error esperado.
3. **Autómatas:** verificación de equivalencia de los autómatas generados contra un conjunto de casos de referencia (los mismos conjuntos de cadenas aceptados/rechazados), incluyendo casos borde (cadena vacía, prefijos, cadenas que cruzan fragmentos).
4. **Extremo a extremo (replay):** el corpus completo de flujos, comparando las acciones disparadas contra los resultados esperados.
5. **Modo live (opcional):** prueba de humo de integración (una política sencilla sobre una respuesta real), documentada pero no determinante para la evaluación.

**Criterios de aceptación mínimos (v1.0):**

- El `.atg` genera el compilador sin errores y sin conflictos LL(1) sin resolver.
- Todos los programas del corpus de prueba compilan (los válidos) o fallan con el diagnóstico esperado (los inválidos).
- Los autómatas aceptan exactamente las cadenas esperadas en los casos de referencia.
- El motor en modo replay reproduce los resultados esperados para el 100 % del corpus.
- La documentación (estas piezas evolucionadas) cubre: especificación, manual de uso, bitácora y guía de ejecución.

### 6.8 Alcance por etapas y cronograma

| Período | Metas internas | Artefactos | Hito de cátedra |
|---|---|---|---|
| 29/09 → 13/10 | Especificación v0.1 congelada; escritura del `.atg` v1; generación con Coco/R funcionando (escáner + parser); inicio formal de la bitácora de prompts | especificación, `lpp.atg`, `Scanner.cs`/`Parser.cs` generados | Parcial 1 (13/10): presentar el lenguaje y la generación |
| 13/10 → 19/10 | Estudio profundo de TASTE y del manual (preparación del oral); ajustes de gramática según hallazgos | apuntes de estudio, gramática revisada | Oral TASTE (19/10) e informe de Parte 1 (~20/10) |
| 19/10 → 26/10 | Análisis semántico completo (tabla de símbolos, verificaciones); construcción AFN→AFD de patrones | `TablaSimbolos.cs`, `VerificadorSemantico.cs`, módulo de autómatas con pruebas unitarias | Parcial 2 (26/10) |
| 26/10 → 02/11 | Generación de código (emisión); motor replay completo; corpus y suite end-to-end; modo live (opcional) | generador, motor, corpus, suite | Parcial 3 (02/11) |
| 02/11 → 10/11 | Informe integrado (Partes 1 y 2), apartado de reflexiones de IA, anexos, video explicativo | informe final, video, bitácora consolidada | Final integrativa (~10/11) |

**Recomendación operativa:** la bitácora de prompts se escribe el mismo día en que se usa la IA (es requisito obligatorio de la Parte 1 y alimenta directamente el apartado de reflexiones); los avances de cada parcial deben estar siempre sostenidos por artefactos ejecutables (nada de diapositivas sin demostración).

### 6.9 Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| El alcance del lenguaje crece sin control | Especificación v1.0 congelada el 13/10; todo agregado va a backlog de extensiones |
| Conflictos LL(1) al escribir la gramática | Documentarlos y resolverlos con las técnicas de la materia (transformación o resolutores de Coco/R) — es material evaluable, no un fracaso |
| La demostración en vivo falla el día de la defensa (dependencia de red/servicios) | El modo replay es la evidencia formal (determinista, local); el vivo es solo demostración y se graba con antelación para el video |
| Datos sensibles en el corpus | Corpus sintético de laboratorio; si se usa cualquier flujo real, sanitizado y con datos ficticios (pautas de cátedra) |
| Tiempo insuficiente por acumulación de materias | Hitos semanales cortos; pruebas automatizadas desde el inicio para evitar regresiones; el proyecto es incremental por etapas |

---

## 7. Entregables esperados y su relación con la evaluación

| Ítem de evaluación (cátedra) | Entregable del proyecto |
|---|---|
| Código | Compilador LPP (generado + clases propias), motor, corpus y suite de pruebas |
| Documento de diseño | Este documento evolucionado + especificación del lenguaje v1.0 + diseño de la generación de autómatas |
| Interfaces | CLI del motor, formato del corpus (JSONL), formato de resultados |
| Manuales de uso | Manual del lenguaje LPP + guía de compilación/ejecución del compilador |
| Video explicativo | Demostración: compilación de una política + aplicación en modo replay (+ fragmento en vivo) |
| Anexos | Gramática completa, ejemplos de código generado, bitácora de prompts |
| Uso de IA y reporte | Bitácora consolidada + apartado «Reflexiones sobre el uso de la IA generativa» (guía de 9 puntos) |
| Redacción y defensa | Informe final integrado + slides de defensa |

---

## 8. Fuentes consultadas

- Compilador generador **Coco/R** — sitio oficial (JKU Linz): <https://ssw.jku.at/Research/Projects/Coco/>
- **User Manual** de Coco/R: <https://ssw.jku.at/Research/Projects/Coco/Doc/UserManual.pdf>
- **Tutorial** (slides JMLC'06, incluye el caso de estudio TASTE): <https://ssw.jku.at/Research/Projects/Coco/Tutorial/>
- Artículo **LL(1) Conflict Resolution in a Recursive Descent Compiler Generator** (JMLC'03): <https://ssw.jku.at/Research/Projects/Coco/Doc/ConflictResolvers.pdf>
- **Compiling with C# and Java** (Pat Terry) — manual de Coco/R con extensiones para C#/Java: <https://www.cs.ru.ac.za/compilerbook/CSharpAndJava/book2017/book2017text/CocoManual.pdf>
- **Aperture** (Tailscale) — documentación conceptual de la pasarela: <https://tailscale.com/docs/aperture> y <https://tailscale.com/docs/aperture/how-aperture-works>
- **Outlines** — generación estructurada (regex/gramática → autómata, enmascarado de tokens): <https://github.com/dottxt-ai/outlines>
- **Automata-based constraints for language model decoding**: <https://arxiv.org/html/2407.08103v3>
- Repositorio de **COMPI** (cátedra): <https://github.com/CompiladoresExactasUNSJ/compi2026>

**Material local analizado:** los tres documentos de la Semana 8; el clon del repositorio COMPI del grupo (`compi2026_grupo`); los apuntes teóricos generales de la materia y el material de la Semana 5.

---

## Anexo A — Precisiones y correcciones detectadas

1. **Coco/R y su atribución institucional.** Los apuntes de la materia lo presentan como «de la ETH Zúrich». Precisión para el informe: **creado en ETH Zürich (1989, Hanspeter Mössenböck); desarrollado y mantenido en JKU Linz** (de allí se descargan las versiones oficiales y cuelgan los enlaces que cita la cátedra).
2. **Granularidad de Aperture.** La documentación de la herramienta describe intercepción a nivel HTTP (mensajes y metadatos de petición/respuesta, conteos de tokens de uso, sesiones); no realiza análisis de tokens BPE. Para el nivel token, la referencia correcta es la línea de decodificación restringida (Outlines, GBNF, artículos citados). Conviene evitar la ambigüedad también en la defensa oral.
3. **El nombre TASTE.** Es intencional: el lenguaje de ejemplo «da una probada» (*a taste*) de cómo escribir un compilador con Coco/R; el nombre no es un acrónimo en la documentación consultada.
4. **Linaje de COMPI.** El namespace `at.jku.ssw.cc` y la notación `(. ... .)` evidencian la procedencia académica (JKU Linz / tradición Mössenböck) del compilador de la cátedra; es un dato verificable en el código y aporta contexto valioso al informe.
