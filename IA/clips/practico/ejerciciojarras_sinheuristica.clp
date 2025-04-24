;Ejercicio 2) CLIPS
;Item 2.1) Problemas de jarras:
;a) Representar, en reglas, el conocimiento que permite realizar los diferentes movimientos de líquidos entre jarras y sus llenados y vaciamiento.
;b) Realizar todo ese espacio de búsqueda (ForwarChaining) enumerando los nodos en una búsqueda hacia lo profundo y hacia lo ancho.
;c) En cada forma de búsqueda exprese los pasos hasta encontrar la solución.
;d) Utilice y explique una heurística que le permita moverse solamente por el camino más promisorio!!
;e) Realice una implementación en Clips que le permita encontrar la solución con alguna de las instancias ciegas y con la heurística propuesta en el punto d) Marque las diferencias en los tiempos de ejecución.
;De qué modo podrías dividir el contenido de una jarra de 24 litros en tres partes iguales, utilizando solamente la jarra original y otras tres de 5, 11 y 13 litros de capacidad respectivamente. (0,65)

;"C:/Users/balta/Documents/GitHub/FACULTAD-FCEFN/IA/clips/practico/ejerciciojarras.clp"

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
    (test (neq ?jarraOrigen ?jarraDestino)) ; Asegura que no se vuelque en la misma jarra
    =>
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
    (printout "Se ha encontrado la solucion: 8, 8, 8, 0" crlf)
    (halt)
)