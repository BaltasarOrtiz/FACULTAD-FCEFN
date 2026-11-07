# Resolución — Práctico de Control de Error 2026 (Área Temática 4)

Teoría de la Información · Licenciatura en Ciencias de la Computación · 2026

> El enunciado original del práctico venía **encriptado** (Vigenère, con la clave escondida en un QR); este documento parte del texto ya descifrado. Todos los cálculos (paridades, divisiones polinómicas, pesos, síndromes, matrices con `G·Hᵀ = 0`, aritmética de GF(16)) fueron verificados por programa; acá se muestra el procedimiento a mano para poder reproducirlo en el examen.

## Convenciones usadas (las del Área 4 y las del apunte de control de error)

- **Cadena de bits ↔ polinomio ("mayores potencias a la derecha")**: `b₀ b₁ … bₙ₋₁` es `b₀ + b₁x + … + bₙ₋₁xⁿ⁻¹`. Para dividir a mano se escribe con la mayor potencia a la izquierda; al terminar se vuelve a la convención del enunciado.
- **Parámetros**: `n` longitud de palabra, `k` bits de información, `n−k` chequeadores, `2ᵏ` palabras válidas de `2ⁿ` posibles. **Redundancia (cátedra) = N/K**; cuanto más cerca de 1, mejor.
- **Capacidad**: `dmin ≥ 2t + 1` para corregir `t` errores; como detector puro detecta `dmin − 1`; corrige `t` y detecta `s` a la vez si `dmin ≥ t + s + 1`.

  | dmin | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
  |---|---|---|---|---|---|---|---|
  | Detector puro (`dmin−1`) | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
  | Corrector (`t`) | — | 1 | 1 (y detecta 2) | 2 | 2 (y detecta 3) | 3 | 3 (y detecta 4) |

- **Hamming (7,4)**: posiciones `1 … 7` = `C1 C2 I1 C3 I2 I3 I4` (chequeadores en las potencias de 2). `S1` mira las posiciones 1,3,5,7 · `S2` las 2,3,6,7 · `S3` las 4,5,6,7. El síndrome `(S3 S2 S1)` leído en binario **es la posición del error** (0 = sin error). "Bit menos significativo a la izquierda" significa que la posición 1 es el primer bit de la cadena. Hamming + bit de paridad (BP): `dmin = 4`.
- **Arreglos gráficos (diapositiva "Arreglos gráficos")**: paridad **par** por defecto. El **rectangular** lleva un bit de chequeo por fila y uno por columna; **sin bit esquina** `dmin = 3` (corrector simple) y **con bit esquina** `dmin = 4` (corrector simple y detector doble). El **triangular** de `P` filas de información tiene `P(P+1)/2` bits de información y `P+1` de chequeo sobre la diagonal.
- **ISBN-10 (base 11, prima)**: pesos `10, 9, …, 1`; válido ⇔ `Σ dígito·peso ≡ 0 (mod 11)`; el último símbolo puede ser `X = 10`. **Base 37** (0–9, A–Z, espacio): `0–9 → 0–9`, `A–Z → 10–35`, espacio `→ 36`.
- **Cíclicos**: `k = grado de h(x)`, `g(x) = (xⁿ + 1)/h(x)`; sistemático `V = xⁿ⁻ᵏ·i(x) + r(x)` con `r = xⁿ⁻ᵏ·i mod g`; `G = [P | Iₖ]`, `H = [Iₙ₋ₖ | Pᵀ]` con la fila `i` de `P` igual a `xⁿ⁻ᵏ⁺ⁱ mod g`; síndrome = resto de `R(x) ÷ g(x)`.
- **Reed–Solomon**: `q = 2ᵐ`, `n = q − 1`, bytes de chequeo `n − k = 2t`, ráfaga corregible con `L` códigos entrelazados `= t·L` bytes.

Los enunciados sin numerar o con numeración repetida en el original se señalan con ⚠. Las figuras 1 a 3 del práctico son imágenes (Fig. 1: código 2 entre 5 bits; Fig. 2: chequeo de paridad por palabras de `ABBC`; Fig. 3: tabla Reed–Solomon); su contenido se reproduce en el ejercicio correspondiente.

---

# PRÁCTICO CONTROL DE ERROR (Área Temática 4)

## Ejercicio 1

> 1.- Dado un byte de 7 bits cuántos errores puede detectar con paridad par y cuantos con paridad impar (Cantidad par e impar respectivamente de errores)?.

**Supuesto:** "byte de 7 bits" = 7 bits de información + 1 bit de paridad = **8 bits**. (Si los 7 bits ya incluyeran el BP, la conclusión sobre qué cantidades se detectan es la misma.)

Al invertir `e` bits de la palabra, la paridad de la cantidad de unos cambia **si y solo si `e` es impar**. Eso no depende de si la convención es par o impar: el código de paridad impar es el de paridad par con un bit complementado, y la distancia entre dos palabras válidas sigue siendo 2.

| Errores `e` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Patrones posibles $\binom{8}{e}$ | 8 | 28 | 56 | 70 | 56 | 28 | 8 | 1 |
| Paridad par | detecta | **no** | detecta | **no** | detecta | **no** | detecta | **no** |
| Paridad impar | detecta | **no** | detecta | **no** | detecta | **no** | detecta | **no** |

**Resultado:**

- Con paridad **par** y con paridad **impar** se detecta **cualquier cantidad impar de errores** (1, 3, 5, 7). Ninguna de las dos detecta una cantidad par.
- La cantidad de patrones de error con exactamente $e$ bits invertidos entre 8 posiciones es el número combinatorio

  $$\binom{8}{e} = \frac{8!}{e!\,(8-e)!}$$

  Patrones detectados (cantidad impar de errores):

  $$\binom{8}{1}+\binom{8}{3}+\binom{8}{5}+\binom{8}{7} = 8+56+56+8 = 128 = 2^{7}$$

  de los $2^8 - 1 = 255$ patrones no nulos. Quedan sin detectar $\binom{8}{2}+\binom{8}{4}+\binom{8}{6}+\binom{8}{8} = 28+70+28+1 = 127$ (los de cantidad par).
- `dmin = 2` ⇒ detecta `dmin − 1 = 1` error con garantía, **no corrige** (para corregir hace falta `dmin ≥ 3`).

⚠ La aclaración "(cantidad par e impar respectivamente)" no significa que la paridad impar detecte cantidad par: **ambas** detectan cantidad impar.

---

## Ejercicio 2

> 2.- Calcular la redundancia de la codificación dos entre cinco y tres entre siete. Fig1

La Fig. 1 muestra el código **2 (unos) entre 5 bits**: de las `2⁵ = 32` palabras posibles solo son válidas las que tienen exactamente dos unos, `C(5,2) = 10` (un dígito decimal por palabra, con pesos 6, 3, 2, 1, 0). El **3 entre 7** es análogo: palabras de 7 bits con exactamente tres unos.

Los bits de información equivalentes son `K = log₂(palabras válidas)`, y la redundancia de la cátedra es `N/K`:

| Código | `N` | Palabras válidas | `K = log₂(válidas)` | **Redundancia `N/K`** | Bits redundantes `N − K` |
|---|---|---|---|---|---|
| 2 entre 5 | 5 | `C(5,2) = 10` de 32 | 3,3219 | **1,505** | 1,678 |
| 3 entre 7 | 7 | `C(7,3) = 35` de 128 | 5,1293 | **1,365** | 1,871 |

Cálculo: `5 / log₂10 = 5 / 3,3219 = 1,505` y `7 / log₂35 = 7 / 5,1293 = 1,365`.

**Conclusión:** el 3 entre 7 es menos redundante (más eficiente: 1,365 contra 1,505). En ambos, un error simple cambia la cantidad de unos (de `w` a `w ± 1`), por lo que **se detecta**; dos errores que intercambian un 1 y un 0 mantienen la cantidad de unos y **no se detectan** (`dmin = 2`).

---

## Ejercicio 3

> 3.- Si p=0,001 y m=100
> a) ¿Cuál es la probabilidad de no error?
> b) y de n y de hasta n errores?

Canal con errores independientes: la cantidad de errores en un bloque de `m` bits es binomial.

### Inciso 3.a)

`P(0) = (1 − p)ᵐ = 0,999¹⁰⁰ = **0,9048**` (90,48 %). La probabilidad de que haya **al menos un error** es `1 − 0,9048 = 0,0952` (9,52 %).

### Inciso 3.b)

- **Exactamente `n` errores:** `P(n) = C(m,n) · pⁿ · (1−p)ᵐ⁻ⁿ`
- **Hasta `n` errores:** `P(≤n) = Σᵢ₌₀ⁿ C(m,i) · pⁱ · (1−p)ᵐ⁻ⁱ`

| `n` | `P(n)` (exactamente `n`) | `P(≤n)` (hasta `n`) |
|---|---|---|
| 0 | 0,904792 | 0,904792 |
| 1 | 0,090570 | 0,995362 |
| 2 | 0,004488 | 0,999850 |
| 3 | 0,000147 | 0,9999964 |
| 4 | 3,56·10⁻⁶ | 0,99999993 |

Ejemplo de cálculo para `n = 2`: `C(100,2) = 4950` ⇒ `4950 · 10⁻⁶ · 0,999⁹⁸ = 4950 · 10⁻⁶ · 0,9066 = 0,004488`.

**Lectura:** con p = 0,001 casi todo el error probable es de **un** bit (9,06 %); tres o más errores en el bloque tienen probabilidad `1 − 0,999850 = 1,5·10⁻⁴`. Por eso un código que corrija `t = 1` o `t = 2` alcanza para la mayoría de los casos.

---

## Ejercicio 4

> 4.- Calcular el chequeo de paridad por palabras para RACING e INDEPENDIENTE.fig2

**Método (Fig. 2):** cada carácter es una fila de 8 bits (ASCII con el bit más significativo en 0). Se agrega una fila de control cuyo bit `j` es el **bit de paridad par de la columna `j`**. Esa fila se transmite como un carácter más al final del mensaje. (Control: la fig. con `A B B C` da `00000010`.)

### RACING

| Carácter | ASCII | `b7 b6 b5 b4 b3 b2 b1 b0` |
|---|---|---|
| R | 82 | `0 1 0 1 0 0 1 0` |
| A | 65 | `0 1 0 0 0 0 0 1` |
| C | 67 | `0 1 0 0 0 0 1 1` |
| I | 73 | `0 1 0 0 1 0 0 1` |
| N | 78 | `0 1 0 0 1 1 1 0` |
| G | 71 | `0 1 0 0 0 1 1 1` |
| **Paridad de columna** | | **`0 0 0 1 0 0 0 0`** |

Columnas: `b6` tiene seis unos (par → 0), `b4` tiene uno (impar → 1), `b3` tiene dos, `b2` dos, `b1` cuatro, `b0` cuatro (todas pares → 0).

**Carácter de control:** `00010000` = `0x10` (16). Se transmite `RACING` + `0x10`.

### INDEPENDIENTE

| Carácter | ASCII | `b7 b6 b5 b4 b3 b2 b1 b0` |
|---|---|---|
| I | 73 | `0 1 0 0 1 0 0 1` |
| N | 78 | `0 1 0 0 1 1 1 0` |
| D | 68 | `0 1 0 0 0 1 0 0` |
| E | 69 | `0 1 0 0 0 1 0 1` |
| P | 80 | `0 1 0 1 0 0 0 0` |
| E | 69 | `0 1 0 0 0 1 0 1` |
| N | 78 | `0 1 0 0 1 1 1 0` |
| D | 68 | `0 1 0 0 0 1 0 0` |
| I | 73 | `0 1 0 0 1 0 0 1` |
| E | 69 | `0 1 0 0 0 1 0 1` |
| N | 78 | `0 1 0 0 1 1 1 0` |
| T | 84 | `0 1 0 1 0 1 0 0` |
| E | 69 | `0 1 0 0 0 1 0 1` |
| **Paridad de columna** | | **`0 1 0 0 1 0 1 0`** |

Cantidad de unos por columna: `b6` = 13 (impar → 1), `b4` = 2 (→ 0), `b3` = 5 (→ 1), `b2` = 10 (→ 0), `b1` = 3 (→ 1), `b0` = 6 (→ 0).

**Carácter de control:** `01001010` = `0x4A` (74) = la letra `J`. Se transmite `INDEPENDIENTE` + `J`.

---

## Ejercicio 5

> 5.- ¿Cuáles son las características de la codificación anterior?

La codificación del ejercicio 4 es un **chequeo de paridad longitudinal** (LRC, paridad por columnas): un carácter de control agregado al final del bloque.

| Característica | Detalle |
|---|---|
| **Redundancia** | Se agregan 8 bits a un bloque de `L` caracteres: `N/K = 8(L+1)/8L = (L+1)/L`. RACING: `7/6 = 1,167`; INDEPENDIENTE: `14/13 = 1,077`. **Mejora (tiende a 1) cuanto más largo es el bloque.** |
| **Detección** | Detecta **cualquier cantidad impar de errores en una misma columna**, y por lo tanto todo error simple. |
| **Ráfagas** | Una ráfaga de bits consecutivos invertidos afecta a las 8 columnas de manera cíclica: se detectan ráfagas de hasta **15 bits** (alguna columna queda con una cantidad impar). Una de **16** bits invierte dos bits en cada columna y es **indetectable** (verificado por simulación). Con un patrón cualquiera dentro de la ráfaga solo se garantiza hasta 8 bits. |
| **No detecta** | Dos errores en la **misma columna** (o cualquier cantidad par por columna), por ejemplo el mismo bit invertido en dos caracteres. |
| **Corrección** | **No corrige**: sabe en qué columna falló, pero no en qué fila. `dmin = 2`. |
| **Mejora posible** | Combinarlo con la paridad por carácter (por fila) arma un **arreglo rectangular**: el cruce de la fila y la columna que fallan localiza el bit y permite corregirlo (ver Ejercicios 2.1 a 2.4). |

---

## Ejercicio 6

> 6.- Chequear el siguiente código ISBN(10) 0-13165332-6; utilice Cryptool2
> Encontrar el dígito verificador 950-311192-"?". Hacerlo manualmente con Cryptool2

CrypTool 2 es una herramienta gráfica: acá se muestra el cálculo manual (el que se carga en la herramienta) y el resultado coincide con el calculado por programa.

### Inciso 6.a) Chequear `0-13165332-6`

Pesos `10, 9, …, 1`:

| Posición | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Dígito | 0 | 1 | 3 | 1 | 6 | 5 | 3 | 3 | 2 | 6 |
| Peso | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
| Dígito × peso | 0 | 9 | 24 | 7 | 36 | 25 | 12 | 9 | 4 | 6 |

**Regla:** un ISBN-10 `d₁ d₂ … d₁₀` es válido si

$$\sum_{i=1}^{10} d_i \cdot (11 - i) \equiv 0 \pmod{11}$$

es decir, si la suma de cada dígito por su peso es **múltiplo de 11**. El último dígito (`d₁₀`, peso 1) es el verificador: se eligió justamente para que la suma dé múltiplo de 11.

**Paso 1 · Multiplicar cada dígito por su peso** (fila "Dígito × peso" de la tabla):

`0·10 = 0`, `1·9 = 9`, `3·8 = 24`, `1·7 = 7`, `6·6 = 36`, `5·5 = 25`, `3·4 = 12`, `3·3 = 9`, `2·2 = 4`, `6·1 = 6`.

**Paso 2 · Sumar los productos:**

`Σ = 0 + 9 + 24 + 7 + 36 + 25 + 12 + 9 + 4 + 6 = 132`

**Paso 3 · Dividir por 11 y mirar el resto:**

`132 ÷ 11 = 12` exacto, porque `12 · 11 = 132`. Entonces `132 mod 11 = 0`, que se escribe `132 ≡ 0 (mod 11)`.

**Conclusión:** el resto es 0 ⇒ **el ISBN es válido**. Si hubiera dado un resto distinto de 0 (por ejemplo 4), el código tendría al menos un dígito mal.

*Qué pasaría con un error:* si por ejemplo el dígito 5 fuera `7` en lugar de `6`, el producto sería `7·6 = 42` en vez de `36`, la suma pasaría a `138` y `138 mod 11 = 6 ≠ 0`: el código se rechaza. Un solo dígito cambiado siempre altera la suma en `peso · diferencia`, que nunca es múltiplo de 11 (11 es primo y ni el peso ni la diferencia son múltiplos de 11).

### Inciso 6.b) Dígito verificador de `950-311192-?`

Los nueve dígitos conocidos son `9 5 0 3 1 1 1 9 2` con pesos `10 … 2`:

| Posición | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Dígito | 9 | 5 | 0 | 3 | 1 | 1 | 1 | 9 | 2 | `?` |
| Peso | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
| Dígito × peso | 90 | 45 | 0 | 21 | 6 | 5 | 4 | 27 | 4 | `?` |

`S = 90 + 45 + 0 + 21 + 6 + 5 + 4 + 27 + 4 = 202`; `202 = 18·11 + 4 ⇒ S ≡ 4`.

El verificador tiene peso 1: `4 + ? ≡ 0 (mod 11)` ⇒ `? = 11 − 4 = 7`.

**Resultado: `950-311192-7`**. Verificación: `202 + 7 = 209 = 19 · 11` ✓.

---

## Ejercicio 7

> 7.- En un código de base 37 codifique la siguiente secuencia: ABCDE-? 12345-?
> Compruebe que una permutación en la secuencia se detecta como error.

Valores: `A = 10, B = 11, C = 12, D = 13, E = 14, …, T = 29`; `0–9` valen su dígito. La base 37 es prima.

### Inciso 7.a) Versión de la diapositiva 9 (suma simple, sin pesos)

Se busca el símbolo `?` que deja la suma múltiplo de 37 (ejemplo de la cátedra: `AZ9-?`, `10 + 35 + 9 = 54`, `(54 + ?) mod 37 = 0 ⇒ ? = 20 = K`).

| Secuencia | Suma | `Suma mod 37` | `? = (37 − mod) mod 37` | Símbolo | Código |
|---|---|---|---|---|---|
| `ABCDE` | 10+11+12+13+14 = 60 | 23 | 14 | **E** | `ABCDE-E` |
| `12345` | 1+2+3+4+5 = 15 | 15 | 22 | **M** | `12345-M` |

Verificación: `60 + 14 = 74 = 2·37` ✓ y `15 + 22 = 37` ✓.

**Permutación con suma simple: NO se detecta.** `BACDE-E` suma `11 + 10 + 12 + 13 + 14 + 14 = 74 ≡ 0`: sigue siendo "válido". La suma no depende del orden.

### Inciso 7.b) Versión pesada (la que detecta permutaciones, como pide el enunciado)

Se multiplica cada símbolo por un peso que depende de su posición (`n+1, n, …, 2` para los datos y `1` para el verificador), igual que en el ISBN pero con base 37.

| Secuencia | Pesos | Productos | `S` | `S mod 37` | `?` | Código |
|---|---|---|---|---|---|---|
| `ABCDE` | 6 5 4 3 2 | 60, 55, 48, 39, 28 | 230 | 8 | `37 − 8 = 29` → **T** | `ABCDE-T` |
| `12345` | 6 5 4 3 2 | 6, 10, 12, 12, 10 | 50 | 13 | `37 − 13 = 24` → **O** | `12345-O` |

Verificación: `230 + 29 = 259 = 7·37` ✓ y `50 + 24 = 74 = 2·37` ✓.

### Permutación detectada

Se intercambian los dos primeros símbolos de `ABCDE-T`: `BACDE-T`:

`11·6 + 10·5 + 12·4 + 13·3 + 14·2 + 29·1 = 66 + 50 + 48 + 39 + 28 + 29 = 260`; `260 mod 37 = 1 ≠ 0` ⇒ **se detecta el error**.

**Por qué:** intercambiar dos símbolos adyacentes `a` y `b` con pesos `w+1` y `w` cambia la suma en `(w+1)a + wb − (w+1)b − wa = a − b`, que es distinto de cero módulo 37 cuando `a ≠ b`. Con pesos iguales (suma simple) ese cambio es 0.

**Conclusión:** para que la permutación se detecte hay que usar la versión pesada (7.b).

---

## Ejercicio 8

> 8.- A los códigos anteriores; ¿por qué se los denomina pesados? Verifique los códigos anteriores por este procedimiento.

**Por qué "pesados":** cada símbolo se **multiplica por un peso que depende de su posición** antes de sumar, y la condición de validez es `Σ dᵢ·wᵢ ≡ 0 (mod base)`. Con pesos distintos y no nulos:

- un **error simple** cambia la suma en `wᵢ·δ`, que no es múltiplo de la base (prima) si `δ ≠ 0` ⇒ se detecta;
- una **permutación** de símbolos distintos cambia la suma ⇒ se detecta (sin pesos no ocurriría);
- los pesos decrecientes `n, …, 1` equivalen a sumar las **sumas parciales** acumuladas.

**Verificación de los códigos obtenidos:**

| Código | Base | Pesos | `Σ dᵢ·wᵢ` | `mod` | ¿Válido? |
|---|---|---|---|---|---|
| ISBN `0-13165332-6` | 11 | 10 … 1 | 132 | `132 = 12·11` → 0 | ✓ |
| ISBN `950-311192-7` | 11 | 10 … 1 | `202 + 7 = 209` | `209 = 19·11` → 0 | ✓ |
| `ABCDE-T` | 37 | 6 … 1 | `230 + 29 = 259` | `259 = 7·37` → 0 | ✓ |
| `12345-O` | 37 | 6 … 1 | `50 + 24 = 74` | `74 = 2·37` → 0 | ✓ |

**Prueba de la permutación en un ISBN:** se intercambian los dígitos 8 y 9 de `0-13165332-6`, quedando `0-13165323-6`: `Σ = 0 + 9 + 24 + 7 + 36 + 25 + 12 + 2·3 + 3·2 + 6 = 131`; `131 = 11·11 + 10` ⇒ resto `10 ≠ 0 (mod 11)` ⇒ **se detecta** (la suma bajó en `w₈ − w₉ = 1`).

(La versión sin pesos, tomada en 7.a, cumple `Σ ≡ 0` pero no detecta la permutación: por eso se la distingue de los códigos pesados.)

---

## Ejercicio 9

> 9.- Investigue el motivo de la conveniencia para el uso de la base prima en los sistemas de codificación.

Para **decodificar** (hallar un dígito faltante o corregir una posición conocida) hay que resolver `w·x ≡ c (mod b)`, donde `w` es el peso de esa posición.

- Si la base `b` es **prima**, todo peso `w ≢ 0` tiene **inverso multiplicativo** en `ℤ_b` y la solución `x = c·w⁻¹` es **única**: no hay ambigüedad. Es lo que la cátedra resume como "la base prima garantiza unicidad en el proceso de decodificación".
- Si la base **no** es prima, pueden existir pesos sin inverso (`gcd(w, b) > 1`) y la ecuación puede tener **varias soluciones** o ninguna.

**Contraejemplo con base 10** (no prima): `2x ≡ 4 (mod 10)` tiene dos soluciones, `x = 2` y `x = 7`. Con base 11: `2x ≡ 4 (mod 11)` ⇒ `x = 4·2⁻¹ = 4·6 = 24 ≡ 2`, y nada más.

Inversos módulo 11: `1→1, 2→6, 3→4, 4→3, 5→9, 6→2, 7→8, 8→7, 9→5, 10→10`.

Por eso el ISBN-10 usa base 11 (necesita el símbolo `X = 10`) y el código alfanumérico usa base 37. (El ISBN-13 usa módulo 10 con pesos 1 y 3, que son coprimos con 10 y por eso invertibles.)

---

# PRÁCTICO N° 2

## Ejercicio 1

> 1.- Discutir la redundancia en las distintas variantes para códigos rectangulares con veinticuatro bits de información.

Con `K = 24` bits de información se arma un rectángulo de `a` filas por `b` columnas con `a·b = 24`. Chequeo: un bit por fila (`a`), uno por columna (`b`) y opcionalmente el **bit esquina** (1).

- Sin esquina: `N = 24 + a + b` ⇒ `R = N/K = 1 + 1/a + 1/b` (`dmin = 3`)
- Con esquina: `N = (a+1)(b+1)` ⇒ `R = (a+1)(b+1)/24` (`dmin = 4`)

| Rectángulo `a × b` | Chequeo sin esquina | `N` | `R` sin esquina | Chequeo con esquina | `N` | `R` con esquina |
|---|---|---|---|---|---|---|
| 1 × 24 | 25 | 49 | 2,0417 | 26 | 50 | 2,0833 |
| 2 × 12 | 14 | 38 | 1,5833 | 15 | 39 | 1,6250 |
| 3 × 8 | 11 | 35 | 1,4583 | 12 | 36 | 1,5000 |
| **4 × 6** | **10** | **34** | **1,4167** | **11** | **35** | **1,4583** |
| 6 × 4 | 10 | 34 | 1,4167 | 11 | 35 | 1,4583 |
| 8 × 3 | 11 | 35 | 1,4583 | 12 | 36 | 1,5000 |
| 12 × 2 | 14 | 38 | 1,5833 | 15 | 39 | 1,6250 |
| 24 × 1 | 25 | 49 | 2,0417 | 26 | 50 | 2,0833 |

**Discusión:**

- La redundancia **mínima** se obtiene con el rectángulo más **cuadrado** posible (4×6 o 6×4): `a + b` es mínimo cuando `a ≈ b`. Los extremos (1×24) son los peores y degeneran (con una sola fila, cada paridad de columna repite el bit).
- Todos los rectángulos tienen la misma distancia (3 sin esquina, 4 con esquina); lo que cambia es el costo: **el bit esquina cuesta 1 bit más y sube la distancia en 1**.
- Una disposición **triangular** de lado `n` contiene `n(n−1)/2` bits de información (21 con `n = 7`, 28 con `n = 8`): no hay una exacta para 24, habría que rellenar (`n = 8`, 4 posiciones sin usar, `R = 36/24 = 1,5`).

---

## Ejercicio 2

> 2.- Estudiar el uso del bit esquina para codificación con paridad par e impar.

**Qué es:** en el arreglo rectangular, el bit esquina es el **chequeo de los chequeos** (la paridad de la columna de bits de fila, que debería coincidir con la paridad de la fila de bits de columna). Protege a los propios bits de paridad y sube `dmin` de 3 a 4 (el arreglo corrige un error y además detecta dos).

**Con paridad PAR** (cada fila y cada columna con cantidad par de unos): el bit esquina es la paridad par de los bits de fila y **coincide siempre** con la paridad par de los bits de columna, porque ambas sumas son iguales a la suma de todos los bits de información. No hay ambigüedad.

**Con paridad IMPAR** (cada fila y cada columna con cantidad impar de unos): sea `T` la suma (mod 2) de todos los bits de información, `a` la cantidad de filas y `b` la de columnas.

- Por filas: bit esquina `= 1 ⊕ (suma de los bits de fila) = 1 ⊕ (a ⊕ T)`
- Por columnas: bit esquina `= 1 ⊕ (suma de los bits de columna) = 1 ⊕ (b ⊕ T)`

Ambos valores coinciden **solo si `a` y `b` tienen la misma paridad**. Si `a` es par y `b` impar (o al revés) **no existe un bit esquina que cumpla las dos condiciones a la vez**: el arreglo con paridad impar pierde la consistencia en la esquina (verificado exhaustivamente: con 2×3 o 3×4 falla el 100 % de los mensajes; con 2×2 o 3×3 no falla ninguno).

| Paridad | Condición para que el bit esquina sea consistente |
|---|---|
| Par | Siempre |
| Impar | `a ≡ b (mod 2)` |

Ejemplo concreto en el Ejercicio 3 (rectángulo 4×5 con paridad impar).

---

## Ejercicio 3

> 3.- Dado un rectángulo de cuatro por cinco codificar lo siguiente:
> 01001101011001010101

**Supuesto:** 4 filas × 5 columnas = 20 bits de información, cargados por filas (de izquierda a derecha, de arriba hacia abajo).

Mensaje por filas: `01001 | 10101 | 10010 | 10101`.

### Paridad par (la convención por defecto de la cátedra)

| | c1 | c2 | c3 | c4 | c5 | BP fila |
|---|---|---|---|---|---|---|
| f1 | 0 | 1 | 0 | 0 | 1 | **0** |
| f2 | 1 | 0 | 1 | 0 | 1 | **1** |
| f3 | 1 | 0 | 0 | 1 | 0 | **0** |
| f4 | 1 | 0 | 1 | 0 | 1 | **1** |
| BP col | **1** | **1** | **0** | **1** | **1** | **0** (esquina) |

Cada BP completa un número par de unos: fila 1 tiene dos unos → 0; fila 2 tiene tres → 1; fila 3 tiene dos → 0; fila 4 tiene tres → 1; columna 1 tiene tres → 1; columna 2 tiene uno → 1; columna 3 tiene dos → 0; columna 4 tiene uno → 1; columna 5 tiene tres → 1. La esquina (`0`) sale igual por filas (`0⊕1⊕0⊕1 = 0`) y por columnas (`1⊕1⊕0⊕1⊕1 = 0`).

Transmisión por filas (con esquina):

```
01001 0 | 10101 1 | 10010 0 | 10101 1 | 11011 0     (30 bits)
```

Sin esquina son 29 bits: `N/K = 29/20 = 1,45`; con esquina `30/20 = 1,50`.

### Paridad impar (para contraste con el Ejercicio 2)

| | c1 | c2 | c3 | c4 | c5 | BP fila |
|---|---|---|---|---|---|---|
| f1 | 0 | 1 | 0 | 0 | 1 | 1 |
| f2 | 1 | 0 | 1 | 0 | 1 | 0 |
| f3 | 1 | 0 | 0 | 1 | 0 | 1 |
| f4 | 1 | 0 | 1 | 0 | 1 | 0 |
| BP col | 0 | 0 | 1 | 0 | 0 | ? |

Como `a = 4` es par y `b = 5` es impar, el bit esquina por filas daría `1` y por columnas `0`: **no hay valor consistente**, como se anticipó en el Ejercicio 2.

---

## Ejercicio 4

> 4.- Deducir las redundancias de la codificación rectangular y triangular.

### Rectangular `a × b`

| Variante | Bits de chequeo | `N` | `R = N/K` |
|---|---|---|---|
| Sin esquina | `a + b` | `ab + a + b` | `1 + 1/a + 1/b` |
| Con esquina | `a + b + 1` | `(a+1)(b+1)` | `(a+1)(b+1)/ab` |
| Cuadrado `L × L` sin esquina | `2L` | `L² + 2L` | `(L²+2L)/L² = 1 + 2/L` |

Ejemplos de la cátedra: 3×4 → `R = 19/12`; 4×4 → `R = 24/16 = 1,5`; dos caracteres ASCII (2×8) → `R = 26/16`.

### Triangular de `P` filas de información

El arreglo tiene filas de `P, P−1, …, 1` bits de información; en la **diagonal** hay un bit de chequeo por fila (`P + 1` en total, la última fila tiene solo su chequeo). Cada bit de chequeo `i` es la paridad par de **su fila más su columna**, así que cada bit de información interviene en **dos** chequeos.

- Información: `K = P(P+1)/2`
- Chequeo: `P + 1`
- **`R = N/K = [P(P+1)/2 + (P+1)] / [P(P+1)/2] = 1 + 2/P`**

Ejemplo de la diapositiva: `P = 5` ⇒ `K = 15`, `N = 21`, `R = 21/15 = 1,4` (un 40 % de bits extra). En la notación de la tabla de la cátedra (lado `n = P+1`): información `n(n−1)/2` y chequeo `n`, es decir `R = (n+1)/(n−1)`.

| Lado `P` | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| Información `K` | 3 | 6 | 10 | 15 | 21 |
| Chequeo | 3 | 4 | 5 | 6 | 7 |
| `R = 1 + 2/P` | 2,000 | 1,667 | 1,500 | 1,400 | 1,333 |

**Distancia:** cada bit de información está en exactamente dos chequeos ⇒ una palabra de un solo bit de información pesa `1 + 2 = 3` (verificado por programa para `P = 5`) ⇒ `dmin = 3`, corrector simple, igual que el rectangular sin esquina. Dos chequeos que fallan identifican fila y columna del error.

---

## Ejercicio 5

> 5.- Codificar según Hamming los siguientes dígitos de información 1010
> ¿Cuál es la distancia de un código Hamming?
> y ¿cuál su capacidad de corrección y/o detección?

### Codificación

`I1 I2 I3 I4 = 1 0 1 0`; posiciones `C1 C2 I1 C3 I2 I3 I4`:

```
C1 = I1 ⊕ I2 ⊕ I4 = 1 ⊕ 0 ⊕ 0 = 1
C2 = I1 ⊕ I3 ⊕ I4 = 1 ⊕ 1 ⊕ 0 = 0
C3 = I2 ⊕ I3 ⊕ I4 = 0 ⊕ 1 ⊕ 0 = 1
```

| Posición | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Rol | C1 | C2 | I1 | C3 | I2 | I3 | I4 |
| Valor | **1** | **0** | 1 | **1** | 0 | 1 | 0 |

**Palabra de Hamming: `1 0 1 1 0 1 0`.**

Comprobación: `S1 = r1⊕r3⊕r5⊕r7 = 1⊕1⊕0⊕0 = 0`, `S2 = r2⊕r3⊕r6⊕r7 = 0⊕1⊕1⊕0 = 0`, `S3 = r4⊕r5⊕r6⊕r7 = 1⊕0⊕1⊕0 = 0` ⇒ síndrome `000` ✓.

### Distancia y capacidad

- **Distancia mínima del código Hamming: `dmin = 3`.**
- Capacidad: **corrige 1 error** (`3 ≥ 2·1 + 1`) **o** como detector puro detecta **2** (`dmin − 1`). No puede hacer las dos cosas a la vez: ante un doble error el síndrome apunta a una posición incorrecta y "corrige" mal.
- Es un código **perfecto** en el caso (7,4): `2³ = 8 = 1 + 7` (cada síndrome sirve a "sin error" o a una de las 7 posiciones).
- Agregando el bit de paridad total (BP) pasa a `dmin = 4`: corrige 1 **y** detecta 2 (ver Ejercicio 10).

---

## Ejercicio 6

> 6.- Si m es la cantidad de chequeadores. ¿Cuál es la probabilidad de que una secuencia aleatoria de 2ᵐ − 1 bits sea una palabra código para Hamming?.

Con `m` chequeadores el código de Hamming tiene longitud `n = 2ᵐ − 1` y `k = n − m` bits de información.

- Palabras válidas: `2ᵏ = 2ⁿ⁻ᵐ`
- Secuencias posibles de `n` bits: `2ⁿ`

**`P = 2ⁿ⁻ᵐ / 2ⁿ = 2⁻ᵐ = 1/2ᵐ`**

Ejemplos: `m = 3` (Hamming (7,4)) ⇒ `P = 16/128 = 1/8`; `m = 4` (Hamming (15,11)) ⇒ `P = 2048/32768 = 1/16`. Es la probabilidad de que el síndrome (de `m` bits) sea nulo para una secuencia al azar.

---

## Ejercicio 7

> 7.- Dado el siguiente mensaje, codificarlo en forma triangular: 101111001101001

Son 15 bits ⇒ `K = P(P+1)/2 = 15` ⇒ **`P = 5`** filas de información (la misma figura de la diapositiva, `N/K = 21/15`). Se cargan por filas: la fila 1 con 5 bits, la 2 con 4, la 3 con 3, la 4 con 2 y la 5 con 1.

```
fila 1:  1 0 1 1 1  #1
fila 2:  1 0 0 1    #2
fila 3:  1 0 1      #3
fila 4:  0 0        #4
fila 5:  1          #5
fila 6:             #6
```

El chequeo de la fila `i` va sobre la diagonal (columna `7 − i`) y es la **paridad par de su fila más su columna** (los bits de información que están en esa misma columna, más arriba).

| Chequeo | Bits de la fila | Bits de la columna | Total de unos | Bit |
|---|---|---|---|---|
| #1 (col 6) | `1 0 1 1 1` → 4 | ninguno | 4 | **0** |
| #2 (col 5) | `1 0 0 1` → 2 | `1` (fila 1, col 5) → 1 | 3 | **1** |
| #3 (col 4) | `1 0 1` → 2 | `1, 1` (filas 1 y 2) → 2 | 4 | **0** |
| #4 (col 3) | `0 0` → 0 | `1, 0, 1` (filas 1, 2, 3) → 2 | 2 | **0** |
| #5 (col 2) | `1` → 1 | `0, 0, 0, 0` (filas 1 a 4) → 0 | 1 | **1** |
| #6 (col 1) | ninguno → 0 | `1, 1, 1, 0, 1` (filas 1 a 5) → 4 | 4 | **0** |

**Arreglo codificado:**

```
1 0 1 1 1 | 0
1 0 0 1   | 1
1 0 1     | 0
0 0       | 0
1         | 1
          | 0
```

**Palabra transmitida (por filas, con su chequeo):** `101110 10011 1010 000 11 0` ⇒ `101110100111010000110` (21 bits).

(El método se contrastó con el ejemplo de la diapositiva: filas `01101 / 1111 / 100 / 11 / 1` dan los chequeos `1 1 0 0 0 0`, que coinciden con los de la figura.)

---

## Ejercicio 8

> 8.- Localizar un error la siguiente palabra Hamming 011100010111110 (bit menos significativo a la izquierda)

15 bits ⇒ Hamming (15,11): 4 chequeadores en las posiciones 1, 2, 4 y 8. La posición 1 es el primer bit (la izquierda).

| Posición | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bit | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 0 |

Cada síndrome suma (mod 2) las posiciones que tienen un 1 en el bit correspondiente de su número en binario:

| Síndrome | Posiciones controladas | Bits | Cantidad de unos | Valor |
|---|---|---|---|---|
| `S1` | 1, 3, 5, 7, 9, 11, 13, 15 | 0, 1, 0, 0, 0, 1, 1, 0 | 3 | **1** |
| `S2` | 2, 3, 6, 7, 10, 11, 14, 15 | 1, 1, 0, 0, 1, 1, 1, 0 | 5 | **1** |
| `S3` | 4, 5, 6, 7, 12, 13, 14, 15 | 1, 0, 0, 0, 1, 1, 1, 0 | 4 | **0** |
| `S4` | 8, 9, 10, 11, 12, 13, 14, 15 | 1, 0, 1, 1, 1, 1, 1, 0 | 6 | **0** |

`(S4 S3 S2 S1) = 0 0 1 1 = 3` ⇒ **el error está en la posición 3**.

(Equivalente: el `XOR` de las posiciones con un 1, `2⊕3⊕4⊕8⊕10⊕11⊕12⊕13⊕14 = 3`.)

**Corrección:** se invierte el bit 3: `011100010111110` → **`010100010111110`**. Comprobación: los cuatro síndromes dan `0000` ✓.

Información decodificada (posiciones 3, 5, 6, 7, 9, 10, …, 15): `0 0 0 0 0 1 1 1 1 1 0`.

---

## Ejercicio 9

> 9.- Corregir y decodificar el siguiente Hamming 1001111 (bit menos significativo a la izquierda)

Hamming (7,4): `C1 C2 I1 C3 I2 I3 I4` con la posición 1 a la izquierda.

| Posición | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Bit | 1 | 0 | 0 | 1 | 1 | 1 | 1 |

```
S1 = r1 ⊕ r3 ⊕ r5 ⊕ r7 = 1 ⊕ 0 ⊕ 1 ⊕ 1 = 1
S2 = r2 ⊕ r3 ⊕ r6 ⊕ r7 = 0 ⊕ 0 ⊕ 1 ⊕ 1 = 0
S3 = r4 ⊕ r5 ⊕ r6 ⊕ r7 = 1 ⊕ 1 ⊕ 1 ⊕ 1 = 0
```

`(S3 S2 S1) = 0 0 1 = 1` ⇒ **error en la posición 1**. Se invierte: `1001111` → **`0001111`** (síndrome `000` ✓).

**Decodificación:** la información está en las posiciones 3, 5, 6 y 7:

`I1 I2 I3 I4 = 0 1 1 1`.

Control: `C1 = I1⊕I2⊕I4 = 0⊕1⊕1 = 0` ✓, `C2 = I1⊕I3⊕I4 = 0⊕1⊕1 = 0` ✓, `C3 = I2⊕I3⊕I4 = 1⊕1⊕1 = 1` ✓.

---

## Ejercicio 10

> 10.- ¿Que sucede en la codificación de Hamming si se agrega un bit de paridad, varía o no la distancia?.

**Sí varía: `dmin` pasa de 3 a 4.**

Se agrega `BP` = paridad par de los 7 bits del Hamming, y se obtiene el código (8,4). Las 16 palabras del Hamming (7,4) tienen estos pesos y, con el BP, quedan así:

| Peso en Hamming (7,4) | Cantidad | BP agregado | Peso en (8,4) |
|---|---|---|---|
| 0 | 1 | 0 | 0 |
| 3 | 7 | **1** (peso impar) | **4** |
| 4 | 7 | 0 | 4 |
| 7 | 1 | **1** | 8 |

Todas las palabras con peso impar ganan un 1: el peso mínimo no nulo pasa de 3 a 4 ⇒ `dmin = 4`.

**Capacidad resultante:** `4 ≥ 1 + 2 + 1` ⇒ **corrige 1 error y a la vez detecta 2**. Con el síndrome de Hamming `S` y el control del BP:

| Síndrome `S` | ¿Falla el BP? | Conclusión |
|---|---|---|
| 0 | no | sin error |
| 0 | sí | error simple en el propio BP |
| ≠ 0 | sí (cantidad impar de errores) | error simple en la posición `S` ⇒ se corrige |
| ≠ 0 | no (cantidad par de errores) | doble error ⇒ se detecta, no se corrige (retransmisión) |

Esto evita lo que ocurre con Hamming solo: un doble error producía un síndrome distinto de 0 que apuntaba a una posición equivocada y se "corregía" mal (se introducía un tercer error).

---

## Ejercicio 11 ⚠ (código lineal, sin numerar en el original)

> *(El original no trae la numeración ni la oración que define el código; solo las tres ecuaciones y los incisos.)*
> U5 = I1 + I2 + I4
> U6 = I1 + I3 + I4
> U7 = I1 + I2 + I3
> a) Encontrar las matrices de generación y chequeo, y calcular la distancia mínima.
> b) Construir un arreglo estándar para el código.
> c) Cuál es la probabilidad de que se produzca un error y no se detecte?.

**Supuestos** (no están en el enunciado): la palabra es `U = (I1, I2, I3, I4, U5, U6, U7)`, es decir que `U1…U4` son los cuatro bits de información y `U5…U7` los chequeadores (código sistemático (7,4)); y para el inciso c) se usa el mismo canal del Ejercicio 3, `p = 0,001`.

### Inciso 11.a) Matrices `G` y `H` y distancia mínima

Cada fila de `G` es la palabra que corresponde a un bit de información en 1 y los demás en 0. `G = [I₄ | P]`:

```
        I1 I2 I3 I4 U5 U6 U7
G = [ 1  0  0  0  1  1  1 ]     (I1: interviene en U5, U6, U7)
    [ 0  1  0  0  1  0  1 ]     (I2: interviene en U5, U7)
    [ 0  0  1  0  0  1  1 ]     (I3: interviene en U6, U7)
    [ 0  0  0  1  1  1  0 ]     (I4: interviene en U5, U6)
```

Como `G = [I | P]`, la matriz chequeadora es `H = [Pᵀ | I₃]`:

```
H = [ 1  1  0  1  1  0  0 ]    (U5 = I1 + I2 + I4)
    [ 1  0  1  1  0  1  0 ]    (U6 = I1 + I3 + I4)
    [ 1  1  1  0  0  0  1 ]    (U7 = I1 + I2 + I3)
```

Verificación: `G·Hᵀ = 0` (las 12 combinaciones fila de `G` por fila de `H` dan 0 mod 2) ✓.

**Distancia mínima.** Como el código es lineal, `dmin` es el peso mínimo de una palabra no nula. Las columnas de `H` (síndromes de un error en cada posición) son `111, 101, 011, 110, 100, 010, 001`: las 7 columnas no nulas posibles, todas distintas ⇒ **es un código de Hamming (7,4)** y no hay palabras de peso 1 ni 2. Enumerando las 15 palabras no nulas: peso 3 (×7), peso 4 (×7) y peso 7 (×1).

**`dmin = 3`** ⇒ corrige 1 error (o detecta 2).

### Inciso 11.b) Arreglo estándar

`2ⁿ⁻ᵏ = 8` filas (clases laterales) × `2ᵏ = 16` columnas (palabras del código). La primera fila son las 16 palabras del código; la primera columna son los **líderes de clase**: el vector nulo y los 7 errores simples (cada uno con síndrome distinto, por eso la clase de cada uno es única). Las palabras del código están ordenadas por `I1 I2 I3 I4 = 0000, 0001, …, 1111`.

Columnas 1 a 8 (información `0000` … `0111`):

```
Síndrome  Líder     0000000 0001110 0010011 0011101 0100101 0101011 0110110 0111000
000       0000000   0000000 0001110 0010011 0011101 0100101 0101011 0110110 0111000
111       1000000   1000000 1001110 1010011 1011101 1100101 1101011 1110110 1111000
101       0100000   0100000 0101110 0110011 0111101 0000101 0001011 0010110 0011000
011       0010000   0010000 0011110 0000011 0001101 0110101 0111011 0100110 0101000
110       0001000   0001000 0000110 0011011 0010101 0101101 0100011 0111110 0110000
100       0000100   0000100 0001010 0010111 0011001 0100001 0101111 0110010 0111100
010       0000010   0000010 0001100 0010001 0011111 0100111 0101001 0110100 0111010
001       0000001   0000001 0001111 0010010 0011100 0100100 0101010 0110111 0111001
```

Columnas 9 a 16 (información `1000` … `1111`):

```
Síndrome  Líder     1000111 1001001 1010100 1011010 1100010 1101100 1110001 1111111
000       0000000   1000111 1001001 1010100 1011010 1100010 1101100 1110001 1111111
111       1000000   0000111 0001001 0010100 0011010 0100010 0101100 0110001 0111111
101       0100000   1100111 1101001 1110100 1111010 1000010 1001100 1010001 1011111
011       0010000   1010111 1011001 1000100 1001010 1110010 1111100 1100001 1101111
110       0001000   1001111 1000001 1011100 1010010 1101010 1100100 1111001 1110111
100       0000100   1000011 1001101 1010000 1011110 1100110 1101000 1110101 1111011
010       0000010   1000101 1001011 1010110 1011000 1100000 1101110 1110011 1111101
001       0000001   1000110 1001000 1010101 1011011 1100011 1101101 1110000 1111110
```

Cada fila es una clase lateral: todas sus palabras tienen el mismo síndrome. **Uso:** se busca la palabra recibida en el arreglo; la palabra del código que encabeza su columna es la decodificada y el líder de su fila es el error. Los 128 vectores de 7 bits quedan cubiertos exactamente una vez (`8 × 16 = 128`): es un código perfecto.

### Inciso 11.c) Probabilidad de error no detectado

Un error **no se detecta** cuando el patrón de error es él mismo una **palabra no nula del código** (la suma da otra palabra válida). Con la distribución de pesos `A₃ = 7`, `A₄ = 7`, `A₇ = 1`:

`P(error no detectado) = Σ Aᵢ · pⁱ · (1−p)⁷⁻ⁱ = 7p³(1−p)⁴ + 7p⁴(1−p)³ + p⁷`

Con `p = 0,001`:

- `7 · 10⁻⁹ · 0,996 = 6,972·10⁻⁹`
- `7 · 10⁻¹² · 0,997 = 6,98·10⁻¹²`
- `p⁷ = 10⁻²¹`

**`P_nd ≈ 6,98·10⁻⁹`** (menos de una vez cada 10⁸ palabras). Comparación: la probabilidad de que haya *algún* error en la palabra es `1 − 0,999⁷ = 6,98·10⁻³`; el código detecta prácticamente todos. Si en cambio se lo usa como **corrector**, la probabilidad de que el error no se corrija (dos o más errores) es `1 − 0,999⁷ − 7·0,001·0,999⁶ = 2,09·10⁻⁵`.

---

## Ejercicio 12

> 12.- Sea g(x) = 1 + x + x² + x⁴ + x⁵ + x⁸ + x¹⁰ polinomio generador de un código cíclico (15,5).
> a) Encontrar el polinomio de paridad h(x) de este código
> b) Encontrar el polinomio código para el mensaje: m(x) = 1 + x + x⁴; en forma sistemática.
> c) Encontrar las matrices generadora y de chequeo.
> d) ¿Es v(x) = 1 + x + x⁵ + x⁸ + x¹² + x¹⁴ un polinomio código? Si no lo es, encuentre el síndrome.
> e) Cuál es la capacidad de detección y corrección del código.

`n = 15`, `k = 5` (grado de `g` = `n − k` = 10 ✓). En bits (mayores potencias a la derecha): `g = 1 1 1 0 1 1 0 0 1 0 1`.

### Inciso 12.a) `h(x) = (x¹⁵ + 1) / g(x)`

División con la mayor potencia a la izquierda (16 bits, de `x¹⁵` a `x⁰`):

| Paso | Resto parcial | Término del cociente | Divisor desplazado | Resto nuevo |
|---|---|---|---|---|
| 1 | `1000000000000001` | `x⁵` | `1010011011100000` | `0010011011100001` |
| 2 | `0010011011100001` | `x³` | `0010100110111000` | `0000111101011001` |
| 3 | `0000111101011001` | `x` | `0000101001101110` | `0000010100110111` |
| 4 | `0000010100110111` | `1` | `0000010100110111` | `0000000000000000` |

Resto 0 ✓ (`g` divide a `x¹⁵ + 1`). El cociente es

**`h(x) = x⁵ + x³ + x + 1`** → en bits (mayores potencias a la derecha) `1 1 0 1 0 1`. Su grado 5 confirma `k = 5`.

### Inciso 12.b) Palabra código sistemática de `m(x) = 1 + x + x⁴`

`V(x) = x¹⁰·m(x) + r(x)`, con `r(x) = x¹⁰·m(x) mod g(x)`.

`x¹⁰·m(x) = x¹⁰ + x¹¹ + x¹⁴` → `100110000000000` (mayor potencia a la izquierda):

| Paso | Resto parcial | Término del cociente | Divisor desplazado | Resto nuevo |
|---|---|---|---|---|
| 1 | `100110000000000` | `x⁴` | `101001101110000` | `001111101110000` |
| 2 | `001111101110000` | `x²` | `001010011011100` | `000101110101100` |
| 3 | `000101110101100` | `x` | `000101001101110` | `000000111000010` |

Resto: `000000111000010` ⇒ **`r(x) = x + x⁶ + x⁷ + x⁸`**.

**`V(x) = x + x⁶ + x⁷ + x⁸ + x¹⁰ + x¹¹ + x¹⁴`**

En bits (mayores potencias a la derecha): `0 1 0 0 0 0 1 1 1 0 | 1 1 0 0 1` (chequeadores en las posiciones 0–9, información `1 1 0 0 1` en las 10–14, que es `m`).

(Forma no sistemática, por comparación: `V = m·g = 1 + x³ + x⁵ + x¹⁰ + x¹¹ + x¹² + x¹⁴`.)

### Inciso 12.c) Matrices `G` y `H`

Las filas de `P` son `x¹⁰⁺ⁱ mod g`:

| Bit de información | `x¹⁰⁺ⁱ mod g(x)` | Fila de `P` (10 bits, potencias crecientes) |
|---|---|---|
| `x¹⁰` | `1 + x + x² + x⁴ + x⁵ + x⁸` | `1 1 1 0 1 1 0 0 1 0` |
| `x¹¹` | `x + x² + x³ + x⁵ + x⁶ + x⁹` | `0 1 1 1 0 1 1 0 0 1` |
| `x¹²` | `1 + x + x³ + x⁵ + x⁶ + x⁷ + x⁸` | `1 1 0 1 0 1 1 1 1 0` |
| `x¹³` | `x + x² + x⁴ + x⁶ + x⁷ + x⁸ + x⁹` | `0 1 1 0 1 0 1 1 1 1` |
| `x¹⁴` | `1 + x + x³ + x⁴ + x⁷ + x⁹` | `1 1 0 1 1 0 0 1 0 1` |

**`G = [P | I₅]` (5 × 15):**

```
1 1 1 0 1 1 0 0 1 0 | 1 0 0 0 0
0 1 1 1 0 1 1 0 0 1 | 0 1 0 0 0
1 1 0 1 0 1 1 1 1 0 | 0 0 1 0 0
0 1 1 0 1 0 1 1 1 1 | 0 0 0 1 0
1 1 0 1 1 0 0 1 0 1 | 0 0 0 0 1
```

**`H = [I₁₀ | Pᵀ]` (10 × 15):**

```
1 0 0 0 0 0 0 0 0 0 | 1 0 1 0 1
0 1 0 0 0 0 0 0 0 0 | 1 1 1 1 1
0 0 1 0 0 0 0 0 0 0 | 1 1 0 1 0
0 0 0 1 0 0 0 0 0 0 | 0 1 1 0 1
0 0 0 0 1 0 0 0 0 0 | 1 0 0 1 1
0 0 0 0 0 1 0 0 0 0 | 1 1 1 0 0
0 0 0 0 0 0 1 0 0 0 | 0 1 1 1 0
0 0 0 0 0 0 0 1 0 0 | 0 0 1 1 1
0 0 0 0 0 0 0 0 1 0 | 1 0 1 1 0
0 0 0 0 0 0 0 0 0 1 | 0 1 0 1 1
```

Verificación: `G·Hᵀ = 0` (50 productos fila por fila, todos 0 mod 2) ✓.

Cada chequeador como combinación de los bits de información (`i₀ … i₄` = posiciones 10 a 14):

| `c0` | `c1` | `c2` | `c3` | `c4` |
|---|---|---|---|---|
| `i0⊕i2⊕i4` | `i0⊕i1⊕i2⊕i3⊕i4` | `i0⊕i1⊕i3` | `i1⊕i2⊕i4` | `i0⊕i3⊕i4` |

| `c5` | `c6` | `c7` | `c8` | `c9` |
|---|---|---|---|---|
| `i0⊕i1⊕i2` | `i1⊕i2⊕i3` | `i2⊕i3⊕i4` | `i0⊕i2⊕i3` | `i1⊕i3⊕i4` |

### Inciso 12.d) ¿Es `v(x) = 1 + x + x⁵ + x⁸ + x¹² + x¹⁴` palabra código?

`v(x)` es múltiplo de `g(x)` si y solo si el resto `v(x) mod g(x)` es 0. En bits (mayor potencia a la izquierda): `v = 101000100100011`.

| Paso | Resto parcial | Término del cociente | Divisor desplazado | Resto nuevo |
|---|---|---|---|---|
| 1 | `101000100100011` | `x⁴` | `101001101110000` | `000001001010011` |

Resto: `000001001010011` ⇒ **`1 + x + x⁴ + x⁶ + x⁹`** (en bits `1 1 0 0 1 0 1 0 0 1`), distinto de cero.

**`v(x)` NO es palabra código.** Su **síndrome** es `S(x) = 1 + x + x⁴ + x⁶ + x⁹`.

**Lectura del síndrome:** para posiciones `i < 10` el síndrome de un error simple es `xⁱ` (una sola potencia); para `i ≥ 10` es la fila de `P` correspondiente (tabla de 12.c). El síndrome obtenido no coincide con ninguno de esos ni con el `XOR` de dos o tres de ellos (se comprobaron los 575 patrones de hasta 3 errores: todos tienen síndromes distintos y ninguno es este), de modo que `v(x)` **tiene más de 3 errores**: se detecta pero **no se puede corregir** (las dos palabras del código más cercanas están ambas a distancia 4). Hay que pedir retransmisión.

### Inciso 12.e) Capacidad del código

Enumerando las `2⁵ − 1 = 31` palabras no nulas `V = m·g`:

| Peso | 7 | 8 | 15 |
|---|---|---|---|
| Cantidad | 15 | 15 | 1 |

(`g` tiene 7 términos y es una de las palabras de peso 7; el peso 15 es la palabra de todos unos, `V = (1 + x³ + x⁴)·g(x)`.)

**`dmin = 7`**, por lo tanto:

- **Corrige `t = ⌊(7−1)/2⌋ = 3` errores.**
- Como detector puro **detecta `dmin − 1 = 6` errores**.
- Redundancia `N/K = 15/5 = 3`.
- Cota de Hamming: `1 + 15 + 105 + 455 = 576 ≤ 2¹⁰ = 1024` ✓ (no es perfecto: sobran 448 síndromes que detectan ≥ 4 errores).
- Con `L` palabras entrelazadas corrige ráfagas de `t·L = 3L` bits.

---

## Ejercicio 13 ⚠ (Reed–Solomon; en el original está numerado "11)")

> 11) Códigos Reed-Solomon.
> a) Completar la siguiente tabla fig 3
> b) (Lo deben resolver los grupos que deben hacer el software) Dado el polinomio f(x)= 1 + x + x⁴ generador de un GF(16) Implementar un corrector de hasta tres bytes (6 bytes chequeadores) (9 bytes de información).
> a) Obtener la palabra válida para el I(x)= α, α⁴, α¹⁵, α¹⁰, α⁴, α², α, α³, α (mayores potencias de x hacia la derecha)
> b) Generar tres errores y corregir.

### Inciso 13.a) Tabla Reed–Solomon (Fig. 3)

Reglas: `q = 2ᵐ` (tamaño del campo = dimensión), `m` = bits por byte = grado del polinomio generador del campo; `n = q − 1`; `n − k = 2t`; ráfaga con 75 códigos entrelazados `= t·75` bytes.

La Fig. 3 trae dos datos por fila (en negrita lo dado):

| Capacidad de corrección `t` (bytes) | Bits por byte `m` | Longitud `n` (bytes) | Dimensión del campo `Q = 2ᵐ` | Grado del pol. generador del campo | Bytes de información `K` | Bytes de chequeo `n−k` | Ráfaga corregible con 75 códigos |
|---|---|---|---|---|---|---|---|
| **20** | **10** | 1023 | 1024 | 10 | 983 | 40 | 1500 bytes |
| **40** | 8 | **255** | 256 | 8 | 175 | 80 | 3000 bytes |
| 12 | 6 | 63 | **64** | 6 | 39 | **24** | 900 bytes |
| 27 | 8 | 255 | 256 | **8** | **201** | 54 | 2025 bytes |

Procedimiento de cada fila:

- **Fila 1** (`t = 20`, `m = 10`): `Q = 2¹⁰ = 1024`, `n = 1023`, `n − k = 2t = 40`, `k = 1023 − 40 = 983`, ráfaga `20 · 75 = 1500`.
- **Fila 2** (`t = 40`, `n = 255`): `255 = 2ᵐ − 1 ⇒ m = 8`, `Q = 256`, `n − k = 80`, `k = 255 − 80 = 175`, ráfaga `40 · 75 = 3000`.
- **Fila 3** (`Q = 64`, 24 chequeo): `64 = 2⁶ ⇒ m = 6`, `n = 63`, `n − k = 24 ⇒ t = 12`, `k = 63 − 24 = 39`, ráfaga `12 · 75 = 900`.
- **Fila 4** (grado del campo 8, `K = 201`): `m = 8`, `Q = 256`, `n = 255`, `n − k = 255 − 201 = 54 ⇒ t = 27`, ráfaga `27 · 75 = 2025`.

Las ráfagas están en **bytes**; en bits son `m` veces más (por ejemplo, la fila 1: 1500 · 10 = 15 000 bits).

### Inciso 13.b) Corrector de hasta 3 bytes en GF(16)

Es el código **RS(15, 9)**: `m = 4` bits por byte, `n = 15`, `k = 9`, `n − k = 6 = 2t ⇒ t = 3`. La parte de software se implementó en Python (Anexo, `rs_gf16.py`); a continuación el procedimiento a mano y los resultados.

#### Campo GF(16), `f(x) = 1 + x + x⁴` (`α⁴ = α + 1`)

| Potencia | Vector `(b₀ b₁ b₂ b₃)` | Potencia | Vector |
|---|---|---|---|
| `α⁰ = 1` | `1000` | `α⁸ = 1 + α²` | `1010` |
| `α¹` | `0100` | `α⁹ = α + α³` | `0101` |
| `α²` | `0010` | `α¹⁰ = 1 + α + α²` | `1110` |
| `α³` | `0001` | `α¹¹ = α + α² + α³` | `0111` |
| `α⁴ = 1 + α` | `1100` | `α¹² = 1 + α + α² + α³` | `1111` |
| `α⁵ = α + α²` | `0110` | `α¹³ = 1 + α² + α³` | `1011` |
| `α⁶ = α² + α³` | `0011` | `α¹⁴ = 1 + α³` | `1001` |
| `α⁷ = 1 + α + α³` | `1101` | `α¹⁵ = α⁰ = 1` | `1000` |

#### Polinomio generador `g(x) = (x + α)(x + α²)(x + α³)(x + α⁴)(x + α⁵)(x + α⁶)`

(Convención habitual: raíces consecutivas `α¹ … α²ᵗ`; el enunciado no fija el exponente inicial.) Productos sucesivos:

| Factores | Producto |
|---|---|
| `(x+α)` | `α + x` |
| `· (x+α²)` | `α³ + α⁵x + x²` |
| `· (x+α³)` | `α⁶ + α¹³x + α¹¹x² + x³` |
| `· (x+α⁴)` | `α¹⁰ + α³x + α⁶x² + α¹³x³ + x⁴` |
| `· (x+α⁵)` | `1 + αx + α⁵x² + α²x³ + α⁷x⁴ + x⁵` |
| `· (x+α⁶)` | **`α⁶ + α⁹x + α⁶x² + α⁴x³ + α¹⁴x⁴ + α¹⁰x⁵ + x⁶`** |

(En vectores: `g = [α⁶ α⁹ α⁶ α⁴ α¹⁴ α¹⁰ 1]`, o en decimal `12 10 12 3 9 7 1` de grado menor a mayor.) Si la cátedra usara otro exponente inicial (`α⁰ … α⁵`), cambian `g` y la palabra válida, pero el procedimiento es idéntico.

#### Inciso b.a) Palabra válida para `I(x)`

`I(x) = α + α⁴x + α¹⁵x² + α¹⁰x³ + α⁴x⁴ + α²x⁵ + αx⁶ + α³x⁷ + αx⁸` (con `α¹⁵ = 1`).

Codificación sistemática: `V(x) = x⁶·I(x) + r(x)`, `r(x) = x⁶·I(x) mod g(x)`.

Dividiendo `x⁶·I(x)` por `g(x)` en GF(16) se obtiene el resto

**`r(x) = α¹⁴ + α⁹x + x² + α²x³ + α³x⁴ + α⁶x⁵`**

y la palabra válida (chequeadores en las posiciones 0–5, información en las 6–14):

**`V = [ α¹⁴, α⁹, 1, α², α³, α⁶ | α, α⁴, 1, α¹⁰, α⁴, α², α, α³, α ]`**

Verificación: `V(α¹) = V(α²) = … = V(α⁶) = 0` (las seis raíces de `g`) ✓ — es decir, todos los síndromes de `V` son nulos.

#### Inciso b.b) Generar tres errores y corregir

Se eligen tres errores arbitrarios: `e(x) = α⁵x + α¹¹x⁸ + α²x¹³` (posiciones 1, 8 y 13, con magnitudes `α⁵`, `α¹¹`, `α²`; mezcla de bytes de chequeo y de información).

**Palabra recibida** `R = V + e`:

`R = [ α¹⁴, α⁶, 1, α², α³, α⁶ | α, α⁴, α¹², α¹⁰, α⁴, α², α, α⁶, α ]`

(En las posiciones 1, 8 y 13: `α⁹ + α⁵ = α⁶`, `1 + α¹¹ = α¹²`, `α³ + α² = α⁶`.)

**Paso 1 · Síndromes** `Sⱼ = R(αʲ)`, `j = 1 … 6`:

| `S₁` | `S₂` | `S₃` | `S₄` | `S₅` | `S₆` |
|---|---|---|---|---|---|
| `α¹¹` | `α¹⁴` | `α¹³` | `α¹³` | `0` | `1` |

No son todos nulos ⇒ hay errores.

**Paso 2 · Polinomio localizador** `Λ(x) = 1 + Λ₁x + Λ₂x² + Λ₃x³` (método de Peterson–Gorenstein–Zierler). Para `t = 3` se resuelve:

```
[ S1  S2  S3 ] [ Λ3 ]   [ S4 ]        [ α¹¹ α¹⁴ α¹³ ] [ Λ3 ]   [ α¹³ ]
[ S2  S3  S4 ] [ Λ2 ] = [ S5 ]   →    [ α¹⁴ α¹³ α¹³ ] [ Λ2 ] = [ 0   ]
[ S3  S4  S5 ] [ Λ1 ]   [ S6 ]        [ α¹³ α¹³ 0   ] [ Λ1 ]   [ 1   ]
```

El determinante de la matriz es `1 ≠ 0` ⇒ se produjeron **3 errores** (si fuera nulo se probaría con la matriz 2×2 y luego con 1×1). La solución (eliminación de Gauss-Jordan en GF(16)) es:

`Λ₃ = α⁷`, `Λ₂ = α¹²`, `Λ₁ = α⁹` ⇒ **`Λ(x) = 1 + α⁹x + α¹²x² + α⁷x³`**

**Paso 3 · Posiciones** (búsqueda de Chien): las raíces de `Λ(x)` son `α⁻ⁱ` para cada posición `i` con error. Se evalúa `Λ(α⁻ⁱ)` para `i = 0 … 14` y se anula para:

**`i = 1, 8, 13`** ✓ (coinciden con las posiciones inyectadas).

**Paso 4 · Magnitudes** `Yₗ`: con `Xₗ = αⁱˡ`, se resuelve `Sⱼ = Σ Yₗ·Xₗʲ` para `j = 1, 2, 3`:

```
S1 = Y1·α¹  + Y2·α⁸  + Y3·α¹³
S2 = Y1·α²  + Y2·α¹⁶ + Y3·α²⁶
S3 = Y1·α³  + Y2·α²⁴ + Y3·α³⁹
```

Resultado: **`Y₁ = α⁵`, `Y₂ = α¹¹`, `Y₃ = α²`**, que son exactamente las magnitudes introducidas.

**Paso 5 · Corrección** `C = R + e'`: se suma cada magnitud a su posición:

```
posición  1:  α⁶  + α⁵  = α⁹
posición  8:  α¹² + α¹¹ = 1
posición 13:  α⁶  + α²  = α³
```

`C = V` ✓ — se recuperó la palabra original (verificado: `C(αʲ) = 0` para `j = 1 … 6` y coincide símbolo a símbolo con `V`). La información decodificada es `α, α⁴, 1, α¹⁰, α⁴, α², α, α³, α`.

**Capacidad:** con `t = 3` corrige hasta 3 bytes erróneos, sin importar cuántos bits tenga dañados cada uno: por eso Reed–Solomon es muy eficaz contra ráfagas (cada byte con un error de 1 a 4 bits cuenta como un solo error de símbolo). Con 4 errores el sistema ya no puede corregir (posiblemente detecta o corrige mal).

---

## Anexo — Software del inciso 13.b (`rs_gf16.py`)

Aritmética de GF(16) por tablas de logaritmos, generador, codificación sistemática y decodificación con síndromes + PGZ + Chien. Al ejecutarlo comprueba con `assert` que la palabra codificada anula las seis raíces y que la corrección recupera `V`.

```python
"""Reed-Solomon (15, 9) sobre GF(16), f(x) = 1 + x + x^4, corrector de 3 bytes.
Convencion: raices alfa^1..alfa^6, byte i = coeficiente de x^i (mayores potencias a la derecha)."""

EXP, LOG = [0] * 30, {}
x = 1
for i in range(15):
    EXP[i], LOG[x] = x, i
    x <<= 1
    if x & 16:
        x ^= 0b10011                      # alfa^4 = alfa + 1
for i in range(15, 30):
    EXP[i] = EXP[i - 15]

def mul(a, b): return 0 if 0 in (a, b) else EXP[LOG[a] + LOG[b]]
def inv(a): return EXP[(15 - LOG[a]) % 15]
def pw(a, e): return 0 if a == 0 else EXP[(LOG[a] * e) % 15]
def A(e): return EXP[e % 15]                       # alfa^e
def name(a): return "0" if a == 0 else f"a^{LOG[a]}"

def peval(p, x0):                                  # Horner, p = [c0, c1, ...]
    r = 0
    for c in reversed(p): r = mul(r, x0) ^ c
    return r

def pmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b): r[i + j] ^= mul(u, v)
    return r

def pmod(a, g):
    a = a[:]
    while len(a) >= len(g):
        c = a.pop()
        if c:
            f, s = mul(c, inv(g[-1])), len(a) - (len(g) - 1)
            for i, v in enumerate(g[:-1]): a[s + i] ^= mul(f, v)
    return a + [0] * (len(g) - 1 - len(a))

def solve(M, b):                                   # Gauss-Jordan en GF(16)
    n = len(M); a = [row[:] + [v] for row, v in zip(M, b)]
    for c in range(n):
        p = next(r for r in range(c, n) if a[r][c])
        a[c], a[p] = a[p], a[c]
        iv = inv(a[c][c]); a[c] = [mul(iv, v) for v in a[c]]
        for r in range(n):
            if r != c and a[r][c]:
                f = a[r][c]; a[r] = [u ^ mul(f, v) for u, v in zip(a[r], a[c])]
    return [a[r][n] for r in range(n)]

# generador g(x) = (x + a)(x + a^2)...(x + a^6)
g = [1]
for j in range(1, 7): g = pmul(g, [A(j), 1])

# a) palabra valida (sistematica): V = x^6 I(x) + (x^6 I(x) mod g)
I = [A(e) for e in (1, 4, 15, 10, 4, 2, 1, 3, 1)]
V = pmod([0] * 6 + I, g) + I
assert all(peval(V, A(j)) == 0 for j in range(1, 7))

# b) tres errores: posicion -> valor
R = V[:]
for pos, val in {1: A(5), 8: A(11), 13: A(2)}.items(): R[pos] ^= val

S = [peval(R, A(j)) for j in range(1, 7)]          # sindromes S1..S6
L3, L2, L1 = solve([[S[0], S[1], S[2]], [S[1], S[2], S[3]], [S[2], S[3], S[4]]], S[3:6])
Lam = [1, L1, L2, L3]                              # localizador
pos = [i for i in range(15) if peval(Lam, A(-i)) == 0]          # Chien
Y = solve([[pw(A(p), j) for p in pos] for j in (1, 2, 3)], S[:3])  # magnitudes
C = R[:]
for p, y in zip(pos, Y): C[p] ^= y
assert C == V
print("g :", [name(c) for c in g])
print("V :", [name(c) for c in V])
print("S :", [name(s) for s in S])
print("Lambda:", [name(c) for c in Lam], "posiciones", pos, "magnitudes", [name(y) for y in Y])
```

Salida del programa:

```
g : ['a^6', 'a^9', 'a^6', 'a^4', 'a^14', 'a^10', 'a^0']
V : ['a^14', 'a^9', 'a^0', 'a^2', 'a^3', 'a^6', 'a^1', 'a^4', 'a^0', 'a^10', 'a^4', 'a^2', 'a^1', 'a^3', 'a^1']
S : ['a^11', 'a^14', 'a^13', 'a^13', '0', 'a^0']
Lambda: ['a^0', 'a^9', 'a^12', 'a^7'] posiciones [1, 8, 13] magnitudes ['a^5', 'a^11', 'a^2']
```

---

## Resumen de resultados

| Ej. | Resultado |
|---|---|
| P1·1 | Paridad par e impar detectan **cantidad impar** de errores (128 de 255 patrones); no corrigen |
| P1·2 | Redundancia `N/K`: 2 entre 5 = **1,505**; 3 entre 7 = **1,365** |
| P1·3 | `P(0) = 0,9048`; `P(n) = C(100,n)pⁿ(1−p)¹⁰⁰⁻ⁿ`; `P(≤n)` en tabla |
| P1·4 | LRC de RACING = `00010000`; de INDEPENDIENTE = `01001010` (`J`) |
| P1·5 | Detecta impares por columna y ráfagas hasta 15; no corrige; redundancia `(L+1)/L` |
| P1·6 | `0-13165332-6` es válido (132 = 12·11); `950-311192-7` |
| P1·7 | Suma simple: `ABCDE-E`, `12345-M` (no detecta permutación). Pesada: `ABCDE-T`, `12345-O` (sí detecta) |
| P1·8 | "Pesados" = suma de `dígito·peso ≡ 0`; los cuatro códigos verifican |
| P1·9 | Base prima ⇒ todo peso invertible ⇒ decodificación única |
| P2·1 | Mínima redundancia con 4×6 (1,4167 sin esquina; 1,4583 con esquina) |
| P2·2 | Esquina: `dmin` 3→4; con paridad impar solo es consistente si `a ≡ b (mod 2)` |
| P2·3 | 4×5 par: BP filas `0 1 0 1`, columnas `1 1 0 1 1`, esquina `0` |
| P2·4 | Rectangular `1 + 1/a + 1/b`; triangular `1 + 2/P` (`21/15`) |
| P2·5 | `1011010`; `dmin = 3`, corrige 1 o detecta 2 |
| P2·6 | `P = 2⁻ᵐ` |
| P2·7 | Triangular: `101110100111010000110` (chequeos `0 1 0 0 1 0`) |
| P2·8 | Error en la posición 3 → `010100010111110` |
| P2·9 | Error en la posición 1 → `0001111`, información `0111` |
| P2·10 | Con BP `dmin` 3→4: corrige 1 y detecta 2 |
| P2·11 | `G`, `H` y arreglo 8×16; `dmin = 3`; `P_nd ≈ 6,98·10⁻⁹` (supuesto `p = 0,001`) |
| P2·12 | `h = 1+x+x³+x⁵`; `V = x+x⁶+x⁷+x⁸+x¹⁰+x¹¹+x¹⁴`; `v(x)` no es código (síndrome `1+x+x⁴+x⁶+x⁹`); `dmin = 7`, corrige 3, detecta 6 |
| P2·13 | Tabla RS: `1023/983/1500`, `255/175/3000`, `63/39/900`, `255/201/2025`; RS(15,9) con 3 errores corregido |
