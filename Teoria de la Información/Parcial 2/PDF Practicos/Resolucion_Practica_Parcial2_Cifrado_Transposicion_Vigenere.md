# Práctica Parcial 2 — Criptografía: CIFRAR (Transposición + Vigenère)

Mismo estilo que el ejercicio del parcial, pero en sentido de **cifrado**. Alfabeto de 27 letras (`n = 27`, A=0 … Z=26, Ñ=14), espacios no se cifran.

## Enunciado

> Dado el siguiente mensaje **ME VOY A MADRID**, cifrarlo utilizando una transposición de una matriz de 3x4, en la que se pusieron las letras por fila y se leen por columna según el siguiente orden (3,1,4,2); el resultado se cifra utilizando la técnica de Vigenère con clave SALTA.
>
> B) Los métodos antes vistos, ¿modifican la entropía de orden cero?
>
> C) En la fuente en claro, y en cada paso de cifrado, calcule la entropía de orden cero para comprobar lo manifestado por usted en el punto anterior.

## Planteo

Orden de cifrado: **mensaje → transposición → Vigenère → criptograma**.

## Paso 1 — Transposición (matriz 3x4)

Mensaje sin espacios: `MEVOYAMADRID` (12 letras = 3x4, no hace falta relleno). Se llena **por fila**:

| | c1 | c2 | c3 | c4 |
|---|---|---|---|---|
| f1 | M | E | V | O |
| f2 | Y | A | M | A |
| f3 | D | R | I | D |

Clave `(3,1,4,2)`: la columna 1 se lee 3.ª, la columna 2 se lee 1.ª, la columna 3 se lee 4.ª y la columna 4 se lee 2.ª. Orden de lectura: **col 2, col 4, col 1, col 3**.

| Lectura | Columna | Letras |
|---|---|---|
| 1.º | c2 | E A R |
| 2.º | c4 | O A D |
| 3.º | c1 | M Y D |
| 4.º | c3 | V M I |

Resultado intermedio: **`EAROADMYDVMI`**

## Paso 2 — Vigenère (clave SALTA)

`C_i = (M_i + K_{i mod 5}) mod 27`, con `SALTA = (19, 0, 11, 20, 0)` (la clave tiene 5 letras y se repite).

| i | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Texto | E | A | R | O | A | D | M | Y | D | V | M | I |
| `m` | 4 | 0 | 18 | 15 | 0 | 3 | 12 | 25 | 3 | 22 | 12 | 8 |
| Clave | S | A | L | T | A | S | A | L | T | A | S | A |
| `k` | 19 | 0 | 11 | 20 | 0 | 19 | 0 | 11 | 20 | 0 | 19 | 0 |
| `m + k` | 23 | 0 | 29 | 35 | 0 | 22 | 12 | 36 | 23 | 22 | 31 | 8 |
| `mod 27` | 23 | 0 | **2** | **8** | 0 | 22 | 12 | **9** | 23 | 22 | **4** | 8 |
| `c` | W | A | C | I | A | V | M | J | W | V | E | I |

**Criptograma: `WACIAVMJWVEI`** → `WACI AVMJ WVEI`

Verificación: descifrando con `M = (C − K) mod 27` y deshaciendo la transposición se vuelve a `MEVOYAMADRID`.

---

## B) ¿Modifican la entropía de orden cero?

`H₀ = −Σ pᵢ·log₂ pᵢ` depende solo de las **frecuencias** de los símbolos.

- **Transposición: NO.** Solo reordena; los símbolos y sus frecuencias son los mismos.
- **Vigenère: SÍ puede.** Es polialfabético: una misma letra se cifra distinto según su posición (`i mod 5`) y letras distintas pueden coincidir en el mismo símbolo cifrado, así que cambian las frecuencias. No siempre aplana: depende del mensaje y de la clave (acá la baja, ver C). Un monoalfabético (César, afín) sí la conservaría.

## C) Cálculo de `H₀` en cada etapa (N = 12)

**Mensaje en claro `MEVOYAMADRID`:** M, A, D ×2 (`p = 2/12`); E, V, O, Y, R, I ×1 (`p = 1/12`).

`H₀ = 3·(2/12)·log₂ 6 + 6·(1/12)·log₂ 12 = 0,5·2,585 + 0,5·3,585 = 3,085 bits`

**Tras transposición `EAROADMYDVMI`:** A, D, M ×2; E, R, O, Y, V, I ×1. Mismas frecuencias.

`H₀ = 3,085 bits`

**Criptograma `WACIAVMJWVEI`:** W, A, I, V ×2 (`p = 2/12`); C, M, J, E ×1 (`p = 1/12`).

`H₀ = 4·(2/12)·log₂ 6 + 4·(1/12)·log₂ 12 = 0,667·2,585 + 0,333·3,585 = 2,918 bits`

| Etapa | Texto | `H₀` (bits/símbolo) |
|---|---|---|
| Mensaje en claro | MEVOYAMADRID | 3,085 |
| Después de transposición | EAROADMYDVMI | 3,085 |
| Después de Vigenère | WACIAVMJWVEI | 2,918 |

**Conclusión (comprueba B):** la transposición deja `H₀` igual (3,085 → 3,085); Vigenère la modifica (3,085 → 2,918). Que en este caso haya bajado, y no subido, es esperable con un mensaje corto: depende de qué letras coinciden tras sumar la clave (por ejemplo, `E+S` y `D+T` dan ambas `W`, y `D+S` y `V+A` dan ambas `V`: letras distintas del claro colapsan en el mismo símbolo cifrado). Lo que importa para el parcial es la idea: **transposición no cambia `H₀`, sustitución polialfabética sí puede**.
