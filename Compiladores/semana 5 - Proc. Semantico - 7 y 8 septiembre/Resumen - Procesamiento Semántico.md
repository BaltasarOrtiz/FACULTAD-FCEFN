# Procesamiento Semántico — Resumen de la semana 5

> **Fuentes** — clases del **7 y 8 de septiembre**
> - 🎬 `clase 5 - proc semant 2026.mp4` (≈33 min) — clase teórica de introducción al tema. Referencias: **[v1 mm:ss]**
> - 🎬 `proc semant parte 2 .mp4` (≈38 min) — seguimiento detallado, paso a paso, de `3 * (2 + 4)`. Referencias: **[v2 mm:ss]**
> - 📊 `05.SemanticProcessing 2026.ppt` — filminas de la cátedra (material de base: Mössenböck / JKU Linz, adaptado)
> - Transcripciones completas con timestamps: `transcripcion/clase5.txt` y `transcripcion/parte2.txt`
>
> En la PPT los atributos se marcan con **★ (estrella llena) = atributo de salida** y **☆ (estrella hueca) = atributo de entrada**.

---

## 1. Dónde entra el procesamiento semántico

COMPI está organizado en módulos, uno por etapa del compilador:

| Unidad | Tema | "Lo que usa" | Código |
|---|---|---|---|
| 1 | Introducción | `this` | Proyecto |
| 2 | Scanner | Autómatas finitos | `Scanner.cs` |
| 3 | Parser | Gramática tipo 2 | `Parser.cs` |
| 4 | Parser adicional | Gramática tipo 2 | `Parser.cs` |
| **5** | **Semantic Processing** | **acciones semánticas: código C#** | **— (no tiene módulo propio)** |
| 6 | Code Generation 1 | Lenguaje intermedio: CIL | `miCodGen.cs` |
| 7 | Tabla de símbolos | Estructura de datos | `SymTab.cs` |
| 8 | Code Generation 2 | Metadatos | `miCodGen.cs` |

**Punto clave:** la unidad 5 *no tiene un archivo de código propio*. La PPT lo marca como "NO"… pero en realidad **las acciones semánticas están insertas dentro del código del parser** (`Parser.cs`) — por eso el tema se estudia directamente sobre el parser [v1 00:37–01:27] [v1 03:37].

Flujo general del compilador: fuente → tokens (Scanner) → el Parser verifica cada token contra la gramática **y** va armando el árbol de derivación → sobre ese parseo se agregan **atributos + acciones semánticas** (esta unidad) → generación de código intermedio CIL (unidad 6).

---

## 2. Repaso de las piezas que se usan (scanner y parser)

Antes de entrar en el tema, la clase repasa los mecanismos sobre los que se montan las acciones semánticas:

- **Lista de tokens + ventana de lookahead.** El programa fuente se convierte en una lista de tokens. Hay dos variables que forman una "ventanita" que avanza: `laToken` (el *lookahead*: el token que sigue) y `token` (el último token reconocido / en análisis) [v1 01:27–02:09].
- **`Scan()`**: corre la ventana — `token = laToken; laToken = Scanner.Next(); la = laToken.kind;`. La primera vez `token = laToken` "no hace nada"; por eso el parser hace un `Scan()` al principio para que el primer token quede disponible [v1 09:37–09:55].
- **`Check(expected)`**: la gramática le dice qué token *debería* venir en esa posición; `Check` compara ese esperado con `la`. Si coincide, avanza (`Scan()`); si no, da error [v1 09:55–10:56].
- **La gramática como verificadora.** El parser usa la gramática para determinar si el programa está bien formado, token por token, y a la vez va construyendo el **árbol de derivación** [v1 02:09–02:49] [v1 04:10–04:52].
- **EBNF vs. BNF.** En las filminas la gramática se muestra en **EBNF** (BNF extendido: `{ ... }` = cero o más repeticiones, `[ ... ]` opcional), que es más cómodo para la parte teórica y conceptual. COMPI internamente usa la versión en **BNF** (sin llavecitas), con no terminales auxiliares recursivos del estilo `MasTerm` [v1 05:42–06:48] [v2 00:21–01:05] [v2 38:05–38:29].

> ⚠️ Frase de la clase: *"que compile bien no quiere decir que el programa sea correcto"* — para saber si el programa hace lo que queremos hay que **ejecutarlo / depurarlo** [v1 02:49–03:21].

---

## 3. Qué es el procesamiento semántico

La idea central de la unidad: **ponerle acciones a la gramática** [v1 05:00–05:11].

Una **acción semántica** es código (en COMPI, sentencias **C#**) asociado a una producción de la gramática. Se escribe en la notación `(. ... .)` intercalada con las producciones:

```
Expr = Term (. int n = 1; .)
       { "+" Term (. n++; .) }
       (. Console.WriteLine(n); .) .
```

Sin acciones semánticas, el parser solo **reconoce** si la cadena es correcta: no calcula nada [v1 07:13–08:36]. Con acciones, además **hace** algo mientras reconoce (sumar, contar, insertar en la tabla de símbolos, generar código…).

### Ejemplo 1 — una acción semántica "sin atributos": contar términos

Objetivo: en vez de sumar, **contar cuántos términos** tiene la cadena [v1 11:40–12:04]:

| Entrada | Resultado |
|---|---|
| `1 + 2 + 3` | 3 términos |
| `47 + 1` | 2 términos |
| `909` | 1 término |

Reglas (marcadas en rojo en la PPT): asociado a `Term` está `(. int n = 1; .)`; asociado a `{ "+" Term }` está `(. n++; .)`; al final `(. Console.WriteLine(n); .)`.

Implementación en C# (estilo de la PPT):

```csharp
static void Expr() {
    Term();
    int n = 1;
    for (;;) {
        if (la == Token.PLUS) { Scan(); Term(); n++; }
        else break;
    }
    Console.WriteLine(n);
}
```

Observación importante: **para esta acción no se necesitó ningún atributo** — la variable `n` es interna al método. Los atributos aparecen cuando hay que *pasar valores* entre las producciones (típicamente en las expresiones) [v1 13:41–14:23] [v1 19:06–19:12].

---

## 4. Atributos

Un **atributo** es un dato ("parámetro") asociado a un símbolo de la gramática — en la implementación: **parámetros de los métodos del parser**. Hay dos tipos [v1 13:41–14:00]:

### 4.1 Atributos de salida (★) — sintetizados

Son el **resultado** que una producción devuelve hacia **arriba** en el árbol, a quien la llamó [v1 18:22–19:34].

Ejemplo: la suma de enteros. Ahora `Expr` y `Term` necesitan pasarse valores: la PPT lo escribe así (★ = salida):

```
Expr (. int sum, val; .) = Term <★sum>
      { "+" Term <★val> (. sum += val; .) }
      (. Console.WriteLine(sum); .) .
```

En C# se ve directo: aparece **`out`** ("se agrega `out` en la definición y en la llamada") [v1 14:48–16:45]:

```csharp
static void Expr() {
    int sum, val;
    Term(out sum);
    for (;;) {
        if (la == Token.PLUS) { Scan(); Term(out val); sum += val; }
        else break;
    }
    Console.WriteLine(sum);
}
```

Con esto: `1+2+3 → 6`, `47+10 → 57`, `909 → 909` (antes solo contaba: `1+2+3 → 3`). La mecánica es "llamo → sumo → llamo → sumo": cada `Term` "entrega" su número y `Expr` lo acumula.

### 4.2 Atributos de entrada (☆) — modificadores de la acción

Un atributo de entrada **baja** desde quien llama hacia la producción: es un **parámetro que modifica la acción** que se ejecuta [v1 17:00–17:57].

Ejemplo de la PPT: `Expr<☆bool printHex>` — si `printHex` es `true`, el resultado se imprime en hexadecimal; si no, en decimal:

```csharp
static void Expr(bool printHex) {
    int sum, val;
    Term(out sum);
    ...
    if (printHex) Console.WriteLine("{0:X}", sum);
    else Console.WriteLine("{0:D}", sum);
}
```

### 4.3 Regla para recordar

> **Los atributos de salida van hacia arriba en el árbol; los de entrada van hacia abajo.** [v1 19:26–19:54]
> - Salida = "el resultado que devuelvo a quien me llamó" (→ sintetizado).
> - Entrada = "el contexto/modificador que recibo" (→ heredado).

No *toda* acción semántica necesita atributos, pero **todas las expresiones necesitan pasar valores** (para arriba): *"la gramática de atributos me permite implementar las acciones semánticas"* [v1 18:56].

---

## 5. Los tres ingredientes de una gramática con atributos

La filmina "Gramáticas con Atributos" resume el tema en tres capas [v1 20:01–20:22]:

1. **Producciones (EBNF)** — la gramática de siempre, p. ej. `Expr = Term { "+" Term }.`
2. **Atributos (parámetros)** — anotados en `<...>`: `Term <★int val>`, `Expr <☆bool printHex>` (salida / entrada).
3. **Acciones semánticas** — `(. ... sentencias en C# ... .)`.

La misma gramática en **BNF puro** (lo que usa COMPI) necesita símbolos auxiliares:

```
Expr   = Term | Term MasTerm.
MasTerm = . | "+" Term MasTerm.
```

(bucle por recursión a la derecha). Es equivalente, pero — como dijo el profe — "ya se complica bastante", y en el compilador real es más complejo todavía [v2 38:00–38:29].

---

## 6. Caso: declaración de variables (`VarDecl`) y la tabla de símbolos

Ejemplo con atributos de salida **y** de entrada a la vez, sobre una declaración múltiple: `int var1, var2, var3;` [v1 20:33–26:19]:

```
VarDecl    = Type IdentList ";".
IdentList  = ident { "," ident }.

Type       (. Struct type; .)              ← el tipo sale como atributo de salida  ★
IdentList  (. Tab.Insert(token.str, type); .)  ← recibe el tipo como entrada  ☆
```

- `Type` **entrega** el tipo (`int`) como **atributo de salida**; ese tipo **entra** a `IdentList` como **atributo de entrada** y se usa en la acción semántica: insertar cada identificador en la **tabla de símbolos** junto con su tipo.
- Implementación en COMPI (estilo PPT):

```csharp
static void VarDecl() {
    Struct type;
    Type(out type);          // out = atributo de salida
    IdentList(type);         // pasaje hacia abajo = atributo de entrada
    Check(Token.SEMICOLON);
}

static void IdentList(Struct type) {
    Check(Token.IDENT);
    Tab.Insert(token.str, type);
    while (la == Token.COMMA) {
        Scan();
        Check(Token.IDENT);
        Tab.Insert(token.str, type);
    }
}
```

Adelanto de la clase siguiente: la **tabla de símbolos** (`SymTab.cs`, unidad 7) almacena variables y su **alcance (scope)**; con alcances, "la misma variable" declarada en funciones distintas son variables diferentes. Acá, por ahora, solo se la usa: insertar nombre (`token.str`) + tipo [v1 22:36–24:06].

---

## 7. Caso central: seguimiento completo de `x = 3 * (2 + 4)` → 18

Todo el video de la parte 2 es el seguimiento, paso a paso, de esta expresión — primero **conceptual** (como si fuera un intérprete) y luego **como lo hace realmente el compilador** [v2 00:00–01:05].

### 7.1 La gramática atribuida (PPT, "Expresiones Constantes")

```
Expr   (. int val .)  = Term <★int val>
                        { "+" Term <★val1> (. val += val1; .)
                        | "-" Term <★val1> (. val -= val1; .) }.

Term   (. int val .)  = Factor <★int val>
                        { "*" Factor <★val1> (. val *= val1; .)
                        | "/" Factor <★val1> (. val /= val1; .) }.

Factor (. int val .)  = number          (. val = token.val; .)
                      | "(" Expr ")"    ← no necesita acción semántica:
                                           usa una sola variable (val).
```

- Entrada: `3 * (2 + 4)` — resultado deseado: `18`.
- Los atributos (`val`, `val1`) son **todos de salida**: cada no terminal devuelve su valor numérico.

### 7.2 El árbol de derivación y el rol del lookahead

En cada punto el parser decide **con la ventana** qué alternativa tomar [v2 02:36–04:26]:

- `Term` **siempre** empieza llamando a `Factor`.
- `Factor` tiene dos opciones: `number` o `"(" Expr ")"`. **Se decide mirando `la`**: si el siguiente token es un paréntesis, va por la segunda; si es un número, por la primera.
- El primer `Factor` encuentra `3` (number) → `Check(NUMBER)` avanza la ventana → `token` queda valiendo `3` → acción: `val = token.val` → **val = 3**.

### 7.3 El punto clave de toda la clase: compilación ≠ ejecución

Al terminar `Factor` con `3`… **en el compilador no "sube" ningún 3**. Lo que sube es *la instrucción*:

| Si fuera un intérprete | Como es un compilador (COMPI) |
|---|---|
| El valor 3 "sube" como atributo y se apila **ahora** | Se **emite la instrucción** `ldc.i4.3` (*load constant integer 3*) — ningún 3 sube todavía a ninguna pila |
| La suma `2+4` se calcula en el momento | Se emite `add` |
| La multiplicación `3*6` se calcula en el momento | Se emite `mul` |
| Resultado `18` disponible durante el análisis | El `18` **recién aparece en la pila cuando se ejecute la máquina virtual** |

> "No pueden mezclar compilación y ejecución" — es el concepto que el profe marcó como **el más importante** [v2 12:47–12:57].

En el seguimiento del árbol, los valores conceptuales (3, 2, 4, 6, 18) sirven de ayuda para entender **qué haría un intérprete**; las instrucciones (load, add, mul) son **lo que realmente hace el compilador**.

### 7.4 Seguimiento paso a paso (síntesis)

| # | Paso en el árbol | Acción semántica / qué pasa | CIL emitido |
|---|---|---|---|
| 1 | `Factor` → `number 3` | `Check(NUMBER)`: avanza la ventana; `token.val = 3` → `val = 3` | `ldc.i4.3` |
| 2 | `Term` ve `*` | `Scan` del `*`; prepara `val *= val1` para el final | — |
| 3 | `Factor` (2º): ve `(` | Entra por `"(" Expr ")"` — `Check(LPAR)` | — |
| 4 | `Expr` interna (`2 + 4`) | `Term`→`Factor`→`number 2`: `val = 2` | `ldc.i4.2` |
| 5 | Ve `+` | `Scan`; `Term`→`Factor`→`number 4`: `val1 = 4` | `ldc.i4.4` |
| 6 | Acción del `+` | (intérprete: `2+4=6`) | `add` |
| 7 | `Check(RPAR)` | El `Factor` 2º "termina valiendo 6" (conceptual) | — |
| 8 | Vuelve al `Term` externo | Acción `val *= val1` → (intérprete: `3*6=18`) | `mul` |
| 9 | Fin de la expresión | (intérprete: "sube" un 18) — el compilador emite todo y termina | — |

**Traza final cuando ejecute la máquina virtual:**

```
ldc.i4.3 → pila: [3]
ldc.i4.2 → pila: [3, 2]
ldc.i4.4 → pila: [3, 2, 4]
add      → pila: [3, 6]       (2+4)
mul      → pila: [18]         (3*6)
```

### 7.5 Detalles finos del seguimiento (los "colores" del video)

- **Cada llamada es una instancia distinta del mismo método.** En el árbol hay cuatro `Factor` (marrón `3`, azul `( )`, magenta `2`, morado `4`) y dos `Expr` (la raíz y la gris interna) que "se llaman igual" pero son llamadas diferentes: cada una tiene su propio **registro de activación** (con su propio `val`) — por eso el profe las pinta con colores distintos. "Es el mismo nombre del método, pero son llamadas diferentes, son instancias diferentes" [v2 15:52–16:19] [v2 21:06–21:20].
- **Terminales vs. no terminales en la implementación**: cada no terminal de la gramática se implementa como un **método** con su nombre; cada terminal se reconoce con un **`Check`** [v2 01:45–01:58].
- **Atributos de salida = parámetros `out`.** En la implementación, cada atributo ★ de la gramática termina siendo un parámetro `out` del método [v1 14:48–16:45] [v2 01:58–02:11].
- **El paréntesis que cierra**: al terminar la `Expr` interna, la gramática "pide" `)` (`Check(RPAR)`); si faltara, sería un **error de sintaxis** [v2 33:10–33:24].
- **Al terminar todo**, el compilador "no sube ningún 18": *"lo único que hizo fue incluir todas estas instrucciones… `load3`, `load2`, `load4`, `add`, `mul`"* [v2 37:42–38:00].

---

## 8. Intérprete vs. compilador — el contraste que dejó la clase

| | Intérprete | Compilador (COMPI) |
|---|---|---|
| Al reconocer un número | Sube/preserva el **valor** en ese momento | Emite `ldc.i4.<n>` (carga diferida) |
| Al reconocer una operación | **Calcula** el resultado (2+4=6) | Emite la instrucción (`add`, `mul`) |
| Cuándo existe el resultado | Durante el análisis | **Recién al ejecutar la máquina virtual**, en la pila |
| Qué "sube" por el árbol conceptual | Valores (para entender el mecanismo) | Nada: se acumulan instrucciones CIL |

Analogía del profe: los valores del seguimiento "es lo que sucedería si fuera un intérprete — sirve para entender, pero lo que realmente sucede es que se genera la instrucción" [v2 28:01–28:20].

---

## 9. Glosario rápido

| Término | Significado en esta unidad |
|---|---|
| **Acción semántica** | Código C# `(. ... .)` asociado a una producción; se ejecuta durante el parseo |
| **Atributo** | "Parámetro" asociado a un símbolo de la gramática (en COMPI: parámetro del método del parser) |
| **Atributo de salida (★)** | Valor que la producción devuelve hacia arriba (sintetizado); en C#: parámetro `out` |
| **Atributo de entrada (☆)** | Valor que baja desde quien llama (heredado); modifica la acción de la producción |
| **Gramática con atributos** | EBNF + atributos + acciones semánticas |
| **Árbol de derivación** | Árbol que arma el parser al reconocer; los atributos "viajan" por sus ramas |
| **Tabla de símbolos** | Estructura (unidad 7) donde se registran variables y su tipo/alcance; acá se usa con `Tab.Insert` |
| **CIL** | Lenguaje intermedio de .NET; las instrucciones que COMPI emite (ldc.i4, add, mul, stloc…) |
| **`token` / `laToken`** | La ventana: último token reconocido / lookahead (el que viene) |
| **`Check(t)` / `Scan()`** | Reconocer el token esperado / avanzar la ventana |

---

## 10. Conexión con la actividad práctica nro 5

La guía pide el seguimiento **a nivel de código** de `x = 3 * (2 + 4)` sobre COMPI (`Parser.cs`) — exactamente el ejemplo de este tema. Traducción entre la notación de la PPT y el código real de COMPI:

| PPT (didáctico) | COMPI real (`Parser.cs`, ver tu entrega) |
|---|---|
| No terminal → método | `Expr()`, `Term()`, `Factor()`, `Designator()` |
| ★ atributo de salida `<★int val>` | parámetro `out Item item` (el `Item` lleva `kind`, `type`, `val`) |
| ☆ atributo de entrada (contexto) | parámetro heredado (`TreeNode padre`, etc.) |
| Acción semántica | sentencias C# embebidas (`Code.Load(...)`, `Code.il.Emit(ADD/MUL)`, `Tab.Insert`, `Code.Assign`) |
| "Genera la instrucción load 3" | `Code.Load(item)` → `ldc.i4 3`; `Emit(ADD)` → `add`; etc. |

Detalle completo en `Entrega - Actividad nro 5 - Analisis semantico.md`.

---

*Resumen generado combinando las transcripciones de los dos videos de clase y el texto de la PPT `05.SemanticProcessing 2026.ppt`. Los números de diapositiva/tiempos citados corresponden a los archivos de esta carpeta.*
