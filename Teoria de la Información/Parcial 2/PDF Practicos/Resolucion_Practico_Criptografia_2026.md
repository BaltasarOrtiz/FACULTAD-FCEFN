# Resolución — Práctico de Criptografía 2026 (Área Temática 2)

Teoría de la Información · Licenciatura en Ciencias de la Computación · 2026

> Todos los cálculos fueron verificados por computadora; acá se muestra el procedimiento a mano para que se pueda reproducir en el examen.

## Convenciones usadas (las de la teoría del Parcial 2)

- **Alfabeto de 27 letras**, `n = 27`, con numeración desde 0:

  | A | B | C | D | E | F | G | H | I | J | K | L | M | N | Ñ | O | P | Q | R | S | T | U | V | W | X | Y | Z |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

- Los espacios y signos de puntuación **no se cifran**: se copian tal cual (solo cambian las letras).
- **César generalizado**: `C_i = (M_i + k) mod n`  ·  `M_i = (C_i − k) mod n = (C_i + k⁻¹) mod n`, donde `k⁻¹ = n − k` es el **inverso aditivo** de `k` en `(ℤₙ, +)`.
- **Vigenère**: `C_i = (M_i + K_{i mod L}) mod n`  ·  `K_i = (C_i − M_i) mod n`.
- **Transposición por bloques** de longitud `N` con clave `K = (k₁,…,k_N)`: el texto se parte en bloques de `N` y el carácter `j` del criptograma es el `k_j`-ésimo del bloque, `C_j = M_{k_j}`. Si el último bloque queda incompleto se rellena con `X`. Para descifrar se usa la **permutación inversa** `K⁻¹`, donde `K_j = i ⇒ K⁻¹_i = j`.
- **Afín / "César por bloques"**: `E(m) = (a·m + b) mod N`, con `gcd(a, N) = 1`; `D(c) = a⁻¹·(c − b) mod N`.
- **RSA**: `n = p·q`, `φ(n) = (p−1)(q−1)`, `gcd(e, φ) = 1`, `d = e⁻¹ mod φ`. Cifrar `C = Mᵉ mod n`, descifrar `M = Cᵈ mod n`. Firmar `S = M^{d_emisor} mod n_emisor`, verificar `M = S^{e_emisor} mod n_emisor`.
- **LFSR de Fibonacci** (el que se usa en criptografía): `f(x) = xⁿ + C_{n−1}xⁿ⁻¹ + … + C₁x + 1`; la celda de salida es la última, y el bit nuevo entra por la primera como XOR de las celdas con coeficiente 1.

---

## Ejercicio 1

> 1. Cifrar con sustitución monoalfabética de Cesar (generalizada) el texto
>
> AL PAN PAN, Y AL VINO...

Valores numéricos del texto (solo letras):

| Letra | A | L | P | N | Y | V | I | O |
|---|---|---|---|---|---|---|---|---|
| `M` | 0 | 11 | 16 | 13 | 25 | 22 | 8 | 15 |

### Inciso 1.a)

> a) Para k=4

Cálculo: `C = (M + 4) mod 27`

| Letra | A | L | P | N | Y | V | I | O |
|---|---|---|---|---|---|---|---|---|
| `M + 4` | 4 | 15 | 20 | 17 | 29 | 26 | 12 | 19 |
| `mod 27` | 4 | 15 | 20 | 17 | **2** | 26 | 12 | 19 |
| `C` | E | O | T | Q | C | Z | M | S |

```
M:  AL PAN PAN, Y AL VINO...
C:  EO TEQ TEQ, C EO ZMQS...
```

### Inciso 1.b)

> b) Para k=18

Cálculo: `C = (M + 18) mod 27`

| Letra | A | L | P | N | Y | V | I | O |
|---|---|---|---|---|---|---|---|---|
| `M + 18` | 18 | 29 | 34 | 31 | 43 | 40 | 26 | 33 |
| `mod 27` | 18 | **2** | **7** | **4** | **16** | **13** | 26 | **6** |
| `C` | R | C | H | E | P | N | Z | G |

```
M:  AL PAN PAN, Y AL VINO...
C:  RC HRE HRE, P RC NZEG...
```

### Pregunta final del ejercicio 1

> ¿Este algoritmo presenta una estructura de grupo? Justifique su respuesta.

**Sí: César es un grupo abeliano**, isomorfo a `(ℤ₂₇, +)`. Sea `E_k(m) = m + k mod 27`:

| Propiedad | Verificación |
|---|---|
| **Cerrado** | `E_{k₂}(E_{k₁}(m)) = m + k₁ + k₂ = E_{k₁+k₂}(m)`: cifrar dos veces equivale a cifrar con **otra clave del mismo conjunto**. |
| **Asociativo** | Heredado de la suma modular. |
| **Elemento neutro** | `k = 0` (`E₀(m) = m`). |
| **Inverso** | Para cada `k` existe `−k = 27 − k` tal que `E_{−k}(E_k(m)) = m`. |
| **Conmutativo** | `k₁ + k₂ = k₂ + k₁`. |

Ejemplo con el texto del enunciado: `PAN` con `k = 4` da `TEQ`; ese resultado cifrado de nuevo con `k = 18` da `LVI`. Con una sola clave `4 + 18 = 22`: `PAN → LVI`. Es lo mismo.

**Consecuencia:** el **cifrado múltiple no aumenta la seguridad** (siempre equivale a un único César) y el espacio de claves sigue siendo 27 (26 útiles). Por eso es vulnerable a fuerza bruta y a análisis de frecuencias. (Contraste: DES **no** es un grupo, y por eso 3‑DES sí mejora la seguridad.)

---

## Ejercicio 2

> 2. Dado el siguiente criptograma YAMNMYOAYPY, descifrarlo, sabiendo que fue cifrado con una sustitución monoalfabética de César cuya clave k es 12. Mantenga la misma estructura del algoritmo, es decir para descifrar utilice la fórmula Dk(mi)=ci+k-1mod(27).
> Hallar el criptograma que se obtiene al aplicar el cifrado por el método de transposición de bloques de longitud n=7 y clave k=(3 7 2 6 4 1 5).
>
> NO POR MUCHO MADRUGAR...

(El ejercicio tiene dos pedidos: el descifrado de `YAMNMYOAYPY` y el cifrado por transposición de `NO POR MUCHO MADRUGAR...`.)

### 2.a) Primer pedido: descifrar `YAMNMYOAYPY`

> Dado el siguiente criptograma YAMNMYOAYPY, descifrarlo, sabiendo que fue cifrado con una sustitución monoalfabética de César cuya clave k es 12. Mantenga la misma estructura del algoritmo, es decir para descifrar utilice la fórmula Dk(mi)=ci+k-1mod(27).

Se mantiene la estructura: `D_k(c_i) = (c_i + k⁻¹) mod 27`, con `k⁻¹ = 27 − 12 = 15`.

| Cripto | Y | A | M | N | M | Y | O | A | Y | P | Y |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `c` | 25 | 0 | 12 | 13 | 12 | 25 | 15 | 0 | 25 | 16 | 25 |
| `c + 15` | 40 | 15 | 27 | 28 | 27 | 40 | 30 | 15 | 40 | 31 | 40 |
| `mod 27` | 13 | 15 | 0 | 1 | 0 | 13 | 3 | 15 | 13 | 4 | 13 |
| `m` | N | O | A | B | A | N | D | O | N | E | N |

**Texto en claro: `NOABANDONEN`** → «NO ABANDONEN».

### 2.b) Segundo pedido: transposición de bloques

> Hallar el criptograma que se obtiene al aplicar el cifrado por el método de transposición de bloques de longitud n=7 y clave k=(3 7 2 6 4 1 5).
>
> NO POR MUCHO MADRUGAR...

Texto: `NO POR MUCHO MADRUGAR...` → sin espacios ni puntos: `NOPORMUCHOMADRUGAR` (19 letras). Se rellena con `XX` para completar 3 bloques de 7 (21 caracteres).

Con `C_j = M_{k_j}`: la posición `j` del criptograma toma la letra `k_j` del bloque.

| Bloque | Posiciones 1‥7 | `M₃ M₇ M₂ M₆ M₄ M₁ M₅` | Cifrado |
|---|---|---|---|
| 1 | N O P O R M U | P U O M O N R | `PUOMONR` |
| 2 | C H O M A D R | O R H D M C A | `ORHDMCA` |
| 3 | U G A R X X X | A X G X R U X | `AXGXRUX` |

**Criptograma: `PUOMONRORHDMCAAXGXRUX`**

---

## Ejercicio 3

> 3. Para el ejercicio anterior encuentre la clave de descifrado y aplíquela al texto cifrado para volver al texto en claro

La clave de descifrado es la **permutación inversa**: si `K_j = i`, entonces `K⁻¹_i = j`.

| `j` | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| `K_j` | 3 | 7 | 2 | 6 | 4 | 1 | 5 |

Armamos `K⁻¹` mirando en qué posición `j` está cada `i = 1…7` de `K`:

| `i` | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| `K⁻¹_i` (posición de `i` en `K`) | 6 | 3 | 1 | 5 | 7 | 4 | 2 |

**`K⁻¹ = (6 3 1 5 7 4 2)`**

Se aplica `K⁻¹` bloque a bloque sobre el criptograma (`C'_j = C_{k⁻¹_j}`):

| Bloque cifrado | `C₆ C₃ C₁ C₅ C₇ C₄ C₂` | Resultado |
|---|---|---|
| `PUOMONR` | N O P O R M U | `NOPORMU` |
| `ORHDMCA` | C H O M A D R | `CHOMADR` |
| `AXGXRUX` | U G A R X X X | `UGARXXX` |

Texto recuperado: `NOPORMUCHOMADRUGARXXX` → «NO POR MUCHO MADRUGAR» (las `X` finales son relleno). ✔

---

## Ejercicio 4

> 4. Un sistema de cifrado que usa el método de sustitución polialfabética de Vigenère, es vulnerado, interceptando un mensaje del que se dispone el criptograma y el mensaje en claro. Sabiendo que la clave tiene longitud 8 y que la pareja mensaje en claro y criptograma son los siguientes:
> Mensaje en claro:
>
> ESLOINESPERADOLOQUESIEMPREOCURRE
>
> Criptografía:
>
> GHVDAFYLRSCOVHFHSJOHAWGITSZQNKMW

(Este ejercicio se completa con el 5, que pide encontrar y verificar la clave. Acá se encuentra la clave.)

Datos: clave de longitud `L = 8`. Como `C_i = M_i + K_i mod 27`, la clave se despeja con `K_i = (C_i − M_i) mod 27`.

Se parte el mensaje en bloques de 8 (largo de la clave):

| Bloque | Claro | Cripto |
|---|---|---|
| 1 | `ESLOINES` | `GHVDAFYL` |
| 2 | `PERADOLO` | `RSCOVHFH` |
| 3 | `QUESIEMP` | `SJOHAWGI` |
| 4 | `REOCURRE` | `TSZQNKMW` |

Cálculo del **primer bloque** (`K = C − M mod 27`):

| `i` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| `M` | E=4 | S=19 | L=11 | O=15 | I=8 | N=13 | E=4 | S=19 |
| `C` | G=6 | H=7 | V=22 | D=3 | A=0 | F=5 | Y=25 | L=11 |
| `C − M` | 2 | −12 | 11 | −12 | −8 | −8 | 21 | −8 |
| `mod 27` | **2** | **15** | **11** | **15** | **19** | **19** | **21** | **19** |
| Letra | C | O | L | O | S | S | U | S |

**Clave: `COLOSSUS`** (longitud 8, coincide con el dato del enunciado).

> Si se hiciera el mismo cálculo con 26 letras (sin Ñ) la clave **no** se repite entre bloques (`CPKPSSUT`, `COLOSTUT`, …). Eso confirma que el sistema trabaja con el alfabeto de 27 letras.

---

## Ejercicio 5

> 5. Encontrar la clave de cifrado y verificarla para todo el mensaje.

Se cifra con `K = COLOSSUS = (2, 15, 11, 15, 19, 19, 21, 19)` repetida cuatro veces y se compara con el criptograma dado:

| Bloque | `M` (valores) | `K` repetida | `M + K mod 27` | Letras | ¿= criptograma? |
|---|---|---|---|---|---|
| 1 | 4 19 11 15 8 13 4 19 | 2 15 11 15 19 19 21 19 | 6 7 22 3 0 5 25 11 | `GHVDAFYL` | ✔ |
| 2 | 16 4 18 0 3 15 11 15 | 2 15 11 15 19 19 21 19 | 18 19 2 15 22 7 5 7 | `RSCOVHFH` | ✔ |
| 3 | 17 21 4 19 8 4 12 16 | 2 15 11 15 19 19 21 19 | 19 9 15 7 0 23 6 8 | `SJOHAWGI` | ✔ |
| 4 | 18 4 15 2 21 18 18 4 | 2 15 11 15 19 19 21 19 | 20 19 26 17 13 10 12 23 | `TSZQNKMW` | ✔ |

Los 32 caracteres coinciden: la clave `COLOSSUS` se **verifica en todo el mensaje**. El mensaje es «ES LO INESPERADO LO QUE SIEMPRE OCURRE».

---

## Ejercicio 6

> 6. ¿Una transposición de una transposición es más segura que una transposición sola?

**No (en general).** Una transposición es una **permutación** de las posiciones.

- Si las dos usan el **mismo largo de bloque `N`**, la composición de dos permutaciones de `N` elementos es **otra permutación de `N` elementos**: las permutaciones forman un grupo (el grupo simétrico `S_N`). Hay `N!` claves y doblar el cifrado no agrega ninguna: equivale a una única transposición con otra clave. **Mismo espacio de claves, misma seguridad.**
- Si usa **largos de bloque distintos** `N₁` y `N₂`, la composición equivale a una única permutación de largo `mcm(N₁, N₂)`. Ahí el espacio de claves efectivo crece y el ataque es más trabajoso, pero **sigue siendo una transposición**.
- En ambos casos queda el problema de fondo: la transposición solo aporta **difusión**, no confusión. Los símbolos son los mismos, por eso **conserva las frecuencias** (entropía de orden 0) y se puede atacar por anagramas y análisis de frecuencias / patrones. La seguridad real viene de **combinarla con una sustitución** (cifrado de producto, como hacen DES y AES).

Es el mismo argumento que en el ejercicio 1 para César: cuando el conjunto de transformaciones forma un grupo, componer no mejora nada.

---

## Ejercicio 7

> 7. Un criptoanalista intercepta un mensaje cifrado MXDQLWR, y sabe que el emisor solo puede haber enviado uno de los siguientes mensajes: JORGITO, JUANITO o JAIMITO. También sabe que para cifrar, sumó el mismo número a todas las letras del texto en claro (no utilizó la letra Ñ).

Como el emisor **sumó el mismo número `k` a todas las letras** y **no usó la Ñ**, el alfabeto es de **26 letras** (A=0, …, Z=25). Se calcula `k = C − M mod 26` letra por letra para cada candidato:

| | J/M | O/X | R/D | G/Q | I/L | T/W | O/R |
|---|---|---|---|---|---|---|---|
| **JORGITO** → `MXDQLWR` | 9→12: **3** | 14→23: **9** | 17→3: **12** | 6→16: **10** | 8→11: **3** | 19→22: **3** | 14→17: **3** |
| **JUANITO** → `MXDQLWR` | 9→12: **3** | 20→23: **3** | 0→3: **3** | 13→16: **3** | 8→11: **3** | 19→22: **3** | 14→17: **3** |
| **JAIMITO** → `MXDQLWR` | 9→12: **3** | 0→23: **23** | 8→3: **21** | 12→16: **4** | 8→11: **3** | 19→22: **3** | 14→17: **3** |

Solo **JUANITO** da un desplazamiento **constante, `k = 3`** (el César clásico). Los otros dos dan desplazamientos distintos letra a letra, así que no pueden ser.

**Mensaje original: `JUANITO`**, cifrado con `k = 3`.

> Observación: si se usara el alfabeto de 27 letras (con Ñ), la `N` iría a `P` y no a `Q`, y ningún candidato cerraría. Por eso el dato "no utilizó la Ñ" es el que fija el alfabeto de 26.

---

## Ejercicio 8

> 8. El siguiente sistema es una variante del sistema de César, para cifrar un mensaje, que lo divide en bloques de k caracteres, cada bloque lo transforma en un número x y el mensaje encriptado está dado por la sucesión de los números EK(mi)=ami+bmod(N), donde N debe ser mayor que el más grande valor posible de mi y a debe tener inverso módulo N. La clave es el par (a,b). N lo consideramos fijo. Alternativamente, en lugar de los números ci, estos pueden codificarse otra vez como bloques de caracteres que se envían en forma de un mensaje sin sentido. Esto presenta la dificultad de que algunos códigos pueden no tener representación escrita, como sucede en ASCII.

### Inciso 8.a)

> a. Para N fijo, ¿cuántas claves diferentes pueden hallarse si N es un número primo?

La clave es el par `(a, b)`:

- `a` debe tener inverso módulo `N`, o sea `gcd(a, N) = 1`. Como `N` es primo, todo `a ∈ {1, …, N−1}` sirve: **`N − 1` valores** (`a = 0` no es válido: la función dejaría de ser biyectiva).
- `b` puede ser cualquiera: `b ∈ {0, …, N−1}`: **`N` valores**.

**Cantidad de claves = `N·(N − 1)` = `φ(N)·N`.** (Para `N = 131`: `131 · 130 = 17 030`.)

### Inciso 8.b)

> b. Se considera N=131, a=3 y b=7. Codificar el siguiente mensaje donde los bloques son formados con un solo caracter sin tener en cuenta espacios en blanco: HAY GENTE QUE DE SU CENCIA TIENE LA CABEZA LLENA

Mensaje sin espacios: `HAYGENTEQUEDESUCENCIATIENELACABEZALLENA` (39 caracteres, un carácter por bloque, código ASCII). `E(m) = (3m + 7) mod 131`.

| Car. | ASCII `m` | `3m + 7` | `mod 131` |
|---|---|---|---|
| H | 72 | 223 | 92 |
| A | 65 | 202 | 71 |
| Y | 89 | 274 | 12 |
| G | 71 | 220 | 89 |
| E | 69 | 214 | 83 |
| N | 78 | 241 | 110 |
| T | 84 | 259 | 128 |
| Q | 81 | 250 | 119 |
| U | 85 | 262 | 0 |
| D | 68 | 211 | 80 |
| S | 83 | 256 | 125 |
| C | 67 | 208 | 77 |
| I | 73 | 226 | 95 |
| L | 76 | 235 | 104 |
| B | 66 | 205 | 74 |
| Z | 90 | 277 | 15 |

(Cada letra se cifra siempre igual: es una sustitución monoalfabética.) Mensaje completo:

```
H  A  Y  G  E  N   T   E  Q   U  E  D  E  S   U  C  E  N   C  I  A  T   I  E  N   E  L   A  C  A  B  E  Z  A  L   L   E  N   A
92 71 12 89 83 110 128 83 119 0  83 80 83 125 0  77 83 110 77 95 71 128 95 83 110 83 104 71 77 71 74 83 15 71 104 104 83 110 71
```

**Criptograma:** `92, 71, 12, 89, 83, 110, 128, 83, 119, 0, 83, 80, 83, 125, 0, 77, 83, 110, 77, 95, 71, 128, 95, 83, 110, 83, 104, 71, 77, 71, 74, 83, 15, 71, 104, 104, 83, 110, 71`

### Inciso 8.c)

> c. Hallar la función inversa Dk(mi)=a-1ci+d mod(N) de Ek(mi)=ami+b mod(N) que permita el desencriptado del mensaje anterior.

Despejamos: `c = a·m + b ⇒ m = a⁻¹(c − b) = a⁻¹·c − a⁻¹·b`, o sea `d = −a⁻¹·b mod N`.

**Inverso de `a = 3` mod 131** (Euclides extendido):

```
131 = 43·3 + 2
  3 =  1·2 + 1
  1 = 3 − 1·2 = 3 − (131 − 43·3) = 44·3 − 1·131
```

⇒ `3⁻¹ ≡ 44 (mod 131)` (comprobación: `3·44 = 132 = 131 + 1` ✔).

`d = −44·7 mod 131 = −308 mod 131`; `308 = 2·131 + 46` ⇒ `−308 ≡ −46 ≡ 85`.

**`D_K(c) = 44·c + 85 mod 131`**

Comprobación: `D(92) = 44·92 + 85 = 4133 = 31·131 + 72 → 72 = H` ✔; `D(0) = 85 = U` ✔.

### Inciso 8.d)

> d. Desencriptar el mensaje siguiente encriptado en dicho sistema por bloques de un caracter, sabiendo que N=131, el último número corresponde a un símbolo de puntuación y que los caracteres más frecuentes en idioma Castellano son, por su orden: e, a, o, l, s. No se consideran espacios en blanco. Se trabaja en ASCII.
> 42, 109, 49, 100, 19, 69, 99, 89, 129, 100, 60, 79, 99, 100, 59, 90, 100, 99,
> 49, 129, 80, 130, 69, 100, 39, 60, 79, 99, 100, 59, 90, 100, 99, 80, 69, 109,
> 60, 109, 70, 129, 100, 59, 60, 109, 74

Criptograma (45 números): `42, 109, 49, 100, 19, 69, 99, 89, 129, 100, 60, 79, 99, 100, 59, 90, 100, 99, 49, 129, 80, 130, 69, 100, 39, 60, 79, 99, 100, 59, 90, 100, 99, 80, 69, 109, 60, 109, 70, 129, 100, 59, 60, 109, 74`

**Paso 1 — Frecuencias del criptograma** (45 símbolos):

| Número | 100 | 99 | 109 | 60 | 69 | 129 | 59 | 49 | 79 | 90 | 80 | resto (1 c/u) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Veces | **8** | 5 | 4 | 4 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 42,19,89,130,39,70,74 |

**Paso 2 — Hipótesis.** El más frecuente (`100`) es la `e` (ASCII 101). Además, el último número `74` es un signo de puntuación; el más probable al final de una frase es el punto (ASCII 46). Dos pares claro → cifrado dan dos ecuaciones para `(a, b)`:

```
a·101 + b ≡ 100  (mod 131)      (e → 100)
a· 46 + b ≡  74  (mod 131)      (. → 74)
```

Restando: `55·a ≡ 26 (mod 131)`. Se despeja con el inverso de 55 o, a mano, probando múltiplos: `55·10 = 550 = 4·131 + 26 ≡ 26` ✔ ⇒ **`a = 10`** (es única, porque 131 es primo).
Luego `b = 100 − 101·10 = −910 ≡ −910 + 7·131 = 7` ⇒ **`b = 7`**.

*(Alternativa del apunte: fijar `e → 100` y probar la segunda letra de la lista `a, o, l, s` contra el siguiente número más frecuente. Con `a → 99` y `a → 109` el desencriptado da basura no imprimible; con `a → 60` sale `a = 10, b = 7` y texto con sentido, que es la validación.)*

**Paso 3 — Clave de cifrado `E(m) = 10·m + 7 mod 131`.** Su inversa: `10⁻¹ mod 131 = 118` (`10·118 = 1180 = 9·131 + 1` ✔):

**`D(c) = 118·(c − 7) mod 131`**

**Paso 4 — Desencriptar** (`m = 118·(c − 7) mod 131`):

| `c` | 42 | 109 | 49 | 100 | 19 | 69 | 99 | 89 | 129 | 100 | 60 | 79 | 99 | 100 | 59 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `m` | 69 | 115 | 109 | 101 | 106 | 111 | 114 | 113 | 117 | 101 | 97 | 112 | 114 | 101 | 110 |
| car. | E | s | m | e | j | o | r | q | u | e | a | p | r | e | n |

| `c` | 90 | 100 | 99 | 49 | 129 | 80 | 130 | 69 | 100 | 39 | 60 | 79 | 99 | 100 | 59 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `m` | 100 | 101 | 114 | 109 | 117 | 99 | 104 | 111 | 101 | 108 | 97 | 112 | 114 | 101 | 110 |
| car. | d | e | r | m | u | c | h | o | e | l | a | p | r | e | n |

| `c` | 90 | 100 | 99 | 80 | 69 | 109 | 60 | 109 | 70 | 129 | 100 | 59 | 60 | 109 | 74 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `m` | 100 | 101 | 114 | 99 | 111 | 115 | 97 | 115 | 98 | 117 | 101 | 110 | 97 | 115 | 46 |
| car. | d | e | r | c | o | s | a | s | b | u | e | n | a | s | . |

**Mensaje:** `Esmejorqueaprendermuchoelaprendercosasbuenas.`
→ «**Es mejor que aprender mucho el aprender cosas buenas.**»

Comprobación: `E(101) = 1017 = 7·131 + 100 → 100` ✔ y `E(46) = 467 = 3·131 + 74 → 74` ✔.

---

## Ejercicio 9

> 9. Para el polinomio primitivo f(x) = x5 + x2 + 1, se pide:

### Inciso 9.a)

> a. Dibujar el registro de desplazamientos LSFR

Con `f(x) = x⁵ + x² + 1` los coeficientes distintos de cero son `C₅ = 1` y `C₂ = 1`, entonces:

`a(t) = a(t−2) ⊕ a(t−5)`

Celdas `S₁ S₂ S₃ S₄ S₅`; sale la celda `S₅`; el bit nuevo entra por `S₁` y vale `S₂ ⊕ S₅`.

```
   ┌──────────────────────────────────────────────┐
   │                                              │
   ▼                                              │
  ┌────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐      │
  │ S1 │──►│ S2 │──►│ S3 │──►│ S4 │──►│ S5 │──────┼──► salida (secuencia cifrante)
  └────┘   └──┬─┘   └────┘   └────┘   └────┘      │
     ▲        │ (x²)                     (x⁵)      │
     │        ▼                                   │
     └────────⊕◄───────────────────────────────────┘
        nuevo S1 = S2 ⊕ S5
```

Lectura: el bit nuevo `S₁ = S₂ ⊕ S₅`; luego todo se corre a la derecha (`S₅ ← S₄ ← S₃ ← S₂ ← S₁`); la salida es el bit que abandona `S₅`.

### Inciso 9.b)

> b. Si la semilla es S=10000, encontrar la secuencia cifrante. ¿Cuál es su período?

Semilla: `S₁S₂S₃S₄S₅ = 1 0 0 0 0`. En cada pulso: salida `= S₅`, `nuevo = S₂ ⊕ S₅`, desplazamiento a la derecha.

| Pulso | Estado `S₁…S₅` | Salida `S₅` | Nuevo `S₂ ⊕ S₅` |
|---|---|---|---|
| 1 | 10000 | 0 | 0⊕0 = 0 |
| 2 | 01000 | 0 | 1⊕0 = 1 |
| 3 | 10100 | 0 | 0⊕0 = 0 |
| 4 | 01010 | 0 | 1⊕0 = 1 |
| 5 | 10101 | 1 | 0⊕1 = 1 |
| 6 | 11010 | 0 | 1⊕0 = 1 |
| 7 | 11101 | 1 | 1⊕1 = 0 |
| 8 | 01110 | 0 | 1⊕0 = 1 |
| 9 | 10111 | 1 | 0⊕1 = 1 |
| 10 | 11011 | 1 | 1⊕1 = 0 |
| 11 | 01101 | 1 | 1⊕1 = 0 |
| 12 | 00110 | 0 | 0⊕0 = 0 |
| 13 | 00011 | 1 | 0⊕1 = 1 |
| 14 | 10001 | 1 | 0⊕1 = 1 |
| 15 | 11000 | 0 | 1⊕0 = 1 |
| 16 | 11100 | 0 | 1⊕0 = 1 |
| 17 | 11110 | 0 | 1⊕0 = 1 |
| 18 | 11111 | 1 | 1⊕1 = 0 |
| 19 | 01111 | 1 | 1⊕1 = 0 |
| 20 | 00111 | 1 | 0⊕1 = 1 |
| 21 | 10011 | 1 | 0⊕1 = 1 |
| 22 | 11001 | 1 | 1⊕1 = 0 |
| 23 | 01100 | 0 | 1⊕0 = 1 |
| 24 | 10110 | 0 | 0⊕0 = 0 |
| 25 | 01011 | 1 | 1⊕1 = 0 |
| 26 | 00101 | 1 | 0⊕1 = 1 |
| 27 | 10010 | 0 | 0⊕0 = 0 |
| 28 | 01001 | 1 | 1⊕1 = 0 |
| 29 | 00100 | 0 | 0⊕0 = 0 |
| 30 | 00010 | 0 | 0⊕0 = 0 |
| 31 | 00001 | 1 | 0⊕1 = 1 |
| 32 | **10000** | (se repite) | |

**Secuencia cifrante (31 bits): `0000101011101100011111001101001`**

**Período: `T = 31 = 2⁵ − 1`.** Es el máximo posible para un LFSR de 5 celdas, y recorre los 31 estados no nulos: es coherente con que `f(x) = x⁵ + x² + 1` sea **primitivo** (el período es `2ⁿ − 1` con cualquier semilla distinta de cero).

### Inciso 9.c)

> c. Con la secuencia cifrante, cifrar ENIGMA (considere el alfabeto ASCII para la representación del mensaje).

`C = M ⊕ S` (XOR bit a bit). El mensaje tiene `6 × 8 = 48` bits, así que se usan los 31 bits de la secuencia y los 17 primeros otra vez (la secuencia se repite).

| Car. | ASCII (dec) | Binario |
|---|---|---|
| E | 69 | 01000101 |
| N | 78 | 01001110 |
| I | 73 | 01001001 |
| G | 71 | 01000111 |
| M | 77 | 01001101 |
| A | 65 | 01000001 |

```
M : 01000101 01001110 01001001 01000111 01001101 01000001
S : 00001010 11101100 01111100 11010010 00010101 11011000
C : 01001111 10100010 00110101 10010101 01011000 10011001
    (79)     (162)    (53)     (149)    (88)     (153)
```

**Criptograma:** `010011111010001000110101100101010101100010011001`

Para descifrar se aplica exactamente la misma operación (`M = C ⊕ S`) con la misma semilla, porque XOR es una involución.

> Nota: la secuencia depende de la convención del circuito (Fibonacci con salida en `S₅`, como se usa en criptografía). Con otra convención (Galois, salida por otra celda) la secuencia sale rotada o reordenada, pero el período sigue siendo 31.

---

## Ejercicio 10

> 10. Para un sistema de cifra RSA con p=97 y q=31, se nos dice que podemos usar cualquiera de las siguientes claves públicas.
>
> a) e=24,  b) e=33,  c) e=45,  d) e=49
>
> ¿Cuáles de ellas son válidas y cuáles no? Justifique su respuesta.

```
n  = 97 · 31 = 3007
φ  = (97 − 1)(31 − 1) = 96 · 30 = 2880 = 2⁶ · 3² · 5
```

Una clave pública `e` es válida si `1 < e < φ` y **`gcd(e, φ) = 1`** (si no, `e` no tiene inverso módulo `φ` y no existe `d`). Como `φ = 2⁶·3²·5`, `e` no puede ser múltiplo de 2, 3 ni 5.

| `e` | Factorización | `gcd(e, 2880)` | ¿Válida? |
|---|---|---|---|
| a) 24 | 2³·3 | 24 | ✘ (par y múltiplo de 3) |
| b) 33 | 3·11 | 3 | ✘ (múltiplo de 3) |
| c) 45 | 3²·5 | 45 | ✘ (múltiplo de 3 y de 5) |
| d) 49 | 7² | **1** | ✔ |

**Solo la d) `e = 49` es válida.** Su clave privada se obtiene con Euclides extendido:

```
2880 = 58·49 + 38
  49 =  1·38 + 11
  38 =  3·11 +  5
  11 =  2· 5 +  1

1 = 11 − 2·5
  = 11 − 2·(38 − 3·11) = 7·11 − 2·38
  = 7·(49 − 38) − 2·38 = 7·49 − 9·38
  = 7·49 − 9·(2880 − 58·49) = 529·49 − 9·2880
```

⇒ **`d = 529`** (comprobación: `49·529 = 25 921 = 9·2880 + 1` ✔).

---

## Ejercicio 11

> 11. Paco y Lola se envían mensajes por correo electrónico que desean se mantengan en secreto. Además para evitar los malentendidos y una que otra sorpresa desagradable, todos los mensajes los firman digitalmente. Para todo el proceso utilizan el alfabeto de 28 elementos constituidos por las letras A=0, B=1, …, Ñ=14,…Z=26, y el espacio en blanco (Blanco=27). El sistema de cifra que utilizan en RSA. El grupo de trabajo de cada uno de ellos es:
>
> PACO: ℤnP= 7 * 5 = 35   ୧p = 11
>
> LOLA: ℤnP= 3 * 11 = 33  ୧p = 7

(Este ejercicio solo da los datos; se usan en el ejercicio 12.)

Alfabeto de 28 elementos: `A=0, B=1, …, N=13, Ñ=14, O=15, …, S=19, …, Z=26`, `blanco = 27`. El número del enunciado (`p`) es la clave pública `e` de cada uno.

### Claves

| | `n` | `φ(n)` | `e` pública | `d` privada (`e·d ≡ 1 mod φ`) |
|---|---|---|---|---|
| **Paco** | 7·5 = 35 | 6·4 = 24 | 11 | 11 (`11·11 = 121 = 5·24 + 1`) |
| **Lola** | 3·11 = 33 | 2·10 = 20 | 7 | 3 (`7·3 = 21 = 20 + 1`) |

Datos de los mensajes: Paco → Lola `SI` = (S=19, I=8). Lola → Paco `NO` = (N=13, O=15).

## Ejercicio 12

> 12. Después de una fuerte discusión, Paco envía a Lola el mensaje “SI”, a lo que Lola contesta con el mensaje “NO”. Ambos firman el primer carácter enviado, es decir la letra S para Paco, y la letra N para Lola. Se pide:

### Inciso 12.a)

> a. Enviar los dos mensajes cifrados. Paco: MPaco=M1Paco,M2Paco y Lola: MLola=M1Lola,M2Lola.

Cifrar con la **clave pública del receptor**.

**Paco → Lola** (`n = 33`, `e = 7`): `C = M⁷ mod 33`

- `19⁷ mod 33`: `19² = 361 ≡ 31 ≡ −2`; `19⁴ ≡ 4`; `19⁷ = 19⁴·19²·19 ≡ 4·(−2)·19 = −152 ≡ −152 + 165 = 13`. → **13**
- `8⁷ mod 33`: `8² = 64 ≡ 31 ≡ −2`; `8⁴ ≡ 4`; `8⁷ = 8⁴·8²·8 ≡ 4·(−2)·8 = −64 ≡ −64 + 66 = 2`. → **2**

**`M_Paco = (M1, M2) = (13, 2)`**

**Lola → Paco** (`n = 35`, `e = 11`): `C = M¹¹ mod 35`

- `13¹¹ mod 35`: `13² = 169 ≡ 29 ≡ −6`; `13⁴ ≡ 36 ≡ 1`; `13⁸ ≡ 1`; `13¹¹ = 13⁸·13²·13 ≡ 1·(−6)·13 = −78 ≡ −78 + 105 = 27`. → **27**
- `15¹¹ mod 35`: `15² = 225 ≡ 15` (porque `225 = 6·35 + 15`) ⇒ `15ᵏ ≡ 15` para todo `k ≥ 1`. → **15**

**`M_Lola = (M1, M2) = (27, 15)`**

> El `15` (O) es un **mensaje no cifrable**: `15¹¹ ≡ 15 (mod 35)`, viaja en claro. Con `n = 35` y `e = 11` hay al menos 9 mensajes así (`0, 1, 6, 14, 15, 20, 21, 29, 34`). No es un error de cálculo; es una debilidad de módulos chicos.

### Inciso 12.b)

> b. Firmar cada uno de los mensajes.

Firmar el primer carácter con la **clave privada del emisor**.

**Paco firma la `S` (19)** con `d = 11`, `n = 35`: `S = 19¹¹ mod 35`

`19² = 361 ≡ 11`; `19⁴ ≡ 121 ≡ 16`; `19⁸ ≡ 256 ≡ 11`; `19¹¹ = 19⁸·19²·19 ≡ 11·11·19 = 2299 = 65·35 + 24` → **firma de Paco = 24**

**Lola firma la `N` (13)** con `d = 3`, `n = 33`: `S = 13³ mod 33 = 2197 mod 33 = 2197 − 66·33 = 19` → **firma de Lola = 19**

(Cada firma es menor que el módulo del receptor — `24 < 33` y `19 < 35` —, así que se puede transmitir sin problemas.)

### Inciso 12.c)

> c. Descifrar los criptogramas y comprobar la firma en cada caso

**Lola descifra lo de Paco** (`d = 3`, `n = 33`): `M = C³ mod 33`

- `13³ = 2197 = 66·33 + 19` → **19 = S**
- `2³ = 8` → **8 = I**
- Mensaje recuperado: **`SI`** ✔

Verifica la firma de Paco con la **pública de Paco** (`e = 11`, `n = 35`): `24¹¹ mod 35`.
`24² = 576 ≡ 16`; `24⁴ ≡ 256 ≡ 11`; `24⁸ ≡ 121 ≡ 16`; `24¹¹ = 24⁸·24²·24 ≡ 16·16·24 = 6144 = 175·35 + 19` → **19 = S** ✔ coincide con la `S` recibida: la firma es auténtica.

**Paco descifra lo de Lola** (`d = 11`, `n = 35`): `M = C¹¹ mod 35`

- `27¹¹ mod 35`: `27² = 729 ≡ 29`; `27⁴ ≡ 36 ≡ 1`; `27⁸ ≡ 1`; `27¹¹ = 27⁸·27²·27 ≡ 29·27 = 783 = 22·35 + 13` → **13 = N**
- `15¹¹ ≡ 15` → **15 = O**
- Mensaje recuperado: **`NO`** ✔

Verifica la firma de Lola con la **pública de Lola** (`e = 7`, `n = 33`): `19⁷ mod 33 = 13` (calculado arriba) → **13 = N** ✔.

| | Cifrado | Firma | Descifrado | Verificación |
|---|---|---|---|---|
| Paco → Lola `SI` | (13, 2) | 24 | S, I | `24¹¹ mod 35 = 19 = S` ✔ |
| Lola → Paco `NO` | (27, 15) | 19 | N, O | `19⁷ mod 33 = 13 = N` ✔ |

---

## Ejercicio 13

> 13. Si la clave pública del receptor de un criptosistema RSA es el par (n, e)=(2291; 17), el mensaje capturado por el intruso es: 575, encontrar la clave para descifrar el mensaje, par (n, d)=(2291, d), descifrar el mensaje. Indique a qué letra del ASCII corresponde el valor encontrado.
> Pista: busque en internet el algoritmo de Fermat para encontrar los factores primos p y q, esto es n=p*q. Codifique en un lenguaje de programación a su elección, el algoritmo de Fermat.

### Paso 1 — Factorizar `n` con el algoritmo de Fermat

Se busca `n = x² − y² = (x + y)(x − y)`: se parte de `x = ⌈√n⌉` y se incrementa hasta que `x² − n` sea cuadrado perfecto.

`√2291 ≈ 47,9 ⇒ x₀ = 48`.

| `x` | `x²` | `x² − n` | ¿Cuadrado? |
|---|---|---|---|
| 48 | 2304 | 13 | no |
| 49 | 2401 | 110 | no |
| 50 | 2500 | 209 | no |
| 51 | 2601 | 310 | no |
| 52 | 2704 | 413 | no |
| 53 | 2809 | 518 | no |
| **54** | 2916 | **625 = 25²** | **sí** |

`x = 54`, `y = 25` ⇒ `p = x + y = 79`, `q = x − y = 29`. Comprobación: `79·29 = 2291` ✔.

Código del algoritmo (Python):

```python
from math import isqrt

def fermat(n):
    x = isqrt(n)
    if x * x < n:
        x += 1
    while True:
        y2 = x * x - n
        y = isqrt(y2)
        if y * y == y2:
            return x + y, x - y
        x += 1
```

### Paso 2 — Clave privada

```
φ(n) = (79 − 1)(29 − 1) = 78 · 28 = 2184
d = 17⁻¹ mod 2184

2184 = 128·17 + 8
  17 =   2· 8 + 1
  1 = 17 − 2·8 = 17 − 2·(2184 − 128·17) = 257·17 − 2·2184
```

⇒ **`d = 257`** (`17·257 = 4369 = 2·2184 + 1` ✔). Clave privada `(n, d) = (2291, 257)`.

### Paso 3 — Descifrar `C = 575`: `M = 575²⁵⁷ mod 2291`

Exponenciación rápida (square and multiply), `257 = 100000001₂`:

| Bit | Operación | Resultado mod 2291 |
|---|---|---|
| 1 | inicio | 575 |
| 0 | `575²` | 721 |
| 0 | `721²` | 2075 |
| 0 | `2075²` | 836 |
| 0 | `836²` | 141 |
| 0 | `141²` | 1553 |
| 0 | `1553²` | 1677 |
| 0 | `1677²` | 1272 |
| 1 | `1272² · 575` | **65** |

**`M = 65` → ASCII 65 = `A`**.

---

## Ejercicio 14

> 14. Intente romper el criptosistema RSA con clave pública (n, e) = (536813567; 3602561), con el software que escribió en el ejercicio anterior. Para romperlo, encuentre la clave d, que permita descifrar todo mensaje cifrado con la clave pública.

Se usa el mismo programa de Fermat del ejercicio 13.

- `√n ≈ 23 169,x ⇒ x₀ = 23 170`.
- El programa encuentra el cuadrado perfecto en la iteración **13 695** con `x = 36 864`, `y = 28 673`:
  - `p = x + y = 65 537`
  - `q = x − y = 8 191`
- Comprobación: `65 537 · 8 191 = 536 813 567` ✔. (Curiosidad: `65 537 = 2¹⁶ + 1` es un primo de Fermat y `8 191 = 2¹³ − 1` es un primo de Mersenne. Como `p` y `q` no están cerca, Fermat necesita miles de iteraciones, pero con un `n` de 29 bits sigue siendo instantáneo.)

Entonces:

```
φ(n) = 65 536 · 8 190 = 536 739 840
gcd(3 602 561, 536 739 840) = 1                 (e es válido)
d = e⁻¹ mod φ(n) = 201 934 721
```

**Clave privada: `(n, d) = (536 813 567, 201 934 721)`.** Comprobación: `e·d ≡ 1 (mod φ)` y ciclo cifrar/descifrar con un mensaje de prueba (`123456`) devuelve el mismo valor ✔. Con `d` se descifra **todo** mensaje cifrado con esa clave pública.

---

## Ejercicio 15

> 15. INVESTIGACIÓN:

### Inciso 15.a)

> a. Investigue algún algoritmo para el cálculo rápido de potencias, para usar en expresiones xm mod(n).

Algoritmo elegido: exponenciación binaria (*square and multiply*).

Idea: en lugar de multiplicar `m − 1` veces, se usa la **representación binaria del exponente** y siempre se reduce módulo `n` en cada paso, para que los números no crezcan. Cuesta `O(log m)` multiplicaciones en lugar de `O(m)`.

Algoritmo (de izquierda a derecha):

```
r ← 1
para cada bit b del exponente m, del más significativo al menos:
    r ← r² mod n
    si b = 1:  r ← r · x mod n
devolver r
```

Ejemplo (ejemplo de la cátedra RSA con `n = 91`): `55²⁹ mod 91`, `29 = 11101₂`:

| Bit | Operación | `r` |
|---|---|---|
| 1 | `1² · 55` | 55 |
| 1 | `55² · 55` | 27 |
| 1 | `27² · 55` | 55 |
| 0 | `55²` | 22 |
| 1 | `22² · 55` | **48** |

`55²⁹ mod 91 = 48` (el mensaje original del ejemplo de la cátedra) ✔. Es el mismo método usado en los ejercicios 11 a 14.

### Inciso 15.b)

> b. Investigue algún algoritmo para factorizar un número natural N.

| Algoritmo | Idea | Cuándo sirve |
|---|---|---|
| **División por tentativas** | Probar divisores `2, 3, 5, …` hasta `√N`. | `N` chico; costo `O(√N)`. |
| **Fermat** | `N = x² − y²` → `(x−y)(x+y)`; buscar `x ≥ √N` con `x² − N` cuadrado. | Cuando `p ≈ q` (por eso en RSA no deben ser cercanos). |
| **ρ de Pollard** | Genera una secuencia pseudoaleatoria módulo `N`; un `gcd` de diferencias revela un factor. | Factores chicos o medianos; costo `≈ O(N^{1/4})`. |
| **p−1 de Pollard** | Funciona si `p − 1` es producto de primos chicos. | Primos con `p−1` "liso"; por eso RSA pide `p−1` con factor primo grande. |
| **Criba cuadrática** | Busca congruencias `x² ≡ y² (mod N)` mediante relaciones sobre una base de factores. | Números de hasta ~100 dígitos. |
| **Criba general del cuerpo de números (GNFS)** | Generaliza la criba cuadrática sobre cuerpos de números. | El más rápido conocido para `N` grande (subexponencial, `e^{(ln N)^{1/3}(ln ln N)^{2/3}}`). |

Todos son **superpolinomiales** en el tamaño de `N`; esa es la dificultad en la que se apoya la seguridad de RSA.

---

## Resumen de resultados

| Ej. | Resultado |
|---|---|
| 1a | `EO TEQ TEQ, C EO ZMQS...` |
| 1b | `RC HRE HRE, P RC NZEG...` · César **sí** es grupo abeliano (`ℤ₂₇, +`) |
| 2a | `YAMNMYOAYPY` → `NOABANDONEN` |
| 2b | `PUOMONRORHDMCAAXGXRUX` |
| 3 | `K⁻¹ = (6 3 1 5 7 4 2)` → `NOPORMUCHOMADRUGAR` |
| 4–5 | Clave Vigenère `COLOSSUS`, verificada en los 32 caracteres |
| 6 | No: componer transposiciones de igual largo es otra transposición (grupo `S_N`) |
| 7 | `MXDQLWR` → `JUANITO` (`k = 3`, alfabeto de 26) |
| 8a | `N(N−1)` claves (`17 030` para `N = 131`) |
| 8b | `92, 71, 12, 89, 83, 110, 128, 83, 119, 0, 83, 80, 83, 125, 0, 77, 83, 110, 77, 95, 71, 128, 95, 83, 110, 83, 104, 71, 77, 71, 74, 83, 15, 71, 104, 104, 83, 110, 71` |
| 8c | `D(c) = 44c + 85 mod 131` |
| 8d | `a = 10`, `b = 7`: «Es mejor que aprender mucho el aprender cosas buenas.» |
| 9 | Período 31; `S = 0000101011101100011111001101001`; `ENIGMA → 010011111010001000110101100101010101100010011001` |
| 10 | Solo `e = 49` es válida (`d = 529`) |
| 11–12 | Paco: `(13, 2)`, firma 24 · Lola: `(27, 15)`, firma 19 · todo verifica |
| 13 | `2291 = 79·29`, `d = 257`, `M = 65 = 'A'` |
| 14 | `n = 65 537 · 8 191`, `d = 201 934 721` |
| 15 | Exponenciación binaria; Fermat / ρ de Pollard / criba cuadrática / GNFS |
