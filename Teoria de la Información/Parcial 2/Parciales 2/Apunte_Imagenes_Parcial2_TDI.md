# Procesamiento de imágenes: guía para el Parcial 2 de TDI

> Unidad 10 de la cátedra. Es la pregunta corta del parcial (1,5 puntos en 2020). Aparece en 2012, 2020 y 2025, y siempre es de los cuatro tipos que están resueltos en la sección 2: **filtro paso bajo, máscaras de rectas, media aritmética y RLE/vectorial**.
> Cómo usar esta guía: leé la sección 1 (los conceptos) y después hacé cada ejercicio de la sección 2 tapando la resolución.

## 0. Mapa rápido: qué pregunta cae y qué concepto necesitás

| Parcial | Pregunta | Concepto que la resuelve |
|---|---|---|
| 17/11/2025 (Tema 1), Ej. 6 | «Dé un ejemplo de filtro paso bajo e indique qué efectos produce sobre una imagen» | 1.4 Filtros paso bajo |
| *(variante propia, aún no salió)* | «Dé un ejemplo de filtro paso alto e indique sus efectos» | 1.4 y 1.8 (Ejercicio 1b) |
| 15/12/2020, Ej. 4 | Vectorial vs. bitmap, y RLE de PCX de `129,129,129,129,129,194` | 1.1 y 1.6 |
| 21/11/2012 (Tema 1) | Con máscaras, ¿a qué recta pertenece el punto central? | 1.5 Máscaras de rectas |
| 21/11/2012 (Tema 2) | Suavizar el punto central de dos ventanas con media aritmética | 1.3 y 1.4 |
| *(variante teórica probable)* | «¿Por qué en PCX el contador se reconoce por los dos primeros bits en 1 y qué pasa con los colores ≥ 192?» | 1.6 (bits del byte) |

> **Revisión de parciales viejos (2012, 2013, 2020, 2025).** Las únicas preguntas de imágenes que aparecen son las de la tabla: **paso bajo** (2025), **RLE de PCX + vectorial/bitmap** (2020), **máscaras de rectas** y **media aritmética** (2012). En 2013 y en los otros archivos de la carpeta no hay preguntas de imágenes. Los dos temas que más conviene dominar son **RLE de PCX (bits y límite 192)** y **filtros paso bajo/paso alto**; tienen respuesta modelo en la sección 0.1.

## 0.1 Las dos preguntas más probables, con respuesta modelo

**A) RLE de PCX: ¿qué son los dos primeros bits y qué pasa hasta el 192?**

- PCX guarda cada color en **1 byte** (8 bits, valores 0 a 255). Si un color se repite, se guardan **2 bytes**: un byte de **cantidad** y un byte de **color**.
- El byte de cantidad se reconoce porque tiene **encendidos (en 1) los dos primeros bits**: `11xxxxxx`. La cantidad va en los **6 bits restantes** (`xxxxxx`), por eso la racha máxima es $2^6-1=63$.
- Los dos primeros bits en 1 valen $128+64=192$ (`11000000` = `0xC0`). Entonces todo byte **$\ge192$** empieza con `11` y se interpreta como contador. Todo byte **$<192$** (0 a 191, empieza con `00`, `01` o `10`) es un **color**.
- **El problema** (la diapositiva lo marca como «PROBLEMAS…»): un color suelto $\ge192$ se confundiría con un contador. Solución: se lo escribe siempre precedido del contador `193` (`11000001` = racha de 1), aunque aparezca una sola vez. Los colores $<192$ sueltos se escriben tal cual.
- Costo: un color suelto $\ge192$ ocupa 2 bytes en vez de 1, así que en imágenes con pocas rachas el RLE puede **agrandar** el archivo.
- Ejemplo con bits: `129,129,129,129,129,194`. $129=10000001$ (empieza con `10`: es color). $194=11000010$ (empieza con `11`: parecería un contador de 2, por eso necesita escape). Resultado: `197,129,193,194` ($197=11000101$, cantidad $5$).

**B) Filtros paso bajo y paso alto: ejemplo y efectos**

| | Paso bajo | Paso alto |
|---|---|---|
| Ejemplo | Media 3×3: $\frac19\begin{pmatrix}1&1&1\\1&1&1\\1&1&1\end{pmatrix}$ (también gaussiano, mediana) | $\begin{pmatrix}-1&-1&-1\\-1&8&-1\\-1&-1&-1\end{pmatrix}$ (también high-boost, centro 9) |
| Coeficientes | **Todos positivos**; se divide por la suma | **Centro positivo, periferia negativa**; suma 0 (no se divide) |
| Qué deja pasar | Bajas frecuencias (zonas lisas) | Altas frecuencias (bordes, detalles) |
| Efecto | **Suaviza y reduce ruido**, pero **emborrona** bordes y detalles. Ventana mayor: más ruido eliminado, más desenfoque | **Realza bordes y detalles** (afila); en zona constante da 0; también **realza el ruido** |
| Ejemplo numérico | $\begin{pmatrix}10&10&10\\10&82&10\\10&10&10\end{pmatrix}\to162/9=18$ | misma ventana $\to 8\cdot82-80=576$ |

---

## 1. Conceptos previos

### 1.1 Qué es una imagen digital

Una imagen continua es una función $f(x,y)$ de intensidad luminosa. La luz que vemos es la que reflejan los objetos, así que:

$$f(x,y)=i(x,y)\cdot r(x,y)$$

- $i(x,y)$ es la **iluminación** (la luz que llega), $0<i<\infty$.
- $r(x,y)$ es la **reflectancia** (qué proporción refleja el objeto), $0<r<1$.

Para que una computadora la use hay que **discretizarla** de dos maneras:

1. **Espacial (muestreo):** se divide el plano en una cuadrícula de $M\times N$ puntos llamados **píxeles**.
2. **En amplitud (cuantización):** a cada píxel se le asigna un entero entre $0$ y $L-1$. Con 8 bits, $L=256$ niveles de gris (0 = negro, 255 = blanco).

Una imagen digital en gris es entonces una **matriz de números**. Todo el procesamiento de esta unidad es hacer cuentas sobre esa matriz.

**Adquisición** (cadena física): sistema óptico → sensor (señal eléctrica analógica) → digitalizador A/D.

**Imagen vectorial vs. bitmap** (cae en 2020):

| | Vectorial | Bitmap (mapa de bits) |
|---|---|---|
| Cómo se guarda | Figuras matemáticas: puntos, rectas, curvas, rellenos | Matriz de píxeles |
| Al ampliar | No pierde calidad | Se **pixela** |
| Tamaño | Chico (depende de la cantidad de figuras) | Más grande (depende de la resolución) |
| Sirve para | Logos, planos, tipografías | Fotos |
| Formatos (presentación) | CDR (CorelDraw), WMF (metaarchivo de Windows), DXF (AutoCad). Se usan en CAD, arquitectura e ingeniería | BMP, PCX, GIF, TIF, JPG |

**La luz y el ojo (presentación PDI 2026).** La luz visible es una porción del espectro electromagnético, aprox. entre **0,4 y 0,7 micrones**. La imagen se forma en la **retina** por dos tipos de receptores:

| | Conos | Bastones |
|---|---|---|
| Cantidad | 6 a 7 millones | 75 a 150 millones |
| Dónde | Concentrados en la **fóvea** | Repartidos por toda la retina |
| Función | **Color** y detalles finos | Impresión general del campo visual y **baja iluminación**; no ven color |
| Visión | **Fotópica** (luz brillante) | **Escotópica** (luz tenue) |

Esto justifica el submuestreo de la crominancia en JPEG (1.10): el ojo es más sensible al brillo (bastones) que al color (conos).

**PDI y ADI.** **PDI** (procesamiento digital de imágenes): pasar la imagen a formato digital y procesarla en computadora; la salida es otra imagen. **ADI** (análisis de imágenes): descripción y reconocimiento del contenido; la salida es una **descripción simbólica**. Tópicos: formación de la imagen (sistema óptico, sensor, digitalizador, con degradaciones), **restauración** (reduce deformaciones y degradaciones), **realce** (reducción de ruido, afilado, contraste), **compresión** (aprovecha la redundancia; **sin pérdida**: GIF, BMP, PCX; **con pérdida**: JPG, fractal; a mayor compresión, mayor degradación), **detección de bordes** (ayuda a segmentar regiones).

**Modelo de imagen simple (valores típicos).** $i(x,y)$: Sol en día soleado 9000 cd/pie², nublado 1000, Luna llena 0,01. $r(x,y)$: terciopelo negro 0,01; acero inoxidable 0,65; pared blanca 0,80; lámina plateada 0,90; nieve 0,93.

**Formatos BMP y PCX (estructura).** Ambos tienen: identificación del archivo, descripción del gráfico, tabla de colores, datos y final.

| | BMP | PCX |
|---|---|---|
| Identificación | Los dos primeros caracteres son `BM` | Primer byte `10`; segundo byte = versión (0 a 5) |
| Compresión | Normalmente sin comprimir (`bicompresion` = 0) | **RLE** |
| Cabecera | tamaño, desplazamiento a los datos, ancho, alto, planos (=1), bits por píxel, resolución, colores usados | rle (modo de codificación), bits por píxel, coordenadas de inicio y fin, resolución (normalmente 100), `byteslinea` |
| Paleta | Tabla de colores (para 256 colores, 768 bytes: R, G, B por cada índice) | Hasta 16 colores en la cabecera; si hay más (p. ej. 256) se usa una tabla de **768 bytes al final del archivo** |

### 1.2 Color (para completar la teoría)

- **RGB:** cada píxel es un vector de tres canales (rojo, verde, azul) de 8 bits cada uno. Son 24 bits por píxel (**True Color**), unos 16,7 millones de colores.
- **Indexado:** se guarda una **paleta** de colores y cada píxel solo tiene un índice (un byte) que apunta a la paleta. Lo usan **GIF, PCX y BMP de 8 bits**. Ahorra tamaño.
- **Luminancia/crominancia** ($YC_bC_r$, $YUV$): se separa el brillo del color. El ojo es muy sensible al brillo y tolera pérdida en el color. Es la base de JPEG y MPEG.

### 1.3 Operaciones sobre la imagen

Hay dos familias.

**Puntuales** (cada píxel de salida depende **solo de su propio valor**, no de sus vecinos):

- Aritméticas: **suma** (promediar varias capturas reduce el ruido), **resta** (elimina el fondo; p. ej. angiografía), **multiplicación/división** (corrige iluminación no uniforme).
- Lógicas: AND, OR, XOR, NOT con máscaras binarias (recortar o tapar objetos).
- **Negativo:** $I' = 255 - I$.
- **Umbralización:** $I'=0$ si $I\le T$, $I'=255$ si $I>T$.
- Traslación y rotación.

**Espaciales o de grupo** (cada píxel de salida depende de **sus vecinos**). Es lo que más cae en el parcial. Tres palabras que tenés que manejar:

- **Ventana:** el trocito de la imagen (3×3, 5×5) centrado en el píxel que estás calculando.
- **Máscara:** matriz de **pesos** del mismo tamaño que la ventana.
- **Convolución espacial:** el píxel de salida es la suma de los productos de cada píxel de la ventana por su peso.

**Receta para aplicar una máscara 3×3 a un píxel:**

1. Centrá la ventana 3×3 en el píxel.
2. Multiplicá cada píxel por el peso que está en la **misma posición** de la máscara.
3. Sumá los 9 productos.
4. Si la máscara es de suavizado (los pesos no suman 0), **dividí por la suma de los pesos** para no cambiar el brillo medio.
5. Redondeá al entero más cercano.

> En el parcial solo calculás el **píxel central** de cada ventana. No hace falta tratar los bordes de la imagen.

### 1.4 Filtros espaciales: paso bajo, paso alto y compañía

Pensá en las **frecuencias espaciales**. Las zonas lisas son bajas frecuencias. Los **bordes y detalles** (un salto brusco de gris) son altas frecuencias.

#### Paso bajo (suavizado)

Atenúa las altas frecuencias, así que **suaviza y emborrona**: reduce el ruido pero también borra bordes y detalles.

| Filtro | Cómo funciona | Particularidad |
|---|---|---|
| **Media** | El centro pasa a ser el promedio de la ventana | Máscara $\frac19\begin{pmatrix}1&1&1\\1&1&1\\1&1&1\end{pmatrix}$. Ventana más grande: más ruido eliminado y más desenfoque |
| **Gaussiano** | Promedio con pesos que decrecen con la distancia al centro | Máscara $\frac1{16}\begin{pmatrix}1&2&1\\2&4&2\\1&2&1\end{pmatrix}$. Emborrona menos que la media |
| **Mediana** | Se **ordenan** los 9 valores y el centro pasa a ser el 5.º | **No lineal**. El más eficaz contra ruido «sal y pimienta»; conserva mejor los bordes |

**Detalles de la presentación sobre paso bajo:**

- **Media:** hace la imagen algo borrosa y reduce ruido; todos los coeficientes son **positivos**. Al pasar de 3×3 a 5×5 se mitiga más el ruido gaussiano, a costa de más desenfoque.
- **Gaussiano:** con 3×3 casi no se nota diferencia contra la media, pero se dice que emborrona un poco menos y por eso suaviza «mejor».
- **Mediana:** se usa cuando se busca **reducir ruido más que difuminar**, porque media y gaussiano difuminan bordes. Ejemplo de la presentación: valores ordenados $3,3,4,4,5,5,5,6,7$ → mediana **5**. Con ruido «sal y pimienta», la ventana 3×3 no elimina todo el ruido; la 5×5 sí lo elimina, pero deja la imagen borrosa.

**Ejemplo con la mediana.** Ventana $\begin{pmatrix}3&18&73\\1&7&20\\9&25&14\end{pmatrix}$. Ordenados: $1,3,7,9,14,18,20,25,73$. El quinto es **14**, así que el centro 7 pasa a 14. El 73 (pico de ruido) no influye.

#### Paso alto (realce de bordes)

Realza las altas frecuencias. Máscara con **centro positivo y periferia negativa**, y la **suma de los pesos es 0**, por lo que en una zona constante la respuesta es nula.

$$\begin{pmatrix}-1&-1&-1\\-1&8&-1\\-1&-1&-1\end{pmatrix}$$

- *(Para armar tus propias ventanas de ejemplo, ver 1.8.)*
- Zona constante (todo 10): $8\cdot10-8\cdot10=0$.
- Un píxel de 50 rodeado de 10: $8\cdot50-8\cdot10=320$ (pico: se ve el borde).

**High-boost:** igual, pero con centro un poco mayor (p. ej. 9). Los pesos suman 1, entonces **conserva parte de las bajas frecuencias** y la imagen no pierde su fondo.

#### Otros

- **Laplaciano:** detección de bordes, p. ej. $\begin{pmatrix}0&1&0\\1&-4&1\\0&1&0\end{pmatrix}$ (suma 0).
- **Paso banda:** deja pasar solo un rango de frecuencias (sirve para restaurar imágenes: se elimina la banda del ruido). En la presentación se muestra con distintas **frecuencias de corte** (64, 32, 16, 8) y para restaurar una imagen dañada con **ruido sinusoidal**, que luego se mejora con técnicas de histograma.
- **Homomórfico:** para ruido **multiplicativo** o iluminación desigual. Se pasa a **logaritmos**, porque el producto se vuelve suma y ahí sí se puede filtrar: $\ln f=\ln i+\ln r$ → se filtra → se vuelve con la exponencial. *(Complemento: la iluminación es de baja frecuencia y la reflectancia de alta, por eso se atenúa la primera y se realza la segunda.)* Resultado visto: bordes mejorados y más detalle en zonas oscuras.

### 1.5 Detectar rectas con máscaras direccionales

**La idea.** Se usan cuatro máscaras que suman 0, cada una con **2 sobre la línea que detecta y −1 en el resto**. Si el píxel central está sobre una recta en esa dirección, los pesos 2 multiplican valores altos y la respuesta da grande y positiva. Si la recta va en otra dirección, la respuesta es baja.

| Dirección | Máscara |
|---|---|
| **Horizontal** | $\begin{pmatrix}-1&-1&-1\\2&2&2\\-1&-1&-1\end{pmatrix}$ |
| **Vertical** | $\begin{pmatrix}-1&2&-1\\-1&2&-1\\-1&2&-1\end{pmatrix}$ |
| **45°** (diagonal secundaria, de abajo-izquierda a arriba-derecha) | $\begin{pmatrix}-1&-1&2\\-1&2&-1\\2&-1&-1\end{pmatrix}$ |
| **135°** (diagonal principal, de arriba-izquierda a abajo-derecha) | $\begin{pmatrix}2&-1&-1\\-1&2&-1\\-1&-1&2\end{pmatrix}$ |

**Criterio:** se aplica **cada** máscara a la ventana y gana la de **mayor respuesta**. Dicho en la práctica: el píxel pertenece a una recta de ese ángulo.

> **Ojo con la convención.** Los nombres 45° y 135° dependen de cómo se numeren los ejes. La referencia habitual es que la máscara de 45° tiene los 2 sobre la diagonal **secundaria** y la de 135° sobre la **principal**. Si en clase usaron la inversa, el método es idéntico y solo se intercambian los nombres. Conviene escribir en el parcial qué diagonal es cada una.

**Chequeo de la idea con ventanas limpias:**

- $\begin{pmatrix}1&1&1\\9&9&9\\1&1&1\end{pmatrix}$ (línea horizontal): horizontal **48**; vertical, 45° y 135° dan 0.
- $\begin{pmatrix}2&2&9\\2&9&2\\9&2&2\end{pmatrix}$ (diagonal secundaria): 45° **42**; las otras dan 0.

### 1.6 Compresión por RLE y la variante PCX

**RLE (Run-Length Encoding, codificación por longitud de recorrido):** reemplaza una racha de símbolos iguales por un **contador** y el símbolo. Es ideal donde hay zonas uniformes, como en imágenes.

Ejemplo: `aaabccdddd` → `3abcc4d`.

**RLE de PCX.** PCX guarda cada color como un byte. Para que se pueda distinguir un contador de un dato, usa el límite **192 = 0xC0** (los dos bits más altos en 1):

| Caso | Se escribe |
|---|---|
| Racha de $r$ valores iguales ($2\le r\le 63$) | byte $192+r$ y luego el valor |
| Valor suelto $<192$ | el valor tal cual |
| Valor suelto $\ge192$ | byte de escape `193` (= racha de 1) y luego el valor |
| Racha de más de 63 | se parte en bloques de 63 como máximo |

**Por qué 192 y por qué «los dos primeros bits»** (presentación, formato PCX 3): cuando se repite un color se guardan 2 bytes, un byte de **cantidad** (identificado porque tiene **encendidos los dos primeros bits**, con la cantidad en los **6 bits restantes**) y un byte de **color**.

| Byte | Binario | Interpretación |
|---|---|---|
| 0 a 63 | `00xxxxxx` | color |
| 64 a 127 | `01xxxxxx` | color |
| 128 a 191 | `10xxxxxx` | color |
| **192 a 255** | **`11xxxxxx`** | **contador** (cantidad = los 6 bits `xxxxxx`, de 0 a 63) |

- $192=128+64=$ `11000000` (`0xC0`): el menor byte con los dos primeros bits en 1.
- Con 6 bits la cantidad máxima es $2^6-1=63$; el byte de cuenta más alto es $192+63=255$ (`11111111`).
- **El problema:** los colores 192 a 255 también empiezan con `11`, y al leer el archivo se confundirían con un contador. Por eso un color $\ge192$ va **siempre** precedido de un contador (`193` = `11000001`, cantidad 1), aunque no se repita. Los colores $<192$ no tienen este problema.
- Consecuencia: la compresión puede **empeorar** si hay muchos colores altos sin repetirse.

**Descodificar:** si un byte es $\ge192$, el contador es $\text{byte}-192$ y el siguiente byte es el valor. Si no, es un valor suelto.

> **Sobre la fuente.** La presentación PDI 2026 confirma el esquema de contador (dos primeros bits en 1, cantidad en 6 bits) y señala el problema de los colores altos; el escape `193` es el del formato PCX estándar. Los apuntes de Rubio dan solo la idea general de RLE. En el parcial 2020 esta pregunta quedó sin responder, así que no hay corrección del docente. Si en clase vieron otra notación, el criterio de racha y valor es el mismo.

### 1.7 Histograma (teoría de la unidad; no salió en estos parciales)

El **histograma** cuenta cuántos píxeles hay en cada nivel de gris.

- **Estiramiento:** expande el rango usado al rango completo, aumenta el contraste.
- **Contracción:** lo comprime, baja el contraste.
- **Desplazamiento:** suma o resta un valor constante, aclara u oscurece.
- **Ecualización:** busca un histograma lo más uniforme posible. Cuatro pasos: (1) suma acumulada, (2) dividir por el total de píxeles, (3) multiplicar por el nivel máximo y redondear, (4) mapear cada nivel antiguo al nuevo.

**Ejemplo** (16 píxeles, niveles 0 a 7, $L-1=7$):

| Nivel | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| Cantidad | 2 | 3 | 5 | 3 | 1 | 1 | 1 | 0 |
| Acumulada | 2 | 5 | 10 | 13 | 14 | 15 | 16 | 16 |
| Acum./16 | 0,125 | 0,3125 | 0,625 | 0,8125 | 0,875 | 0,9375 | 1 | 1 |
| ×7 y redondeo | **1** | **2** | **4** | **6** | **6** | **7** | **7** | **7** |

**Fórmulas de la presentación** (sea $I$ el nivel de gris de un píxel; $I_{MAX}$ e $I_{MIN}$ el mayor y menor nivel presentes en la imagen; $MAX$ y $MIN$ los posibles, p. ej. 255 y 0):

- **Stretching:** $\;I'=\dfrac{I-I_{MIN}}{I_{MAX}-I_{MIN}}\,(MAX-MIN)+MIN$ (estira al rango completo; sube el contraste).
- **Shrinking:** $\;I'=\dfrac{Shrink_{MAX}-Shrink_{MIN}}{I_{MAX}-I_{MIN}}\,(I-I_{MIN})+Shrink_{MIN}$ (comprime al rango deseado; baja el contraste; la presentación lo muestra con rango $[75,175]$).
- **Slide (desplazamiento):** $\;I'=I+OFFSET$ (OFFSET positivo aclara, negativo oscurece; conserva la relación entre niveles).

*(Complemento: las ecuaciones de la presentación están como imagen; estas son las expresiones estándar que coinciden con sus definiciones.)*

**Segundo ejemplo de ecualización (el de la presentación).** Histograma de 8 niveles con 10, 8, 9, 2, 14, 1, 5, 2 píxeles (total 51):

| Nivel | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| Acumulada | 10 | 18 | 27 | 29 | 43 | 44 | 49 | 51 |
| ÷ 51 × 7, redondeo | **1** | **2** | **4** | **4** | **6** | **6** | **7** | **7** |

Los niveles 0, 1, 2, 3... pasan a 1, 2, 4, 4... La ecualización da resultados parecidos aunque la imagen de entrada sea clara, oscura o de poco contraste.

### 1.8 Cómo armar tu propia ventana de ejemplo

Hay dos situaciones distintas, y el criterio cambia:

| Situación | De dónde salen los 9 valores |
|---|---|
| El enunciado **trae una imagen** (2012: «dada la siguiente imagen…») | **No los elegís.** La ventana es el píxel que piden (el **centro**) **más sus 8 vecinos**: arriba, abajo, izquierda, derecha y las 4 diagonales. Se copian de la imagen. En una imagen de 3×4 entran dos ventanas: una centrada en cada píxel pedido |
| El enunciado **dice «dé un ejemplo»** (2025: «dé un ejemplo de filtro paso bajo…») | **Los inventás vos.** Los valores no se evalúan. Lo importante es que el ejemplo **muestre el efecto** del filtro |

Para el segundo caso, el criterio es: **elegí una ventana donde se note lo que hace el filtro**. Si todos los valores son iguales, el resultado no cambia y no mostrás nada.

#### Receta: ventana con un pico (sirve para media, mediana y paso alto)

1. **Elegí un fondo:** un nivel de gris que se repita en casi toda la ventana. Por ejemplo, 10.
2. **Metele un pico al centro:** un valor claramente distinto al fondo, que haga de «ruido» o de detalle. Por ejemplo, 82.
3. **Escribí la ventana:** los 8 vecinos valen el fondo y el centro vale el pico.

$$\begin{pmatrix}10&10&10\\10&82&10\\10&10&10\end{pmatrix}$$

4. **Aplicá el filtro** y comprobá que el resultado muestra el efecto.

**Trucos:**

- **Suma fácil de dividir por 9.** En el ejemplo, $8\cdot10+82=162$ y $162/9=18$, entero y sin redondeo. Elegí el pico de modo que la suma total sea múltiplo de 9.
- **Un solo pico alcanza.** Si querés que parezca más real, cambiale uno o dos vecinos unos puntos.

#### Receta: ventana con un escalón (para mostrar bordes)

Un escalón es un salto brusco entre dos zonas lisas, o sea un **borde**:

$$\begin{pmatrix}10&10&80\\10&10&80\\10&10&80\end{pmatrix}$$

Dos columnas de fondo (10) y una columna de otro nivel (80). El centro queda justo al lado del salto.

#### Qué ventana usar para cada filtro

| Querés mostrar… | Ventana | Cuenta | Resultado | Qué se ve |
|---|---|---|---|---|
| **Media: reduce ruido** | pico (fondo 10, centro 82) | $(8\cdot10+82)/9=162/9$ | **18** | El pico se acerca a su entorno |
| **Media: emborrona bordes** | escalón (10 y 80) | $(6\cdot10+3\cdot80)/9=300/9$ | **33** | El salto 10→80 queda en un valor intermedio, más suave |
| **Mediana** | pico extremo, p. ej. $\begin{pmatrix}10&200&12\\11&13&9\\14&12&10\end{pmatrix}$ | ordenar: $9,10,10,11,12,12,13,14,200$ | **12** | El 200 se ignora por completo |
| **Paso alto: zona lisa** | todo 10 | $8\cdot10-8\cdot10$ | **0** | Sin detalle, sin respuesta |
| **Paso alto: pico** | pico (fondo 10, centro 82) | $8\cdot82-8\cdot10=656-80$ | **576** | El detalle aislado se realza mucho |
| **Paso alto: borde** | escalón, centro del lado de los 10 | $8\cdot10-(10+10+80+10+80+10+10+80)=80-290$ | **−210** | Responde sobre el borde; con el centro del lado de los 80 da $+210$ |
| **Recta horizontal** | $\begin{pmatrix}1&1&1\\9&9&9\\1&1&1\end{pmatrix}$ | máscara horizontal | **48** | Las otras tres máscaras dan 0 |
| **Recta a 45°** | $\begin{pmatrix}2&2&9\\2&9&2\\9&2&2\end{pmatrix}$ | máscara de 45° | **42** | Las otras tres máscaras dan 0 |

> **En el paso alto, el signo importa poco.** El negativo indica de qué lado del borde está el píxel. En la práctica se suele tomar el valor absoluto o recortar a 0.

**RLE:** ahí no hay ventana, el dato es una secuencia. Para inventar un ejemplo, armá una secuencia con **una racha** (varios valores iguales), **un valor suelto menor a 192** y **un valor suelto mayor o igual a 192**, para que aparezcan los tres casos de la tabla de 1.6. Ej.: `10,10,10,200,7`.

### 1.9 Detección de discontinuidades: puntos, rectas y bordes (presentación)

La presentación agrupa tres detecciones, todas con máscaras:

- **Puntos:** una máscara con centro positivo y periferia negativa (la del paso alto, $8$ en el centro y $-1$ alrededor); un punto aislado da respuesta grande.
- **Rectas:** las cuatro máscaras de 1.5 (horizontal, 45°, vertical, 135°).
- **Bordes con operadores de gradiente:** se calculan dos derivadas ($G_x$ y $G_y$) y se combina $|G|\approx|G_x|+|G_y|$. Los operadores que aparecen son **Roberts**, **Sobel**, **Prewitt** y **Laplaciano**.

| Operador | $G_x$ | $G_y$ |
|---|---|---|
| **Roberts** (2×2) | $\begin{pmatrix}-1&0\\0&1\end{pmatrix}$ | $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ |
| **Prewitt** | $\begin{pmatrix}-1&0&1\\-1&0&1\\-1&0&1\end{pmatrix}$ | $\begin{pmatrix}-1&-1&-1\\0&0&0\\1&1&1\end{pmatrix}$ |
| **Sobel** | $\begin{pmatrix}-1&0&1\\-2&0&2\\-1&0&1\end{pmatrix}$ | $\begin{pmatrix}-1&-2&-1\\0&0&0\\1&2&1\end{pmatrix}$ |
| **Laplaciano** | $\begin{pmatrix}0&1&0\\1&-4&1\\0&1&0\end{pmatrix}$ (una sola máscara, segunda derivada) | |

*(Complemento: en la presentación las máscaras están como imagen; estas son las estándar. Sobel pesa más la fila/columna central, así que suaviza un poco el ruido. Es teoría de la unidad que no salió en parciales.)*

### 1.10 Compresión JPEG (presentación)

JPEG es una compresión **con pérdida** que reduce la **redundancia espacial** (píxeles vecinos parecidos, como el cielo). Es un codificador por **transformación** (transform coding): usa la **DCT** para pasar al dominio de frecuencias. Pasos:

1. **Conversión RGB → $YC_bC_r$:** separa la luminancia $Y$ de las dos crominancias ($C_b$ = diferencia del azul, $C_r$ = diferencia del rojo).
2. **Submuestreo:** se reduce la resolución de la crominancia, porque el ojo es más sensible al brillo (bastones, 75 a 150 millones) que al color (conos, 6 a 7 millones). Lo que sigue se aplica por **bloques de 8×8**, a luminancia y a crominancias.
3. **DCT:** concentra la mayor parte de la información en pocos coeficientes. *(Aclaración: la esquina superior izquierda es el coeficiente continuo DC, de frecuencia cero y mayor valor; hacia la derecha y abajo suben las frecuencias, con valores decrecientes y muchos ceros.)*
4. **Cuantización:** cada coeficiente se **divide** por un entero (tabla de cuantización, una para luminancia y otra para crominancia) y se **trunca**. **Es el paso donde se pierde información**; deja más ceros.
5. **Recorrido en zig-zag** hasta el último elemento no nulo, y **RLE de las corridas de ceros** entre coeficientes no nulos (termina con `EOB`).
6. **Huffman** sobre los símbolos del RLE, con tablas fijas según la probabilidad de cada corrida.

Ejemplo de la presentación (bloque ya recorrido en zig-zag): `150,7,8,1,5,2,2,4,2,1,0,1,2,2,0,0,0,1,0,0,0,0,0,0,1,EOB`.

---

## 2. Ejercicios de parcial resueltos

### Ejercicio 1: Filtro paso bajo (Parcial 17/11/2025, Tema 1, Ej. 6)

> **Enunciado:** Dé un ejemplo de filtro paso bajo, e indique qué efectos produce sobre una imagen.

**Qué necesitás:** 1.4 (paso bajo).

**Resolución:**

- **Filtro:** la **media** 3×3. Cada píxel se reemplaza por el promedio de su ventana, con la máscara $\frac19\begin{pmatrix}1&1&1\\1&1&1\\1&1&1\end{pmatrix}$.
- **Ejemplo numérico.** El enunciado **no trae imagen**, así que la ventana la inventás vos (criterio y recetas en 1.8: se busca que el centro se destaque de sus vecinos, para que se note el efecto). Con la ventana $\begin{pmatrix}12&8&15\\6&22&10\\18&14&9\end{pmatrix}$: suma $12+8+15+6+22+10+18+14+9=114$, y $114/9=12{,}67\approx13$. El centro 22 pasa a 13. Armada desde cero con la receta del pico (fondo 10, centro 82): $(8\cdot10+82)/9=18$.
- **Efectos:** reduce el ruido y suaviza la imagen (atenúa las altas frecuencias), pero **emborrona los bordes y detalles**. Cuanto más grande la ventana, más ruido se elimina y más desenfoque aparece.
- **Alternativa válida:** la **mediana** (no lineal). Con la ventana $\begin{pmatrix}3&18&73\\1&7&20\\9&25&14\end{pmatrix}$, el centro 7 pasa a 14 y el pico 73 desaparece. Es la más eficaz contra ruido «sal y pimienta».

**Errores comunes:**

- Decir que un paso bajo «afila» o «realza bordes»: eso es paso alto.
- Olvidar nombrar el efecto secundario (el emborronado). Es lo que el docente quiere ver.
- Dar un ejemplo sin definirlo. Conviene escribir la máscara o el procedimiento.
- Elegir una ventana con todos los valores iguales: el filtro no cambia nada y no se ve el efecto.

*En la resolución de alumna de la transcripción se respondió «filtro de mediana, reduce el ruido»: es correcto, pero conviene completar con la matriz, un ejemplo numérico y el efecto sobre los bordes.*

---

### Ejercicio 1b (variante, no salió todavía): Filtro paso alto

> **Enunciado (variante propia del 2025):** Dé un ejemplo de filtro paso alto, e indique qué efectos produce sobre una imagen.

**Qué necesitás:** 1.4 (paso alto) y 1.8 (cómo armar la ventana).

**Resolución:**

- **Filtro:** paso alto con la máscara $\begin{pmatrix}-1&-1&-1\\-1&8&-1\\-1&-1&-1\end{pmatrix}$. Los pesos suman 0, así que **no se divide**. Se calcula $8\cdot\text{centro}-\text{suma de los 8 vecinos}$.
- **Ejemplos** (ventanas armadas con las recetas de 1.8):
  - Zona lisa, todo 10: $8\cdot10-8\cdot10=\mathbf{0}$.
  - Pico, $\begin{pmatrix}10&10&10\\10&82&10\\10&10&10\end{pmatrix}$: $8\cdot82-8\cdot10=656-80=\mathbf{576}$.
  - Borde, $\begin{pmatrix}10&10&80\\10&10&80\\10&10&80\end{pmatrix}$: $8\cdot10-290=\mathbf{-210}$ (con el centro del lado de los 80 daría $+210$).
- **Efectos:** realza las altas frecuencias, o sea **bordes y detalles finos**. En zonas lisas la respuesta es 0 y sobre un borde o un punto aislado da valores grandes. La imagen se ve más **afilada** y con los contornos marcados, pero **también se realza el ruido**.
- **High-boost:** con el centro en 9 los pesos suman 1, y se conserva parte de la imagen original (bajas frecuencias).

**Errores comunes:**

- Decir que reduce el ruido: es lo contrario, lo realza.
- Dividir por la suma de pesos: acá la suma es 0 y no se divide.
- Interpretar un resultado negativo como un error: indica de qué lado del borde está el píxel.

---

### Ejercicio 2: Vectorial vs. bitmap y RLE de PCX (Parcial 15/12/2020, Ej. 4)

> **Enunciado:** **a)** ¿Cuál es la diferencia entre una imagen vectorial y una bitmapeada? **b)** Dada la secuencia de valores de color de una imagen `129, 129, 129, 129, 129, 194`, codificarla usando la codificación RLE de PCX.

**Qué necesitás:** 1.1 y 1.6.

**a)** La imagen **vectorial** se describe con figuras matemáticas (puntos, rectas, curvas, rellenos): escala sin perder calidad y ocupa poco. La **bitmap** es una matriz de píxeles: ocupa más, depende de la resolución y se pixela al ampliarla.

**b) Paso a paso:**

1. Separá en rachas: cinco `129` y un `194`.
2. Racha de 5 valores 129 (es una racha, $r=5$): byte $192+5=197$, luego el valor `129`. Sale `197, 129`.
3. El `194` aparece una sola vez. Como $194\ge192$, **no puede ir pelado**, porque se confundiría con un contador. Se escribe con el escape `193` delante. Sale `193, 194`.
4. Juntás todo.

**Resultado: `197, 129, 193, 194`** (en hexadecimal `C5 81 C1 C2`).

**Chequeo descodificando:** `197` es $\ge192$, entonces $197-192=5$ repeticiones del siguiente byte (129). Después `193` es $\ge192$, entonces $193-192=1$ repetición del siguiente byte (194). Recuperás `129,129,129,129,129,194`. ✓

**Errores comunes:**

- Escribir el `194` solo, sin escape.
- Poner un escape también al 129 si fuera suelto: es $<192$, no lo necesita.
- Confundir la cuenta: el byte de cuenta es $192+r$, no $r$.

**Nota:** en el escaneo del parcial esta pregunta quedó sin resolver (el docente puso «FALTA IMÁGENES 0/1,5»). La resolución de arriba es la del esquema PCX estándar.

---

### Ejercicio 3: Máscaras de rectas (Parcial 21/11/2012, Tema 1)

> **Enunciado:** Dada la siguiente imagen, utilizando las máscaras pertinentes, determinar a qué tipo de recta pertenece el punto central (horizontal, vertical, a 45°, a 135°):
>
> $\begin{pmatrix}19&3&21\\4&19&11\\16&16&19\end{pmatrix}$

**Qué necesitás:** 1.3 (receta de máscara) y 1.5.

**Resolución:** se aplica cada máscara y se suman los 9 productos.

**Horizontal** $\begin{pmatrix}-1&-1&-1\\2&2&2\\-1&-1&-1\end{pmatrix}$:

$$-(19+3+21)+2(4+19+11)-(16+16+19)=-43+68-51=-26$$

**Vertical** $\begin{pmatrix}-1&2&-1\\-1&2&-1\\-1&2&-1\end{pmatrix}$:

$$-(19+4+16)+2(3+19+16)-(21+11+19)=-39+76-51=-14$$

**45°** $\begin{pmatrix}-1&-1&2\\-1&2&-1\\2&-1&-1\end{pmatrix}$ (2 en la diagonal secundaria: $21,19,16$):

$$2(21+19+16)-(19+3+4+11+16+19)=112-72=40$$

**135°** $\begin{pmatrix}2&-1&-1\\-1&2&-1\\-1&-1&2\end{pmatrix}$ (2 en la diagonal principal: $19,19,19$):

$$2(19+19+19)-(3+21+4+11+16+16)=114-71=43$$

| Máscara | Horizontal | Vertical | 45° | **135°** |
|---|---|---|---|---|
| Respuesta | −26 | −14 | 40 | **43** |

**Respuesta:** la mayor respuesta es la de 135° → el punto central pertenece a una **recta a 135°**.

**Cómo se ve a ojo:** la diagonal principal es $19,19,19$, tres valores iguales y altos, mientras que la secundaria es $21,19,16$. Coincide con el resultado.

**Cosas a aclarar en el examen:**

- La diferencia entre 135° (43) y 45° (40) es chica. Mostrá las cuentas para que se vea que no es un error.
- Aclará tu convención de ángulos (qué diagonal es cada una).
- Horizontal y vertical dan negativo: la recta no está en esas direcciones.

**Errores comunes:**

- Olvidar un signo (por eso conviene separar «pesos 2» de «pesos −1» como arriba).
- Tomar la respuesta con signo en vez de la de mayor valor.
- No aplicar las cuatro máscaras: hay que probarlas todas.

---

### Ejercicio 4: Media aritmética (Parcial 21/11/2012, Tema 2)

> **Enunciado:** Dada la siguiente imagen, utilizando la máscara pertinente, suavizar el punto central (de las dos ventanas), utilizando una máscara de media aritmética:
>
> $\begin{pmatrix}160&161&163&180\\200&11&21&190\\199&161&165&191\end{pmatrix}$

**Qué necesitás:** 1.3 (receta) y 1.4 (media).

**Resolución:** la imagen es de 3×4, así que entran **dos ventanas 3×3**: la de las columnas 1 a 3 (centro 11) y la de las columnas 2 a 4 (centro 21). La máscara es $\frac19$ en todas las posiciones.

**Ventana 1** (columnas 1 a 3, centro **11**): $\begin{pmatrix}160&161&163\\200&11&21\\199&161&165\end{pmatrix}$

$$160+161+163+200+11+21+199+161+165=1241\;\rightarrow\;\frac{1241}{9}=137{,}9\approx\mathbf{138}$$

**Ventana 2** (columnas 2 a 4, centro **21**): $\begin{pmatrix}161&163&180\\11&21&190\\161&165&191\end{pmatrix}$

$$161+163+180+11+21+190+161+165+191=1243\;\rightarrow\;\frac{1243}{9}=138{,}1\approx\mathbf{138}$$

**Respuesta:** los dos centros pasan a **138**.

**Interpretación:** el 11 y el 21 eran valores muy bajos rodeados de valores cercanos a 160 o 200 (parecen ruido). La media los acerca a su entorno, que es justamente suavizar.

**Errores comunes:**

- Tomar una sola ventana: el enunciado dice «las dos ventanas».
- Olvidar dividir por 9.
- Armar mal la segunda ventana (hay que correrla una columna, no repetir la primera).

---

## 3. Ejercicios de práctica extra (para entrenar)

**3.1 Mediana.** Calculá el centro filtrado con la mediana en la ventana $\begin{pmatrix}10&200&12\\11&13&9\\14&12&10\end{pmatrix}$.
*Resolución:* ordenados $9,10,10,11,12,12,13,14,200$ → el quinto es **12**. El centro 13 pasa a 12. El 200 se ignora.

**3.2 Paso alto.** Aplicá $\begin{pmatrix}-1&-1&-1\\-1&8&-1\\-1&-1&-1\end{pmatrix}$ a $\begin{pmatrix}10&10&10\\10&50&10\\10&10&10\end{pmatrix}$.
*Resolución:* $8\cdot50-8\cdot10=320$. Un pico claro: el 50 es un detalle aislado.

**3.3 Recta.** ¿Qué recta es $\begin{pmatrix}2&2&9\\2&9&2\\9&2&2\end{pmatrix}$?
*Resolución:* horizontal 0, vertical 0, 135° 0, **45° 42**. Es una recta a 45° (diagonal secundaria), con la convención de este apunte.

**3.4 RLE de PCX (codificar).** `10,10,10,200,7,7`.
*Resolución:* tres 10 → $192+3=195,10$; el 200 suelto es $\ge192$ → `193,200`; dos 7 → $192+2=194,7$. **`195,10,193,200,194,7`**.

**3.5 RLE de PCX (descodificar).** `196,5,193,230,200,1`.
*Resolución:* $196-192=4$ veces el 5; `193,230` es el 230 suelto; $200-192=8$ veces el 1. Resultado: `5,5,5,5,230,1,1,1,1,1,1,1,1` (13 valores).

**3.6 Un caso donde el RLE agranda.** `255`.
*Resolución:* es $\ge192$ y suelto → `193,255`: pasan a ser 2 bytes en lugar de 1. Cuando hay pocas rachas, el RLE puede expandir.

**3.7 Setenta ceros.**
*Resolución:* el máximo por bloque es 63 → $192+63=255$, luego el valor `0`, y quedan 7 → `199,0`. **`255,0,199,0`**.

**3.8 Bits del contador.** El byte `11001010`, ¿qué es y qué dice?
*Resolución:* empieza con `11`, es un contador. Cantidad = `001010` = 10 (o $202-192=10$). El byte siguiente es el color que se repite 10 veces.

**3.9 ¿Es contador o color?** Clasificá `100`, `191`, `192`, `255`.
*Resolución:* `100` ($01100100$) color; `191` ($10111111$) color; `192` ($11000000$) contador de 0 (no se usa); `255` ($11111111$) contador de 63.

**3.10 Codificar con binario.** `64,64,64` y luego `250`.
*Resolución:* tres 64 → $192+3=195$ (`11000011`), `64`; el 250 es $\ge192$ → `193,250`. Resultado: `195,64,193,250`.

**3.11 Paso bajo vs. paso alto.** Una imagen con mucho ruido granulado, ¿qué filtro aplicás y qué esperás? ¿Y si querés marcar contornos?
*Resolución:* ruido → paso bajo (media, gaussiano o, mejor para «sal y pimienta», mediana): baja el ruido pero emborrona bordes. Contornos → paso alto (suma de pesos 0): realza bordes, pero también el ruido.

---

## 4. Resumen de último momento

| Si te piden… | Hacé esto |
|---|---|
| Un filtro paso bajo y sus efectos | Media (1/9) o mediana; efecto: **reduce ruido, emborrona bordes** |
| Aplicar una máscara 3×3 | Multiplicar posición a posición, sumar; **dividir por la suma de pesos si no suma 0**; redondear |
| Suavizar con media aritmética | Sumar los 9 valores y dividir por 9 (una ventana por cada punto pedido) |
| ¿A qué recta pertenece el punto? | Aplicar las 4 máscaras, **gana la de mayor respuesta** (aclarar la convención de 45° y 135°) |
| Mediana | Ordenar los 9 y tomar el 5.º |
| Vectorial vs. bitmap | Figuras matemáticas (escala sin pérdida) vs. matriz de píxeles (se pixela) |
| RLE de PCX | Racha: $192+r$ y valor. Suelto $<192$: tal cual. Suelto $\ge192$: `193` y valor. Máximo 63 por bloque |
| «¿Por qué 192 / los dos primeros bits?» | Contador = `11xxxxxx` ($128+64=192$), cantidad en 6 bits (máx. 63). Colores $\ge192$ también empiezan con `11` → ambigüedad → escape `193` |
| Paso alto vs. paso bajo | Bajo: coef. positivos, suaviza/emborrona. Alto: centro $+$, periferia $-$, suma 0, realza bordes (y ruido) |
| Histograma | Stretching/shrinking/slide; ecualización en 4 pasos (ejemplos en 1.7) |
| JPEG | $YC_bC_r$ → submuestreo → bloques 8×8 → DCT → cuantización (pérdida) → zig-zag → RLE + Huffman |
| Bordes (Roberts, Sobel, Prewitt, Laplaciano) | Gradiente $G_x$, $G_y$; Laplaciano una máscara (1.9) |
| Paso alto / high-boost | Centro positivo, periferia negativa, suma 0 (high-boost: suma 1) |

**Antes de entregar:** revisá los signos de las máscaras, las divisiones por 9 y que hayas probado **todas** las máscaras o ventanas que pide el enunciado.
