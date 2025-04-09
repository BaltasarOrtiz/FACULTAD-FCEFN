; Item3
; Convierta la siguiente red semántica en una serie de hechos de una instrucción deffacts.
; Utilice un deftemplate para describir los hechos y realice las reglas que permitan mostrar las siguientes relaciones familiares: Abuela, nieto, tia, medio-hermano.


(deftemplate persona
   (slot nombre)
   (slot hijos)
   (slot esposo-de (default nil))
   (slot esposa-de (default nil))
)

; Hechos iniciales que representan el árbol genealógico
(deffacts familia
   ; Personas
   (persona (nombre Ana) (hijos Susana) (esposa-de Luis))
   (persona (nombre Luis) (hijos Susana) (esposo-de Ana))
   (persona (nombre Carolin) (hijos Tomás) (esposa-de David))
   (persona (nombre David) (hijos Tomás) (esposo-de Carolin))
   (persona (nombre Susana) (hijos Juan Pedro) (esposa-de Tomás))
   (persona (nombre Tomás) (hijos Juan Pedro) (esposo-de Susana))
   (persona (nombre Juan) (hijos))
   (persona (nombre Pedro) (hijos))
   (persona (nombre Maria) (hijos Pedro))
)

; Regla para identificar relación de abuela
(defrule abuela
   (persona (nombre ?abuela) (hijos $? ?hijo $?)) ; $? comodin multicampo que me permite emparejar uno o mas hijos ?abuela → ?hijo
   (persona (nombre ?hijo) (hijos $? ?nieto $?)) ; ?abuela → ?hijo → ?nieto
   (test (neq ?abuela nil)) ; test para verificar que abuela no sea nulo
   (test (neq ?hijo nil)) ; test para verificar hijo que no sea nulo
   (test (neq ?nieto nil)) ; test para verificar nieto que no sea nulo
   =>
   (printout t ?abuela " es abuela de " ?nieto crlf)
)

; Regla para identificar relación de nieto
(defrule nieto
   (persona (nombre ?abuelo) (hijos $? ?padre $?)) 
   (persona (nombre ?padre) (hijos $? ?nieto $?))
   (test (neq ?abuelo nil))
   (test (neq ?padre nil))
   (test (neq ?nieto nil))
   =>
   (printout t ?nieto " es nieto/a de " ?abuelo crlf)
)

; Regla para identificar relación de tia
(defrule tia
   (persona (nombre ?padre) (hijos $? ?hijo $?))
   (persona (nombre ?padre) (hijos $? ?hermano $?))
   (persona (nombre ?hermano) (esposa-de ?))
   (test (neq ?hermano ?hijo))
   (test (neq ?padre nil))
   (test (neq ?hijo nil))
   (test (neq ?hermano nil))
   =>
   (printout t ?hermano " es tia de " ?hijo crlf)
)

; Regla para identificar relación de medio-hermano
(defrule medio-hermano
   (persona (nombre ?padre1) (hijos $? ?hijo1 $?))
   (persona (nombre ?padre2) (hijos $? ?hijo1 $? ?hijo2 $?))
   (persona (nombre ?madre) (hijos $? ?hijo2 $?))
   (test (neq ?hijo1 ?hijo2))
   (test (neq ?padre1 ?padre2))
   (test (neq ?madre ?padre1))
   =>
   (printout t ?hijo1 " es medio-hermano/a de " ?hijo2 crlf)
)