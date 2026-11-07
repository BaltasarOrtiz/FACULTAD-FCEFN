# Teoría de la Información — Parcial 2: enunciados

> Solo enunciados, sin resoluciones. Fuente: carpeta `Teoria de la Información/Parcial 2/Parciales 2/`. Las resoluciones están en `Parcial 2 - Transcripcion completa.md`.
> Los textos son los de los PDF originales; lo único que cambió es la ortografía de los símbolos matemáticos (potencias, subíndices). Los parciales vienen ordenados del más nuevo al más viejo.

| Parcial | Fecha | Temas | Contenido |
|---|---|---|---|
| 1 | 17/11/2025 | Tema 1 | Control de error (cíclico, ISBN-13, código rectangular), afín, entropía, imágenes |
| 2 | 15/12/2020 | único | Control de error, ISBN-10, afín, imágenes |
| 3 | 29/11/2010 | único | Vigenère + permutación, control de error, teóricas |
| 4 | 21/11/2012 | Temas 1 y 2 | Control de error, transposición + Vigenère, imágenes, teóricas |
| 5 | 12/11/2013 | Temas 1 y 2 | Cripto compuesta, control de error, ISBN, teóricas |
| 6 | s/f | — | Preguntas teóricas de cripto y control de error |

---

# 1 — Parcial 17/11/2025 — Tema 1

**PARCIAL 2 TEORÍA DE LA INFORMACIÓN** — FECHA: 17/11/25 — TEMA 1

*(Este mismo enunciado aparece en dos archivos de resolución: el de Bulián Melani y el de Contreras Matías, ambos "Tema 1". Es el mismo texto; solo cambia `G(x)` por `g(x)` en el archivo de Contreras.)*

**Codificación de Canal: Control de Error**

**1. Códigos de Bloques Lineales. Códigos cíclicos:** Sea el código (14, 4, dmin) cuyo espacio de palabras válidas lo permite construir el siguiente polinomio cíclico: `G(x) = 11010001101` (mayores potencias a la derecha).

- a. Encuentre la capacidad de código.
- b. Encuentre las matrices generadora y chequeador.
- c. Indicar si la palabra recibida: `R(x) = 11110001101000` (mayores potencias a la derecha) es válida o no.
- d. Si no lo fuere, detectar y corregir el error.
- e. Si se entrelazan 25 de esos códigos, ¿cuál sería la capacidad de corrección en ráfagas adquiridas?

**2. Códigos ISBN:** Sea el siguiente código ISBN13 `978-1-80056-662-3`, verifique si el mismo es válido o no. Si no lo fuera, ¿es posible corregirlo? Puede usar cryptool2.

**Arreglos Geométricos.**

**3.** Dado un código rectangular, donde cada fila es una palabra Hamming, y existen paridades por filas y por columnas. Encontrar la dmin del código expresando la capacidad del mismo e indicar de qué manera se lograrían reconocer y corregir los errores.

```
C10  C20  I10  BPP0
C11  C21  I11  BPP1
C12  C22  I12  BPP2
BPP3 BPP4 BPP5
```

La siguiente palabra, ¿es válida?

```
1 0 0 1
0 0 0 1
1 1 1 1
0 0 0
```

**Criptografía**

**4.** El siguiente texto fue cifrado usando la sustitución afín, con clave `(a, b) = (13, 9)`, `n = 40`.

- Texto cifrado: `U5K5CRUPKNLWNNWZAZY9K8EFQDURKJ886ERUPKIUKÑQ7`
- Alfabeto: `ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789(espacio en blanco)/,`

```
A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9 ␣ / ,
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39
```

Encuentre: la clave inversa y el texto descifrado. Si `n = 1.000.003` y `a = 139`: `a⁻¹ = ?`, `φ(n) = ?`

**5.** ¿Qué algoritmo, de los vistos en clases, mantiene la entropía de orden 0 entre texto claro y texto cifrado, considerándolos como proceso de Markov de orden 0, pero altera las entropías de orden superior (1, 2, etc.)? Justifique su respuesta.

**6.** Dé un ejemplo de filtro paso bajo, e indique qué efectos produce sobre una imagen.

---

# 2 — Parcial 15/12/2020

**PARCIAL N° 2 DE TEORÍA DE INFORMACIÓN** — FECHA: 15-12-2020

**1) CONTROL DE ERROR (3,5P):** Sea el siguiente polinomio `h(X) = X³ + X² + X + 1` de un código (n, k, dmin) (12, ?, ?).
- **A)** Encontrar la cantidad de dígitos de información `k` que constituyen la palabra válida.
- **B)** Encontrar el valor de la distancia mínima indicando las cualidades del código funcionando como corrector y como detector.
- **C)** Encuentre el polinomio Generador `g(X)`.
- **D)** Encuentre la matriz generador `G` y chequeadora `H`.
- **E)** Explique qué sucede, en la instancia decodificadora, ante la presencia de un error triple!! Y qué sucedería si se llegara a comparar el síndrome con las filas de `Hᵀ`?

**2) Dado el siguiente ISBN (3P)**
- **A)** encontrar el valor de dígito faltante (?) según la forma de codificación con solamente 10 dígitos (versión anterior del código) y no con 13 (versión actual del código) `3-540-?3218-9`.
- **B)** Qué características tiene el código y cuál es su distancia mínima.
- **C)** Cuál es la justificación por la cual se usa la base prima en toda instancia de codificación para el control de error?

**Criptografía (2p)**

**3)** Dado el siguiente criptograma `SGHPKQ$SGT`, se sabe que fue cifrado con una sustitución afín, con clave `(a, b) = (3, 11)`, `n = 29`, usando el siguiente alfabeto `A=0, B=1, …, Ñ=14, …, Z=26, $=27, #=28`. Se pide: encontrar los inversos de `a` y `b`, y decodificar el criptograma.

**Imágenes (1,5p)**

**4)**
- **a)** Cuál es la diferencia entre una imagen Vectorial y una imagen bitmapeada?
- **b)** Dada la siguiente secuencia de valores de color de una imagen: `129, 129, 129, 129, 129, 194`, codificarla usando la codificación RLE de PCX.

---

# 3 — Parcial 29/11/2010

**PARCIAL N° 2 DE COMUNICACIONES II (TEORÍA DE INFORMACIÓN)** — FECHA: 29/11/2010

**Ejercicio 1) Criptografía:** El siguiente criptograma `LFXOJKLWEOPKYDJQPJUCADCG` fue encriptado usando secuencialmente, primero un método de Vigenère con clave `RACING`, y posteriormente una clave de permutación `(6,5,4,3,2,1)`.
- **A)** Encuentre el mensaje original.
- **B)** Calcule los valores de entropía (como modelo independiente) que adquiere la fuente en cada etapa de encriptación.
- **C)** Especifique qué niveles de entropía (de orden 0 —independiente—, o de orden 1 —Markov de orden 1—, o de orden 2 etc.) modifica cada una de las estrategias utilizadas.
- **D)** Calcule la redundancia de la fuente original.

(El universo de símbolos considerado es: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`, A=1 … Z=26.)

**Ejercicio 2) Control de error:** Sea el siguiente polinomio `h(x) = x³ + x² + x + 1` de un código (12, K, dmin).
- **A)** Encuentre la capacidad del código.
- **B)** Especifique, como combinación de qué bits de información, se obtiene cada uno de los chequeadores.
- **C)** Decodifique el stream de bits recibido `110011001110`; en caso de haber algún error corrija y obtenga la palabra válida (las mayores potencias de x están a la derecha).
- **D)** Dibuje el circuito de `h(x)`.

**Ejercicio 3) Teóricas:**
- **A)** Ubique los siguientes archivos en orden decreciente de entropía relativa (justifique): `*.exe; *.txt; *.rar`.
- **B)** Si se entrelazan 7 códigos del tratado en el punto dos, qué nuevas capacidades adquiere el código.
- **C)** Marque las diferencias entre criptografía simétrica y asimétrica.
- **D)** Cuál de las tres fuentes, del ejercicio 1 (la encriptada final, la encriptada intermedia o la original) conviene comprimir (justifique).

---

# 4 — Parcial 21/11/2012

## Tema 1

**CONTROL DE ERROR:** Sea el código (15, K?, dmin?) generado por el siguiente polinomio generador `h(X) = X⁴ + X + 1`.
- **a)** Encuentre el polinomio generador `g(X)`.
- **b)** Determine las capacidades del código si funciona como corrector y/o detector, encontrando la distancia mínima.
- **c)** Especifique como combinación lineal de qué dígitos de información se obtiene cada chequeador (mayores potencias de G a la derecha).
- **d)** Determine si el polinomio `R(x) = X⁸ + X⁴ + X²` es válido o no. Si no lo es corríjalo.
- **e)** Obtenga la capacidad de corrección a nivel de ráfaga si se entrelazan 20 códigos generados por `h(x)`.

**CRIPTOGRAFÍA:** Dado el siguiente criptograma, `GAUQ YBXM OÑSK`, descifrarlo, sabiendo que fue cifrado utilizando una transposición de una matriz de 3x4, en la que se pusieron las letras por fila y se leyeron por columna según el siguiente orden `(4,1,3,2)`; el resultado fue cifrado utilizando la técnica de Vigenère con clave `CANCUN`.
- **B)** Los métodos antes vistos modifican la entropía de orden cero?
- **C)** En la fuente cifrada, y en cada paso de descifrado, calcule la entropía de orden cero para comprobar lo manifestado por usted en el punto anterior.

**IMÁGENES:** Dada la siguiente imagen, utilizando las máscaras pertinentes, determinar a qué tipo de recta pertenece el punto central (horizontal, vertical, a 45°, a 135°):

```
19  3 21
 4 19 11
16 16 19
```

**TEÓRICAS:**
- **2)** En un buen sistema criptográfico cuánto debe valer la Información Mutua `I(A,B)`, asumiendo que A es el mensaje original y B es el mensaje cifrado? Justifique.
- **3)** Escriba las propiedades del polinomio generador de un código cíclico.

## Tema 2

**CONTROL DE ERROR:** Sea el código (14, K?, dmin?) generado por el siguiente polinomio generador `h(X) = X⁴ + X² + X + 1`.
- **a)** Encuentre el polinomio generador `g(X)`.
- **b)** Determine las capacidades del código si funciona como corrector y/o detector, encontrando la distancia mínima.
- **c)** Especifique como combinación lineal de qué dígitos de información se obtiene cada chequeador (mayores potencias de G a la derecha).
- **d)** Determine si el polinomio `R(x) = X⁸ + X⁴` es válido o no. Si no lo es corríjalo.
- **e)** Obtenga la capacidad de corrección a nivel de ráfaga si se entrelazan 20 códigos generados por `h(x)`.

**CRIPTOGRAFÍA:** Dado el siguiente criptograma, `BOEU MIHJ FDFX DVDT`, descifrarlo, sabiendo que fue cifrado utilizando la técnica de Vigenère con clave `AZULES`, y al resultado se lo dispuso por filas en una matriz de 4x4, y luego leído por columnas según el siguiente orden `(2,4,1,3)`. Cuál de las dos alternativas usadas garantiza mayor seguridad o capacidad de encriptación? Justifique.

**IMÁGENES:** Dada la siguiente imagen, utilizando la máscara pertinente, suavizar el punto central (de las dos ventanas), utilizando una máscara de media aritmética:

```
160 161 163 180
200  11  21 190
199 161 165 191
```

**TEÓRICAS:**
- **1)** Justifique la necesidad de la base prima.
- **2)** Calcule el dígito faltante en el siguiente ISBN: `234323?323`.
- **3)** Llene el siguiente cuadro con información asociada a campos de Galois y códigos Reed-Solomon:

| Tamaño del campo de Galois GF(q) | Grado del polinomio generador del campo de Galois GF(q) | Longitud de palabra válida en bytes (n) | Cantidad de bits por byte | Cantidad de bytes chequeadores | Cantidad de bytes de información | Capacidad de corrección del código (t) | Si entrelazo 7 códigos de este tipo puedo corregir una ráfaga de cuántos bytes? |
|---|---|---|---|---|---|---|---|
| 2048 | | | | | | 100 bytes | |
| | 9 | | | | 461 | | |
| | | 127 | | 10 | | | |

---

# 5 — Parcial 12/11/2013

## Tema 1

**a) CRIPTOGRAFÍA:**
- **A1)** Dado el siguiente texto cifrado: `Q V V Ñ M W H F V Y M Q S V K Ñ T K A G`, se sabe que fue cifrado con cifrador compuesto, utilizando los algoritmos: Vigenère con clave `K1 = (K,E,R,B,E,R,O,S)` y luego una transposición, utilizando una matriz de 4x5, con clave `K2 = (2,5,3,1,4)` (el texto en matriz fue dispuesto por filas). Encuentre las claves para descifrar el texto y el texto en claro.
- **A2)** Defina confusión y difusión. Identifique en el punto anterior si alguno de los algoritmos introdujo confusión, difusión o ambos.
- **A3)** Para cada algoritmo, indique si se modificaron las entropías de orden cero (Independiente) y/o de orden 1. Bajo este concepto cuál de los dos algoritmos es mejor? Justifique su respuesta.

**B) CONTROL DE ERROR:** Sea el código (14, K?, dmin?) generado por el siguiente polinomio generador `h(X) = X⁴ + X² + X + 1`.
- **a)** Encuentre el polinomio generador `g(X)`.
- **b)** Determine las capacidades del código si funciona como corrector y/o detector, encontrando la distancia mínima.
- **c)** Especifique como combinación lineal de qué dígitos de información se obtiene cada chequeador (mayores potencias de G a la derecha).
- **d)** Determine si el polinomio `R(x) = X⁸ + X⁴` es válido o no. Si no lo es corríjalo.
- **e)** Obtenga la capacidad de corrección a nivel de ráfaga si se entrelazan 20 códigos generados por `h(x)`.

## Tema 2

**A) CRIPTO:**
- Dado el siguiente texto cifrado: `F P N Q C M O A A J X S X G T Y H N F G O`, se sabe que fue cifrado con cifrador compuesto, utilizando los algoritmos: Vigenère con clave `K1 = (H,E,L,L,M,A,N)` y luego una transposición, utilizando una matriz de 3x7, con clave `K2 = (6,5,1,7,3,2,4)` (el texto en matriz fue dispuesto por filas). Encuentre las claves para descifrar el texto y el texto en claro.
- **b)** Identifique ventajas y desventajas de los métodos de cifrado simétrico y asimétrico. Cómo funciona un sistema de cifrado híbrido.
- **c)** Si se consideran A: Mensaje original y B: Mensaje encriptado, cuánto debe valer la información mutua `I(A,B)` para que el sistema criptográfico se considere bueno. Justifique su respuesta.

**CONTROL DE ERROR:** Sea el polinomio `h(x) = X³ + X² + X + 1` generador de un código (12, k, dmin).
- **a)** Encuentre la capacidad del código.
- **b)** Encuentre la matriz generadora `G` y especifique como combinación lineal de qué dígitos de información se obtiene cada chequeador.
- **c)** Si se entrelazan 20 de los anteriores códigos qué nueva capacidad adquiere el código?
- **d)** Sea el siguiente código ISBN (con diez dígitos) encontrar el símbolo (?): `1-122-?3445-5`. ¿Cuál es la capacidad del código?

---

# 6 — Preguntas teóricas (solo las preguntas)

Archivo `Preguntas Teóricas parcial 2 Teoría de la información.pdf`.

**Criptografía**
1. Orden decreciente según entropía relativa `*.exe`, `*.txt`, `*.rar`.
2. Diferencias entre criptografía simétrica y asimétrica. Ventajas y desventajas de ambos.
3. Cómo funciona un sistema de cifrado híbrido.
4. ¿Cuál fuente conviene comprimir: la original, la de encriptado intermedia o la de encriptado final?
5. Cuánto debe valer la información mutua `I(A, B)` donde A es el mensaje original y B el encriptado. Justificar. (¿La información mutua debe ser máxima o mínima?)
6. Necesidad de una base prima.
7. Definir confusión y difusión. Cuál algoritmo introduce cada uno.
8. Niveles de entropía modificados por cada algoritmo. Cuál algoritmo es mejor.

**Corrección de errores**
1. Si se entrelazan `n` códigos, qué nuevas capacidades adquiere el código.
2. Propiedades del polinomio generador de un código cíclico.
3. Calcular el dígito faltante en un ISBN.
4. Capacidad de un código ISBN.
5. Cuadro con información de un campo de Galois y códigos Reed-Solomon.
6. Capacidad de corrección a nivel de ráfaga si se entrelazan `n` códigos generados por `h(x)`.
7. Qué características tienen las matrices `G` y `H` entre sí. Y qué significa.
8. Un código cíclico con capacidad 10, qué capacidad tiene.
