;Ejercicio 2) CLIPS
;Item 2.1) Problemas de jarras:
;a) Representar, en reglas, el conocimiento que permite realizar los diferentes movimientos de líquidos entre jarras y sus llenados y vaciamiento.
;b) Realizar todo ese espacio de búsqueda (ForwarChaining) enumerando los nodos en una búsqueda hacia lo profundo y hacia lo ancho.
;c) En cada forma de búsqueda exprese los pasos hasta encontrar la solución.
;d) Utilice y explique una heurística que le permita moverse solamente por el camino más promisorio!!
;e) Realice una implementación en Clips que le permita encontrar la solución con alguna de las instancias ciegas y con la heurística propuesta en el punto d) Marque las diferencias en los tiempos de ejecución.
;De qué modo podrías dividir el contenido de una jarra de 24 litros en tres partes iguales, utilizando solamente la jarra original y otras tres de 5, 11 y 13 litros de capacidad respectivamente. (0,65)

;(load "C:/Users/balta/Documents/GitHub/FACULTAD-FCEFN/IA/clips/practico/ejerciciojarras_conheuristica.clp")

; Definicion de una plantilla para representar un estado del juego de las jarras en un momento especifico
(deftemplate estado
	(multislot contenido (type INTEGER) (range 0 24) (cardinality 4 4)) ; Puede verse como una "tupla" de 4 elementos que representan la cantidad de litros en cada jarra
	; Los valores contenidos en la tupla pueden variar entre 0 y 24, que es la capacidad maxima de la jarra mas grande
	; La cardinalidad es 4 4, lo que significa que la tupla siempre tendra 4 elementos (minimo 4 y maximo 4)
	(slot heuristica (type INTEGER)) ; Valor de la heuristica para el estado actual, a menor valor, mas cercano a la solucion
)

(deffunction calcularHeuristica (?contenidos) ; Funcion que calcula la heuristica para un estado dado
	; La heuristica se calcula como la suma de las diferencias absolutas entre la cantidad de litros en cada jarra en comparacion con estado final
	(+
		(abs (- 8 (nth$ 1 ?contenidos)))
		(abs (- 8 (nth$ 2 ?contenidos)))
		(abs (- 8 (nth$ 3 ?contenidos)))
		(nth$ 4 ?contenidos)
	)
)

(defrule estado_inicial_jarras
    =>
    (assert (jarra 1)) 
    (assert (jarra 2)) 
    (assert (jarra 3)) 
    (assert (jarra 4))
    (assert (estado (contenido 24 0 0 0) (heuristica 32))) ; Estado inicial de las jarras
)

(defrule estadoFinal
	; Regla que se ejecuta una vez se llego al estado final, se declara la prioridad maxima (10000) y se detiene el programa
	(declare (salience 10000))
	(estado (contenido 8 8 8 0) (heuristica 0))
	=>
	(printout t "Estado Final" crlf)
	(halt)
)

; Vuelca el contenido de una jarra en la otra cuando cabe completamente
(defrule volcar
    (estado (contenido $?contenidos) (heuristica ?heu)) ; Obtener el estado actual
    (jarra ?jarraOrigen ?capacidadOrigen) ; Jarra origen
    (jarra ?jarraDestino ?capacidadDestino) ; Jarra destinos
    (test (> (nth$ ?jarraOrigen ?contenidos) 0)) ; Asegura que la jarra origen no esté vacía
    (test (neq ?jarraOrigen ?jarraDestino)) ; Asegura que no se vuelque en la misma jarra
    (not (estado (heuristica ?h2&:(< ?h2 ?heu)))) ; Verifica que no haya un estado con mejor heurística
    (not (estadoSinSalida $?contenidos)) ; Verifica que no sea un estado sin salida
    =>
    (bind ?x (nth$ ?jarraOrigen ?contenidos)) ; Cantidad de litros en la jarra origen
    (bind ?y (nth$ ?jarraDestino ?contenidos)) ; Cantidad de litros en la jarra destino
	; Obtener la capacidad de la jarra destino
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

	; Se calcula la cantidad de litros a mover, que seria la cantidad de litros en la jarra origen o el faltante en la jarra destino para llenarse
    (bind ?litros (min ?x (- ?capacidadDestino ?y))) 
	(bind ?contenidos (replace$ ?contenidos ?jarraOrigen ?jarraOrigen  (- ?x  ?litros))) ; Se actualiza la cantidad de litros en la jarra origen
	(bind ?contenidos (replace$ ?contenidos ?jarraDestino ?jarraDestino (+ ?y ?litros))) ; Se actualiza la cantidad de litros en la jarra destino
	(assert (estado (contenido $?contenidos) (heuristica (calcularHeuristica ?contenidos)))) ; Se agrega el nuevo estado a la base de hechos
)


 
(defrule eliminarEstadosSinSalida
	(declare (salience -50)) ; Se declara una prioridad negativa para que se ejecute al final cuando la regla de volcar ya no pueda hacer nada, es decir que los estados con la menor heuristica fueron explorados completamente
	?fact <- (estado (heuristica ?heu) (contenido $?contenido)) ; Se obtiene un estado
	(not (estado (heuristica ?h2&:(< ?h2 ?heu)))) ; Se verifica que sea uno de los estados con menor heuristica
	=>
	(retract ?fact) ; Se elimina el estado
	(assert (estadoSinSalida ?contenido)) ; Se agrega el estado a la lista de estados sin salida
	; Al eliminar todos los estados con menor heuristica, la menor heuristica "sube" por asi decirlo, lo que permite que en la regla volcar se puedan explorar otros estados debido a que ciertos estados pasarian a cumplir la condicion de tener la menor heuristica
)