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