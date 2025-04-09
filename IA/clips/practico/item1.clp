; a) La información en CLIPS se maneja mediante hechos. Los hechos pueden tener un solo campo, en general tienen
;    más de uno, las formas más comunes de expresar hechos en CLIPS son:
    ;   <Atributo><valor>
    ;   <Objeto><atributo><valor>
    ;   <Relación><atributo><valor>
    ;   De un ejemplo de cada una.
; b) Hechos iniciales. ¿Cuándo y cómo se cargan en la MT? Mediante un ejemplo muestre como se realiza.
; c) ¿Qué es la Agenda? ¿Dónde se encuentra? ¿qué contiene? ¿Cuándo se agrega o se elimina una elemento en ella? Indique el orden en el que un elemento es agregado a ella.


; a)
; <Atributo><valor>
; (color Rojo)
; <Objeto><atributo><valor>
; (coche color Rojo)
; <Relación><atributo><valor>
; (padre-de Juan Pedro)

; b)
(deffacts estado-inicial
    (color Rojo)
    (coche color Rojo)
    (padre-de Juan Pedro)
)
; Los hechos iniciales se cargan en la memoria de trabajo (MT) al inicio del programa o mediante la función (reset).
; Se pueden insertar hechos iniciales en la MT utilizando la función (deffacts) que define un conjunto de hechos.

; c)
; La Agenda en CLIPS es una estructura de datos interna que funciona como una lista priorizada de reglas que han sido activadas pero que aún no se han ejecutado. Es esencialmente una "cola de espera" donde se mantienen las reglas que están listas para ser ejecutadas por el motor de inferencia.

; La Agenda contiene:
    ; Las activaciones de reglas (instancias de reglas cuyos patrones se han emparejado con hechos en la Memoria de Trabajo)
    ; Cada activación incluye:
        ; - El nombre de la regla
        ; - Los hechos específicos que provocaron su activación
        ; - La prioridad de la regla (determinada por su salience y la estrategia de resolución de conflictos)

; Se agrega una activación a la Agenda cuando:
    ; - Se introduce un nuevo hecho en la Memoria de Trabajo (mediante assert)
    ; - Se modifica un hecho existente (mediante modify)
    ; - Se elimina un hecho (mediante retract)

; Factores que determinan el Orden de la Agenda
; - La prioridad de las reglas (salience)
; - La estrategia de resolución de conflictos (DEPTH, BREADTH, COMPLEXITY, SIMPLICITY, LEX, MEA)
; - El orden de definición de las reglas (el orden en que se escribieron en el código)
