# Preguntas y Respuestas de Parciales - Compiladores

**Fuente:** capturas de exámenes reales tomados en el Campus Virtual (Moodle) de la cátedra *Compiladores - LCC - FCEFN - UNSJ*, incluidas en `DATA PARCIALES.pdf` (evaluaciones parciales e integradoras, cohortes 2022-2023). Se transcribió cada pregunta completa, con todas sus opciones, y se indica cuál es la correcta según la corrección de Moodle (resaltado en verde / marcada como respuesta correcta en las capturas), más una explicación breve apoyada en el apunte teórico (`01 - APUNTE TEORICO GENERAL.md`).

**Cómo usar esta guía:** cada pregunta trae un tema asociado (Scanner, Parser, Semántico, Tabla de Símbolos, CodeGen) para que puedas cruzarla con la sección correspondiente del apunte teórico. Varias preguntas se repiten (idénticas o casi) en distintos exámenes de la fuente — es una señal fuerte de que son puntos que la cátedra evalúa sistemáticamente.

---

## Índice

1. [Scanner / análisis léxico](#1-scanner--análisis-léxico)
2. [Parser / análisis sintáctico](#2-parser--análisis-sintáctico)
3. [Procesamiento semántico](#3-procesamiento-semántico)
4. [Tabla de símbolos](#4-tabla-de-símbolos)
5. [Generación de código (CIL)](#5-generación-de-código-cil)
6. [Checklist rápido de respuestas correctas](#6-checklist-rápido-de-respuestas-correctas)

---

## 1. Scanner / análisis léxico

### Pregunta 1

> En cada momento de la ejecución del COMPI, existe conceptualmente una ventana doble, que contiene un TOKEN y un LATOKEN. En este contexto, ¿cuál es la función del Método SCAN?

**Opciones:**
- ✅ **Mover un lugar la ventana doble**
- ❌ Sólo formar un TOKEN
- ❌ Sólo implementar un autómata finito determinístico
- ❌ Separar espacios

**Respuesta correcta:** *Mover un lugar la ventana doble.*

**Por qué:** la ventana doble (`token` / `laToken`) es el mecanismo de *lookahead* de un token del COMPI: en todo momento el parser ya tiene el token actual (`token`) y puede mirar el siguiente (`laToken`) sin consumirlo. `Scan()` es la operación que **desliza** esa ventana un lugar: el viejo `laToken` pasa a ser el nuevo `token`, y se lee un token nuevo del scanner para convertirse en el nuevo `laToken`. Formar el token (reconocerlo carácter a carácter) es responsabilidad de `Next()`/el autómata interno del scanner, no de `Scan()` en sí — por eso las otras opciones son distractores que confunden capas distintas del mecanismo. Ver §3 del apunte teórico (Scanner → "Ventana doble").

---

### Pregunta 2

> ¿En la gramática de la interface del Compi, se usa?

**Opciones:**
- ❌ Una EBNF (BNF extendida)
- ❌ Una gramática con acciones semánticas
- ❌ Ninguna de las anteriores
- ✅ **Una BNF**

**Respuesta correcta:** *Una BNF.*

**Por qué:** la "interface" o gramática de referencia que describe la sintaxis del lenguaje fuente de COMPI se expresa en **BNF pura** (Backus-Naur Form), sin las extensiones de la EBNF (`{ }`, `[ ]`) ni las acciones semánticas embebidas — esas sí aparecen, pero en la gramática **con atributos** que usa el generador del parser/codegen, que es un documento distinto. Es un distractor clásico confundir "la gramática que describe el lenguaje" con "la gramática que usa el generador de código". Ver §4 (Parser → BNF/EBNF) y §5 (Procesamiento semántico → gramática con atributos).

---

## 2. Parser / análisis sintáctico

### Pregunta 3

> La raíz de cada subárbol del árbol de derivación, que tenga al menos un hijo, se corresponde con:

**Opciones:**
- ✅ **Un No Terminal**
- ❌ Un terminal
- ❌ Un paréntesis
- ❌ La ejecución de un método en el programa fuente del COMPI

**Respuesta correcta:** *Un No Terminal.*

**Por qué:** en un árbol de derivación, solo los **No Terminales** se expanden (tienen producción → tienen hijos). Un **Terminal** es siempre una hoja del árbol (no puede tener hijos, porque no se reescribe más). Por eso "al menos un hijo" identifica inequívocamente a un No Terminal. Ver §4 (Parser → árbol de derivación).

---

### Pregunta 4

> ¿En qué caso, el token se resalta con verde en la opción "Paso a paso" en la etapa de compilación?

**Opciones:**
- ❌ En el caso de que se detecte un error.
- ✅ **En el caso de que, en el proceso de expansión del árbol de derivación, la producción de la gramática actual tenga más de una opción.**
- ❌ En el caso de que, en el proceso de expansión del árbol de derivación, la producción de la gramática actual sólo tenga una opción.
- ❌ En el caso de que alcance el final del programa.

**Respuesta correcta:** *cuando la producción actual tiene más de una opción (alternativa).*

**Por qué:** el resaltado en verde es una ayuda visual del modo "Paso a paso" del COMPI para señalar los puntos donde el parser tuvo que **decidir entre alternativas** de la gramática usando el token de *lookahead* (`laToken`) — es decir, dónde el parser realmente "eligió un camino" en la EBNF (`{ opc1 | opc2 | ... }`). Cuando la producción es una secuencia determinística de un solo camino, no hay decisión que mostrar, así que no se resalta: el `Check()` simplemente se cumple o falla, sin necesidad de mirar más adelante. Este es un punto muy remarcado en la transcripción de la clase de Parser — ver §4 (Parser → "resaltado en verde").

---

### Pregunta 5

> Para implementar la parte del Análisis Sintáctico (Parser) de un NO Terminal, se debe:

**Opciones:**
- ❌ Llamar al método NEXT
- ❌ Mover un lugar la ventana doble
- ✅ **Hacer una llamada a un Método que tiene el mismo nombre que él No Terminal**
- ❌ Llamar al método CHECK

**Respuesta correcta:** *hacer una llamada a un método homónimo al No Terminal.*

**Por qué:** en un parser de descenso recursivo (recursive descent), cada No Terminal de la gramática se traduce en un **método C# con el mismo nombre** (`Expr()`, `Term()`, `MethodDecl()`, etc.), que a su vez llama a los métodos de los No Terminales/Terminales de su producción. Es la regla estructural fundamental de todo el Parser.cs del COMPI. Ver §4 (Parser → "No Terminal → método homónimo").

---

### Pregunta 6

> Para implementar la parte del Análisis Sintáctico (Parser) de un Terminal, se debe:

**Opciones:**
- ✅ **a. Llamar al método CHECK**
- ❌ b. Llamar al método NEXT
- ❌ c. Implementar una gramática tipo 2
- ❌ d. Mover un lugar la ventana doble

**Respuesta correcta:** *llamar al método CHECK.*

**Por qué:** es la contracara exacta de la pregunta anterior: un **Terminal** no dispara una llamada recursiva (no tiene producción propia), sino que se verifica directamente contra el `token` actual con `Check(TERMINAL_ESPERADO)`, que compara y, si coincide, hace avanzar la ventana (`Scan()`); si no coincide, reporta error sintáctico. **No Terminal → método homónimo** / **Terminal → `Check`** es probablemente *la* pregunta más repetida de todo el banco de exámenes. Ver §4 (Parser).

---

## 3. Procesamiento semántico

### Pregunta 7

> La Gramática con atributos se usa para:

**Opciones:**
- ❌ Implementar sólo parámetros de salida de Métodos asociados a No Terminales
- ❌ Implementar parámetros de entrada y de salida de Métodos asociados a Terminales
- ❌ Implementar sólo parámetros de entrada de Métodos asociados a No Terminales
- ✅ **Implementar parámetros de entrada y de salida de Métodos asociados a No Terminales**

**Respuesta correcta:** *implementar parámetros de entrada y de salida de métodos asociados a No Terminales.*

**Por qué:** solo los **No Terminales** se traducen en métodos con cuerpo (los Terminales solo llaman a `Check`, no tienen atributos propios). La gramática con atributos anota cada No Terminal con parámetros de entrada (información que "baja" desde el contexto, atributos heredados) y de salida (información que "sube" desde la subexpresión evaluada, atributos sintetizados), que en C# se traducen literalmente en parámetros normales y parámetros `out`/`ref` del método correspondiente al No Terminal. Los Terminales, al no ser métodos con lógica propia, no llevan atributos de este tipo. Ver §5 (Procesamiento semántico → gramática con atributos).

---

### Pregunta 8

> En el contexto del procesamiento semántico, tal como se dio en clases, y dadas las siguientes cadenas de entradas y sus correspondientes salidas. ¿En qué caso es necesario usar parámetros de salida?

**Opciones:**
- ❌ Ninguna de las anteriores
- ✅ **1+2+3 --> 6 (suma)**
- ❌ Write('hola') --> hola
- ❌ 1+2+3 --> 3 (cuenta)

**Respuesta correcta:** *1+2+3 --> 6 (suma).*

**Por qué:** el caso "suma" necesita que cada No Terminal (`Term`, `Factor`) **devuelva hacia arriba** el valor numérico que calculó, para que el nivel superior lo pueda acumular — eso es exactamente un **atributo de salida** (parámetro `out`/valor de retorno) que sube por la recursión. En cambio, `Write('hola') --> hola` es una operación de I/O directa (no hay valor que sintetizar y propagar: se imprime y listo), y "contar" (`1+2+3 --> 3`, cantidad de operandos) puede resolverse con un contador incremental que no necesariamente requiere que cada nivel devuelva un valor calculado hacia arriba de la misma manera que una suma acumulada — el ejemplo de la cátedra usa específicamente la suma para mostrar el caso canónico donde el atributo de salida es indispensable. Ver §5 (Procesamiento semántico → "cuándo hacen falta parámetros de salida").

---

### Pregunta 9

> En qué caso la concatenación de las hojas del árbol de derivación pueden coincidir con la cadena de entrada (programa fuente), es decir mirando la producción de la gramática, la cadena es válida. Sin embargo el compilador acusa error.

**Opciones:**
- ❌ Sólo Cuando encuentra un while identificador incorrecto.
- ❌ Ninguna de las anteriores
- ✅ **Sólo cuando existe alguna variable que no fue declarada en el scope correspondiente**
- ❌ Sólo Cuando encuentra un paréntesis que no está balanceado

**Respuesta correcta:** *cuando existe alguna variable no declarada en el scope correspondiente.*

**Por qué:** esta pregunta evalúa la diferencia entre **validez sintáctica** y **validez semántica**. Que las hojas del árbol de derivación (los tokens, leídos de izquierda a derecha) reconstruyan exactamente el programa fuente significa que el programa es **sintácticamente correcto** (el parser lo aceptó sin errores de gramática). Pero el compilador puede seguir rechazando el programa por errores **semánticos**, que no dependen de la forma sino del significado — el caso típico y más citado en la cátedra es usar una variable que **no fue declarada en el scope correspondiente** (falla la búsqueda en la Tabla de Símbolos, `Tab.Find` no la encuentra). Un paréntesis no balanceado o un identificador de `while` mal escrito, en cambio, **sí** habrían hecho fallar al parser (son errores sintácticos, no dejarían que el árbol coincida con la cadena de entrada). Ver §6 (Tabla de símbolos → "validez sintáctica vs. semántica").

---

## 4. Tabla de símbolos

### Pregunta 10

> Cuantos Scopes genera el siguiente programa fuente:
> ```
> class ProgPpal
> {
>   void Main()
>   {
>     writeln("hola");
>   }
> }
> ```

**Opciones:**
- ❌ 1 Scope
- ✅ **2 Scopes**
- ❌ Ninguna de las anteriores
- ❌ 3 Scopes

**Respuesta correcta:** *2 Scopes.*

**Por qué:** la regla de la cátedra es **"se abre un Scope solamente cada vez que se inserta un método o una clase"** en la tabla de símbolos (no por cada bloque `{ }`, ni por cada sentencia). En este programa hay exactamente dos declaraciones de ese tipo: la **clase** `ProgPpal` (1 scope) y el **método** `Main` (otro scope, anidado dentro del de la clase). El `writeln("hola")` es una sentencia de I/O, no declara nada, así que no abre scope propio — por eso no son 3. Y no puede ser 1, porque método y clase son dos unidades de scope distintas (las variables locales de `Main` no viven en el mismo scope que los miembros de `ProgPpal`). Ver §6 (Tabla de símbolos → "Scope: cuándo se abre").

---

### Pregunta 11

> En la tabla de símbolos, se debe abrir un Scope, solamente cada vez que se inserta:

**Opciones:**
- ❌ Una variable global o una constante
- ✅ **Un método o una clase**
- ❌ Ninguna de las respuestas anteriores
- ❌ Un método o una variable global
- ❌ Una clase o una variable global

**Respuesta correcta:** *un método o una clase.*

**Por qué:** es la formulación explícita de la regla usada para resolver la Pregunta 10. Las variables (globales, locales o constantes) se **insertan como símbolos dentro de** un scope ya existente; no generan un scope nuevo por sí mismas. Solo dos construcciones abren un scope nuevo en este lenguaje: declarar un **método** (scope para sus parámetros y variables locales) o declarar una **clase** (scope para sus miembros). Ver §6 (Tabla de símbolos).

---

### Pregunta 12

> Cuando se usa la llamada `Tab.Find("int")`, el método devuelve una instancia de la clase:

**Opciones:**
- ❌ 1. Ninguna de las respuestas anteriores
- ❌ 2. Parser
- ✅ **3. Symbol**
- ❌ 4. Struct
- ❌ 5. Tab

**Respuesta correcta:** *Symbol.*

**Por qué:** `Tab.Find(nombre)` busca un identificador (variable, tipo, método, clase) recorriendo la pila de scopes desde el más interno hacia el más externo, y devuelve el **`Symbol`** asociado a ese nombre (el registro completo con nombre, tipo, clase de símbolo — variable/método/clase —, scope, dirección, etc.). No devuelve directamente un `Struct` (que es la clase que representa **tipos**, no símbolos): si necesitás el tipo del símbolo, tenés que acceder a `symbol.type`, que **sí** es un `Struct`. Confundir `Symbol` con `Struct` es un error común señalado por la cátedra. Ver §6 (Tabla de símbolos → "qué devuelve `Tab.Find`").

---

### Pregunta 13

> El Stack Frame está formado por:

**Opciones:**
- ❌ Sólo valores de Variables Locales
- ✅ **Method States**
- ❌ Sólo Variables Locales
- ❌ Sólo argumentos de Métodos

**Respuesta correcta:** *Method States.*

**Por qué:** el **Stack Frame** (marco de pila / registro de activación) que se crea en cada llamada a un método no contiene *solo* una de las partes por separado (ni solo locales, ni solo argumentos): es el **Method State** completo del CLR/CIL — el conjunto de argumentos, variables locales y la pila de evaluación (*evaluation stack*) que ese método necesita durante su ejecución. Las otras opciones son subconjuntos incompletos, un distractor típico de "es verdad pero no es toda la verdad". Ver §7 (Generación de código → "Stack Frame / Method State").

---

## 5. Generación de código (CIL)

### Pregunta 14

> En la sentencia `il.DeclareLocal(sym.type.sysType)`, la variable `"il"`, se usa para:

**Opciones:**
- ✅ **Asociar el Metadato de la variable local apuntada por "sym", al Metadato del Método en donde se define.**
- ❌ Asociar el Metadato de la variable local apuntada por "sym", a la variable apuntada por "sym"
- ❌ Asociar el Metadato de la variable local apuntada por "sysType", al Metadato del Método, en donde se define.
- ❌ Ninguna de las anteriores

**Respuesta correcta:** *asociar el metadato de la variable local apuntada por "sym" al metadato del método en donde se define.*

**Por qué:** `il` es una instancia de `ILGenerator` (`System.Reflection.Emit`), obtenida desde el `MethodBuilder` del método que se está generando. Cuando llamás `il.DeclareLocal(...)`, le estás diciendo al **método actualmente en construcción** ("el Metadato del Método en donde se define") que registre una nueva variable local — es decir, `il` es el vínculo/canal que asocia esa declaración de variable local con el método dueño de ese cuerpo de código. No es la variable en sí, ni conecta tipos entre sí: es el "generador de instrucciones" del método actual. Ver §7 (Generación de código → `il.DeclareLocal`).

---

### Pregunta 15

> En la sentencia `il.DeclareLocal(sym.type.sysType)`, el argumento `"sym.type.sysType"`:

**Opciones:**
- ❌ Apunta al Tipo del Método, al cual pertenece la variable local
- ❌ Apunta al Metadato de Tipo del Método, al cual pertenece la variable local
- ✅ **Apunta al Metadato de Tipo de la variable local, cuyo Metadato se está definiendo.**
- ❌ Apunta al Tipo del Método, al cual pertenece la variable local (repetida)

**Respuesta correcta:** *apunta al metadato de tipo de la variable local cuyo metadato se está definiendo.*

**Por qué:** `sym` es el `Symbol` (de la Tabla de Símbolos) de la variable local que se está declarando; `sym.type` es su `Struct` (el tipo del lenguaje fuente: `int`, `bool`, etc.); y `sym.type.sysType` es la traducción de ese `Struct` a un **`System.Type` real de .NET** (el metadato de tipo que entiende Reflection.Emit — por ejemplo `typeof(int)`). Es decir, el argumento completo le dice a `DeclareLocal` **de qué tipo CLR** es la variable local que se está registrando — no describe el método, describe el **tipo de la variable en sí**. Nótese cómo esta pregunta se complementa con la anterior: `il` = "en qué método", `sym.type.sysType` = "de qué tipo es la variable". Ver §7 (Generación de código → `il.DeclareLocal`, cadena `Symbol → Struct → System.Type`).

---

### Pregunta 16

> En el siguiente código, que asigna una operación aritmética a una variable, analice el código y exprese matemáticamente dicha expresión:
> ```
> 0: .locals init(int32 V_0)
> 1: ldloc.0
> 2: ldc.i4 2
> 3: ldc.i4 3
> 4: ldc.i4 5
> 5: add
> 6: ldc.i4 7
> 7: mul
> 8: add
> 9: stloc.0
> 10: pop
> 11: ret
> ```

**Respuesta dada como correcta en la fuente:**
```
int V_0
V_0 = 2 + (7 * (3 + 5))
```

**Por qué (traza completa de la pila de evaluación — *evaluation stack*):**

| # | Instrucción | Efecto | Pila resultante (tope a la derecha) |
|---|---|---|---|
| 0 | `.locals init(int32 V_0)` | declara `V_0` (local 0) | `[]` |
| 1 | `ldloc.0` | push valor actual de `V_0` | `[V_0]` |
| 2 | `ldc.i4 2` | push constante 2 | `[V_0, 2]` |
| 3 | `ldc.i4 3` | push constante 3 | `[V_0, 2, 3]` |
| 4 | `ldc.i4 5` | push constante 5 | `[V_0, 2, 3, 5]` |
| 5 | `add` | pop 3,5 → push 8 | `[V_0, 2, 8]` |
| 6 | `ldc.i4 7` | push constante 7 | `[V_0, 2, 8, 7]` |
| 7 | `mul` | pop 8,7 → push 56 | `[V_0, 2, 56]` |
| 8 | `add` | pop 2,56 → push 58 | `[V_0, 58]` |
| 9 | `stloc.0` | pop 58 → guarda en `V_0` | `[V_0_viejo]` |
| 10 | `pop` | descarta el valor que quedó (el `ldloc.0` inicial) | `[]` |
| 11 | `ret` | retorna | — |

Resultado: `V_0 = 2 + (7 * (3 + 5)) = 2 + (7 * 8) = 2 + 56 = 58`.

El `ldloc.0` inicial y el `pop` final son un patrón del generador de código del COMPI para sentencias de asignación tratadas como expresión: se carga el valor viejo de la variable al principio (por cómo está estructurada la gramática con atributos de la asignación) y, como ese valor no se termina usando en el cálculo real, se descarta al final con `pop` una vez que el resultado nuevo ya fue guardado con `stloc.0`. Es clave para leer trazas de CIL en el parcial: identificar qué instrucciones son el cálculo real (2 al 8) y cuáles son "ruido" estructural del patrón de asignación (1 y 10). Ver §7 (Generación de código → traza completa de `2 + (7 * (3 + 5))`).

---

## 6. Checklist rápido de respuestas correctas

Para repaso de último momento, sin las explicaciones — la respuesta correcta de cada pregunta del banco:

| # | Pregunta (resumen) | Respuesta correcta |
|---|---|---|
| 1 | Función del método `SCAN` | Mover un lugar la ventana doble |
| 2 | Gramática de la interface del Compi | Una BNF |
| 3 | Raíz de subárbol con ≥1 hijo | Un No Terminal |
| 4 | Cuándo se resalta el token en verde ("Paso a paso") | Cuando la producción tiene más de una opción |
| 5 | Implementar un No Terminal en el Parser | Llamar a un método homónimo al No Terminal |
| 6 | Implementar un Terminal en el Parser | Llamar al método `CHECK` |
| 7 | Para qué se usa la gramática con atributos | Params de entrada/salida de métodos de No Terminales |
| 8 | Caso que necesita parámetro de salida | `1+2+3 --> 6` (suma) |
| 9 | Árbol válido pero el compilador acusa error | Variable no declarada en el scope correspondiente |
| 10 | Scopes de `class ProgPpal { void Main(){...} }` | 2 Scopes |
| 11 | Cuándo se abre un Scope nuevo | Al insertar un método o una clase |
| 12 | Qué devuelve `Tab.Find("int")` | Una instancia de `Symbol` |
| 13 | De qué está formado el Stack Frame | Method States |
| 14 | `il` en `il.DeclareLocal(sym.type.sysType)` | Asocia el metadato de la variable local (`sym`) al metadato del método donde se define |
| 15 | `sym.type.sysType` en `il.DeclareLocal(...)` | Apunta al metadato de tipo de la variable local que se está definiendo |
| 16 | Traza CIL de asignación con `add`/`mul` | `V_0 = 2 + (7 * (3 + 5))` = 58 |
