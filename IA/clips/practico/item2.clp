; Item2
;   Confeccione tres reglas que indiquen:
;       • Persona mayor de 18 anios (nombre)
;       • Todo el mundo es menor de edad
;       • Persona de nombre Maria o Marta

(deftemplate persona
    (slot nombre (type STRING))
    (slot edad (type INTEGER))
)

(deffacts personas-iniciales
    (persona (nombre "Juan") (edad 25))
    (persona (nombre "Ana") (edad 17))
    (persona (nombre "Carlos") (edad 42))
    (persona (nombre "Maria") (edad 30))
)

(defrule mayor-de-edad
    ?p <- (persona (nombre ?n) (edad ?e&:(> ?e 18))) ; CONDICIONES
    =>
    (printout t "Persona mayor de 18 anios: " ?n ", " ?e " anios" crlf) ; ACCIONES
)

(defrule menor-de-edad
    ?p <- (persona (nombre ?n) (edad ?e&:(<= ?e 18))) ; CONDICIONES
    =>
    (printout t "Persona menor de edad: " ?n ", " ?e " anios" crlf) ; ACCIONES
)

(defrule nombre-maria-o-marta
    ?p <- (persona (nombre ?n&:(or (eq ?n "Maria") (eq ?n "Marta")))) ; CONDICIONES
    =>
    (printout t "Persona de nombre Maria o Marta: " ?n crlf) ; ACCIONES
)

; "C:/Users/balta/Documents/GitHub/FACULTAD-FCEFN/IA/clips/practico/item2.clp"