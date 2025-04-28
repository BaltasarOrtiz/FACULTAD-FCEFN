; Calculadora de Notas
; Define un template para estudiantes con nombre y múltiples notas
; Implementa reglas para:
;   Calcular el promedio de cada estudiante
;   Determinar si aprobó o reprobó (aprobado >= 6)
;   Identificar el estudiante con mejor promedio
; (load "C:/Users/balta/Documents/GitHub/FACULTAD-FCEFN/IA/clips/repasoclips/e3.clp")

;;; 1. Definición del template para estudiantes
(deftemplate estudiante
   (slot nombre)
   (slot carrera (default "No especificada"))
   (multislot notas)
   (slot promedio (default 0.0))
   (slot estado (default "pendiente"))
)

;;; 2. Definición del template para control del mejor estudiante
(deftemplate mejor-estudiante
   (slot nombre (default "ninguno"))
   (slot promedio (default 0.0))
)

;;; 3. Hechos iniciales para pruebas
(deffacts estudiantes-ejemplo
   (estudiante (nombre "Juan Perez") (carrera "Informatica") (notas 7 8 6 9))
   (estudiante (nombre "Maria Lopez") (carrera "Matematicas") (notas 9 9 8 10))
   (estudiante (nombre "Carlos Gomez") (carrera "Fisica") (notas 5 6 5 7))
   (estudiante (nombre "Ana Rodriguez") (carrera "Informatica") (notas 8 7 8 6))
   (mejor-estudiante)
)

;;; 4. Regla para calcular el promedio de cada estudiante
(defrule calcular-promedio
   ?est <- (estudiante (nombre ?nombre) (notas $?notas) (promedio 0.0))
   =>
   (bind ?suma 0)
   (bind ?cantidad 0)
   
   ;; Sumar todas las notas
   (foreach ?nota ?notas
        (bind ?suma (+ ?suma ?nota))
        (bind ?cantidad (+ ?cantidad 1))
   )
   
   ;; Calcular el promedio si hay notas
   (if (> ?cantidad 0)
        then
            (bind ?prom (/ ?suma ?cantidad))
            (modify ?est (promedio ?prom))
            (printout t "El promedio de " ?nombre " es: " ?prom crlf)
        else
            (printout t ?nombre " no tiene notas registradas." crlf)
   )
)

;;; 5. Regla para determinar si un estudiante aprobó o reprobó
(defrule determinar-estado
   ?est <- (estudiante (nombre ?nombre) (promedio ?prom&:(> ?prom 0)) (estado "pendiente"))
   =>
   (if (>= ?prom 6)
      then
         (modify ?est (estado "aprobado"))
         (printout t ?nombre " ha APROBADO con promedio " ?prom crlf)
      else
         (modify ?est (estado "reprobado"))
         (printout t ?nombre " ha REPROBADO con promedio " ?prom crlf)
   )
)

;;; 6. Regla para actualizar al mejor estudiante cuando se encuentra uno mejor
(defrule actualizar-mejor-estudiante
   ?est <- (estudiante (nombre ?nombre) (promedio ?prom&:(> ?prom 0)))
   ?mejor <- (mejor-estudiante (promedio ?mejor-prom&:(< ?mejor-prom ?prom)))
   =>
   (modify ?mejor (nombre ?nombre) (promedio ?prom))
   (printout t "Nuevo mejor estudiante: " ?nombre " con promedio " ?prom crlf)
)

;;; 7. Regla para mostrar el resultado final
(defrule mostrar-resultados
   (declare (salience -100))  ;; Baja prioridad para que se ejecute al final
   (mejor-estudiante (nombre ?nombre&~"ninguno") (promedio ?prom))
   =>
   (printout t crlf)
   (printout t "===================================" crlf)
   (printout t "RESULTADOS FINALES:" crlf)
   (printout t "El mejor estudiante es: " ?nombre " con promedio " ?prom crlf)
   (printout t "===================================" crlf)
)

;;; 8. Función para agregar un nuevo estudiante
(deffunction agregar-estudiante (?nombre ?carrera $?notas)
   (assert (estudiante (nombre ?nombre) (carrera ?carrera) (notas $?notas)))
   (printout t "Estudiante " ?nombre " agregado correctamente." crlf)
)

;;; Instrucciones para el usuario
(defrule inicializar
    =>
    (printout t "Calculadora de Notas cargada correctamente!" crlf)
    (printout t "Ejecuta (reset) para inicializar y (run) para procesar los datos" crlf)
    (printout t "Para agregar un nuevo estudiante, usa la función:" crlf)
    (printout t "(agregar-estudiante \"Nombre\" \"Carrera\" nota1 nota2 ...)" crlf)
)
