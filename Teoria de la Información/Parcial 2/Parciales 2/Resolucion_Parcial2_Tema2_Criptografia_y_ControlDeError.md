# Resolución — Parcial 2 (Tema 2) · Teoría de la Información

Cripto, Procesamiento de Imágenes y Codificación de Canal · Licenciatura en Ciencias de la Computación

> Todos los cálculos (inverso modular, descifrado afín, estructura del código, división polinómica, síndromes, distancia mínima del arreglo, ISBN) fueron verificados por programa. Acá se muestra el procedimiento a mano para reproducirlo en el examen.

## Convenciones usadas

- **Afín:** `C = (a·M + b) mod n`; descifrado `M = a⁻¹·(C − b) mod n`. Existe `a⁻¹` **sólo si `mcd(a, n) = 1`**.
- **Cadena de bits ↔ polinomio ("mayores potencias a la derecha")**: `b₀ b₁ … bₙ₋₁` es `b₀ + b₁x + … + bₙ₋₁xⁿ⁻¹`. Para dividir a mano se escribe con la mayor potencia a la izquierda.
- **Redundancia (cátedra) = N/K**.
- **Capacidad:** `dmin ≥ 2t + 1` para corregir `t` errores; como detector puro detecta `dmin − 1`; corrige `t` y detecta `s` a la vez si `dmin ≥ t + s + 1`.
- **Cíclicos sistemáticos:** `G = [P | Iₖ]`, `H = [Iₙ₋ₖ | Pᵀ]`; síndrome = resto de `R(x) ÷ g(x)` = suma de las filas de `Hᵀ` donde `R` tiene un 1.
- **ISBN-10 (base 11, prima):** pesos `10, 9, …, 1`; válido ⇔ `Σ dígito·peso ≡ 0 (mod 11)`; el último símbolo puede ser `X = 10`.

---

# PARTE I — CRIPTOGRAFÍA

## Ejercicio 1 — Cifrado afín (Holmes y Watson)

> El inspector Sherlock Holmes recibió un mensaje cifrado, y con el solo hecho de saber que ha sido cifrado con una sustitución afín, con los parámetros `(a, b, n) = (21, 3, 36)`, dada su gran afición a la matemática discreta y al cifrado/descifrado, miró a su amigo el Dr. John Watson y le dijo: «¡No te molestes en encontrar la clave para descifrar el texto recibido, el mensaje es indescifrable!». ¿En qué se basó Holmes para decir esto?
>
> Pasados los días, se vuelve a comunicar el mismo remitente con Sherlock Holmes; nuevamente, con el solo hecho de saber que el remitente utilizó la sustitución afín con los parámetros `(a, b, n) = (25, 7, 36)`, autorizó al Dr. Watson a descifrar el mensaje. El mensaje cifrado es `471I9ZW9AHK7Z19TWA97VDAA9`, siendo el alfabeto fuente `ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`. Encuentre la clave de descifrado y el texto claro.

Son **dos mensajes distintos con claves distintas**: el primero cifrado con `a = 21`, el segundo con `a = 25`. Holmes decide mirando sólo los parámetros, sin ver el criptograma.

### Inciso 1.a) ¿En qué se basó Holmes para decir que el mensaje es indescifrable?

Para descifrar hace falta el inverso de `a` módulo `n`. Ese inverso existe sólo si `a` y `n` son **coprimos**, o sea, si el único divisor común es el 1:

- Divisores de 21: `1, 3, 7, 21`
- Divisores de 36: `1, 2, 3, 4, 6, 9, 12, 18, 36`
- Comunes: `1` y `3` ⇒ `mcd(21, 36) = 3 ≠ 1` ⇒ **`21` no tiene inverso módulo `36`** ⇒ no hay clave de descifrado `(a⁻¹, b, n)`.

Esto significa que la función `C = 21·M + 3 mod 36` **no es biyectiva**: es una *clave no válida* para cifrar.

- Los valores que puede tomar `C` son sólo `3, 6, 9, …, 33, 0` (múltiplos de 3): **12 de los 36 símbolos**.
- **Tres** símbolos del claro distintos terminan en el mismo símbolo cifrado, porque `21·12 = 252 = 7·36 ≡ 0 (mod 36)`; es decir `M`, `M + 12` y `M + 24` dan el mismo `C`.

Ejemplo: `A (0)`, `M (12)` y `Y (24)` se cifran los tres como `21·0 + 3 = 3 = D`. Ante una `D` en el criptograma no se puede saber cuál de las tres era.

Para un mensaje de `L` símbolos hay `3ᴸ` claros posibles (para 25 símbolos, `3²⁵ ≈ 8,5·10¹¹`): el mensaje es **indescifrable de forma unívoca**, y Holmes lo supo con sólo mirar los parámetros.

> **Regla:** las claves válidas son las que cumplen `mcd(a, n) = 1`. Con `n = 36` hay `φ(36) = 12` valores válidos de `a` (1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35) y 36 de `b`: **432 claves**.

### Inciso 1.b) Segundo mensaje, `(a, b, n) = (25, 7, 36)`

> Mensaje: `471I9ZW9AHK7Z19TWA97VDAA9`. Alfabeto fuente: `ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`. Encuentre la clave de descifrado y el texto claro.

**Alfabeto numerado** (`n = 36`): `A=0, B=1, …, Z=25, 0=26, 1=27, …, 9=35`.

**Paso 1 · Verificar que se puede descifrar:** `mcd(25, 36) = 1` ✓ (`25 = 5²` y 5 no divide a 36; el único divisor común es el 1).

**Paso 2 · Inverso de `a` (Euclides extendido):**

```
36 = 1·25 + 11
25 = 2·11 +  3
11 = 3·3  +  2
 3 = 1·2  +  1

1 = 3 − 2
  = 3 − (11 − 3·3) = 4·3 − 11
  = 4·(25 − 2·11) − 11 = 4·25 − 9·11
  = 4·25 − 9·(36 − 25) = 13·25 − 9·36
```

`25⁻¹ ≡ 13 (mod 36)`. Comprobación: `25·13 = 325 = 9·36 + 1` ✓.

**Variante alternativa — Euler + cuadrados sucesivos** (otra forma manual de obtener el mismo inverso):

1. **Conjunto reducido de restos** de `36` (`36 = 2²·3²`, se descartan los pares y los múltiplos de 3):

   `{1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35}` → **12** elementos.

2. **Función de Euler:** `φ(36) = φ(2²)·φ(3²) = (4 − 2)·(9 − 3) = 2·6 = 12` ✓. Como `25` pertenece al conjunto, tiene inverso.

3. **Teorema de Euler:** `a^φ(n) ≡ 1 (mod n)` ⇒ `a⁻¹ ≡ a^(φ(n) − 1)`. Entonces

   `25⁻¹ ≡ 25^(12 − 1) = 25¹¹ (mod 36)`

4. **Cuadrados sucesivos:** `11 = 8 + 2 + 1 = 1011₂`:

   | Potencia | Cálculo | mod 36 |
   |---|---|---|
   | `25¹` | | **25** |
   | `25²` | `25² = 625 = 17·36 + 13` | **13** |
   | `25⁴` | `13² = 169 = 4·36 + 25` | **25** |
   | `25⁸` | `25² ≡ 13` (ya calculado) | **13** |

5. **Armar el exponente:** `25¹¹ = 25⁸ · 25² · 25¹ = 13 · 13 · 25`

   - `13 · 13 = 169 ≡ 25`
   - `25 · 25 = 625 ≡ 13`

   **`25⁻¹ ≡ 13 (mod 36)`** ✓, igual que con Euclides.

**Paso 3 · Clave de descifrado:**

`M = 13·(C − 7) mod 36 = 13·C − 91 mod 36 = (13·C + 17) mod 36`

**Clave de descifrado: `(a⁻¹, b, n) = (13, 7, 36)`** (con `M = 13·(C − 7)`); ambas formas coinciden porque `−91 ≡ 17 (mod 36)`.

**Paso 4 · Descifrado símbolo a símbolo:**

| # | C | c | c−7 | 13·(c−7) | mod 36 | M |
|---|---|---|---|---|---|---|
| 1 | 4 | 30 | 23 | 299 | 11 | L |
| 2 | 7 | 33 | 26 | 338 | 14 | O |
| 3 | 1 | 27 | 20 | 260 | 8 | I |
| 4 | I | 8 | 1 | 13 | 13 | N |
| 5 | 9 | 35 | 28 | 364 | 4 | E |
| 6 | Z | 25 | 18 | 234 | 18 | S |
| 7 | W | 22 | 15 | 195 | 15 | P |
| 8 | 9 | 35 | 28 | 364 | 4 | E |
| 9 | A | 0 | −7 | −91 | 17 | R |
| 10 | H | 7 | 0 | 0 | 0 | A |
| 11 | K | 10 | 3 | 39 | 3 | D |
| 12 | 7 | 33 | 26 | 338 | 14 | O |
| 13 | Z | 25 | 18 | 234 | 18 | S |
| 14 | 1 | 27 | 20 | 260 | 8 | I |
| 15 | 9 | 35 | 28 | 364 | 4 | E |
| 16 | T | 19 | 12 | 156 | 12 | M |
| 17 | W | 22 | 15 | 195 | 15 | P |
| 18 | A | 0 | −7 | −91 | 17 | R |
| 19 | 9 | 35 | 28 | 364 | 4 | E |
| 20 | 7 | 33 | 26 | 338 | 14 | O |
| 21 | V | 21 | 14 | 182 | 2 | C |
| 22 | D | 3 | −4 | −52 | 20 | U |
| 23 | A | 0 | −7 | −91 | 17 | R |
| 24 | A | 0 | −7 | −91 | 17 | R |
| 25 | 9 | 35 | 28 | 364 | 4 | E |

Los negativos se llevan a su resto: `−91 mod 36 = 17`, `−52 mod 36 = 20`. Ojo: el cuarto símbolo es la **letra** `I` (`I = 8`), no el dígito `1` (`1 = 27`).

**Texto claro:** `LOINESPERADOSIEMPREOCURRE` → **"LO INESPERADO SIEMPRE OCURRE"**.

**Comprobación (cifrando):** `4` se obtiene de `L`: `25·11 + 7 = 282 = 7·36 + 30 → 30 = 4` ✓; `7` de `O`: `25·14 + 7 = 357 = 9·36 + 33 → 33 = 7` ✓. El texto completo vuelve a dar `471I9ZW9AHK7Z19TWA97VDAA9`.

---

## Ejercicio 2 — Firma digital con RSA

> Bruno quiere enviar un mensaje firmado a Alicia. Claves de Bruno: pública `(e_b, n_b)`, privada `(e⁻¹_b, n_b)`. Indique el procedimiento y cómo Alicia sabe que el mensaje proviene de Bruno.

**Notación (la del enunciado):** `e⁻¹_b` es el inverso de `e_b` módulo `φ(n_b)` (`e_b · e⁻¹_b ≡ 1 mod φ(n_b)`), y es el exponente de la clave privada de Bruno. Alicia tiene su par `(e_a, n_a)` pública y `(e⁻¹_a, n_a)` privada.

**Idea clave:** en RSA el par de claves es simétrico: lo que se cifra con una se descifra con la otra. Para **firmar** se usa la clave **privada** del emisor (sólo Bruno la tiene); para **verificar**, la clave **pública**.

### Procedimiento de Bruno (emisor)

1. **Firma (rúbrica):** cifra el mensaje con **su clave privada**: `R = M^(e⁻¹_b) mod n_b`, con `M < n_b` (si es más largo, se parte en bloques).
2. **Envío:** manda a Alicia `(M, R)`: el mensaje y su firma.
3. **Opcional, si además quiere confidencialidad:** cifra `M` con la **clave pública de Alicia**, `C = M^(e_a) mod n_a`, y envía `(C, R)`. Esto es un paso aparte: **no forma parte de la firma**.

### Procedimiento de Alicia (receptor) — cómo sabe que viene de Bruno

1. Si el mensaje venía cifrado, lo recupera con **su clave privada**: `M = C^(e⁻¹_a) mod n_a`.
2. Descifra la firma con la **clave pública de Bruno**: `M' = R^(e_b) mod n_b`.
3. **Compara `M' = M`.**
   - **Coinciden:** el mensaje lo firmó Bruno y no fue alterado.
   - **No coinciden:** la firma no corresponde a ese mensaje (o fue modificado, o no lo firmó Bruno) ⇒ se rechaza.

**Por qué prueba que fue Bruno:** `R^(e_b) = M^(e⁻¹_b·e_b) = M (mod n_b)` sólo si `R` se generó con `e⁻¹_b`. Nadie más lo conoce, y calcularlo a partir de `(e_b, n_b)` exige factorizar `n_b` (problema computacionalmente inviable). Por lo tanto la firma provee:

| Propiedad | Por qué |
|---|---|
| **Autenticidad** | sólo quien tiene `e⁻¹_b` pudo producir `R` |
| **Integridad** | si alguien cambia `M`, el `R^(e_b)` deja de coincidir con él |
| **No repudio** | Bruno no puede negar haberlo firmado: la verificación con su clave pública lo prueba |

Resumen de qué clave se usa para qué:

| Objetivo | Emisor (Bruno) usa | Receptor (Alicia) usa |
|---|---|---|
| **Firma** (autenticidad) | su **privada** `e⁻¹_b` | la **pública de Bruno** `e_b` |
| **Confidencialidad** (opcional) | la **pública de Alicia** `e_a` | su **privada** `e⁻¹_a` |

Alicia debe obtener la clave pública de Bruno por un canal confiable (certificado / autoridad de certificación), si no un atacante podría presentarle la suya como si fuera la de Bruno.

> **Variante con hash (nota):** en la práctica no se firma `M` entero sino su resumen `h = H(M)` (por ejemplo SHA-256): `R = h^(e⁻¹_b) mod n_b`. Alicia calcula `H(M)` por su cuenta, obtiene `R^(e_b) mod n_b` y compara ambos. El hash no tiene clave ni se "descifra": sólo hace la firma más corta y rápida. El resto del procedimiento es igual.

---

## Ejercicio 3 — Procesamiento de imágenes: RLE en PCX

> Explique el algoritmo de compresión RLE aplicado en el formato PCX. Ejemplifique. Explique cuándo surgen problemas con la codificación del byte de cantidad y los colores. Ejemplifique.

### Idea general

**RLE (Run-Length Encoding)** es compresión **sin pérdida** que reemplaza una repetición de valores iguales por un par **(cantidad, valor)**. Sirve cuando hay tramos largos de píxeles idénticos (fondos lisos).

```
5 5 5 5 5 5 5 5 5 5   → 10 bytes
(10 veces) 5          →  2 bytes
```

### Regla de PCX: los dos bits altos del byte deciden

```
11 cccccc   → CONTADOR: los 6 bits cccccc = repeticiones (1..63); el SIGUIENTE byte es el dato
00/01/10 …  → DATO literal (valores 0..191)
```

- Todo byte `≥ 192` (`11000000`) empieza con `11` y se interpreta como contador; todo byte `< 192` es un dato.
- **Byte contador = 192 + cantidad.** Máximo `11111111 = 192 + 63 = 255` ⇒ **63 repeticiones**.

### Ejemplo de codificación

Flujo de píxeles de una línea: `5 5 5 7 200 200 200 200 150 150`.

| Tramo | Cantidad | Bytes | En bits |
|---|---|---|---|
| `5 5 5` | 3 | `195, 5` | `11000011 00000101` |
| `7` (suelto, `< 192`) | 1 | `7` | `00000111` |
| `200 200 200 200` | 4 | `196, 200` | `11000100 11001000` |
| `150 150` | 2 | `194, 150` | `11000010 10010110` |

10 bytes de entrada se reducen a 8: `195 5 7 196 200 194 150`.

### Decodificación

```
11000011 00000101 00000111 11000001 11001000
```

1. `11000011` → empieza con `11` ⇒ contador = `000011` = 3.
2. `00000101` → dato 5 ⇒ se escribe `5 5 5`.
3. `00000111` → empieza con `00` ⇒ dato literal `7`.
4. `11000001` → contador = 1.
5. `11001000` → dato 200 (viene **después** de un contador, se lee como dato) ⇒ `200`.

Resultado: `5 5 5 7 200`. El mismo byte `11001000` puede ser contador o dato **según su posición** en el flujo.

### Problemas con el byte de cantidad y los colores

**Problema 1 — Dato suelto `≥ 192` (colisión color/contador).** Un píxel de color 200 que no se repite no se puede escribir como `11001000`, porque el decodificador lo tomaría por contador (`200 − 192 = 8`) y se comería el byte siguiente. Se lo prefija con el contador "×1" (`193 = 11000001`):

| Color suelto | Se escribe | Bytes |
|---|---|---|
| 150 (`10010110`, `< 192`) | `10010110` | 1 |
| 191 (el mayor sin prefijo) | `10111111` | 1 |
| 200 (`11001000`, `≥ 192`) | `11000001 11001000` | **2** |

Consecuencia: RLE **puede agrandar** el archivo. En una imagen con muchos colores `≥ 192` y sin repeticiones (fotos, ruido) el tamaño llega hasta el **doble**. Se atenúa reordenando la paleta para que los colores más frecuentes tengan índice `< 192`.

**Problema 2 — El contador es de sólo 6 bits (máx. 63).** Una repetición mayor se parte en **varios pares independientes** `(contador, dato)`:

```
5 repetido 70 veces = 63 + 7  →  11111111 00000101   11000111 00000101
                                  (63 veces el 5)      (7 veces el 5)
5 repetido 200 veces = 63 + 63 + 63 + 11 → 255,5  255,5  255,5  203,5   (8 bytes en lugar de 200)
```

Cada par es independiente: el decodificador los escribe uno tras otro, no "arma un número" con varios contadores.

**Problema 3 — Una repetición de 2 con color `≥ 192`.** `200 200` sale `194, 200` (2 bytes), igual que escribir cada uno con prefijo (`193,200,193,200` serían 4): conviene agrupar. En cambio, `150 150` (`< 192`) también ocupa 2 bytes (`194,150`) igual que sin comprimir: **no se gana nada con repeticiones de 2 para colores `< 192`**; la ganancia empieza en 3.

**Respuesta corta:** en RLE de PCX cada byte se interpreta por sus dos bits altos; con `11` (valor `≥ 192`) es un contador de 6 bits (1 a 63) que repite el byte siguiente; si no, es un dato literal. Por eso un dato suelto `≥ 192` se escribe `193, dato` (puede agrandar el archivo) y las repeticiones mayores a 63 se parten en varios pares.

---

# PARTE II — CODIFICACIÓN DE CANAL (CONTROL DE ERROR)

## Ejercicio 1 — Código dado por la matriz generadora

> Dada la anterior matriz generadora `G` (mayores potencias hacia la derecha) de un código `(N, K, dmin) = (?, ?, ?)`:
>
> ```
> F1  1 1 0 1 0 0 0 1 1 0 1 0 0 0
> F2  0 1 1 0 1 0 0 0 1 1 0 1 0 0
> F3  1 1 1 0 0 1 0 1 1 1 0 0 1 0
> F4  1 0 1 0 0 0 1 1 0 1 0 0 0 1
> ```
>
> a) Encuentre las capacidades del código como corrector y detector, especificando además `N`, `K`, `dmin`, `g(x)` y redundancia.
> b) Encuentre `H`.
> c) Encuentre si la palabra `10101101000110` (mayores potencias hacia la derecha) es válida o no; si no lo fuera, encuentre y corrija el error.
> d) Si se entrelazan 50 de los códigos anteriores, ¿cuál sería la capacidad de corrección de errores en ráfaga?

Se lee `G` de `4 × 14`: **`N = 14`**, **`K = 4`** (4 filas linealmente independientes), `N − K = 10` chequeadores.

### Inciso 1.a) Capacidades, `N`, `K`, `dmin`, `g(x)` y redundancia

**Las 16 palabras del código** (combinaciones lineales de las filas, `i = i₁ i₂ i₃ i₄`). Cada palabra son **dos copias de 7 bits** (la misma palabra repetida):

| Información | Palabra | Peso |
|---|---|---|
| 0000 | `0000000 0000000` | 0 |
| 0001 | `1010001 1010001` (F4) | 6 |
| 0010 | `1110010 1110010` (F3) | 8 |
| 0011 | `0100011 0100011` (F3+F4) | 6 |
| 0100 | `0110100 0110100` (F2) | 6 |
| 0101 | `1100101 1100101` (F2+F4) | 8 |
| 0110 | `1000110 1000110` (F2+F3) | 6 |
| 0111 | `0010111 0010111` (F2+F3+F4) | 8 |
| 1000 | `1101000 1101000` (F1) | 6 |
| 1001 | `0111001 0111001` (F1+F4) | 8 |
| 1010 | `0011010 0011010` (F1+F3) | 6 |
| 1011 | `1001011 1001011` (F1+F3+F4) | 8 |
| 1100 | `1011100 1011100` (F1+F2) | 8 |
| 1101 | `0001101 0001101` (F1+F2+F4) | 6 |
| 1110 | `0101110 0101110` (F1+F2+F3) | 8 |
| 1111 | `1111111 1111111` (F1+F2+F3+F4) | 14 |

Al ser lineal, `dmin` = menor peso no nulo ⇒ **`dmin = 6`**. (Cada mitad es una palabra del Hamming `(7, 4, 3)`, y como se repite, los pesos son `2·3 = 6`, `2·4 = 8` y `2·7 = 14`.)

**Parámetros:** el código es **`(N, K, dmin) = (14, 4, 6)`**.

**Redundancia** (cátedra): `N/K = 14/4 = 3,5`.

**Polinomio generador `g(x)`:** es la palabra no nula de **menor grado**. Los grados de las 15 palabras no nulas van de 10 a 13; el único de grado 10 es `F1 = 11010001101000`. Entonces

**`g(x) = 1 + x + x³ + x⁷ + x⁸ + x¹⁰`** (grado 10 = `N − K` ✓), que factoriza como `(1 + x + x³)(1 + x⁷)`.

El código es cíclico (`F2 = x·g` y `F3 = (1 + x²)·g`). Polinomio de paridad: `h(x) = (x¹⁴ + 1)/g(x) = 1 + x + x² + x⁴` (grado 4 = `K` ✓, resto 0).

**Capacidad** (`dmin = 6`):

| Modo | Capacidad |
|---|---|
| **Detector puro** | `dmin − 1 = ` **5 errores** |
| **Corrector puro** | `2t + 1 ≤ 6 ⇒ t = ` **2 errores** |
| **Mixto** | corrige 2 **y** detecta hasta 3 (`2 + 3 + 1 = 6`); también corrige 1 y detecta 4 |

### Inciso 1.b) Matriz de chequeo `H`

`G` ya está en forma sistemática `G = [P | I₄]` (las cuatro últimas columnas son la identidad):

```
P =  1 1 0 1 0 0 0 1 1 0   (F1 = P₁ | 1 0 0 0)
     0 1 1 0 1 0 0 0 1 1   (F2 = P₂ | 0 1 0 0)
     1 1 1 0 0 1 0 1 1 1   (F3 = P₃ | 0 0 1 0)
     1 0 1 0 0 0 1 1 0 1   (F4 = P₄ | 0 0 0 1)
```

Entonces `H = [I₁₀ | Pᵀ]`, de `10 × 14`. Cada fila `i` de `H` tiene un 1 en la columna `i` y, a la derecha, la columna `i` de `P`:

```
H = [ 1 0 0 0 0 0 0 0 0 0 | 1 0 1 1 ]
    [ 0 1 0 0 0 0 0 0 0 0 | 1 1 1 0 ]
    [ 0 0 1 0 0 0 0 0 0 0 | 0 1 1 1 ]
    [ 0 0 0 1 0 0 0 0 0 0 | 1 0 0 0 ]
    [ 0 0 0 0 1 0 0 0 0 0 | 0 1 0 0 ]
    [ 0 0 0 0 0 1 0 0 0 0 | 0 0 1 0 ]
    [ 0 0 0 0 0 0 1 0 0 0 | 0 0 0 1 ]
    [ 0 0 0 0 0 0 0 1 0 0 | 1 0 1 1 ]
    [ 0 0 0 0 0 0 0 0 1 0 | 1 1 1 0 ]
    [ 0 0 0 0 0 0 0 0 0 1 | 0 1 1 1 ]
```

Verificación: `G·Hᵀ = 0` ✓ (las 16 palabras del código dan síndrome 0). Control rápido con `F1 = 1101000110 | 1000` y la fila 1 de `H`: `1·1 + 1·1 = 0` ✓.

### Inciso 1.c) ¿Es válida la palabra `10101101000110`?

**Mayores potencias a la derecha:** la posición 1 es el primer bit; `r(x) = 1 + x² + x⁴ + x⁵ + x⁷ + x¹¹ + x¹²`. Los 1 están en las posiciones `1, 3, 5, 6, 8, 12, 13`.

**Método 1 — Síndrome por división polinómica** (mayor potencia a la izquierda; `g = 10110001011`, `r = 01100010110101`):

```
r(x)      = 01100010110101      (x¹³ … x⁰)
g(x)·x²   = 01011000101100      (g desplazado 2 lugares)
            ----------------
            00111010011001
g(x)·x    = 00101100010110      (g desplazado 1 lugar)
            ----------------
            00010110001111
g(x)      = 00010110001011      (g sin desplazar)
            ----------------
resto     = 00000000000100  =  x²
```

El resto `S(x) = x² ≠ 0` ⇒ **la palabra NO es válida**.

**Método 2 — Con `H`** (sumar las filas de `Hᵀ` donde `r` tiene un 1; `Hᵀ` tiene las filas 1 a 10 = identidad y las filas 11 a 14 = `P₁ … P₄`):

```
posiciones 1,3,5,6,8 (identidad)  →  1010110100
posición 12 (P₂)                  →  0110100011
posición 13 (P₃)                  →  1110010111
                                     ----------
S = r·Hᵀ                          =  0010000000
```

`S = 0 0 1 0 0 0 0 0 0 0` es igual a la **columna 3** de `H` ⇒ el error simple está en la **posición 3**.

**Corrección:** se invierte el bit 3 (`x²`):

`10101101000110` → **`10001101000110`** (= F2 + F3, palabra válida ✓; el resto ahora es 0).

**Mensaje de información:** por ser sistemático, son los últimos 4 bits: **`0110`**. El error estaba en un bit de chequeo.

**Observación (otra forma de verlo):** como cada palabra válida son dos copias iguales de 7 bits, la recibida `1010110 | 1000110` ya muestra que algo falló: las mitades no coinciden. La segunda mitad `1000110` es una palabra del Hamming `(7, 4)` y la primera `1010110` no; difieren en el bit 3.

**Por qué la corrección es confiable:** `dmin = 6` ⇒ corrige hasta 2 errores; la palabra válida más cercana a la recibida está a distancia 1 (las demás están a 5 o más), de modo que el error simple es la única explicación con hasta 2 errores.

### Inciso 1.d) Entrelazado de 50 códigos: capacidad en ráfaga

Una ráfaga de `B` bits consecutivos, entrelazando `L` códigos, reparte los bits entre las `L` palabras: cada palabra recibe como máximo `⌈B/L⌉` errores. Se corrige la ráfaga si cada palabra queda con a lo sumo `t = 2` errores:

**Ráfaga máxima corregible = `t · L = 2 · 50 = 100 bits`.**

(Como detector puro: `5 · 50 = 250` bits.) El costo de entrelazar es la latencia (hay que acumular las 50 palabras) pero no cambia la redundancia (`N/K = 3,5`).

---

## Ejercicio 2 — Arreglo cuadrado de palabras Hamming (3,1,3) con bit de paridad

> Cada fila es una palabra Hamming `(N, K, dmin) = (3, 1, 3)` con bit de paridad. Encuentre la capacidad del código funcionando como corrector y/o detector, especificando la `dmin` y formas de corregir desde un error simple hasta la capacidad expresada (las posiciones erróneas las define usted).
>
> ```
> C1 C2 I1  BP
> C1 C2 I1' BP'
> C1 C2 I1''BP''
> BP BP BP
> ```

### Estructura del código

El Hamming `(3,1,3)` es el de repetición: `C1 = C2 = I1`. Con el bit de paridad de la fila, `BP` = paridad par de `C1 C2 I1` = el mismo bit, así que **cada fila es el bit de información repetido 4 veces**. La última fila lleva la **paridad de cada columna** (sin bit esquina), y como las columnas `C1`, `C2` e `I1` valen `I1, I1', I1''` en cada fila, la fila final es el XOR `p = I1 ⊕ I1' ⊕ I1''` repetido 3 veces.

- `K = 3` bits de información (uno por fila: `I1`, `I1'`, `I1''`)
- `N = 4 + 4 + 4 + 3 = 15`
- Redundancia `N/K = 15/3 = 5`

Palabra: `(i₁ i₁ i₁ i₁)(i₂ i₂ i₂ i₂)(i₃ i₃ i₃ i₃)(p p p)` con `p = i₁ ⊕ i₂ ⊕ i₃`.

### Distancia mínima

| Info `i₁ i₂ i₃` | Palabra | Peso |
|---|---|---|
| 000 | `0000 0000 0000 000` | 0 |
| 100 | `1111 0000 0000 111` | **7** |
| 010 | `0000 1111 0000 111` | **7** |
| 001 | `0000 0000 1111 111` | **7** |
| 110 | `1111 1111 0000 000` | 8 |
| 101 | `1111 0000 1111 000` | 8 |
| 011 | `0000 1111 1111 000` | 8 |
| 111 | `1111 1111 1111 111` | 15 |

Código lineal ⇒ `dmin` = peso mínimo no nulo = **`dmin = 7`**. (Un solo bit de información en 1 aporta 4 bits de su fila + 3 de la fila de paridad.)

### Capacidad

| Modo | Capacidad |
|---|---|
| **Corrector puro** | `2t + 1 ≤ 7 ⇒ t = ` **3 errores** |
| **Detector puro** | `dmin − 1 = ` **6 errores** |
| **Mixto** (`t + s + 1 ≤ 7`, `s ≥ t`) | corrige 3 y detecta 3 · corrige 2 y detecta 4 · corrige 1 y detecta 5 |

### Formas de corregir (elijo las posiciones erróneas)

Información `I1 I1' I1'' = 1 0 0`. **Palabra enviada** (se transmite fila por fila):

`1111 0000 0000 111` → `111100000000111` (15 bits)

| | C1 | C2 | I1 | BP |
|---|---|---|---|---|
| fila 1 | 1 | 1 | 1 | 1 |
| fila 2 | 0 | 0 | 0 | 0 |
| fila 3 | 0 | 0 | 0 | 0 |
| paridad de columnas | 1 | 1 | 1 | |

**Cómo se llena cada celda del arreglo del enunciado** (las posiciones `C1 C2 I1 BP` son las del enunciado, no una cadena aparte):

| Celda | Regla | Fila 1 (`I1 = 1`) | Fila 2 (`I1' = 0`) | Fila 3 (`I1'' = 0`) |
|---|---|---|---|---|
| `I1` | bit de información elegido | 1 | 0 | 0 |
| `C1` | Hamming (3,1,3): copia de `I1` | 1 | 0 | 0 |
| `C2` | Hamming (3,1,3): copia de `I1` | 1 | 0 | 0 |
| `BP` | paridad par de `C1 C2 I1` | 1 | 0 | 0 |

Fila inferior (`BP BP BP`): paridad par de cada columna: `C1`: `1⊕0⊕0 = 1`; `C2`: `1`; `I1`: `1`.

La "palabra enviada" es simplemente el arreglo leído fila por fila: `1111`, `0000`, `0000`, `111`.

Reglas de lectura:

- **Paridad de fila** (`BP` de cada fila contra su `C1 C2 I1`) y **paridad de columna** (fila inferior contra la columna).
- **Voto por mayoría** dentro de cada fila (la palabra `(3,1,3)` corrige 1 error por sí sola).
- **Decisión final: mínima distancia** a las 8 palabras válidas (garantizado hasta 3 errores: se verificó que, para todo patrón de 0 a 3 errores, hay una única palabra más cercana).

**Un error simple** — se invierte `C2` de la fila 2:

```
1 1 1 | 1
0 1 0 | 0   ← error (fila 2, columna C2)
0 0 0 | 0
1 1 1
```

- Falla la paridad de la **fila 2** (`0 1 0` tiene un 1 pero `BP = 0`).
- Falla la paridad de la **columna C2** (`1,1,0` ⇒ paridad 0 contra el 1 transmitido).
- Fila y columna se cruzan en `(fila 2, C2)` ⇒ se corrige ese bit. (Además la mayoría de la fila 2 es 0, que coincide.)
- Si falla **sólo** una fila, el error está en su `BP`; si falla **sólo** una columna, el error está en la fila de paridad de columnas.

**Dos errores** — se invierten `C1` y `C2` de la fila 1 (ambos en la misma fila):

```
0 0 1 | 1       ← dos errores en la fila 1
0 0 0 | 0
0 0 0 | 0
1 1 1
```

- La paridad de la fila 1 **no** detecta el doble error (`0 0 1` tiene un 1 y `BP = 1`).
- Fallan las columnas `C1` y `C2` ⇒ hay un error, pero la cruz fila/columna no lo localiza.
- El voto por mayoría de la fila (`0 0 1 1`) es un empate.
- **Se decide por mínima distancia:** distancia a `100…` = 2; a `000…` = 5 ⇒ se corrige a la palabra de información `1 0 0` (se reponen `C1` y `C2` de la fila 1).

**Tres errores (límite de corrección, `t = 3`)** — se invierten `C1`, `C2` e `I1` de la fila 1:

```
0 0 0 | 1       ← tres errores en la fila 1
0 0 0 | 0
0 0 0 | 0
1 1 1
```

- Distancia a la palabra enviada (`1 0 0`): **3**; a la palabra todo ceros: **4**.
- La mínima distancia sigue siendo única (3 < 4) ⇒ se corrige a `1 0 0` ✓. Por voto por mayoría la fila 1 daría 0 (¡equivocado!); acá lo que salva el caso es la paridad de columnas, que obliga a decidir por distancia sobre todo el arreglo.

**Cuatro errores (se excede `t`)** — se invierten los cuatro bits de la fila 1:

```
0 0 0 | 0
0 0 0 | 0
0 0 0 | 0
1 1 1
```

- Distancia a `100…` = 4; a `000…` = **3** ⇒ el decodificador "corrige" mal a `0 0 0`: el arreglo se acepta con un error de **información no detectado como tal** (sólo queda la señal de las columnas que fallan).
- Como **detector** el código sí detecta hasta 6 errores; si el decodificador **no corrige** y sólo detecta, la palabra recibida con 4 errores no es válida y se pide retransmisión.
- Con **7 errores** (los 7 bits de peso de otra palabra) se llega a otra palabra válida: **no se detecta**. Es la capacidad máxima (`dmin = 7`).

**Observación:** un arreglo rectangular genérico sin bit esquina tiene `dmin = 3`. Acá la `dmin` es 7 porque las filas **no son libres**: cada fila es un código de repetición `(4,1)` y la fila de paridad cubre las tres.

---

## Teóricas

### Inciso a) ISBN₁₁ `45?989012-X`: dígito faltante, características y ventaja de la base prima

**Dígito faltante.** Base 11 (ISBN-10), pesos `10 … 1`, `X = 10`:

| Posición | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Símbolo | 4 | 5 | `?` | 9 | 8 | 9 | 0 | 1 | 2 | X (=10) |
| Peso | 10 | 9 | **8** | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
| Producto | 40 | 45 | `8?` | 63 | 48 | 45 | 0 | 3 | 4 | 10 |

`S = 40 + 45 + 63 + 48 + 45 + 0 + 3 + 4 + 10 = 258` y `258 = 23·11 + 5 ⇒ S ≡ 5 (mod 11)`.

La suma total tiene que ser múltiplo de 11, o sea `258 + 8·?` debe ser múltiplo de 11. Ya sabemos que `258` deja resto 5, así que `8·?` tiene que dejar resto `11 − 5 = 6`.

Buscamos un número que deje resto 6 al dividirlo por 11 **y** sea múltiplo de 8. Se prueba sumando 11 hasta que aparezca un múltiplo de 8:

`6` no · `17` no · `28` no · `39` no · `50` no · `61` no · **`72` sí** (`72 = 8·9`)

Entonces `8·? = 72` ⇒ **`? = 9`**.

**Otra forma — probar directamente `8x + 5` para `x = 0, 1, …, 9`** (hay que llegar a `0 mod 11`):

| `x` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| `8x + 5` | 5 | 13 | 21 | 29 | 37 | 45 | 53 | 61 | 69 | **77** |
| `mod 11` | 5 | 2 | 10 | 7 | 4 | 1 | 9 | 6 | 3 | **0** |

`77 = 7·11` ⇒ **`x = 9`**. (Atajo: cada vez que `x` sube 1, `8x + 5` sube 8, o sea baja 3 módulo 11.)

**Resultado: `45` **`9`** `989012-X`**. Verificación: `258 + 8·9 = 330 = 30·11` ✓.

**Características del código ISBN₁₁:**

- **10 símbolos:** 9 de información + 1 de chequeo (el último) ⇒ `N = 10`, `K = 9`, redundancia `N/K = 10/9 ≈ 1,11`.
- **Base 11 (prima):** símbolos `0–9` y `X` (= 10); pesos `10, 9, …, 1`; es válido si `Σ dᵢ·wᵢ ≡ 0 (mod 11)`.
- **`dmin = 2`:** **detecta 1 error** y **no corrige** (corregir pediría `dmin ≥ 3`). Detecta además las transposiciones de dos dígitos. Sólo se puede *recuperar* un dígito cuando se **conoce su posición** (como se hizo arriba con el dígito faltante).

**Ventaja de la base prima:** como 11 es primo, **todo peso `wᵢ` (1 a 10) tiene inverso módulo 11**. Consecuencias:

- **Error simple:** si un dígito cambia en `δ ≠ 0`, la suma cambia en `wᵢ·δ`, producto de dos números no nulos módulo un primo, que **nunca es múltiplo de 11** ⇒ **siempre se detecta**.
- **Transposición:** intercambiar `dᵢ` y `dⱼ` cambia la suma en `(wᵢ − wⱼ)(dⱼ − dᵢ)`; con pesos todos distintos y base prima eso **no es múltiplo de 11** salvo que los dígitos sean iguales ⇒ **se detecta**.
- **Dígito faltante:** `wᵢ·? ≡ −S (mod 11)` tiene **solución única** porque `wᵢ` tiene inverso (acá `8⁻¹ = 7`). En una base no prima (por ejemplo 10) un peso como 2 ó 5 no tiene inverso y la solución podría no existir o no ser única.

**Complemento — ISBN con 10 vs 13 dígitos:**

| | ISBN-10 | ISBN-13 |
|---|---|---|
| Base / módulo | 11 (prima), símbolos `0–9` y `X` | 10 |
| Pesos | `10, 9, …, 1` (todos distintos) | `1, 3, 1, 3, …` (alternados) |
| Bits de chequeo / `K` | 1 de 10 ⇒ `N/K = 10/9 = 1,11` | 1 de 13 ⇒ `N/K = 13/12 = 1,08` |
| Error simple | **detecta todos** | **detecta todos** |
| Transposición de **adyacentes** | **detecta todas** | **no detecta** las de dígitos que difieren en 5 (ej. `2` y `7`) |
| Inconveniente | necesita el símbolo `X` | ninguno de notación |

- **Capacidad en ambos:** `dmin = 2` ⇒ **detectan 1 error, no corrigen** (para corregir haría falta `dmin ≥ 3`). Sólo se puede *recuperar* un dígito cuando se **sabe su posición** (como se hizo arriba).
- ISBN-10 es **mejor detector** por usar base prima y pesos todos distintos (`wᵢ − wⱼ ≠ 0` y con inverso); ISBN-13 sacrifica poder de detección (módulo 10 no es primo, pesos repetidos 1,3) a cambio de menor redundancia y de eliminar el `X`.

### Inciso b) Voyager 1: distancia y tipo de codificación

**Distancia.** Un día luz es lo que recorre la luz en un día:

`d = c · t = 299 792,458 km/s · 86 400 s ≈ 2,59 × 10¹⁰ km ≈ 25 900 millones de km`

(unas 173 veces la distancia Tierra–Sol: `25,9·10⁹ / 149,6·10⁶ ≈ 173 UA`). Una señal tarda **24 horas** en llegar, y una consulta con su respuesta, **48 horas**.

**Tipo de codificación: CORRECTORA (FEC, *Forward Error Correction*).** Justificación:

1. **No se puede retransmitir.** Un código detector exige pedir reenvío (ARQ): cada ciclo cuesta 2 días de ida y vuelta, y el dato original puede ya no estar disponible o ser irrepetible (una observación puntual).
2. **Canal muy ruidoso:** señal extremadamente débil (transmisor de ~20 W, tasa de unos cientos de bit/s), `p` de error alto; con tanta pérdida los reenvíos fallarían a su vez.
3. **Redundancia aceptable:** a cambio de más bits por mensaje, el receptor repara los errores solo.

Voyager usó códigos correctores de errores: el **Golay extendido (24,12)** para las imágenes de Júpiter y Saturno (`dmin = 8`: corrige 3 errores y detecta 4) y, desde Urano/Neptuno, la **concatenación de un código convolucional (rate 1/2, `K = 7`) con Reed–Solomon (255,223)** (corrige hasta 16 bytes por bloque), y el entrelazado para soportar ráfagas.

---

## Resumen de resultados

| Punto | Resultado |
|---|---|
| Cripto 1.a (Holmes) | `mcd(21, 36) = 3 ≠ 1` ⇒ `a` sin inverso, el afín no es biyectivo ⇒ indescifrable |
| Cripto 1.b | `25⁻¹ = 13` ⇒ clave `(13, 7, 36)`; texto: **LO INESPERADO SIEMPRE OCURRE** |
| Cripto 2 (firma) | Bruno: `R = M^(e⁻¹_b) mod n_b`; Alicia: `R^(e_b) mod n_b = M` (variante con hash: `R = H(M)^(e⁻¹_b)`, compara con `H(M)`) ⇒ autenticidad, integridad, no repudio |
| Imágenes | RLE PCX: `11cccccc` = contador (1..63); dato suelto `≥ 192` ⇒ `193, dato`; repeticiones `> 63` ⇒ varios pares |
| CE 1.a | `(14, 4, 6)`, `g(x) = 1 + x + x³ + x⁷ + x⁸ + x¹⁰`, `h(x) = 1 + x + x² + x⁴`, redundancia 3,5; corrige 2 / detecta 5 |
| CE 1.b | `H = [I₁₀ \| Pᵀ]` (10 × 14) |
| CE 1.c | `10101101000110` inválida, `S = x²`, error en posición 3 ⇒ `10001101000110`, info `0110` |
| CE 1.d | `t·L = 2·50 = 100` bits de ráfaga |
| CE 2 | `N = 15, K = 3, dmin = 7` ⇒ corrige 3 / detecta 6 |
| Teórica a | ISBN: dígito faltante **9**; `dmin = 2` (detecta 1, no corrige); base prima ⇒ pesos con inverso |
| Teórica b | `≈ 2,59·10¹⁰ km`; codificación **correctora** (FEC) |
