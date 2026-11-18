# RLE de PCX: cómo funciona y por qué el límite 192

## Idea general

Una imagen tiene tramos largos de píxeles idénticos (fondo blanco, cielo liso).
RLE (Run-Length Encoding) reemplaza una repetición por un par **(cantidad, valor)**:

```
5 5 5 5 5 5 5 5 5 5   → 10 bytes
11001010 00000101     → 2 bytes: "10 veces el 5"
```

Es **compresión sin pérdida**: se aprovecha que los datos se repiten.

## ¿Por qué "se repite"?

Los bits no hacen nada por sí solos: es una **convención del formato**. Escritor y
lector acuerdan una regla, y el decodificador la aplica:

> Si un byte empieza con `11`, no es un dato sino una instrucción:
> repetir N veces el byte que viene después.

Con otra regla, los mismos bits significarían otra cosa.

## La regla de PCX (los 2 bits altos deciden todo)

```
11 cccccc   → CONTADOR  (cccccc = 6 bits = 0..63 repeticiones; el SIGUIENTE byte es el dato)
00/01/10 …  → DATO literal (valores 0..191)
```

- `192 = 11000000`: primer valor con los dos bits altos en 1.
- Todo byte ≥ 192 tiene el flag `11`; todo byte < 192 no.
- El contador son los 6 bits restantes leídos como binario normal:
  `11000011` → `000011` = 3 → repetir 3 veces.
- Byte contador = **192 + cantidad**. Máximo: `11111111` = 192 + 63 = 255 → 63 veces.

## Casos sueltos (un solo byte)

| Valor | En bits | Dos bits altos | Qué es | Se escribe |
|---|---|---|---|---|
| 5 | `00`000101 | 00 | dato | `00000101` |
| 150 | `10`010110 | 10 | dato | `10010110` |
| 191 | `10`111111 | 10 | dato (el mayor sin prefijo) | `10111111` |
| 200 | `11`001000 | **11** | parecería contador | `11000001` `11001000` (prefijo "×1" + dato) |

Por eso un dato suelto ≥ 192 se escribe con el prefijo `193` (`11000001` = repetir 1 vez)
delante: sin él, el decodificador lo confundiría con un contador. Esto hace que RLE
**pueda agrandar** el archivo cuando no hay repeticiones.

## Casos con repetición (contador + dato)

**El 5 repetido 3 veces**
```
11 000011   00000101
flag   3    dato = 5
```

**El 200 repetido 4 veces**
```
11 000100   11001000
flag   4    dato = 200
```
El dato 200 empieza con `11`, pero viene *después* de un contador, así que se lee como dato.

## Más de 63 repeticiones: se encadenan pares

No se "construye un número" con varios bloques: cada par `(contador, dato)` es
independiente y el decodificador los escribe uno tras otro.

El 5 repetido 70 veces = 63 + 7:
```
11 111111 00000101    11 000111 00000101
  (63 veces el 5)       (7 veces el 5)
```

El 5 repetido 200 veces = 63 + 63 + 63 + 11:
```
255,5   255,5   255,5   203,5      → 8 bytes en vez de 200
```

## Decodificar un flujo completo

```
11000011 00000101 00000111 11000001 11001000
```

1. `11000011` → empieza con 11 → contador = 3.
2. `00000101` → dato 5 → escribo **5 5 5**.
3. `00000111` → empieza con 00 → dato literal **7**.
4. `11000001` → contador = 1.
5. `11001000` → dato 200 → escribo **200**.

Resultado: `5 5 5 7 200`.

El byte `11001000` es contador o dato **según su posición** en el flujo.

## Respuesta corta para el parcial

> En RLE de PCX cada byte se interpreta según sus dos bits más altos. Si son `11`
> (valor ≥ 192), el byte es un **contador**: los 6 bits restantes indican cuántas veces
> (1 a 63) se repite el byte siguiente. Si no son `11` (valor < 192), es un dato literal.
> Por eso un dato suelto ≥ 192 se escribe como `193, dato`, para no confundirlo con un
> contador; esto puede agrandar el archivo. Y como el contador tiene solo 6 bits, una
> repetición mayor a 63 se parte en varios pares `(contador, dato)` consecutivos.
