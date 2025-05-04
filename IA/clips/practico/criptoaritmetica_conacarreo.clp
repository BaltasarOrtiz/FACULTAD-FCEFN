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
    
    ; Acarreos
    (numero ?r1 & :(or (= ?r1 0) (= ?r1 1)))
    (numero ?r2 & :(or (= ?r2 0) (= ?r2 1)))
    (numero ?r3 & :(or (= ?r3 0) (= ?r3 1)))
    (numero ?r4 & :(or (= ?r4 0) (= ?r4 1)))

    ; R1 = A (1) 
    ; R2 + D + T = D + 10*R1 (2) 
    ; R3 + E + O = I + 10*R2 (3) 
    ; R4 + L + D = O + 10*R3 (4) 
    ; E + O = S + 10*R4 (5)

    ; R1 = A (Ecuación 1)
    (numero ?a & :(= ?a ?r1))
    (test (and (<> ?a ?d) (<> ?a ?e) (<> ?a ?l) (<> ?a ?o) (<> ?a ?t)))
    
    ; R2 + T = 10*R1 (Ecuación 2 simplificada)
    (test (= (+ ?r2 ?t) (* 10 ?r1)))
    
    ; Ecuación 3: debe existir un I tal que R3 + E + O = I + 10*R2
    (test (and (>= (- (+ ?r3 ?e ?o) (* 10 ?r2)) 0) 
               (<= (- (+ ?r3 ?e ?o) (* 10 ?r2)) 9)))
    
    (numero ?i & :(= ?i (mod (- (+ ?r3 ?e ?o) (* 10 ?r2)) 10)))
    (test (and (<> ?i ?d) (<> ?i ?e) (<> ?i ?l) (<> ?i ?o) (<> ?i ?t) (<> ?i ?a)))
    
    ; Ecuación 4: R4 + L + D = O + 10*R3
    (test (= (+ ?r4 ?l ?d) (+ ?o (* 10 ?r3))))
    
    ; Ecuación 5: debe existir un S tal que E + O = S + 10*R4
    (test (and (>= (- (+ ?e ?o) (* 10 ?r4)) 0) 
               (<= (- (+ ?e ?o) (* 10 ?r4)) 9)))
    
    (numero ?s & :(= ?s (mod (- (+ ?e ?o) (* 10 ?r4)) 10)))
    (test (and (<> ?s ?d) (<> ?s ?e) (<> ?s ?l) (<> ?s ?o) (<> ?s ?t) (<> ?s ?i) (<> ?s ?a)))
    
    ; Comprobación final
    (test (= (+ (* ?d 1000) (* ?e 100) (* ?l 10) ?e
               (* ?t 1000) (* ?o 100) (* ?d 10) ?o)
            (+ (* ?a 10000) (* ?d 1000) (* ?i 100) (* ?o 10) ?s)))
    =>
    (printout t "Solución alternativa:" crlf)
    (printout t "D = " ?d ", E = " ?e ", L = " ?l ", O = " ?o ", T = " ?t crlf)
    (printout t "A = " ?a ", I = " ?i ", S = " ?s crlf)
    (printout t "Acarreos: R1 = " ?r1 ", R2 = " ?r2 ", R3 = " ?r3 ", R4 = " ?r4 crlf)
    (printout t crlf)
    (printout t "   " ?r4 ?r3 ?r2 ?r1 crlf)
    (printout t "    " ?d ?e ?l ?e crlf)
    (printout t "  + " ?t ?o ?d ?o crlf)
    (printout t "  --------" crlf)
    (printout t "  " ?a ?d ?i ?o ?s crlf)
    
    (assert (solucion-alternativa ?d ?e ?l ?o ?t ?a ?i ?s ?r1 ?r2 ?r3 ?r4))
)