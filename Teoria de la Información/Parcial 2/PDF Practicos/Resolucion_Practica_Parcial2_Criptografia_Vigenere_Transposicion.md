# Resolución — Práctica Parcial 2: Criptografía (Vigenère + Transposición)

Mismas convenciones que `Resolucion_Practico_Criptografia_2026.md`: alfabeto de **27 letras** (`n = 27`, A=0 … Z=26, con Ñ=14), espacios no se cifran.

> Dado el siguiente criptograma GAUQ YBXM OÑSK, descifrarlo, sabiendo que fue cifrado utilizando una transposición de una matriz de 3x4, en la que se pusieron las letras por fila y se leyeron por columna según el siguiente orden (4,1,3,2); el resultado fue cifrado utilizando la técnica de Vigenère con clave CANCUN.

## Planteo

El cifrado se hizo en este orden: **mensaje → transposición → Vigenère → criptograma**.
Para descifrar se invierte el orden: **primero Vigenère inverso, después transposición inversa**.

## Paso 1 — Descifrar Vigenère (clave CANCUN)

`M_i = (C_i − K_{i mod 6}) mod 27`, con `CANCUN = (2, 0, 13, 2, 21, 13)`.

| i | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cripto | G | A | U | Q | Y | B | X | M | O | Ñ | S | K |
| `c` | 6 | 0 | 21 | 17 | 25 | 1 | 24 | 12 | 15 | 14 | 19 | 10 |
| Clave | C | A | N | C | U | N | C | A | N | C | U | N |
| `k` | 2 | 0 | 13 | 2 | 21 | 13 | 2 | 0 | 13 | 2 | 21 | 13 |
| `c − k` | 4 | 0 | 8 | 15 | 4 | −12 | 22 | 12 | 2 | 12 | −2 | −3 |
| `mod 27` | 4 | 0 | 8 | 15 | 4 | **15** | 22 | 12 | 2 | 12 | **25** | **24** |
| `m` | E | A | I | O | E | O | V | M | C | M | Y | X |

Resultado intermedio (salida de la transposición): **`EAIOEOVMCMYX`**

## Paso 2 — Deshacer la transposición (matriz 3x4)

La clave `(4,1,3,2)` indica, para cada columna, **en qué turno se lee**:

| Columna | c1 | c2 | c3 | c4 |
|---|---|---|---|---|
| Turno de lectura (clave) | 4 | 1 | 3 | 2 |

Para obtener el orden de lectura se recorren los turnos 1, 2, 3, 4 y se busca a qué columna le tocó cada uno (es decir, en qué posición de la clave está ese número):

- turno **1** → está en la posición 2 → **col 2**
- turno **2** → está en la posición 4 → **col 4**
- turno **3** → está en la posición 3 → **col 3**
- turno **4** → está en la posición 1 → **col 1**

Entonces el orden de lectura fue **col 2, col 4, col 3, col 1**. Cada columna tiene 3 letras, así que se parte `EAIOEOVMCMYX` en 4 bloques de 3 y cada uno vuelve a su columna:

| Bloque (lectura) | Letras | Columna de la matriz |
|---|---|---|
| 1.º | E A I | 2 |
| 2.º | O E O | 4 |
| 3.º | V M C | 3 |
| 4.º | M Y X | 1 |

Matriz reconstruida (se llena por columna, se lee por fila):

| | c1 | c2 | c3 | c4 |
|---|---|---|---|---|
| f1 | M | E | V | O |
| f2 | Y | A | M | E |
| f3 | X | I | C | O |

Leyendo por filas: `MEVO YAME XICO`

**Texto en claro: `MEVOYAMEXICO` → «ME VOY A MEXICO»** (la clave CANCUN ya lo anticipaba 😉)

---

## B) ¿Estos métodos modifican la entropía de orden cero?

La entropía de orden cero es `H₀ = −Σ pᵢ·log₂ pᵢ`, depende **solo de las frecuencias de los símbolos**, no de su posición.

- **Transposición: NO la modifica.** Solo permuta posiciones; los símbolos y sus frecuencias son los mismos. (Por eso la transposición no resiste el análisis de frecuencias: da difusión pero no confusión.)
- **Vigenère: SÍ puede modificarla.** Es polialfabético: la misma letra del mensaje se cifra distinto según la posición (`i mod 6`), y letras distintas pueden caer en la misma. Cambian las frecuencias, y por eso tiende a **aplanar** la distribución (sube `H₀` hacia el máximo `log₂ 27 ≈ 4,755`). Un monoalfabético (César, afín) sí la conservaría, porque es una biyección fija de símbolos.

## C) Cálculo de `H₀` en cada etapa (N = 12 símbolos)

**Fuente cifrada `GAUQYBXMOÑSK`:** 12 letras distintas, cada una con `p = 1/12`.

`H₀ = log₂ 12 = 3,585 bits`

**Tras Vigenère inverso `EAIOEOVMCMYX`:** E, O, M aparecen 2 veces (`p = 2/12`); A, I, V, C, Y, X una vez (`p = 1/12`).

`H₀ = 3·(2/12)·log₂(12/2) + 6·(1/12)·log₂ 12 = 0,5·2,585 + 0,5·3,585 = 3,085 bits`

**Tras transposición inversa `MEVOYAMEXICO`:** mismas letras con las mismas frecuencias (M, E, O ×2; V, Y, A, X, I, C ×1).

`H₀ = 3,085 bits`

| Etapa | Texto | `H₀` (bits/símbolo) |
|---|---|---|
| Criptograma | GAUQYBXMOÑSK | 3,585 |
| Después de Vigenère⁻¹ | EAIOEOVMCMYX | 3,085 |
| Después de transposición⁻¹ | MEVOYAMEXICO | 3,085 |

**Conclusión (comprueba B):** el paso de transposición deja `H₀` **igual** (3,085 → 3,085); el paso de Vigenère la **cambia** (3,585 ↔ 3,085). En el criptograma cada letra aparece una sola vez (distribución uniforme sobre 12 símbolos, el máximo posible para N = 12), mientras que el texto en claro repite letras, como cualquier lenguaje natural.
