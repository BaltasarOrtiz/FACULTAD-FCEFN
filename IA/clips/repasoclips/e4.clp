; Ejercicio 1: Lista de Compras
; Objetivo: Crear un sistema que registre productos de una lista de compras y calcule el total.
; Requisitos:
;   Crear un template para productos con nombre, precio y cantidad
;   Crear reglas para:

; Calcular el costo de cada producto (precio × cantidad)
;   Sumar el total de toda la lista
;   Identificar el producto más caro

; Datos de prueba:
;   Leche: $2.50, 2 unidades
;   Pan: $1.75, 3 unidades
;   Huevos: $3.25, 1 unidad
;   Manzanas: $0.50, 6 unidades

(deftemplate producto
    (slot nombre (type STRING))
    (slot precio (type FLOAT))
    (slot cantidad (type INTEGER))
)

(deftemplate producto-costo
    (slot nombre (type STRING))
    (slot costo (type FLOAT) (default 0.0))
)

(deftemplate costo-total
    (slot valor (type FLOAT) (default 0.0))
)

(defrule productosIniciales
    =>
    (assert (producto (nombre "Leche") (precio 2.50) (cantidad 2)))
    (assert (producto (nombre "Pan") (precio 1.72) (cantidad 3)))
    (assert (producto (nombre "Huevos") (precio 3.25) (cantidad 1)))
    (assert (producto (nombre "Manzanas") (precio 0.50) (cantidad 6)))
)

(defrule costo-total
    =>
    (assert (costo-total (valor 0.0)))
)

(defrule calcular-costo-total
    ?prod <- (producto (nombre ?nom) (precio ?prec) (cantidad ?cant))
    =>
    (bind ?costo (* ?prec ?cant))
    (printout t "El costo de " ?nom " es: $" ?costo crlf)
    (assert (producto-costo (nombre ?nom) (costo ?costo)))

)

(defrule sumar-al-total
    ?prod-costo <- (producto-costo (nombre ?nom) (costo ?costo))
    ?total <- (costo-total (valor ?valor-actual))
    =>
    (bind ?nuevo-total (+ ?valor-actual ?costo))
    (modify ?total (valor ?nuevo-total))
    (retract ?prod-costo)
    (printout t "Aniadido " ?nom " al total. Nuevo total: $" ?nuevo-total crlf)
)

; (load "C:/Users/balta/Documents/GitHub/FACULTAD-FCEFN/IA/clips/repasoclips/e4.clp")