; Definición de reglas y hechos básicos en CLIPS

; Definición de una plantilla para personas
(deftemplate persona
   (slot nombre (type STRING))
   (slot edad (type INTEGER))
   (slot profesion (type STRING)))

; Insertar algunos hechos usando la plantilla
(deffacts personas-iniciales
   (persona (nombre "Juan") (edad 30) (profesion "Ingeniero"))
   (persona (nombre "Maria") (edad 25) (profesion "Médico"))
   (persona (nombre "Carlos") (edad 40) (profesion "Profesor")))

; Definir una regla simple
(defrule mostrar-personas-mayores-30
   (persona (nombre ?n) (edad ?e) (profesion ?p))
   (test (> ?e 30))
   =>
   (printout t "Persona mayor de 30: " ?n ", " ?e " años, " ?p crlf))

; Definir otra regla
(defrule contar-profesionales
   (persona (profesion ?p))
   =>
   (printout t "Encontrado un profesional: " ?p crlf))
