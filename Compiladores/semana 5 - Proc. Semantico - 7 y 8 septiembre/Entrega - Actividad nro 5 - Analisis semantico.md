# Actividad nro 5 — Análisis semántico
## Seguimiento a nivel de código de la expresión `x = 3 * (2 + 4)`

**Herramienta:** COMPI (repo `CompiladoresExactasUNSJ/compi2026`, versión del grupo `compi2026_grupo`)
**Archivo analizado:** `text Box Mio/Parser.cs`

---

## 0. Programa fuente para COMPI

Programa en el lenguaje de la cátedra que COMPI debe compilar (la expresión a seguir está en la asignación de `x`):

```
class Cl
{
    void Main()
    {
        int x;
        x = 3 * (2 + 4);
        write(x, 3);
    }
}
```

Se guardó también como `Programa_COMPI_x_3x(2+4).txt` en esta misma carpeta.

---

## 1. Métodos que implementan los símbolos no terminales de la gramática que define este tipo de expresiones

La gramática de expresiones (forma **EBNF**, como se presenta en el material):

```
Expr     = Term { ("+" | "-") Term }.
Term     = Factor { ("*" | "/" | "%") Factor }.
Factor   = Designator OpcRestOfMethCall | number | charConst | "new"...
           | "(" Expr ")".
Designator = ident opcRestOfDesignator.
```

En el código de COMPI la gramática de expresiones se ve implementada tal cual se carga en pantalla
(`Code.cargaProgDeLaGram`):

```
Expr                  = OpcMinus Term OpcAddopTerms.
Term                  = Factor OpcMulopFactors.
Factor                = Designator OpcRestOfMethCall | number | charConst | new | "(" Expr ")".
Designator            = ident opcRestOfDesignator.
OpcAddopTerms         = Addop Term OpcAddopTerms | ".".
OpcMulopFactors       = Mulop Factor OpcMulopFactors | ".".
Addop                 = "+" | "-".
Mulop                 = "*" | "/" | "%".
```

Cada **símbolo no terminal** está implementado por un **método** del parser. Los que participan
al reconocer una expresión aritmética como `3 * (2 + 4)` son:

| No terminal | Método en `Parser.cs` (línea) |
|-------------|-------------------------------|
| `Expr`      | `Expr(out Item item)` — **línea 1442**; `Expr(out Item item, TreeNode padre)` — **línea 1545** |
| `Term`      | `Term(out Item item)` — **línea 1836**; `Term(out Item item, TreeNode padre)` — **línea 1903** |
| `Factor`    | `Factor(out Item item)` — **línea 1728**; `Factor(out Item item, TreeNode padre)` — **línea 2006** |
| `Designator`| `Designator(out Item item)` — **línea 1643**; `Designator(out Item item, TreeNode padre)` — **línea 2135** |

> Nota: cada no terminal tiene **dos sobrecargas**. La primera (sin `TreeNode`) se usa cuando solo
> importa calcular el valor/tipo y generar código; la segunda (con `TreeNode padre`) además va
> construyendo el **árbol de derivación** colgando subárboles. Ambas comparten los mismos atributos
> y acciones semánticas; solo cambia que la segunda tiene el parámetro de contexto `padre`.

Los terminales/auxiliares que acompañan, aunque no son no terminales "de expresión" propiamente:
`Check(expected)` (reconocer un token), `Scan()` (avanzar de token), `Designator` (para `x`),
`ActPars` (argumentos), `Type`, `Tab`, `Code`, etc.

---

## 2. Atributos de salida y de entrada por método

### El registro de atributo que circula: `Item`

El valor que se "propaga" por los métodos de expresión es un objeto **`Item`** (clase definida en
`miCodGen.cs`, línea 734). Un `Item` modela los atributos de un operando durante la generación de
código y guarda:

- `kind` → `Const`, `Local`, `Static`, `Stack`, `Field`, `Elem`, `Arg`, `Meth`, `Cond`
- `type` → tipo (`Struct`: `int`, `char`, clase, arreglo…)
- `val`  → valor numérico (si `kind == Const`)
- `adr`  → offset (si es local/argumento)
- `sym`, `relop`, `tLabel`/`fLabel` → símbolo de la tabla, operador relacional, labels

### Tabla de atributos

| Método | **Atributos de salida** | **Atributos de entrada** | Concepto |
|--------|-------------------------|--------------------------|----------|
| `Expr(out Item item)` | `out Item item` | *(ninguno)* | `item` = **sintetizado**: valor+tipo de la expresión completa |
| `Expr(out Item item, TreeNode padre)` | `out Item item` | `TreeNode padre` | `padre` = **heredado (contexto)**: nodo del árbol donde colgar la derivación |
| `Term(out Item item)` | `out Item item` | *(ninguno)* | `item` = sintetizado: valor+tipo del término |
| `Term(out Item item, TreeNode padre)` | `out Item item` | `TreeNode padre` | `padre` = heredado (árbol) |
| `Factor(out Item item)` | `out Item item` | *(ninguno)* | `item` = sintetizado: valor+tipo del factor |
| `Factor(out Item item, TreeNode padre)` | `out Item item` | `TreeNode padre` | `padre` = heredado (árbol) |
| `Designator(out Item item)` | `out Item item` | *(ninguno)* | `item` = sintetizado: el `Item` del identificador |
| `Designator(out Item item, TreeNode padre)` | `out Item item` | `TreeNode padre` | `padre` = heredado (árbol) |

### Lectura conceptual

- **Atributo de salida (sintetizado) = `item`.** Es el "valor" de la subexpresión tal como lo usa su
  padre. Fluye **de abajo hacia arriba** (de las hojas a la raíz). Esto se ve directamente en la
  firma: `Term(out item)`, `Factor(out item)`, etc. — el `out` indica que el hijo **produce** el valor.

- **Atributo de entrada (heredado) = `padre`.** Es un nodo del árbol de derivación que el contexto
  baja hacia los hijos para que cuelguen su subárbol. Fluye **de arriba hacia abajo**. Es el único
  atributo de entrada que el código real del grupo usa para las expresiones.

> **Aclaración sobre el material:** en el PPT de la cátedra se muestra un atributo de entrada
> pedagógico `Expr<bool printHex>` (elige salida hex/decimal). Ese ejemplo es *ilustrativo* de cómo
> se vería una gramática de atributos con parámetro de entrada. El código de COMPI del grupo **no
> implementa** ese `printHex`: el único atributo de entrada efectivo en las expresiones es el
> `TreeNode padre` (para el árbol de derivación). Si se quiere reflejar la notación del PPT, se
> podría declara `Expr<TreeNode padre, out Item item>` → `padre` = entrada, `item` = salida.

---

## 3. Acciones semánticas por método

Las *acciones semánticas* en COMPI son las sentencias C# embebidas entre el reconocimiento de
producciones (el equivalente de los `(. ... .)` de la notación con atributos). Aparecen bajo
`(.../* produccion en pantalla */...)` y son el código que **calcula atributos** o **genera CIL**.

### 3.1 `Expr` — `Expr = OpcMinus Term OpcAddopTerms` (líneas 1442 / 1545)

1. **Signo unario (OpcMinus).** Si `la == Token.MINUS`: `Check(MINUS)` y se parsea `Term`.
   - Acción: verificar tipo `item.type == int` (si no, error *"Operando debe ser de tipo int"*).
   - Acción: si es constante → `item.val = -item.val` (negación a nivel de valor).
   - Acción: si es variable → `Code.Load(item); Code.il.Emit(Code.NEG)` (negación CIL).
2. **Repetir mientras haya `+`/`-` (OpcAddopTerms).** Para cada `Addop Term`:
   - `Scan()` (reconoce y avanza el operador); se fija `op = Code.ADD` o `Code.SUB`.
   - Acción: `Code.Load(item)` → cargar el acumulado en la pila.
   - `Term(out itemSig)` → parsear el término que sigue.
   - Acción: `Code.Load(itemSig)`; verificar que ambos sean `int`;
     `Code.il.Emit(op)` (**emite el CIL `add`/`sub`**);
     `nroDeInstrCorriente++` y `cil[nroDeInstrCorriente].accionInstr = add/sub` (registra la acción
     para el seguimiento/análisis del CIL).
   - El resultado queda en la pila (Item sintetizado de la suma/resta).

### 3.2 `Term` — `Term = Factor OpcMulopFactors` (líneas 1836 / 1903)

1. `Factor(out item)` → parsear el primer factor.
2. **Repetir mientras haya `*`/`/`/`%` (OpcMulopFactors).** Para cada `Mulop Factor`:
   - `Scan()`; `op = Code.MUL` / `Code.DIV` / `Code.REM`.
   - Acción: `Code.Load(item)`; `Factor(out itemSig)`; `Code.Load(itemSig)`;
     verificar tipo `int`; `Code.il.Emit(op)` (**CIL `mul`/`div`**);
     `nroDeInstrCorriente++`, `cil[nroDeInstrCorriente].accionInstr = mul/div`.
3. Si no hubo multiplicación/división, se cierra `OpcMulopFactors = "."` (no hay acción semántica
   numérica: el valor del `Factor` es el valor del `Term`).

### 3.3 `Factor` — `Factor = Designator OpcRestOfMethCall | number | charConst | new | "(" Expr ")"` (líneas 1728 / 2006)

- **`number`:** `Check(NUMBER)`.
  - Acción: `item = new Item(token.val)` → **crea el `Item` Const** con el valor numérico
    (`new Item(int)` y `kind = Const, type = int, val = valor`).
  - Acción: `Code.Load(item)` → **emite la carga de la constante** (CIL `ldc.i4 <valor>`).
- **`charConst`:** `item = new Item(token.val); item.type = charType`.
- **`ident`:** `Designator(out item)` → resuelve el nombre (variable/campo).
- **`"(" Expr ")"`:** `Check(LPAR)`, `Expr(out item)`, `Check(RPAR)`.
  - **No hay acción semántica adicional:** el paréntesis solo altera la precedencia; el Item
    sintetizado por la `Expr` interna sube tal cual. (Confirmado en el PT: *"No necesita acción sem.
    porque usa una sola var (val)"*).
- **`new`:** construye objetos (`Code.il.Emit(NEWOBJ)`) o arreglos (`Code.il.Emit(NEWARR)`).

### 3.4 `Designator` — `Designator = ident opcRestOfDesignator` (líneas 1643 / 2135)

- `Check(IDENT)`; `Symbol sym = Tab.Find(token.str)` (busca en la **tabla de símbolos**); si no está →
  error.
  - Acción: `item = new Item(sym)` → crea el `Item` a partir del símbolo (kind `Local`, `Static`,
    `Field`…) con su tipo.
- Si hay `.` o `[`: resuelve campo (`item.sym = symField; item.type = item.sym.type`) o índice
  (`Expr` del índice, `item.kind = Elem`).

---

## 4. Seguimiento a nivel de código de `x = 3 * (2 + 4)`

Tokens: `ident(x)` `assign(=)` `number(3)` `times(*)` `lpar(()` `number(2)` `plus(+)` `number(4)` `rpar())` `semi(;)`

### Paso a paso

| # | Método | Token / acción | Acción semántica / efecto | Valor sintetizado |
|---|--------|----------------|---------------------------|-------------------|
| 1 | `Statement` | `la = IDENT(x)` | — | — |
| 2 | `Designator(out itemIzq)` (l.2135) | `Check(IDENT)`; `Tab.Find("x")` | `itemIzq = new Item(sym)` → `kind=Local`, type=`int` | `itemIzq` (x) |
| 3 | `Statement` | `Check(ASSIGN)` (`=`) | entra caso `Token.ASSIGN` | — |
| 4 | `Expr(out itemDer)` (l.1545) | `la = NUMBER(3)` (no `MINUS`) → `Term` | — | — |
| 5 | `Term(out item)` (l.1903) | `Factor(out item)` | — | — |
| 6 | `Factor(out item)` (l.2006) | `Check(NUMBER)` → `number(3)` | `item = new Item(3)`; `Code.Load(item)` → `ldc.i4 3` | **item = 3** (Const, int) |
| 7 | `Term` | `la = TIMES(*)` → bucle `OpcMulopFactors` | `Scan()`; `op = MUL`; `Code.Load(item=3)` | 3 (pila) |
| 8 | `Factor(out itemSig)` (l.2006) | `la = LPAR` → `Check(LPAR)` | entra `"(" Expr ")"` | — |
| 9 | `Expr(out itemSig)` (l.1545) | `la = NUMBER(2)` → `Term` | — | — |
| 10 | `Term(out t2)` | `Factor` → `number(2)` | `item = new Item(2)`; `Code.Load` → `ldc.i4 2` | **2** |
| 11 | `Term(t2)` | `la = PLUS(+)` → bucle `OpcAddopTerms` | `Scan()`; `op = ADD`; `Code.Load(2)` | 2 (pila) |
| 12 | `Term(out t4)` | `Factor` → `number(4)` | `item = new Item(4)`; `Code.Load` → `ldc.i4 4` | **4** |
| 13 | `Term(t2)` | `Expr` interno | `Code.Load(4)`; check int; **`Code.il.Emit(ADD)`**; `cil[nro]=add` | **2 + 4 = 6** (pila) |
| 14 | `Factor(itemSig)` | `Check(RPAR)` | el Valor sube | **itemSig = 6** |
| 15 | `Term(item)` | `Expr` (afuera) | `Code.Load(6)`; check int; **`Code.il.Emit(MUL)`**; `cil[nro]=mul` | **3 * 6 = 18** (pila) |
| 16 | `Expr(itemDer)` | `la = SEMI` → sale del bucle | — | **itemDer = 18** (int) |
| 17 | `Statement` | — | **`Code.Assign(itemIzq, itemDer)`** → genera `stloc` para guardar 18 en `x` | x = 18 |
| 18 | `Statement` | `Check(SEMICOLON)` | fin de la asignación | — |

### Árbol de derivación y valores

```
              Expr                            (18)
                |
              Term                            (18)
             /    \
        Factor(3)  OpcMulopFactors
        (number)         |
                     Mulop('*') Factor -> Expr  (6)
                                      /       \
                                 Term(2)   OpcAddopTerms
                                           |         \
                                       Addop('+')   Term(4)
```

**Resultado final: `3 * (2 + 4) = 3 * 6 = 18`** — la precedencia es correcta porque el paréntesis
fuerza a la suma `2+4` dentro de un `Factor`, y la multiplicación se aplica sobre ese factor.

### Acciones semánticas que realmente generan CIL en el seguimiento

| Operación | Acción semántica | CIL emitido |
|-----------|------------------|-------------|
| `3`       | `item = new Item(3); Code.Load(item)` | `ldc.i4 3` |
| `2`       | `item = new Item(2); Code.Load(item)` | `ldc.i4 2` |
| `4`       | `item = new Item(4); Code.Load(item)` | `ldc.i4 4` |
| `2 + 4`   | `Code.il.Emit(ADD)` | `add` |
| `3 * 6`   | `Code.il.Emit(MUL)` | `mul` |
| guardar x | `Code.Assign(itemIzq, itemDer)` | `stloc x` |

---

## 5. Verificación de la herramienta (paso previo de la guía)

La guía pide *"Compile y ejecute el código para asegurarse que funciona bien"*. En este entorno
(Linux, sin `dotnet` ni `mono`, sin sudo para `apt`) la herramienta COMPI —una aplicación de
**Windows Forms** (`.NET Framework 2015`)— no se puede compilar ni ejecutar. El análisis de la
actividad se hizo directamente sobre el código fuente del parser (`Parser.cs`), que es la fuente
correcta para identificar los métodos, atributos y acciones semánticas. El paso de compilación queda
pendiente de un entorno Windows con Visual Studio / Mono.
