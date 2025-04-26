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
		(nth$ 2 ?contenidos)
		(abs (- 8 (nth$ 3 ?contenidos)))
		(abs (- 8 (nth$ 4 ?contenidos)))
	)
)

(defrule estado_inicial_jarras
    =>
    (assert (jarra 1 24)) ; Jarra 1 con capacidad de 24 litros
    (assert (jarra 2 5))  ; Jarra 2 con capacidad de 5 litros
    (assert (jarra 3 11)) ; Jarra 3 con capacidad de 11 litros
    (assert (jarra 4 13)) ; Jarra 4 con capacidad de 13 litros
    (assert (estado (contenido 24 0 0 0) (heuristica 32))) ; Estado inicial de las jarras
)

(defrule estadoFinal
	; Regla que se ejecuta una vez se llego al estado final, se declara la prioridad maxima (10000) y se detiene el programa
	(declare (salience 10000))
	(estado (contenido 8 0 8 8) (heuristica 0))
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
    (not (estadoSinSalida ?contenido)) ; Verifica que no sea un estado sin salida
    =>
    (bind ?x (nth$ ?jarraOrigen ?contenidos)) ; Cantidad de litros en la jarra origen
    (bind ?y (nth$ ?jarraDestino ?contenidos)) ; Cantidad de litros en la jarra destino

	; Se calcula la cantidad de litros a mover, que seria la cantidad de litros en la jarra origen o el faltante en la jarra destino para llenarse
    (bind ?litros (min ?x (- ?capacidadDestino ?y))) 
	(bind ?contenidos (replace$ ?contenidos ?jarraOrigen ?jarraOrigen  (- ?x  ?litros))) ; Se actualiza la cantidad de litros en la jarra origen
	(bind ?contenidos (replace$ ?contenidos ?jarraDestino ?jarraDestino (+ ?y ?litros))) ; Se actualiza la cantidad de litros en la jarra destino
	; Verificar que no sea un estado sin salida
	(if (not (any-factp ((?f estadoSinSalida))
                    (eq ?f:implied $?contenidos)))
    then 
    (assert (estado (contenido ?contenidos) (heuristica (calcularHeuristica ?contenidos))))
	)	

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