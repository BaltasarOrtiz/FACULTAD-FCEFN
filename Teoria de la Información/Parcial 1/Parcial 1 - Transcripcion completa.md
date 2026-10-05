# Teoría de la Información — Parcial 1: transcripción completa de incisos y resoluciones

> Fuente: todo el contenido de la carpeta `Teoria de la Información/Parcial 1/`.
> Marcas usadas: **[Corrección]** = comentario/nota del docente en el escaneo; **[Nota]** = aclaración mía (verificación de cuentas o algo ilegible); **[Completado]** = resolución que el archivo no traía y agregué yo.
> No pude procesar el audio `WhatsApp Ptt 2023-10-08 at 12.33.25 PM.ogg` (no tengo forma de transcribir audio acá).

## Índice de archivos y qué contiene

| Archivo | Contenido |
|---|---|
| `WhatsApp Image 2023-10-05 ... .jpeg` | Enunciado Parcial 1 del 27/09/2022 (Tema I), sin resolución |
| `Parcial1TIpdf_1.pdf` | Enunciados Temas 1–4 del parcial (2023) |
| `Parcial 1 Tema 1.xlsx` | Resolución completa del Tema 1 (inciso 1) y planilla inicial del Tema 2 |
| `Preguntas teóricas Parcial 1.docx` | Respuestas a las preguntas teóricas de los Temas 1–4 |
| `Parcial N°1 2023 CORREGIDOS.pdf` (20 págs.) | Parcial del 10-10-2023 resuelto por 4 alumnos, con correcciones |
| `Parcial N°1 2023 PARTE 2 CORREGIDOS.pdf` (7 págs.) | Parcial del 10-10-2023 resuelto por otra alumna (Radicetti) |
| `Parcial N°1 de ... Johana Arce-CORREGIDO.pdf` | Otro parcial: Shannon/Huffman, encriptación, canal |
| `Parcial1-Galdame-2023.pdf` | Recuperatorio Tema 2 (reprobado), con correcciones |
| `Parcial_1_-_VISTO-KLE.pdf` y `Condicional.pdf` | Parcial de Nanni Rebollo (5 símbolos, canal ternario, Huffman/aritmético) y examen condicional (PCM/DPCM) |

---

# PARTE 0 — Recetas generales (cómo se resuelve cada tipo de inciso)

## 0.1 Entropía, entropía máxima y redundancia (fuente independiente)
1. Contar apariciones de cada símbolo → `p(si) = frecuencia / n`.
2. `H = Σ p(si)·log2(1/p(si))` (bits/símbolo).
3. `Hmax = log2(q)` con q = cantidad de símbolos distintos.
4. Rendimiento `Hr = H/Hmax`; **Redundancia** `R = 1 − H/Hmax` (×100 para %).
   - Si se compara contra un código de longitud fija de L bits: `R = 1 − H/L`.

## 0.2 Codificación de Shannon
1. Ordenar símbolos de mayor a menor probabilidad.
2. Longitud `li` = **cota inferior (techo)** tal que `log2(1/pi) ≤ li < log2(1/pi) + 1`, es decir `li = ⌈log2(1/pi)⌉`.
   - [Corrección Arce] Si la cantidad de información `log2(1/pi)` es un entero, se trabaja con ese valor exacto (no se suma 1). Usar la cota superior en ese caso es error.
3. Frecuencia acumulada `FA(si) = Σ pj` de los símbolos anteriores (el primero vale 0).
4. Pasar FA a binario (multiplicando por 2 sucesivamente, tomando la parte entera).
5. El código es los primeros `li` bits de esa expansión binaria.
6. Longitud media `L = Σ pi·li`. Grado de compresión vs. código fijo: `1 − L/Lfijo`.

## 0.3 Huffman estático
1. Ordenar probabilidades de mayor a menor.
2. Sumar las dos menores, reinsertar la suma en el orden, repetir hasta llegar a 1. Asignar 0/1 a cada rama.
3. Leer el código desde la raíz. Es **instantáneo** (ningún código es prefijo de otro) y de **doble lectura** (primero se cuentan frecuencias, después se codifica).

## 0.4 Huffman dinámico
Árbol arranca con el nodo NYT (“no transmitido todavía”). Cada símbolo nuevo se emite como `código del NYT + código fijo del símbolo`; los repetidos se emiten con su código actual. Después de cada símbolo se actualiza el peso y se verifica la **Sibling Property** (los nodos, recorridos de abajo hacia arriba y de izquierda a derecha, deben tener pesos no decrecientes); si no se cumple, se intercambian nodos. El objetivo de la propiedad es garantizar que el árbol siga siendo un árbol de Huffman óptimo tras cada actualización.

## 0.5 Fuente de Markov de primer orden
1. **Matriz de transición**: `P(sj | si) = (nº de veces que sj sigue a si) / (nº de veces que aparece si)`. Cada fila suma 1. (Se cuentan los pares consecutivos.)
2. **Matriz/vector estacionario**: resolver `[p1 … pn]·P = [p1 … pn]` junto con `Σ pi = 1` (se reemplaza una ecuación redundante por la de normalización). La matriz estacionaria es la matriz con ese vector repetido en todas las filas.
3. **Ergódico**: lo es si desde cualquier estado se puede llegar a cualquier otro. Si la matriz tiene ceros que impiden llegar a algún estado (hay estados inalcanzables desde otros), **no es ergódico**.
4. **Entropía de la fuente**: `H(B/A) = Σ p(ai)·H(B/ai)`, donde `H(B/ai) = Σ p(bj/ai)·log2(1/p(bj/ai))`.
5. **Probabilidad de una cadena** (p. ej. `p(eeii)`): `p(e)·p(e|e)·p(i|e)·p(i|i)`.

## 0.6 Canal: capacidad e información mutua
- `I(A,B) = H(B) − H(B/A)`.
- Probabilidades de salida: `p(bj) = Σ p(ai)·p(bj/ai)`.
- **BSC** (matriz `[[p, 1−p],[1−p, p]]`): capacidad con entrada equiprobable `C = 1 − H(p)` = `1 − [p·log2(1/p) + (1−p)·log2(1/(1−p))]`.
- Canal **simétrico**: todas las filas son permutación de la primera. Canal **uniforme**: además las columnas también.
- **Peor canal** (BSC o ternario uniforme): todas las probabilidades condicionales iguales (BSC: 0,5/0,5; ternario: 1/3 en todo). `H(B/A) = H(B)`, `I(A,B)=0`, `C=0`: emisor y receptor son independientes.
- **Mejor canal**: identidad (1 en la diagonal): `C = log2(q)`.
- Para llegar a la capacidad hace falta la distribución de entrada que maximiza `I`; en canales simétricos es la equiprobable.

## 0.7 Digitalización PCM / DPCM
- Nº de niveles/segmentos = `rango dinámico / ancho de segmento`. Bits = `⌈log2(niveles)⌉`.
- Si se toma el **valor medio del segmento**, `error = ancho/2`, o sea ancho = 2·error.
- **PCM**: se cuantifican directamente las muestras (rango = Vmax − Vmin).
- **DPCM**: se cuantifica la *diferencia* entre muestras sucesivas (rango dinámico de las diferencias, normalmente menor) → menos bits para el mismo error.
- Bits transmitidos = muestras × bits/muestra, con `fs = 2·fmax` (Nyquist).

## 0.8 Codificación predictiva (compuerta OREX / XOR) y K óptimo
- El predictor compara; salida `1 = error`, `0 = coincidencia`.
- Para cada K se codifica la cantidad de 0 consecutivos antes de cada 1 usando K bits; el valor `2^K − 1` (todos 1) significa “continúa la racha de ceros”, y se concatena con otro grupo. Los ceros finales también se codifican.
- Se prueba K = 2, 3, 4, … y se elige el K que da **menos bits totales**; se corta la búsqueda cuando K+1 empeora respecto del anterior (K óptimo).

## 0.9 Codificación aritmética
Intervalo [0,1); a cada símbolo se le asigna un subintervalo proporcional a su probabilidad (ordenado). Por cada símbolo leído: `cota_inf' = cota_inf + (cota_sup − cota_inf)·inf(s)`; `cota_sup' = cota_inf + (cota_sup − cota_inf)·sup(s)`. La salida es un número binario dentro del último intervalo. Cuando (con la precisión dada) cota inferior y superior coinciden, ya no se puede discernir un valor entre ellas → error de precisión / se debe detener.

## 0.10 Cuando coinciden Huffman, Shannon y Fano
Cuando `p(si) = r^(−li)` (potencias de la base, base 2: 1/2, 1/4, 1/8…). Entonces `Σ r^(−li) = 1` (**Kraft = 1**) y `H = L` (código óptimo, sin redundancia). En general `H ≤ L`; perforar esa cota implicaría pérdida de información. Ejemplos: 4 símbolos → ½, ¼, ⅛, ⅛; 5 símbolos → ½, ¼, ⅛, 1⁄16, 1⁄16; 6 símbolos → ½, ¼, ⅛, 1⁄16, 1⁄32, 1⁄32; 7 símbolos → ½, ¼, ⅛, 1⁄16, 1⁄32, 1⁄64, 1⁄64.

---

# PARTE 1 — Parcial 27/09/2022, Tema I (enunciado)

*(Imagen `WhatsApp Image 2023-10-05 at 21.47.53.jpeg`; no trae resolución.)*

1. El árbol final de los algoritmos Huffman dinámico y Huffman estático, ¿siempre coinciden? Verdadero / Falso. Justifique.
2. Dada la secuencia de caracteres `amnr$aaag`, reordenada con la transformada de Burrows-Wheeler, encontrar la cadena original.
3. **Codificación de fuente**: fuente de vocales `…eiou!aeiouaaeiouaaaeiouaaaaeioueiou!aeiou…` (los `!` son separadores de trama). **Como fuente independiente**: a) Encuentre la redundancia. b) Codificación de Shannon y verificar el grado de compactación respecto de un código de longitud fija. c) Proponga una asignación de probabilidades que garantice el mismo grado de compactación de Shannon y Huffman; verifique cuánto vale la inecuación de Kraft. **Como fuente dependiente de primer orden**: c) Calcular la entropía de la fuente. d) Encontrar la matriz de transición y estacionaria; ¿el proceso es ergódico? **Teórica**: e) Dado un archivo de texto, si secuencialmente se deben aplicar una técnica basada en diccionario y otra estadística tipo Huffman, ¿en qué orden para garantizar el mayor grado de compactación?
4. **Canal y capacidad de canal**: BSC con p(0/0)=0,85. a) Encontrar la capacidad de canal. Para un canal BSC encuentre su matriz representativa y defina las bondades de un canal con: b) p(0/1)=1 y c) p(0/1)=0,5.

---

# PARTE 2 — Parcial 2023: enunciados de los Temas 1–4 (`Parcial1TIpdf_1.pdf`)

Todos los temas comparten estructura: 1) Codificación de fuente (A: independiente, B: Markov de 1er orden), 2) Canal, 3) Teóricas. Fuente: vocales `a, e, i, o, u`, con `|` como separador.

### Tema 1 — `…aaaae|aeieouaaiiuaoaueeooiiuuaoaaaae|aei…`
- **1A (independiente)**: 1) Entropía. 2) Redundancia. 3) Codificar por **Shannon**. 4) Comparar el grado de compresión respecto de un código de igual longitud necesario para codificar ese universo de símbolos.
- **1B (Markov 1er orden)**: 1) Matriz de transición y entropía. 2) ¿Ergódico? 3) Matriz estacionaria. 4) `p(eeii)`.
- **2) Canal**: BSC con p(0/0)=0,95. Capacidad C.
- **3) Teóricas**: a) Si se aplican secuencialmente LZW y Huffman a una fuente de texto, ¿en qué orden para máximo grado de compactación? Justifique. b) Fuente de 7 símbolos: ¿con qué probabilidad deben generarse para que Huffman, Shannon y Fano (base 2) coincidan en longitud promedio? ¿Cuánto vale Kraft y qué relación hay entre H y L? c) Justifique la necesidad y explique el fenómeno de la compansión.

### Tema 2 — `…ooooa|aeieouaaiiuaoaueeooiiuuaoooooa|aei…`
- **1A**: 1) Entropía. 2) Redundancia. 3) Codificar por **Huffman dinámico** los primeros 5 caracteres; identificar en qué paso(s) se aplica la **Sibling Property** y cuál es el objetivo de que el árbol la cumpla. 4) Comparar el grado de compresión (hasta los 5 primeros caracteres) respecto de un código de igual longitud.
- **1B**: Markov: matriz de transición y entropía; ergódico; matriz estacionaria; `p(eiua)`.
- **2) Canal**: BSC con p(0/0)=0,5. Capacidad.
- **3) Teóricas**: a) Propiedades de la cantidad de información I. b) ¿En qué se basan y diferencian PCM y DPCM? Fuente de 5 símbolos: probabilidades para que Huffman/Shannon/Fano coincidan; Kraft; relación H–L. c) Peor canal de comunicación uniforme ternario: valor de la capacidad y cómo se consideran los extremos emisor/receptor.

### Tema 3 — `…aaaae|aeieouaaooeuuuuueooiiuuaoaaaae|aei…`
- **1A**: 1) Entropía. 2) Redundancia. 3) Con solo **tres dígitos decimales**, codificar mediante **codificación aritmética** hasta que no logren diferenciarse las cotas superior e inferior. 4) Comparar compresión (hasta la cantidad de caracteres codificados en 3) con código de igual longitud.
- **1B**: Markov: transición/entropía; ergódico; estacionaria; `p(uuaa)`.
- **2) Canal**: BSC con p(0/0)=0,85 y p(0)=0,7. **Información mutua**.
- **3) Teóricas**: a) ¿Por qué los métodos estadísticos estáticos (Huffman, Shannon, Fano) se llaman de doble lectura? ¿Con o sin pérdidas? b) ¿Mayor compactación con mayor o menor redundancia? c) ¿Instantáneos ⊂ unívocos o al revés? ¿Huffman encuentra códigos que son prefijo entre sí? d) Fuente de 4 símbolos: probabilidades para que coincidan Huffman/Shannon/Fano; Kraft; H vs L. e) Peor canal ternario uniforme.

### Tema 4 — `…eeeee|aeieouaaiieouaaeiieouaeeeee|aei…`
- **1A**: 1) Entropía. 2) Redundancia. 3) Con **longitud de ventana de 8 caracteres**, codificar mediante **LZ con ventana deslizante** lo establecido entre barras. 4) Comparar compresión con código de igual longitud.
- **1B**: Markov: transición/entropía; ergódico; estacionaria; `p(aaii)`.
- **2) Canal**: BSC con p(0/0)=0,85 y p(1)=0,7. Información mutua.
- **3) Teóricas**: a) Tras codificar una misma fuente, ¿los árboles de Huffman estático y dinámico deberían ser iguales? b), c), d), e) idénticos a Tema 3.

---

# PARTE 3 — Tema 1: resolución completa (`Parcial 1 Tema 1.xlsx`)

Fuente (n = 30 símbolos, q = V = 5):
`a e i e o u a a i i u a o a u e e o o i i u u a o a a a a e`

## 3.1 Entropía
| Símbolo | Frecuencia | p | I = log2(1/p) |
|---|---|---|---|
| a | 10 | 10/30 | log2(30/10)=log2 3 = 1,585 |
| e | 5 | 5/30 | log2(30/5)=2,585 |
| i | 5 | 5/30 | 2,585 |
| o | 5 | 5/30 | 2,585 |
| u | 5 | 5/30 | 2,585 |

`H = (15,85 + 12,925·4)/30 = 2,251 bits/símbolo`, o equivalentemente
`H = 1/3·log2 3 + (5/30·log2 6)·4 = 0,53 + 1,723 = 2,253 bits/símbolo`.

## 3.2 Redundancia
1. `Hmax = log2 5 = 2,322`
2. Rendimiento `Hr = H/Hmax = 2,253/2,322 = 0,97`
3. `R = 1 − Hr = 0,03 → 3 %`

## 3.3 Shannon
| Si | P(Si) | FA(Si) | Binario de FA | Longitud | Código |
|---|---|---|---|---|---|
| A | 10/30 | 0 | 0 | 2 | 00 |
| E | 5/30 | 0,33 | 0,01010101 | 3 | 010 |
| I | 5/30 | 0,5 | 0,10000000 | 3 | 100 |
| O | 5/30 | 0,667 | 0,10101011 | 3 | 101 |
| U | 5/30 | 0,8333 | 0,11010101 | 3 | 110 |

## 3.4 Grado de compresión
- Código de longitud fija: 5 símbolos → 2³ = 8 → **3 bits/símbolo**; total 3·30 = 90 bits.
- `Lsh = 1/3·2 + (5/30·3)·4 = 0,6667 + 2 = 2,6667 bits/símbolo` → 2,6667·30 = **80 bits**.
- Compresión = `(1 − 80/90)·100 = 11,11 %`.

## 3.5 Fuente de Markov de 1er orden
Matriz de transición `p(bj/ai)` (filas = estado actual, columnas = siguiente; orden a, e, i, o, u), tal como figura en la planilla:

| | a | e | i | o | u |
|---|---|---|---|---|---|
| a | 4/10 | 2/10 | 1/10 | 2/10 | 1/10 |
| e | 1/5 | 1/5 | 1/5 | 2/5 | 0 |
| i | 0 | 1/5 | 2/5 | 0 | 2/5 |
| o | 2/5 | 0 | 1/5 | 1/5 | 1/5 |
| u | 3/5 | 1/5 | 0 | 0 | 1/5 |

> [Nota] La fila de **a** suma 10/10 porque la planilla cuenta la transición del último símbolo hacia el siguiente bloque (“…|aei…”).

**Sistema estacionario** (`p·P = p`):
- `p(a) = p(a)·4/10 + p(e)·1/5 + p(i)·0 + p(o)·2/5 + p(u)·3/5`
- `p(e) = p(a)·2/10 + p(e)·1/5 + p(i)·1/5 + p(o)·0 + p(u)·1/5`
- `p(i) = p(a)·1/10 + p(e)·1/5 + p(i)·2/5 + p(o)·1/5 + p(u)·0`
- `p(o) = p(a)·2/10 + p(e)·2/5 + p(i)·0 + p(o)·1/5 + p(u)·0`
- `p(u) = p(a)·1/10 + p(e)·0 + p(i)·2/5 + p(o)·1/5 + p(u)·1/5`
- más `Σ p = 1` (en la planilla se arma el sistema homogéneo `(P^T − I)·p = 0` con una fila de unos para la normalización).

**Entropías condicionales**
- `H(B/a) = 4/10·1,322 + 2/10·2,322 + 1/10·3,322 + 2/10·2,322 + 1/10·3,322 = 2,122`
- `H(B/e) = 3·(1/5·2,322) + 2/5·1,322 = 1,922`
- `H(B/i) = 1/5·2,322 + 2·(2/5·1,322) = 1,522`
- `H(B/o) = 2/5·1,322 + 3·(1/5·2,322) = 1,922`
- `H(B/u) = 3/5·0,737 + 2·(1/5·2,322) = 1,371`
- `H(B/A) = 1/3·2,122 + 1/6·1,922 + 1/6·1,522 + 1/6·1,922 + 1/6·1,371 = 1,83 bits/símbolo`

(`H(A) = 2,253` como fuente independiente.)

## 3.3b Ejercicio 2 — Canal (Tema 1)
BSC con p(0/0) = 0,95: matriz `[[0,95; 0,05],[0,05; 0,95]]`. Capacidad `C = max I(A,B)` (ver cuenta completa en la Parte 4, inciso 3A: **C = 0,7136 bits**).

## 3.4b Tema 2 (planilla iniciada)
Secuencia: `a e i e o u a a i i u a o a u e e o o i i u u a o o o o o a` (30 símbolos, q = 5). Probabilidades: a 7/30, e 4/30, i 5/30, o 9/30, u 5/30. Solo se llegó a este paso (entropía).

---

# PARTE 4 — Parcial del 10-10-2023 (`Parcial N°1 2023 CORREGIDOS.pdf`)

Existen **dos versiones** del enunciado en el PDF:

**Versión A (Zeballos / Radicetti)**
1. **Discretización**: codificación **DPCM**, rango dinámico de las diferencias entre muestras en ±1 V; se quiere discretizar con error menor a ±0,005 V; ¿cuántos bits? (valor discreto = valor medio de cada segmento). Al final discutir con el grupo las conclusiones.
2. **Codificación de fuente**. 2A) Fuente `…HOY-YOHAGOYOGAHOY-YOHA…` **como fuente independiente**: A) redundancia; B) codificación de **Shannon** (base 2); C) distribución de probabilidades que iguale las longitudes promedio de Huffman y Shannon. **Como fuente de Markov de primer orden**: matriz estacionaria y decir si el proceso es ergódico. 2B) En una codificación predictiva, la cadena de 0 y 1 es la salida de la compuerta OREX `10000001010000100000` (en la hoja de Zeballos/Radicetti figura una cadena de largo similar): encontrar el **Kopt** de mejor compresión.
3. **Canal**: BSC con P(1/0)=0,95 [dice 0,95]: capacidad de canal. Canal ternario uniforme: probabilidades condicionales del **peor canal**. Para el canal binario P(0/0)=0,65, P(1/1)=0,95: A) ¿es simétrico? B) Cualitativamente, ¿qué símbolo se debe dar con mayor probabilidad a la entrada para transmitir a la capacidad de canal?

**Versión B (Retner / Carbajo / Capdevila)**
1. **Discretización**: señal temporal codificada en **PCM**, varía entre −5 V y 5 V; error de discretización menor a ±0,005 V; ¿cuántos bits? (valor medio del segmento).
2A) Fuente `…TINA-ANITALAVALATINA-ANIT…` como independiente: A) redundancia; B) **Huffman** (base 2); C) distribución de probabilidades que iguale las longitudes de Huffman y Shannon; **Markov** 1er orden: matriz estacionaria y ergodicidad. 2B) Cadena OREX `10000001010000100000`: encontrar Kopt.
3) Canal: mismo enunciado que versión A (BSC 0,95, ternario peor canal, canal binario 0,65/0,95).

---

## 4.1 VERSIÓN A

### 4.1.1 Inciso 1 — Discretización (DPCM, ±1 V, error ±0,005 V)
- Rango de la diferencia: [−1 V, 1 V] → 2 V.
- Con valor medio de cada segmento, el error es la mitad del ancho: ancho del segmento = 2·0,005 = 0,01 V.
- Nº de segmentos = 2 V / 0,01 V = **200** → 2⁷ = 128 < 200 ≤ 256 = 2⁸ → **8 bits**.
- [Corrección sobre las respuestas de Zeballos y Radicetti] Ambas plantearon 400 niveles y 9 bits (2⁹ = 512) y/o dieron un error de ±0,003 V con 9 bits; el docente marcó: “en realidad el rango del segmento es ±0,005 = 0,01 → 2 V/0,01 = 200 segmentos, con 256 llego: 2⁸”. Puntaje: 50 %.
- (Zeballos tomó la versión PCM ±1 V·2 = 400 niveles; Radicetti probó 2⁸ = 256 → 0,007 V “no alcanza” y 2⁹ → 0,003 V; ambas quedaron mal por usar el ancho = error y no el doble.)

### 4.1.2 Inciso 2A — Fuente independiente `YOHAGOYOGAHOY`
Símbolos (13): Y 3, O 4, H 2, A 2, G 2 → `p(O)=4/13, p(Y)=3/13, p(H)=p(A)=p(G)=2/13`.

**A) Redundancia**
1. Probabilidades: arriba.
2. `H = 3/13·log2(13/3) + 4/13·log2(13/4) + 3·(2/13·log2(13/2))`
   `= 0,48838 + 0,52737 + 1,24635 ≈ 2,25776 bits`
3. `Hmax = log2 5 = 2,32193`
4. `R = 1 − 2,25776/2,32193 = 0,02763` (≈ 2,76 %).

**B) Shannon (base 2)**
Orden por probabilidad: O, Y, H, A, G.
| Si | P(Si) | FA | FA decimal | Binario | Long. | Código |
|---|---|---|---|---|---|---|
| O | 4/13 | 0 | 0,0000 | 0 | 2 | 00 |
| Y | 3/13 | 4/13 | 0,3076 | 0,0100 | 3 | 010 |
| H | 2/13 | 7/13 | 0,5384 | 0,1000 | 3 | 100 |
| A | 2/13 | 9/13 | 0,6923 | 0,1011 | 3 | 101 |
| G | 2/13 | 11/13 | 0,8461 | 0,1101 | 3 | 110 |

Longitudes: para O, `log2(13/4)=1,7004 ≤ x ≤ 2,7004 → x = 2`; para Y, `log2(13/3)=2,1154 ≤ y ≤ 3,1154 → y = 3`; para H, A, G, `log2(13/2)=2,7004 ≤ w ≤ 3,7004 → w = 3`.
Binarios por multiplicaciones sucesivas de 2 (ejemplo Y: 0,3076→0 ; 0,6152→0 [parte entera]; 1,2304→1; 0,4608→0; … = 0,0100).

**C) Distribución que iguala Huffman y Shannon**: `p(si) = 2^(−li)` → O = 1/2, Y = 1/4, H = 1/8, A = 1/16, G = 1/16. Comprobación: `2⁻¹ + 2⁻² + 2⁻³ + 2⁻⁴ + 2⁻⁴ = 1` → cumple Kraft.
(Radicetti propuso 1/4, 1/8, 1/16, 1/32 y 1/32 para 5 símbolos; la suma da 15/32 ≠ 1: el docente la marcó “Bien” solo por la idea de “múltiplos de la base”; debe sumar 1.)

### 4.1.3 Inciso 2A — Markov de 1er orden (Zeballos / Radicetti)
Se cuentan los pares consecutivos de `YOHAGOYOGAHOY` (con cierre circular `…Y-Y…`) y cada fila se divide por las apariciones del estado de origen. Zeballos usó el orden Y, O, H, A, G con los mismos valores. La hoja es de lectura difícil; la matriz limpia es esta (orden H, O, Y, A, G):

```
      H     O     Y     A     G
H     0    1/2    0    1/2    0
O    1/4    0    2/4    0    1/4
Y     0    2/3   1/3    0     0
A    1/2    0     0     0    1/2
G     0    1/2    0    1/2    0
```
Vector estacionario: `[p(H); p(O); p(Y); p(A); p(G)] = [2/13; 4/13; 3/13; 2/13; 2/13]`.
Sistema: `p(H) = p(O)·1/4 + p(A)·1/2`; `p(O) = p(H)·1/2 + p(Y)·2/3 + p(G)·1/2`; `p(Y) = p(O)·2/4 + p(Y)·1/3`; `p(A) = p(H)·1/2 + p(G)·1/2`; `p(G) = p(O)·1/4 + p(A)·1/2`; `Σ p = 1`.
Matriz estacionaria: las 5 filas iguales a `[2/13, 4/13, 3/13, 2/13, 2/13]` (en el orden de estados correspondiente).

**¿Ergódico?** **No**: la matriz de transición contiene ceros, o sea no se puede llegar a cualquier estado desde cualquier otro.

### 4.1.4 Inciso 2B — Codificación predictiva (Kopt)
Cadena OREX: `1 0 0 0 0 0 0 1 0 1 0 0 0 0 1 0 0 0 0 0` (20 bits). `1` = error, `0` = coincidencia. Rachas de ceros antes de cada 1: 0, 6, 1, 4 y 5 ceros finales.

| K | Codificación (grupos de K bits) | Total |
|---|---|---|
| 2 | `00 11 11 00 01 11 01 11 10` (6 = 3+3+0 → `11,11,00`; 1 → `01`; 4 → `11,01`; 5 → `11,10`) | **18 bits** |
| 3 | `000 110 001 100 101` (0, 6, 1, 4, 5) | **15 bits** |
| 4 | `0000 0110 0001 0100 0101` | **20 bits** |

**Conclusión: Kopt = 3** (15 bits, mínimo). Con K = 4 ya empeora (20 > 15), se corta la búsqueda: un K mayor no mejora.
[Corrección] En la hoja de Zeballos: “Regular. Codificó como si hubiera un 1 al principio”; en la de Radicetti: “debió verificar que con K=4 aumenta la cantidad de bits transmitidos”.

### 4.1.5 Inciso 3 — Canal
**3A) BSC con p(0/0) = 0,95**: matriz `[[0,95; 0,05],[0,05; 0,95]]`.
1. `p(0)=0,5·0,95+0,5·0,05 = 0,5`; `p(1)=0,5`.
2. `H(B) = 0,5·log2(1/0,5)·2 = 1`.
3. `H(B/A) = 0,05·log2(1/0,05) + 0,95·log2(1/0,95) = 0,28639`.
4. `I(A,B) = 1 − 0,28639 = 0,71361` → **C = 0,7136 bits/símbolo** (con entrada equiprobable, que es lo que maximiza).

**3B) Peor canal ternario uniforme**: todas las probabilidades condicionales = 1/3 (matriz 3×3 con 1/3 en todas las celdas). Con eso la mitad… “el 33 % de las veces miente” — la capacidad es 0: `H(B/A)=H(B)=log2 3`, `I(A,B)=0` (emisor y receptor independientes).

**3C) Canal binario P(0/0)=0,65, P(1/1)=0,95**: matriz `[[0,65; 0,35],[0,05; 0,95]]`.
- A) **No es simétrico**: las filas no son permutación una de la otra (y la fila 0 no suma bien con la 1 en términos de permutación).
- B) Se debe dar **mayor probabilidad al símbolo 1** a la entrada, porque es el que el canal menos confunde (acierta el 95 %).

---

## 4.2 VERSIÓN B — `…TINA-ANITALAVALATINA-ANIT…`

Cadena base: `ANITALAVALATINA` (15 símbolos): A 6, N 2, I 2, T 2, L 2, V 1.

### 4.2.1 Inciso 1 — Discretización (PCM, ±5 V, error ±0,005 V)
- Rango: 10 V. Con valor medio, ancho de segmento = 2·0,005 = 0,01 V.
- Nº de segmentos = 10/0,01 = **1000** → 2¹⁰ = 1024 ≥ 1000 → **10 bits**.
- Verificación (Carbajo): `10 V / 1024 = 0,009766 V`; `/2 = 0,00488 V ≤ 0,005 V` ✔.
- Agustín Retner: partió de ±0,01 V con el mismo razonamiento → 1000 niveles → 10 bits.
- Capdevila: “10 V/0,005 V = 2000 segmentos; al tomar el valor medio se reduce a la mitad → 1000 segmentos; con 10 bits (1024)”.
- Comentario habitual de la consigna: discutir con el grupo que tomar el valor medio **duplica el ancho** y permite 1 bit menos que sin esa condición.

### 4.2.2 Inciso 2A.A — Redundancia (independiente)
`p(A)=6/15; p(N)=p(I)=p(T)=p(L)=2/15; p(V)=1/15`.
`H = 6/15·log2(15/6) + 4·(2/15·log2(15/2)) + 1/15·log2 15 = 0,5288 + 1,5503 + 0,2605 ≈ 2,3396 bits/símbolo`
`Hmax = log2 6 = 2,585` → `R = 1 − 2,3396/2,585 ≈ 0,095` (≈ 9,5 %).

> [Nota] Cada alumno obtuvo valores distintos: Capdevila H = 2,331, R = 9,82 % (marcado “Bien”); Carbajo H = 2,543 → R = 1,6 % (el valor de H no corresponde: el cálculo correcto es 2,3396); Retner calculó la redundancia contra un código bloque de 3 bits (`R = 1 − 2,3395/3 = 0,2201`, 22 %), es decir `R = 1 − H/L` con L = longitud del código ASCII/bloque de 3 bits. Lo habitual de la consigna es `R = 1 − H/Hmax`.

### 4.2.3 Inciso 2A.B — Huffman
Pasos (ordenar y sumar las dos menores):
1. `A 6/15 | N 2/15 | I 2/15 | T 2/15 | L 2/15 | V 1/15` → sumar `L+V = 3/15`.
2. Quedan `6, 3, 2, 2, 2` → sumar `I+T`(4/15) [o similar].
3. `6, 4, 3, 2` … hasta llegar a `9/15` y `6/15`, y finalmente 15/15.

Código obtenido (todos coinciden):
```
A = 1
N = 001
I = 010
T = 011
L = 0000
V = 0001
```
Longitud media `L = 6/15·1 + 2/15·3·3 + 2/15·4 + 1/15·4 = 36/15 = 2,4 bits/símbolo`.

Agustín Retner presentó otro código: A=0, N=101, I=110, T=111, L=1000, V=1001 (también válido: depende de dónde se asigna el 0/1).

### 4.2.4 Inciso 2A.C — Probabilidades que igualan Huffman y Shannon
6 símbolos: `p(si)=2^(−li)` → **A = 1/2, N = 1/4, I = 1/8, T = 1/16, L = 1/32, V = 1/32** (Σ = 1, Kraft = 1).
[Corrección] Capdevila escribió A = 1/2, N = 1/4, I = T = L = V = 1/16 (suma 1; los `log2(1/p)` son enteros, así que también cumple) y quedó “Bien” en el escaneo. Carbajo y Retner usaron 1/2, 1/4, 1/8, 1/16, 1/32, 1/32.

### 4.2.5 Inciso 2A — Fuente de Markov de 1er orden
Transiciones contadas sobre `ANITALAVALATINA` (+ cierre circular con `A`). Matriz (orden A, N, I, T, L, V):
```
        A     N     I     T     L     V
A     1/6   1/6    0    1/6   2/6   1/6
N     1/2    0    1/2    0     0     0
I      0    1/2    0    1/2    0     0
T     1/2    0    1/2    0     0     0
L      1     0     0     0     0     0
V      1     0     0     0     0     0
```
(Retner: A→A 1/6; A→N 1/6; A→T 1/6; A→L 2/6; A→V 1/6; etc.)

**Sistema estacionario** (`p·P = p`):
- `p(A) = 1/6 p(A) + 1/2 p(N) + 1/2 p(T) + p(L) + p(V)`
- `p(N) = 1/6 p(A) + 1/2 p(I)`
- `p(I) = 1/2 p(N) + 1/2 p(T)`
- `p(T) = 1/6 p(A) + 1/2 p(I)`
- `p(L) = 2/6 p(A)`
- `p(V) = 1/6 p(A)`
- `Σ p = 1`

Solución: `[6/15, 2/15, 2/15, 2/15, 2/15, 1/15]`. **Matriz estacionaria**: 6 filas iguales a ese vector.
**¿Ergódico?** **No**: hay ceros en la matriz de transición, es decir existe al menos una transición imposible y desde algunos estados no se puede acceder a todos los demás.

### 4.2.6 Inciso 2B — Codificación predictiva (mismo método y resultado)
Cadena `10000001010000100000`. K=2 → 18 bits; K=3 → **15 bits**; K=4 → 20 bits → **Kopt = 3**.
[Corrección Retner] “K=4 > K=3 ⇒ cortamos la búsqueda del K óptimo, porque esto es un indicio suficiente para no seguir probando contenedores de más bits.”

### 4.2.7 Inciso 3 — Canal
**3A) BSC con p(0/0) = 0,95**: igual que en la versión A: `I(A,B) = H(B) − H(B/A) = 1 − 0,2864 = 0,7136` → C = 0,7136.
(Carbajo: `H(B/A) = 0,95·log2(1/0,95) + 0,05·log2(1/0,05) = 0,2864`; `I = 0,7136`. [Corrección Capdevila] Calculó 8,7178: error, `I` no puede superar 1 bit.)

**3B) Peor canal ternario uniforme**:
```
      0     1     2
0   1/3   1/3   1/3
1   1/3   1/3   1/3
2   1/3   1/3   1/3
```
Con esas probabilidades las salidas son independientes de las entradas; `I(A,B) = 0`: **no hay flujo de información, los extremos A y B son independientes**.
[Corrección Retner] “Debió escribir el valor de las condicionales; efectivamente vale 0,333”.

**3C) Canal binario P(0/0)=0,65 … P(1/1)=0,95**:
- A) **No es simétrico** (las filas no son permutación una de la otra).
- B) Se debe dar mayor probabilidad al símbolo **1**.
Retner: para el binario `[[0,65, 0,35],[0,05, 0,95]]` calculó `p(0)=0,5·0,95+0,5·0,15 = 11/20` (mal, mezcló matrices), `H(B)=0,9457…`; marcado “Falló el resultado”.

---

# PARTE 5 — Parcial 10-10-2023, “Parte 2” (`Parcial N°1 2023 PARTE 2 CORREGIDOS.pdf`, Radicetti)

Corresponde a la **Versión A** (HOY-YOHAGOYOGAHOY, DPCM). Resumen de lo que resolvió y de las correcciones:

1. **Discretización**: mal (50 %): usó 400 niveles / 9 bits; correcto: 2 V / 0,01 V = 200 segmentos → **8 bits** (ver 4.1.1).
2. **2A**: `H = 2,25776`, `R = 1 − 2,2577/2,3219 = 2,76 %`. Shannon (misma tabla que en 4.1.2) con binarios por multiplicaciones sucesivas por 2 (ej.: 0,3077→0; 0,6154→0 [parte entera]; 1,2308→1 …). C) “las probabilidades deben ser potencias de la base: 1/4, 1/8, 1/16, 1/32, 1/64, deben sumar 1”.
3. **Markov**: matriz con estados H, O, Y, A, G (ver 4.1.3), estacionaria `[2/13, 4/13, 3/13, 2/13, 2/13]` → “no es ergódico porque la matriz de transición contiene ceros”.
4. **2B** (predictiva): K = 2: 18 bits; K = 3: 15 bits (`110 001 100 101` + grupo inicial); [Corrección] “es mejor un K = 3 por la cantidad de bits que ocupa; debió verificar que con K=4 aumenta la cantidad de bits transmitidos.”
5. **Canal**: BSC 0,95: `P(0)=P(1)=0,5`, `H(B)=1`, `H(B/A)=0,2863`, `I = 0,7137` ✔. 3B: condicionales del peor canal = 0,33 ✔. 3C: “es un canal simétrico, no uniforme [sic]” `[[0,95; 0,05],[0,35; 0,65]]`: se debería dar el 0 [la consigna era la matriz 0,65/0,95].
6. **Puntajes**: 100 % en canal; 90 % en 2A; 70 % en 2B; 50 % en discretización.

---

# PARTE 6 — Parcial de Arce (`Parcial N°1 de … Johana Arce-CORREGIDO.pdf`)

> [Nota] El PDF no incluye el enunciado, solo la resolución. Se deduce que consta de: Codificación de fuente (2 distribuciones de 8 símbolos, Shannon y Huffman), Encriptación, y Canal de comunicación. Nota total: **7/10**.

## 6.1 Codificación de fuente
### Distribución I (16 posibles, 8 símbolos) — `p(si)` en 16avos
A 4/16, E 4/16, B 2/16, D 2/16, C 1/16, F 1/16, G 1/16, H 1/16.
Longitud fija: 8 símbolos → 3 bits/símbolo (“8b por símbolo, 64b”, para 8·8… comparación sobre una secuencia total de 16 símbolos: 48 bits).

**Shannon** (orden A, E, B, D, C, F, G, H):
| Si | FA | Decimal | Binario | log2(1/p) | +1 | Long. | Código |
|---|---|---|---|---|---|---|---|
| A | 4/16 | 0 | 0 | 2 | 3 | 3 | 000 |
| E | 4/16 | 0,25 | 0,010 | 2 | 3 | 3 | 010 |
| B | 2/16 | 0,5 | 0,1000 | 3 | 4 | 4 | 1000 |
| D | 2/16 | 0,625 | 0,1010 | 3 | 4 | 4 | 1010 |
| C | 1/16 | 0,75 | 0,11000 | 4 | 5 | 5 | 11000 |
| F | 1/16 | 0,8125 | 0,11010 | 4 | 5 | 5 | 11010 |
| G | 1/16 | 0,875 | 0,11100 | 4 | 5 | 5 | 11100 |
| H | 1/16 | 0,9375 | 0,11110 | 4 | 5 | 5 | 11110 |

`L(S) = 3,75 bits/símbolo` (8×3,75 = 30 b).
[Corrección] “SI LA CANTIDAD DE INFORMACIÓN ES UN ENTERO, SIEMPRE SE TRABAJA CON LA COTA INFERIOR DE ESE VALOR. USTED TOMÓ LA COTA SUPERIOR. DE HECHO, PARA ESTA DISTRIBUCIÓN, ES COINCIDENTE LA LS CON LA LH.” → Las longitudes correctas: A, E → 2; B, D → 3; C, F, G, H → 4; `L_Shannon = 2,75`, igual a Huffman.

**Huffman** (misma distribución): L(H) = **2,75 bits/símbolo** (8×2,75 = 22 b).
Códigos: A = 10, E = 11, B = 010, D = 011, C = 0000, F = 0001, G = 0010, H = 0011.

### Distribución II (en 20avos)
A 4/20, B 4/20, C 2/20, D 2/20, E 2/20, F 2/20, G 2/20, H 2/20.
**Shannon**: A: 3 (000), B: 3 (001), C: 4… `log2(20/4) = 2,32 → 3`; C…H: `log2(20/2) = 3,32 → 4`.
Tabla FA/Decimal/Binario: A 0 / 0,2 / 0,4 / 0,5 / 0,6 / 0,7 / 0,8 / 0,9 → códigos 000, 001, 0110, 1000, 1001, 1011, 1100, 1110. `L(S) = 3,6 bits/símbolo` (8×3,6 = 28,8 b).
**Huffman**: L(H) = **3** (8×3 = 24 b): códigos A=000, B=001, C=010, D=011, E=100, F=101, G=110, H=111.
[Corrección] “FALTÓ QUE RESPONDIERA LAS PREGUNTAS. PJE OBTENIDO 2/3,5.”

## 6.2 Encriptación
- Clave de transposición: `(8, 7, 6, 5, 4, 3, 2, 1)` (se invierte cada bloque de 8 letras); clave Vigenère: **BLUE**.
- Texto cifrado: `VPOJSPSE TCYZJYUR UWYHPTLE PEIQFCLI`.
- **A) Procedimiento**: restar la clave (BLUE repetida) letra a letra módulo 26 (ej.: `V − B = U`, `P − L = E`, `O − U = U`, `J − E = F` …) → `UEUFREYA SREVINAN TLEDOIRA OTOMERRE`; luego invertir cada bloque de 8 según la clave (8,7,6,5,4,3,2,1) → `AYERFUEU NANIVERS ARIODELT ERREMOTO` = **“AYER FUE UN ANIVERSARIO DEL TERREMOTO”**.
  (Notas al margen: `H + O + L + A = I + Z + F`, con `H = I − 8` etc.; mod 26.)
- **B) Entropías**: `H_original = 3,60534`; `H_BLUE (texto encriptado) = 4,01532`; el original es el de menor entropía (la encriptación reparte las frecuencias y sube H). Se detalla `p(si)` en 32avos de cada letra del texto cifrado y del original.
- **C)** “Considero más seguro la encriptación de **Vigenère**, ya que rompe bastante con las probabilidades de ocurrencia de los símbolos, por lo que es más difícil descifrarlo.”
- **D)** “Lo conveniente sería **primero comprimir y luego encriptar**, ya que los algoritmos de compresión se basan bastante en la frecuencia de aparición de los símbolos; el proceso podría no ser muy conveniente luego de encriptar, ya que se rompe con esas frecuencias.”
[Corrección] 3,5/3,5.

## 6.3 Canal de comunicación
**A) Canal binario 2×2** con `p(a1)=0,7, p(a2)=0,3`, matriz `[[0,8; 0,2],[0,2; 0,8]]`:
1. `p(b1) = 0,7·0,8 + 0,3·0,2 = 0,62`; `p(b2) = 0,7·0,2 + 0,3·0,8 = 0,38`.
2. `H(B/A) = 0,62·0,8·log2(1/0,8)… ` [según la hoja: `0,4476 + 0,2743 = 0,7219`].
3. `H(B) = 0,62·log2(1/0,62) + 0,38·log2(1/0,38) = 0,958`.
4. `I(A,B) = 0,958 − 0,7219 = 0,2361`.
5. **Capacidad**: con `p(a1)=p(a2)=0,5` → `H(B)=1`, `H(B/A)=0,7219` → **C = 0,2781**.
[Corrección] “NO ENTIENDO POR QUÉ HACE EL CÁLCULO CON P(0)=0,7 Y P(1)=0,3 SI SOLAMENTE SE PEDÍA CALCULAR LA ‘C’ CAPACIDAD DE CANAL. QUE LO HACE EN LA SIGUIENTE FILA.” [Nota] La hoja escribe “C = I(A,B) = 0,7219”, pero 0,7219 es `H(B/A)`; la capacidad correcta con entrada uniforme es `1 − 0,7219 = 0,2781`.

**B) Canal ternario** con todas las condicionales 0,3333: `p(b1)=p(b2)=p(b3)=0,3333`; `H(B)=1,5849`; `H(B/A)=0,3333·0,3333·log2(1/0,3333)·…` (hoja: 0,5283); `I(A,B) = 1,5849 − 0,5283 = 1,0566` “← capacidad de canal”.
[Corrección] “LA IDEA Y LO SOLICITADO ERA QUE TRABAJARA CON EL MEJOR CANAL TERNARIO, POR EJ. AQUEL CON UNOS EN LA DIAGONAL PRINCIPAL. USTED HA PROPUESTO TRABAJAR CON EL PEOR CANAL CUYA CAPACIDAD DEBIÓ HABER DADO CERO. MAL. PUNTAJE OBTENIDO: 1,5/3. PJE TOTAL OBTENIDO 7/10.”

---

# PARTE 7 — Recuperatorio Tema 2 (Galdame) — `Parcial1-Galdame-2023.pdf`

## Enunciado
**RECUPERATORIO Parcial 1 — Teoría de la Información, 4to. año LCC 2022, Tema 2: Compresión y Fuentes de Markov.**
- **Ejercicio 1)** Fuente de Markov: `…EQUETENGUEEMEREQUEGUEGEJE…`. Se pide: 1.1) Encontrar la matriz de transición para un proceso de Markov de orden 1. 1.2) Comprimir utilizando **Shannon**. 1.3) Comprimir utilizando **Fano**, considerando la fuente como independiente. 1.4) Comparar los resultados.
- **Ejercicio 2)** Canal BSC `[[7/8, 1/8],[1/8, 7/8]]`: encontrar `I(A,B) = H(B) − H(B/A)`.
- **Ejercicio 3)** Huffman dinámico: descomprimir `000010010010011010`, sabiendo que fuente y codificación son: A 00, N 01, D 10, B 11.
- **Teoría**: 1) ¿Cómo cree que serían los resultados del punto 1.2 si se usara una transformada de Burrows-Wheeler previa a encontrar la matriz de transición? Justifique. 2) Dada una fuente binaria, ¿cuál es el peor canal BSC? Justifique.

## Resolución del alumno + correcciones
**1.1) Matriz de transición**: `n = 23`, `q = 8`. Frecuencias: E = 10, Q = 2, U = 4, T = 1, N = 1, G = 3, M = 1, R = 1. Contó las transiciones entre cada par de símbolos (E→E: 2, E→Q: 2, E→T: 1, E→N: 1, E→G: 2, E→M: 1, E→R: 1, Q→U: 2, U→E: 4, T→E: 1, N→G: 1, G→E: 1, G→U: 2, M→E: 1, R→E: 1) y armó la matriz **dividiendo por 23** (probabilidad conjunta).
> [Nota] Para una matriz de transición correcta cada fila se divide por la cantidad de veces que aparece el estado de origen (p. ej. fila E: 2/10, 2/10, 1/10, 1/10, 2/10, 1/10, 1/10). El docente marcó con signo de pregunta “¿y Markov?”.

**1.2) Shannon** (con probabilidades de frecuencia sobre 23): E 10/23, U 4/23, G 3/23, Q 2/23, T N M R 1/23. Longitudes por cotas: E → 2, U → 3, G → 3, Q → 4, T/N/M/R → 5. Códigos: E 00, U 011, G 100, Q 1011, T 11010, N 11011, M 11101, R 11110. Archivo comprimido total: **67 bits**.
**1.3) Fano**: el alumno comprimió con **Huffman** en lugar de Fano (el docente anotó “NO. Comprimió x Huffman”). Resultado: `Lf = 2,47826` bits/símbolo.
**1.4) Comparación**: `L_Shannon = 3 [sic] > L_Fano = 2,478` → “Fano es más óptimo”.

**2) Canal** — el alumno asumió `p(a1) = 0,6`, `p(a2) = 0,4` e hizo: `p(b1) = 0,575`, `p(b2) = 0,425`; posteriores con Bayes (0,9130; 0,1765; 0,0870; 0,8235), `H(B) = 0,9837`, `H(B/A) = 1,0987`, `I = −0,115`.
[Corrección] “No. Corresponde esto, sería I(A,B) = H(A) − H(A/B)”, y `I` nunca puede ser negativa (error). Lo correcto: con la entrada equiprobable `p(0)=p(1)=0,5`, `H(B)=1`, `H(B/A) = (7/8)log2(8/7) + (1/8)log2 8 = 0,5436`, `I(A,B) = 0,4564 bits`. *[Completado]*

**3) Huffman dinámico (descompresión)**: resultado **“ANDABAN”** (marcado B = bien). Pasos: `00` → A (primer símbolo con código fijo), `0 01` → NYT + N, `00 10` → NYT + D, `1` → A (ya en el árbol), `0 11` → NYT + B, `10` → …, final `1`. Reconstruyó el árbol con pesos paso a paso aplicando la Sibling Property (SP) hasta el árbol final `B1 D1 N2 2 A3 4 7`.

**Teoría**
1) Con BWT los resultados del punto 1.2 determinaron una longitud promedio del código mucho menor a la que se obtuvo, logrando aproximarse a la entropía de la fuente. [Corrección] El docente puso “¿Por qué?” (la respuesta debe justificar: BWT agrupa símbolos iguales → la matriz de transición queda con muchos valores próximos a 1 y menor entropía condicional).
2) **El peor canal BSC** es `[[0,5; 0,5],[0,5; 0,5]]`: nunca se podría saber con exactitud a qué se hace referencia, si al 1 o al 0, debido a esa equiprobabilidad al enviar información. (Marcado B = bien.)
El examen figura **“Reprobado”**.

---

# PARTE 8 — Parcial de Nanni Rebollo (`Parcial_1_-_VISTO-KLE.pdf`) y examen Condicional (`Condicional.pdf`)

## 8.1 `Parcial_1_-_VISTO-KLE.pdf` (nota total 6,1)
**Ej. 1)** `V = {a, e, i, o, u}`, `r = 5`. Secuencia: `aeieeieouou aaaa` (15 símbolos). `p(a)=5/15`, `p(e)=4/15`, `p(i)=p(o)=p(u)=2/15`.
`H(S) = 5/15·log5(15/5) + 4/15·log5(15/4) + 3·(2/15·log5(15/2)) = 0,9473` (en unidades de base 5) y `R = 1 − H(S)/L = 1 − 0,9473/1 = 0,0527` (5,26 %).
[Corrección] 100/100 · 1,5 P.

**Ej. 3)** Canal ternario `[[0,8; 0,1; 0,1],[0,1; 0,8; 0,1],[0,1; 0,1; 0,8]]`, `p(0)=p(1)=p(2)=1/3`.
- a) `H(B) = 1,5849`; `H(B/A) = 0,8·log2(1/0,8) + 0,1·log2(1/0,1) + 0,1·log2(1/0,1) = 0,9219`; `I(A,B) = 1,5849 − 0,9219 = 0,663` → **C = 0,663 bits**.
- b) Matriz con todos los elementos 1/3: el canal es el peor posible; “debido a que la entropía del receptor vista desde el emisor (error) se igualará con la entropía de salida, la capacidad del canal será **cero**”.
[Corrección] 100/100 · 2,5 P.

**Ej. 4)** Cadena `aabbccbacabcaaa` [según la hoja: 8 a, 4 b, 4 c, total 16]:
- **a) Huffman**: `a 8/16`, `b 4/16`, `c 4/16`. Se unen `b+c = 8/16`; códigos `a = 1`, `b = 00`, `c = 01`. Los primeros 4 símbolos `aabb` → `1 1 00 00` = **110000 (6 bits)**.
- **b) Aritmético**: fórmulas `cota_inf = cota_ant_inf + (cota_ant_sup − cota_ant_inf)·cota_inf(s)`; `cota_sup = cota_ant_inf + (…)·cota_sup(s)`. El alumno dio `aabb → 0,578125 → 100101` (6 bits).
- [Corrección] Anotaciones en la hoja: “la cota inferior es 0,5”, “cota inferior 0,75”, “cota inferior es 0,8125”, “cota superior 0,875”, y “SON IGUALES LAS COTAS SUPERIOR E INFERIOR. ERROR: NO SE PUEDE DISCERNIR UN VALOR ENTRE ELLO”. Puntaje 60/100 · 2,1 P. Comentario general: “Consulta: PCM-DPCM y aritmético”.
- *[Completado]* Con el orden de intervalos que usa el docente (c = [0; 0,25), b = [0,25; 0,5), a = [0,5; 1)): tras `a` → [0,5; 1); tras `aa` → [0,75; 1); tras `aab` → [0,8125; 0,875); tras `aabb` → [0,828125; 0,84375). Un número dentro: 0,828125 = 0,110101₂ → **110101 (6 bits)**, la misma longitud que Huffman en esos 4 símbolos.

## 8.2 `Condicional.pdf`
**Enunciado (Condicional)**: Una señal de rango dinámico −10 V a 10 V se ha codificado en PCM y cada segmento tiene una variación de **2 microvolt**. A) Encontrar el error en que se incurre si se aproxima la señal discreta al valor medio del segmento. B) Decir con cuántos bits se ha codificado esa instancia PCM. Para una señal de audio, cuya frecuencia máxima es **2 kHz**, especificar cuántos bits se transmiten en PCM para codificar **5 minutos** de señal. Asimismo, si en una codificación **DPCM** el rango dinámico entre muestras es de 2 V, ¿cuántos bits serán necesarios para mantener el error de PCM y cuántos se transmitirán en los mismos 5 minutos de aquella señal de audio?

**Resolución del alumno (parte A)**: `Vmax = 10, −Vmax = −10, salto = 0,000002 V`; rango = 20 V; `Error = salto/2 = 0,000002/2 = 0,000001 V` (**1 µV**). La parte B quedó sin resolver en la hoja.
*[Completado B]*:
- Nº de niveles = 20 V / 2·10⁻⁶ V = 10⁷ → `log2(10⁷) = 23,25` → **24 bits** por muestra.
- Frecuencia de muestreo (Nyquist) = 2·2 kHz = 4000 muestras/s. En 5 min = 300 s → 1.200.000 muestras.
- PCM: 1.200.000·24 = **28.800.000 bits** (28,8 Mbit).
- DPCM, mismo error (segmento 2 µV): niveles = 2 V / 2·10⁻⁶ V = 10⁶ → `log2(10⁶) = 19,93` → **20 bits/muestra** → 1.200.000·20 = **24.000.000 bits** (24 Mbit). Ahorro = 4 bits/muestra (≈16,7 %).

**Ejercicio 2 (Condicional)**: alfabeto q = 3 `{a, b, c}`, secuencia `c-abc abc abc abc abc-a` (18 símbolos).
- a) `P(a)=P(b)=P(c)=6/18`. Huffman: se unen b+c = 12/18 → un símbolo recibe `1`, otros 2 bits (`L = 6/18·1 + 12/18·2 = 1,6667 bits`). `H = 3·(6/18·log2 3) = 1,5849`. `R = 1 − H/L = 1 − 1,5849/1,6667 = 0,049` (4,9 %).
- b) **Markov**: matriz de transición determinística: `P(b/a)=1`, `P(c/b)=1`, `P(a/c)=1` y el resto 0. Como en cada estado existe un único símbolo posible, y por la secuencia dada solo se pueden formar cadenas “abc” repetidas, se codifica ese subconjunto con el código `0`.

---

# PARTE 9 — Preguntas teóricas con sus respuestas (`Preguntas teóricas Parcial 1.docx`)

*(Respuestas armadas por los alumnos; algunas aclaran de dónde salieron: “según mis conocimientos”, “chat gpt”, etc.)*

1. **¿Qué técnica va primero, LZW o Huffman?** → Primero **LZW** y después **Huffman**. LZW elimina redundancias de secuencias/patrones repetidos creando un diccionario de códigos para ellas; el texto resultante todavía tiene frecuencias dispares entre símbolos, y Huffman las explota. El orden inverso o usar cada uno solo comprime menos. (La efectividad concreta depende del texto de entrada.)
2. **Fuente de 7 símbolos para que Huffman, Shannon y Fano coincidan** → distribución `p(si) = r^(−li)`: a=1/2, b=1/4, c=1/8, d=1/16, e=1/32, f=1/64, g=1/64. **Kraft**: `2⁻¹+2⁻²+2⁻³+2⁻⁴+2⁻⁵+2⁻⁶+2⁻⁶ = 1`. **Relación H–L**: `H ≤ L`; la entropía es la cota inferior de cualquier longitud promedio de una codificación; si las probabilidades son múltiplos (potencias) de la base, `H = L` y Kraft = 1. Una codificación que perfore la cota es con pérdida de información.
3. **Compansión (necesidad y fenómeno)**: es la compresión (cuantificación no uniforme) de la señal antes de cuantificar y la expansión luego de recibirla; se usa para dar mayor resolución a las amplitudes pequeñas, que son las más frecuentes (voz), y menor a las grandes. Necesidad: eficiencia en almacenamiento y transmisión, ahorro de costos. (El docx lo explica desde “datos con redundancias y patrones que pueden eliminarse sin perder información esencial”.)
4. **Propiedades de la cantidad de información I**: 1) siempre es positiva; 2) es inversamente proporcional a la probabilidad (un evento raro, p = 1/100, da mucha información); 3) aumenta con la cantidad de posibles eventos o mensajes; 4) para eventos independientes es **aditiva**; 5) la información promedio (entropía H) se **maximiza ante sucesos equiprobables**.
5. **PCM vs DPCM**: **PCM**: se muestrea la señal, se cuantifica cada muestra y se codifica en binario (palabra de longitud `⌈log2 niveles⌉`). **DPCM**: se codifica la *diferencia* entre una muestra y la anterior (el rango de diferencias es menor), se cuantifican esas diferencias y se codifican en binario. Diferencias: enfoque (muestras vs diferencias), eficiencia (DPCM usa menos bits/ancho de banda cuando las muestras varían poco) y mayor tolerancia al ruido.
6. **Fuente de 5 símbolos**: ½, ¼, ⅛, 1⁄16, 1⁄16 → Kraft `2⁻¹+2⁻²+2⁻³+2⁻⁴+2⁻⁴ = 1`; relación H–L: `H ≤ L`, aquí `H = L`.
7. **Peor canal ternario uniforme**: todas las probabilidades condicionales en 0,33 → capacidad **0**. Emisor y receptor se consideran **independientes** (“yo ya sé lo que vos estás pensando, no necesito que me transmitas información”). Es el canal de máxima incertidumbre/ruido.
8. **¿Por qué los estáticos (Huffman, Shannon, Fano) son de doble lectura? ¿Con o sin pérdida?** → Primero se lee todo el archivo para calcular las probabilidades y recién después se lee otra vez para comprimir. **Son sin pérdida.**
9. **¿Mayor compactación con mayor o menor redundancia?** → **Mayor redundancia**: hay patrones/información innecesaria y más oportunidades de representarlos eficientemente (“ya sabés lo que va a venir, más podés comprimir”).
10. **¿Instantáneos ⊂ unívocos, o los unívocos son instantáneos?** → Todo código instantáneo es unívoco (no al revés). Fano, Shannon y Huffman garantizan códigos unívocos **e instantáneos**: ningún código es prefijo de otro. Huffman no produce códigos que sean prefijos entre sí.
11. **Fuente de 4 símbolos**: a = 1/2, b = 1/4, c = 1/8, d = 1/8; Kraft `2⁻¹+2⁻²+2⁻³+2⁻³ = 1`; `H = L`.
12. **¿Los árboles de Huffman estático y dinámico siempre coinciden? (Verdadero/Falso)** → **Falso.** El estático arma un árbol fijo con las frecuencias totales del conjunto de datos (doble lectura); el dinámico lo construye a medida que lee y comprime, y se va adaptando. Ejemplo del archivo (imagen del docx): con símbolos A, C, S, el estático da `A = 1, C = 00, S = 01`, mientras que el dinámico queda `A = 0, S = 10, C = 11`; los árboles son distintos.
13. **¿Cuál es el peor canal BSC?** → La matriz con todo en 0,5 (`[[0,5; 0,5],[0,5; 0,5]]`), porque nunca se puede saber con exactitud a qué se hace referencia (1 o 0) por la equiprobabilidad al enviar información. Capacidad 0.
14. **¿Por qué los archivos comprimidos tienen mayor entropía y menor redundancia?** → Porque se incrementa la incertidumbre: cuanta más redundancia tiene la fuente, más se puede comprimir; al quitar la redundancia, los símbolos del archivo comprimido quedan casi equiprobables.

---

# PARTE 10 — Resumen de errores frecuentes marcados por el docente
1. **Shannon**: si `log2(1/p)` es entero, se usa ese entero (no +1). Hay que usar siempre la cota inferior (techo).
2. **Discretización**: con valor medio, el error es la mitad del ancho del segmento; ancho = 2·error. En DPCM se usa el rango de las *diferencias*.
3. **Predictiva**: verificar K+1; con K más grande que el óptimo ya empeora y se corta.
4. **Canal**: la capacidad se calcula con entrada equiprobable (BSC); no mezclar `p(0)=0,7` si solo se pide C. Peor canal ternario → capacidad **0**, no 1,0566.
5. **Aritmético**: si cota inferior = cota superior con la precisión disponible, no se puede seguir (error de precisión).
6. **Markov**: dividir cada fila por las apariciones del estado origen (no por n), y declarar “no ergódico” si hay ceros que impiden acceder a todos los estados.
7. **Fano ≠ Huffman**: leer cuál algoritmo piden.
8. **Contestar todas las preguntas** (Arce perdió puntos por no responderlas).
