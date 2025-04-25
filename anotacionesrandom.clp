; Vuelca parcialmente de una jarra a otra cuando no cabe todo
(defrule verter-jarra-parcial
    ?f <- (estado ($?valores))
    (jarra ?jarraX)
    (jarra ?jarraY)
    (test (neq ?jarraOrigen ?jarraDestino)) ; Asegura que no se vuelque en la misma jarra
    =>
    (bind ?capacidadOrigen 
        (if (= ?jarraOrigen 1) 24
            (if (= ?jarraOrigen 2) 5
                (if (= ?jarraOrigen 3) 11
                    (if (= ?jarraOrigen 4) 13)
                )
            )
        )
    ) ; Capacidad de la jarra origen

    (bind ?capacidadDestino 
        (if (= ?jarraDestino 1) 24
            (if (= ?jarraDestino 2) 5
                (if (= ?jarraDestino 3) 11
                    (if (= ?jarraDestino 4) 13)
                )
            )
        )
    ) ; Capacidad de la jarra destino

    (bind ?x (nth$ ?jarraOrigen ?valores)) ; Cantidad de litros en la jarra origen
    (bind ?y (nth$ ?jarraDestino ?valores)) ; Cantidad de litros en la jarra destino

    (bind ?diferencia (- ?capacidadDestino ?y)) ; Diferencia entre la capacidad de la jarra destino y su contenido actual
    (bind ?volumen (- ?x (- ?capacidadDestino - y))) ; Volumen a verter (mínimo entre el contenido de la jarra origen y la diferencia de la jarra destino)
    (bind ?nuevoX (- ?x ?volumen)) ; Nuevo contenido de la jarra origen
    (bind ?nuevoY (+ ?y ?volumen)) ; Nuevo contenido de la jarra destino
    
)



; No usamos template por que lo consideramos innecesario para este problema

(defrule inicio
    ; Se definen los estados iniciales
    ; Podria hacerse usando deffacts, pero al hacerlo como regla no hace falta usar (reset) para ejecutar el programa
    => 
    (assert (numero 1))
    (assert (numero 2))
    (assert (numero 3))
    (assert (numero 4))
    (assert (contenido 24 0 0 0))
)

(defglobal ?*capacidades* = (create$ 24 13 11 5))  ; Definicion de una variable global que contiene las capacidades de las jarras

(defrule estadoFinal
    ; Regla que se ejecuta una vez se llego al estado final, se declara la prioridad maxima (10000) y se detiene el programa
    (declare (salience 1000))
    (contenido 8 8 8 0)
    =>
    (printout t "Estado Final" crlf)
    (halt)
)

(defrule moverDeJarraEnJarra
    ; Regla que se encarga de mover el contenido de una jarra origen a una jarra destino
    (numero ?origen)
    (numero ?destino)
    (test (neq ?origen ?destino))  ; No se puede mover de una jarra a si misma
    (contenido $?contenidos)  ; Se obtiene el estado actual
    =>
    (bind ?conOrigen (nth$ ?origen ?contenidos))      ; Se obtiene la cantidad de litros en la jarra origen
    (bind ?conDestino (nth$ ?destino ?contenidos))    ; Se obtiene la cantidad de litros en la jarra destino
    (bind ?capDestino (nth$ ?destino ?*capacidades*)) ; Se obtiene la capacidad de la jarra destino
    (bind ?litros (min ?conOrigen (- ?capDestino ?conDestino))) ; Se calcula la cantidad de litros a mover, que seria la cantidad de litros en la jarra origen o el faltante en la jarra destino para llenarse
    (bind ?contenidos (replace$ ?contenidos ?origen  ?origen  (- ?conOrigen  ?litros))) ; Se actualiza la cantidad de litros en la jarra origen
    (bind ?contenidos (replace$ ?contenidos ?destino ?destino (+ ?conDestino ?litros))) ; Se actualiza la cantidad de litros en la jarra destino
    (assert (contenido $?contenidos)) ; Se agrega el nuevo estado
)


    (bind ?capacidadOrigen 
        (if (= ?jarraOrigen 1) then 24 
            else 
                (if (= ?jarraOrigen 2) then 5 
                    else 
                        (if (= ?jarraOrigen 3) then 11 
                            else 13
                        )
                )
        )
    )

    (bind ?capacidadDestino 
        (if (= ?jarraDestino 1) then 24 
            else 
                (if (= ?jarraDestino 2) then 5 
                    else 
                        (if (= ?jarraDestino 3) then 11 
                            else 13
                        )
                )
        )
    )


    ;(defrule estado
;    (slot x (type INTEGER) (default 0))
;    (slot y (type INTEGER) (default 0))
;   (slot z (type INTEGER) (default 0))
;    (slot w (type INTEGER) (default 0))
;)

; Inicializa la base de hechos
;(deffacts estado_inicial_jarras
;    (estado (24 0 0 0))
;    ; Para tomar la jarra origen y destino
;    (jarra 1)
;    (jarra 2)
;    (jarra 3)
;    (jarra 4)
;)

;EJERCICIO FUNCIONANDO CORRECTAMENTE DEL MISMO PROBLEMA

; Definición de una plantilla para representar un estado del juego de las jarras
(deftemplate estado
    (multislot contenido (type INTEGER) (range 0 24) (cardinality 4 4))
    (slot heuristica (type INTEGER))
)

; Definición de las capacidades de las jarras como una variable global
(defglobal ?*capacidades* = (create$ 24 5 11 13))

(deffunction calcularHeuristica (?contenidos)
    ; La heurística es la suma de las diferencias absolutas con el estado final (8,8,8,0)
    (+
        (abs (- 8 (nth$ 1 ?contenidos)))
        (abs (- 8 (nth$ 2 ?contenidos)))
        (abs (- 8 (nth$ 3 ?contenidos)))
        (nth$ 4 ?contenidos)
    )
)

(defrule estado_inicial_jarras
    =>
    (assert (estado (contenido 24 0 0 0) (heuristica 32)))
    (assert (numero 1))
    (assert (numero 2))
    (assert (numero 3))
    (assert (numero 4))
)

(defrule estadoFinal
    (declare (salience 10000))
    (estado (contenido 8 8 8 0) (heuristica 0))
    =>
    (printout t "Estado Final alcanzado: (8 8 8 0)" crlf)
    (halt)
)

; Regla para volcar el contenido de una jarra en otra
(defrule volcar
    (numero ?origen)
    (numero ?destino)
    (test (neq ?origen ?destino))
    (estado (contenido $?contenidos) (heuristica ?heu))
    (test (> (nth$ ?origen ?contenidos) 0)) ; La jarra origen debe tener contenido
    (test (< (nth$ ?destino ?contenidos) (nth$ ?destino ?*capacidades*))) ; La jarra destino no debe estar llena
    (not (estado (heuristica ?h2&:(< ?h2 ?heu))))
    (not (estadoSinSalida $?contenidos))
    =>
    ; Obtener contenidos actuales
    (bind ?conOrigen (nth$ ?origen ?contenidos))
    (bind ?conDestino (nth$ ?destino ?contenidos))
    (bind ?capDestino (nth$ ?destino ?*capacidades*))
    
    ; Calcular cuánto volcar
    (bind ?litros (min ?conOrigen (- ?capDestino ?conDestino)))
    
    ; Actualizar contenidos
    (bind ?nuevosContenidos (replace$ ?contenidos ?origen ?origen (- ?conOrigen ?litros)))
    (bind ?nuevosContenidos (replace$ ?nuevosContenidos ?destino ?destino (+ ?conDestino ?litros)))
    
    ; Calcular nueva heurística y crear nuevo estado
    (bind ?nuevaHeuristica (calcularHeuristica ?nuevosContenidos))
    (assert (estado (contenido ?nuevosContenidos) (heuristica ?nuevaHeuristica)))
    
    ; Imprimir los pasos (opcional, para depuración)
    (printout t "Moviendo " ?litros " litros de jarra " ?origen " a jarra " ?destino ": " ?nuevosContenidos " (h=" ?nuevaHeuristica ")" crlf)
)

(defrule eliminarEstadosSinSalida
    (declare (salience -50))
    ?fact <- (estado (heuristica ?heu) (contenido $?contenido))
    (not (estado (heuristica ?h2&:(< ?h2 ?heu))))
    =>
    (retract ?fact)
    (assert (estadoSinSalida ?contenido))
    (printout t "Estado sin salida: " ?contenido crlf)
)