(defrule estado_inicial_jarras
    =>
    (assert (estado 24 0 0 0)) ; Estado inicial de las jarras
    (assert (jarra 1 24)) ; Jarra de 24 litros
    (assert (jarra 2 5)) ; Jarra de 5 litros
    (assert (jarra 3 11)) ; Jarra de 11 litros
    (assert (jarra 4 13)) ; Jarra de 13 litros
)

; Vuelca el contenido de una jarra en la otra cuando cabe completamente
(defrule volcar
    (estado $?valores) ; Estado actual de las jarras
    (jarra ?jarraOrigen ?capacidadOrigen) ; Jarra origen
    (jarra ?jarraDestino ?capacidadDestino) ; Jarra destino
    ; La jarra origen no puede tener contenido 0
    (test (> (nth$ ?jarraOrigen ?valores) 0)) ; Asegura que la jarra origen no esté vacía
    (test (neq ?jarraOrigen ?jarraDestino)) ; Asegura que no se vuelque en la misma jarra
    =>
    ; Obtiene la capacidad de las jarras origen y destino
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
    (bind ?x (nth$ ?jarraOrigen ?valores)) ; Cantidad de litros en la jarra origen
    (bind ?y (nth$ ?jarraDestino ?valores)) ; Cantidad de litros en la jarra destino

    (bind ?diferencia (- ?capacidadDestino ?y)) ; Diferencia entre la capacidad de la jarra destino y su contenido actual
    (bind ?volumen (min ?x ?diferencia)) ; Volumen a verter (mínimo entre el contenido de la jarra origen y la diferencia de la jarra destino)
    (bind ?nuevoX (- ?x ?volumen)) ; Nuevo contenido de la jarra origen
    (bind ?nuevoY (+ ?y ?volumen)) ; Nuevo contenido de la jarra destino

    (bind ?nuevoEstado (replace$ ?valores ?jarraOrigen ?jarraOrigen ?nuevoX)) ; Reemplaza el valor de la jarra origen
    (bind ?nuevoEstado (replace$ ?nuevoEstado ?jarraDestino ?jarraDestino ?nuevoY)) ; Reemplaza el valor de la jarra destino
    (assert (estado $?nuevoEstado)) ; Agrega el nuevo estado a la base de hechos
)

 
(defrule comprobar
    (declare (salience 1000)) ; Prioridad máxima para esta regla
    (estado 8 0 8 8)
    =>
    (printout "Se ha encontrado la solucion: 8, 0, 8, 8" crlf)
    (halt)
)