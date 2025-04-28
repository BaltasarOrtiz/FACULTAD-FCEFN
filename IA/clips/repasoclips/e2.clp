; Conversor de Temperatura
; Crea reglas que conviertan temperaturas entre Celsius, Fahrenheit y Kelvin
;   Se coloca una temperatura en cualquier unidad y se obtiene su conversión a las otras unidades

(deftemplate temperatura
   (slot valor (type FLOAT))
   (slot unidad (type STRING))
)

(defrule temperaturasEjemplo
    =>
    (assert (temperatura (valor 0.0) (unidad "Celsius")))
    (assert (temperatura (valor 32.0) (unidad "Fahrenheit")))
    (assert (temperatura (valor 273.15) (unidad "Kelvin")))
    (assert (temperatura (valor 100.0) (unidad "Celsius")))
    (assert (temperatura (valor 212.0) (unidad "Fahrenheit")))
    (assert (temperatura (valor 373.15) (unidad "Kelvin")))
)

(deffunction convertirTemperatura (?valor ?unidadOrigen ?unidadDestino)
    (bind ?resultado 0)
    (if (eq ?unidadOrigen "Celsius") then
        (if (eq ?unidadDestino "Fahrenheit") then
            (bind ?resultado (+ (* ?valor (/ 9.0 5.0)) 32)) ; Conversión Celsius a Fahrenheit
        else if (eq ?unidadDestino "Kelvin") then
            (bind ?resultado (+ ?valor 273.15)) ; Conversión Celsius a Kelvin
        )
    else if (eq ?unidadOrigen "Fahrenheit") then
        (if (eq ?unidadDestino "Celsius") then
            (bind ?resultado (/ (- ?valor 32) (/ 9.0 5.0))) ; Conversión Fahrenheit a Celsius
        else if (eq ?unidadDestino "Kelvin") then
            (bind ?resultado (+ (/ (- ?valor 32) (/ 9.0 5.0)) 273.15)) ; Conversión Fahrenheit a Kelvin
        )
    else if (eq ?unidadOrigen "Kelvin") then
        (if (eq ?unidadDestino "Celsius") then
            (bind ?resultado (- ?valor 273.15)) ; Conversión Kelvin a Celsius
        else if (eq ?unidadDestino "Fahrenheit") then
            (bind ?resultado (+ (* (- ?valor 273.15) (/ 9.0 5.0)) 32)) ; Conversión Kelvin a Fahrenheit
        )
    )
    return ?resultado
)

(defrule realizarConversiones
    ?t1 <- (temperatura (valor ?v1) (unidad ?u1))
    ?t2 <- (temperatura (valor ?v2) (unidad ?u2))
    (test (neq ?u1 ?u2)) ; Me aseguro que no sean la misma unidad
    =>
    (bind ?resultado (convertirTemperatura ?v1 ?u1 ?u2))
    (printout t "La temperatura " ?v1 " " ?u1 " es igual a " ?resultado " " ?u2 crlf)
)