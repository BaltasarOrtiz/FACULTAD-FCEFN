# Modelo de Parcial 2 (Tema 2) · Teoría de la Información

Cripto, Procesamiento de Imágenes y Codificación de Canal. Mismo formato que el Tema 1. **Primero el enunciado para resolver solo; la resolución verificada por programa está al final.**

---

# ENUNCIADO

## PARTE I — CRIPTOGRAFÍA

### Ejercicio 1 — Cifrado afín (Poirot y Hastings)

El detective Poirot recibe un mensaje cifrado con una sustitución afín de parámetros `(a, b, n) = (8, 5, 36)`. Alfabeto fuente: `ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`. Al ver sólo los parámetros, Poirot afirma que el mensaje es indescifrable.

Días después, el mismo remitente se comunica de nuevo. Poirot sabe que ahora usó la afín con `(a, b, n) = (7, 5, 36)` y autoriza a Hastings a descifrar el mensaje:

`7K47X5Q57X4F7YKF45QQ78`

a) ¿En qué se basó Poirot para decir que el primer mensaje es indescifrable?
b) Encuentre la clave de descifrado y el texto claro del segundo mensaje.
c) Calcule `a⁻¹` por dos métodos distintos.

### Ejercicio 2 — Firma digital con RSA

Bruno y Alicia usan RSA. Claves de Bruno: pública `(e_b, n_b)`, privada `(e⁻¹_b, n_b)`, con `p = 7`, `q = 11`, `e_b = 7`.

a) Calcule `n_b`, `φ(n_b)` y `e⁻¹_b`.
b) Bruno firma el mensaje `M = 5`. Calcule la firma `R` usando cuadrados sucesivos.
c) Explique cómo Alicia verifica la firma y cómo sabe que viene de Bruno.
d) Un atacante cambia el mensaje a `M' = 6` y reenvía `(M', R)`. ¿Qué obtiene Alicia al verificar?

### Ejercicio 3 — Procesamiento de imágenes: RLE en PCX

a) Codifique con RLE de PCX la fila de píxeles:
`9 9 9 9 9 200 4 4 150 255 255 255 255` seguido de 70 píxeles `0`. Indique la cantidad de bytes de entrada y de salida.
b) Decodifique el flujo (en decimal): `195 9 6 194 200 191 255 2`.
c) Explique cuándo surgen problemas con el byte de cantidad y los colores, y cuándo RLE agranda el archivo.

---

## PARTE II — CONTROL DE ERROR

### Ejercicio 1 — Código cíclico

Se tiene un código cíclico sistemático de longitud `N = 7` con polinomio generador `g(x) = 1 + x² + x³ + x⁴`. Convención: bits de información a la derecha.

a) Determine `(N, K, dmin)` y la redundancia (`N/K`).
b) Obtenga `G = [P | Iₖ]` y `H = [Iₙ₋ₖ | Pᵀ]`.
c) Capacidad del código como corrector y/o detector.
d) Llega `1100001`. Calcule el síndrome, corrija si puede y dé la información.
e) Llega `1000111`. Ídem. ¿Qué concluye?
f) Si se transmiten palabras entrelazadas de a 5, ¿qué ráfaga máxima se corrige?

### Ejercicio 2 — Arreglo cuadrado con paridad

Un arreglo de `4 × 4`: las 3 primeras filas son palabras `(4, 3, 2)` (3 bits de información + 1 de paridad par) y la cuarta fila contiene la paridad par de cada columna.

a) Encuentre `(N, K, dmin)`, la redundancia y la capacidad como detector y/o corrector.
b) Cargue el arreglo con información `101 / 011 / 110` y escriba la palabra enviada (16 bits, fila por fila).
c) Se recibe el arreglo con un bit erróneo (elija posición). Muestre cómo se localiza y corrige.
d) Muestre con un ejemplo de 2 errores que se detectan pero no se pueden corregir.

### Teóricas

a) Complete el dígito faltante del ISBN-10 `0-387-9?104-0`.
b) ¿Qué diferencia hay entre el control de ISBN-10 y el de ISBN-13? ¿Cuál detecta mejor las transposiciones?

---
---

# RESOLUCIÓN

## PARTE I — CRIPTOGRAFÍA

### Ejercicio 1

Convención: `C = (a·M + b) mod n`, `A=0 … Z=25, 0=26 … 9=35`.

**a) Primer mensaje `(8, 5, 36)`:** `mcd(8, 36) = 4 ≠ 1` (divisores comunes: 1, 2, 4; el mayor es 4). Entonces `8` no tiene inverso módulo 36 y no existe clave de descifrado. La función no es biyectiva: `8·9 = 72 = 2·36 ≡ 0`, así que `M`, `M+9`, `M+18`, `M+27` dan el mismo `C`. Ejemplo: `A(0)`, `J(9)`, `S(18)`, `2(27)` se cifran todos como `5 = F`. Sólo salen 9 símbolos cifrados distintos (`5, 9, 13, …`).

**b) Segundo mensaje `(7, 5, 36)`:** `mcd(7, 36) = 1` ✓ (7 es primo y no divide a 36). Inverso por Euclides extendido:

```
36 = 5·7 + 1   ⇒   1 = 36 − 5·7   ⇒   7⁻¹ ≡ −5 ≡ 31 (mod 36)
```

Comprobación: `7·31 = 217 = 6·36 + 1` ✓. Clave de descifrado: **`(31, 5, 36)`**, `M = 31·(C − 5) mod 36`.

Primeros símbolos: `7 = 33` → `31·28 = 868 = 24·36 + 4` → `E`; `K = 10` → `31·5 = 155 = 4·36 + 11` → `L`; `4 = 30` → `31·25 = 775 = 21·36 + 19` → `T`.

Texto claro: **`ELTESOROESTAENLATORRE9`** ("EL TESORO ESTA EN LA TORRE 9").

**c) Segundo método (Euler):** el conjunto reducido de 36 es `{1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35}`, `φ(36) = 12`, entonces `7⁻¹ = 7^(φ−1) = 7¹¹ mod 36`. Cuadrados sucesivos: `7² = 49 ≡ 13`, `7⁴ = 169 ≡ 25`, `7⁸ = 625 ≡ 13`. Como `11 = 8 + 2 + 1`: `13·13·7 = 169·7 ≡ 25·7 = 175 = 4·36 + 31` ⇒ **31** ✓.

### Ejercicio 2

**a) Claves de Bruno, paso a paso**

**Paso 1 — `n_b` y `φ(n_b)`:**
- `n_b = 7·11 = 77` → es el módulo con el que se firma y se verifica.
- `φ(n_b) = (7 − 1)(11 − 1) = 6·10 = 60` → es el módulo en el que se busca `e⁻¹_b`.

**Paso 2 — `e_b`:** viene dado, `e_b = 7`. Se verifica `mcd(7, 60) = 1` ✓.

**Paso 3 — `e⁻¹_b`** (el inverso se busca módulo **60**, no módulo 77): hay que hallar `e⁻¹_b` tal que `7·e⁻¹_b ≡ 1 (mod 60)`.

*Euclides extendido:*

```
60 = 8·7 + 4
 7 = 1·4 + 3
 4 = 1·3 + 1

1 = 4 − 3
  = 4 − (7 − 4) = 2·4 − 7
  = 2·(60 − 8·7) − 7 = 2·60 − 17·7   ⇒   7⁻¹ ≡ −17 ≡ 43 (mod 60)
```

*Euler (variante):* `φ(60) = 60·(1/2)·(2/3)·(4/5) = 16`, entonces `e⁻¹_b = 7^(16−1) = 7¹⁵ mod 60`. Cuadrados sucesivos: `7¹ = 7`, `7² = 49`, `7⁴ = 2401 ≡ 1`, `7⁸ ≡ 1`. Como `15 = 8 + 4 + 2 + 1`: `1·1·49·7 = 343 = 5·60 + 43` ⇒ **43**.

Verificación: `7·43 = 301 = 5·60 + 1` ✓ ⇒ **`e⁻¹_b = 43`**. Claves: pública `(7, 77)`, privada `(43, 77)`.

**b) Paso 4 — Firmar `M = 5`:** `R = M^(e⁻¹_b) mod n_b = 5⁴³ mod 77`. Como `43 = 32 + 8 + 2 + 1`:

| `5^k` | 5¹ | 5² | 5⁴ | 5⁸ | 5¹⁶ | 5³² |
|---|---|---|---|---|---|---|
| mod 77 | 5 | 25 | 9 | 4 | 16 | 25 |

`5⁴³ = 5³²·5⁸·5²·5¹ ≡ 25·4·25·5`: `25·4 = 100 ≡ 23`; `23·25 = 575 ≡ 36`; `36·5 = 180 ≡ 26`. **`R = 26`**. Bruno envía `(M, R) = (5, 26)`.

**c)** Alicia calcula con la **pública de Bruno** `R^(e_b) mod n_b = 26⁷ mod 77`: `26² ≡ 60`, `26⁴ ≡ 58`, `26⁷ = 26⁴·26²·26 ≡ 58·60·26 ≡ 15·26 = 390 ≡ 5`. Obtiene `5 = M` ✓. Sólo quien tiene `e⁻¹_b = 43` pudo generar un `R` que, elevado a `e_b`, devuelva `M`; calcularlo desde `(e_b, n_b)` exige factorizar `n_b`. Provee autenticidad, integridad y no repudio. La confidencialidad sería un paso aparte (cifrar con la pública de Alicia).

**d)** Alicia calcula `26⁷ mod 77 = 5` y lo compara con `M' = 6`: **no coinciden** ⇒ el mensaje fue alterado o no lo firmó Bruno, y se rechaza.

*(Variante con hash, nota corta: se firma `H(M)` en vez de `M`; Alicia compara `R^(e_b)` con su propio `H(M)`.)*

### Ejercicio 3

**a)** Reglas: contador = `192 + cantidad` (1..63); dato `< 192` va solo; dato `≥ 192` aislado se escribe `193, dato`.

| Píxeles | Bytes |
|---|---|
| `9 ×5` | `197, 9` |
| `200 ×1` | `193, 200` (aislado ≥ 192) |
| `4 ×2` | `194, 4` |
| `150 ×1` | `150` (< 192, va solo) |
| `255 ×4` | `196, 255` |
| `0 ×70 = 63 + 7` | `255, 0` y `199, 0` |

Salida: `197 9 193 200 194 4 150 196 255 255 0 199 0` → **13 bytes** para **83 píxeles** de entrada.

**b)** `195, 9` → `9 9 9`; `6` (< 192) → literal `6`; `194, 200` → `200 200`; `191` (< 192) → literal `191`; `255, 2` → `2` repetido 63 veces. Resultado: `9 9 9 6 200 200 191` y 63 veces `2` (70 píxeles).

**c)** Un byte `≥ 192` empieza con `11` y se confunde con un contador, por eso un color suelto `≥ 192` se precede de `193`: ese píxel ocupa **2 bytes** y RLE puede **agrandar** el archivo si no hay repeticiones. El contador tiene 6 bits, así que una repetición `> 63` se parte en varios pares `(contador, dato)`.

---

## PARTE II — CONTROL DE ERROR

### Ejercicio 1

**a)** `grado g = 4 = N − K` ⇒ `K = 3`; `(N, K) = (7, 3)`. Redundancia (cátedra) `N/K = 7/3 ≈ 2,33`. Las 8 palabras tienen peso 0 o 4, así que **`dmin = 4`**.

**b)** Filas de `P`: `x⁴ mod g = 1 + x² + x³` → `1011`; `x⁵ mod g = 1 + x + x²` → `1110`; `x⁶ mod g = x + x² + x³` → `0111`.

```
G = [P | I₃] = 1 0 1 1 | 1 0 0
               1 1 1 0 | 0 1 0
               0 1 1 1 | 0 0 1

H = [I₄ | Pᵀ] = 1 0 0 0 | 1 1 0
                0 1 0 0 | 0 1 1
                0 0 1 0 | 1 1 1
                0 0 0 1 | 1 0 1
```

Palabras: `000→0000000`, `001→0111001`, `010→1110010`, `011→1001011`, `100→1011100`, `101→1100101`, `110→0101110`, `111→0010111`.

**c)** `dmin = 4 ≥ 2t + 1` ⇒ corrige `t = 1`. Como detector puro detecta `dmin − 1 = 3`. Simultáneo: `dmin ≥ t + s + 1` ⇒ corrige 1 y detecta 2.

**Cómo se determina cuánto detecta y cuánto corrige.** Todo sale de `dmin`, la mínima cantidad de bits en que difieren dos palabras válidas.

1. **Sólo detectar:** el error pasa desapercibido únicamente si convierte una palabra válida en *otra* válida, y eso requiere al menos `dmin` bits cambiados. Detecta hasta **`dmin − 1`** errores (acá, 3).
2. **Sólo corregir:** corregir es elegir la palabra válida más cercana, y la recibida tiene que estar más cerca de la correcta que de cualquier otra. Corrige `t` errores si **`dmin ≥ 2t + 1`**, es decir `t = ⌊(dmin − 1)/2⌋` (acá, `⌊3/2⌋ = 1`). Con 2 errores y `dmin = 4` puede haber empate entre dos palabras válidas, por eso no corrige 2.
3. **Ambas a la vez:** si el decodificador corrige hasta `t`, un error de más de `t` bits podría quedar cerca de otra palabra y "corregirse" mal. Para seguir detectando hasta `s ≥ t` errores hace falta **`dmin ≥ t + s + 1`**.

| Configuración (`dmin = 4`) | Cuenta | ¿Vale? |
|---|---|---|
| `t = 0`, `s = 3` | `0 + 3 + 1 = 4` | sí (sólo detector) |
| `t = 1`, `s = 2` | `1 + 2 + 1 = 4` | sí (corrige 1 y detecta 2) |
| `t = 1`, `s = 3` | `1 + 3 + 1 = 5` | **no**, supera `dmin` |

Corregir tiene un costo de detección: se pasa de detectar 3 a detectar 2. Esto es lo que ocurre en el punto e): el síndrome `1010` no coincide con ningún error simple, así que se detecta que hubo más de un error pero no se puede corregir.

**d)** `r = 1100001` → `R(x) = 1 + x + x⁶`. Se divide por `g` y el resto es `1 + x² + x³` (síndrome `1011`). La tabla de síndromes de un solo error: pos 1 `1000`, 2 `0100`, 3 `0010`, 4 `0001`, **5 `1011`**, 6 `1110`, 7 `0111`. Error en la posición 5 ⇒ palabra corregida `1100101`, información `101`.

**e)** `r = 1000111` → síndrome `1010`, que **no coincide con ningún síndrome de error simple**. Se detecta un error múltiple (2 errores) pero **no se puede corregir**: se pide retransmisión. Coherente con "corrige 1, detecta 2".

**f)** Con entrelazado de `L = 5` palabras, una ráfaga de hasta `t·L = 1·5 =` **5 bits** consecutivos cae como máximo un bit por palabra y se corrige.

### Ejercicio 2

**a)** El arreglo es el producto de dos códigos `(4, 3, 2)`: `N = 16`, `K = 3·3 = 9`, `dmin = 2·2 =` **4**. Redundancia `N/K = 16/9 ≈ 1,78`. Capacidad: corrige **1** error y detecta **2** (`4 ≥ 1 + 2 + 1`); como detector puro detecta 3.

**b)** Información `101 / 011 / 110`:

```
1 0 1 | 0        paridad fila 1 = 0
0 1 1 | 0        paridad fila 2 = 0
1 1 0 | 0        paridad fila 3 = 0
------+--
0 0 0 | 0        paridad de columnas
```

Palabra enviada: `1010 0110 1100 0000` → **`1010011011000000`**.

**c)** Si se invierte el bit de la fila 2, columna 3 (`1 → 0`), falla la paridad de la **fila 2** y la de la **columna 3**; el cruce da la posición `(2, 3)`, se invierte y se corrige.

**d)** Dos errores en distintas filas y columnas (por ejemplo `(1,1)` y `(2,2)`): fallan 2 filas y 2 columnas, pero el cruce admite 2 pares posibles (`(1,1),(2,2)` o `(1,2),(2,1)`) ⇒ se **detecta pero no se corrige**. Dos errores en la misma fila: la paridad de esa fila pasa y fallan 2 columnas ⇒ también detectado.

### Teóricas

**a) ISBN `0-387-9?104-0`:** dígitos con pesos `10..1`: `0·10 + 3·9 + 8·8 + 7·7 + 9·6 + x·5 + 1·4 + 0·3 + 4·2 + 0·1 = 206 + 5x`. Debe ser `≡ 0 (mod 11)`; `206 ≡ 8`, así que `5x + 8 ≡ 0`. Probando `x`: `0→8, 1→2, 2→7, 3→1, 4→6, 5→0` ⇒ **`x = 5`** (ISBN `0-387-95104-0`).

**b)** ISBN-10 usa módulo 11 (primo) con pesos `10..1` y puede terminar en `X`; detecta todo error simple y toda transposición de dígitos adyacentes. ISBN-13 usa módulo 10 con pesos alternados `1, 3` y detecta todo error simple, pero **no** las transposiciones de dígitos que difieren en 5 (el cambio es `2·(a − b) ≡ 0 mod 10`). Detecta mejor las transposiciones el **ISBN-10**.

---

## Resumen de resultados

| Punto | Resultado |
|---|---|
| Cripto 1.a | `mcd(8, 36) = 4 ≠ 1` ⇒ sin inverso ⇒ indescifrable |
| Cripto 1.b | `7⁻¹ = 31` ⇒ clave `(31, 5, 36)`; texto `ELTESOROESTAENLATORRE9` |
| Cripto 2 | `n_b = 77`, `φ = 60`, `e⁻¹_b = 43`, `R = 26`; con `M' = 6` la verificación falla |
| Imágenes | codificación de 13 bytes; decodificación `9 9 9 6 200 200 191` + 63 veces `2` |
| CE 1 | `(7, 3, 4)`, redundancia 7/3, corrige 1 / detecta 2; `1100001` → error pos 5, info `101`; `1000111` detecta sin corregir; ráfaga 5 |
| CE 2 | `N = 16`, `K = 9`, `dmin = 4`; palabra `1010011011000000` |
| Teóricas | ISBN: `x = 5`; ISBN-10 detecta mejor transposiciones |
