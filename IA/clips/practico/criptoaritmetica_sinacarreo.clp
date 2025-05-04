(deffacts numeros
    ; Hechos que son todos los numeros posibles
    (numero 0)
    (numero 1)
    (numero 2)
    (numero 3)
    (numero 4)
    (numero 5)
    (numero 6)
    (numero 7)
    (numero 8)
    (numero 9)
)

; DELE + TODO = ADIOS

(defrule buscarSolucion
    ; Se asignan valores a las variables y se comprueban que sean valores distintos a las variables previamente asignadas
    (numero ?e)
    (numero ?d &~ ?e)
    (numero ?l &~ ?e &~ ?d)
    (numero ?o &~ ?e &~ ?d &~ ?l)
    (numero ?s &~ ?e &~ ?d &~ ?l &~ ?o)
    (numero ?t &~ ?e &~ ?d &~ ?l &~ ?o &~ ?s)
    (numero ?a &~ ?e &~ ?d &~ ?l &~ ?o &~ ?s &~ ?t)
    (numero ?i &~ ?e &~ ?d &~ ?l &~ ?o &~ ?s &~ ?t &~ ?a)
    
    ; Se comprueba si estas asignaciones de numeros a las variables cumplen la ecuacion
    ; (D * 1000 + E * 100 + L * 10 + E) + (T * 1000 + O * 100 + D * 10 + O) = A * 10000 + D * 1000 + I * 100 + O * 10 + S
    (test (eq
        (+ (* ?d 1000) (* ?e 100) (* ?l 10) ?e
           (+ (* ?t 1000) (* ?o 100) (* ?d 10) ?o))
        (+ (* ?a 10000) (* ?d 1000) (* ?i 100) (* ?o 10) ?s
    )))
    =>
    ; Si cumple significa que es solucion
    (printout t "Solucion: A = " ?a ", D = " ?d ", I = " ?i ", L = " ?l ", O = " ?o ", S = " ?s ", T = " ?t ", E = " ?e crlf)
    (assert (solucion ?a ?d ?i ?l ?o ?s ?t ?e))
)