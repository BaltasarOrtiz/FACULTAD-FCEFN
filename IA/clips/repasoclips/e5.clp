;Ejercicio 2: Control de Temperatura
;Objetivo: Crear un sistema que monitoree temperaturas y genere alertas.
;Requisitos:
;    Crear un template para registros de temperatura con ubicación, valor y timestamp

;Crear reglas para:
;    Identificar temperaturas extremas (>30°C o <0°C)
;        Calcular la temperatura promedio por ubicación
;        Generar una alerta si hay un cambio brusco (>5°C en la misma ubicación)



;    Datos de prueba:
;        Cocina, 22°C, 08:00
;        Exterior, 15°C, 08:00
;        Sótano, 18°C, 08:00
;        Cocina, 24°C, 12:00
;        Exterior, 28°C, 12:00
;        Sótano, 17°C, 12:00

(deftemplate registroTemp
    (slot ubicacion (type STRING))
    (slot valor (type FLOAT))
    (slot timestamp (type STRING))
)

(defrule temperaturasPrueba
    =>
    (assert (registroTemp (ubicacion "Cocina") (valor 22.0) (timestamp "08:00")))
    (assert (registroTemp (ubicacion "Exterior") (valor 15.0) (timestamp "08:00")))
    (assert (registroTemp (ubicacion "Sotano") (valor 18.0) (timestamp "08:00")))
    (assert (registroTemp (ubicacion "Cocina") (valor 24.0) (timestamp "12:00")))
    (assert (registroTemp (ubicacion "Exterior") (valor 28.0) (timestamp "12:00")))
    (assert (registroTemp (ubicacion "Sotano") (valor 17.0) (timestamp "12:00")))
)

(defrule identificar-extremas
    (registroTemp (ubicacion ?ubi) (valor ?val) (timestamp ?ts))
    (or 
        (test (> ?val 20))
        (test (< ?val 0))
    )
    =>
    (printout t "Se ha identificado temperatura extrema en: " ?ubi " con: " ?val crlf)
)