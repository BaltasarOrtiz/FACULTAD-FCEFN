; (load "C:/Users/balta/Documents/GitHub/FACULTAD-FCEFN/IA/clips/repasoclips/practicabasica.clp")

;;; Archivo de práctica básica para CLIPS
;;; Este archivo contiene ejemplos básicos para practicar con CLIPS

;;; SECCIÓN 1: HECHOS SIMPLES Y DEFFACTS
;;; Definición de hechos iniciales que se cargarán automáticamente con (reset)
(deffacts hechos-iniciales
   (color rojo)
   (color azul)
   (color verde)
   (fruta manzana)
   (fruta naranja)
   (fruta uva)
   (numero 1)
   (numero 2)
   (numero 5)
   (numero 10)
)

;;; SECCIÓN 2: DEFINICIÓN DE TEMPLATES
;;; Plantilla para representar personas
(deftemplate persona
   (slot nombre)
   (slot edad (type INTEGER))
   (slot profesion (default "desconocida"))
   (multislot hobbies)
)

;;; Plantilla para representar productos
(deftemplate producto
   (slot nombre)
   (slot precio (type FLOAT))
   (slot stock (type INTEGER))
   (slot categoria)
)

;;; SECCIÓN 3: HECHOS INICIALES CON TEMPLATES
(deffacts personas-iniciales
   (persona (nombre "Juan") (edad 25) (profesion "Ingeniero") (hobbies futbol natacion lectura))
   (persona (nombre "Maria") (edad 30) (profesion "Medica") (hobbies pintura musica viajes))
   (persona (nombre "Carlos") (edad 40) (profesion "Profesor") (hobbies cine lectura))
)

(deffacts productos-iniciales
   (producto (nombre "Laptop") (precio 1200.50) (stock 10) (categoria "Electronica"))
   (producto (nombre "Smartphone") (precio 800.75) (stock 15) (categoria "Electronica"))
   (producto (nombre "Mesa") (precio 350.00) (stock 5) (categoria "Muebles"))
)

;;; SECCIÓN 4: REGLAS BÁSICAS
;;; Regla para identificar colores
(defrule identificar-color
   (color ?c)
   =>
   (printout t ?c " es un color." crlf)
)

;;; Regla para sumar números
(defrule sumar-numeros
   (numero ?n1)
   (numero ?n2&:(> ?n2 ?n1))
   =>
   (bind ?suma (+ ?n1 ?n2))
   (printout t "La suma de " ?n1 " y " ?n2 " es " ?suma crlf)
)

;;; SECCIÓN 5: REGLAS CON TEMPLATES
;;; Regla para identificar personas jóvenes
(defrule persona-joven
   (persona (nombre ?nombre) (edad ?edad&:(< ?edad 30)))
   =>
   (printout t ?nombre " es una persona joven de " ?edad " años." crlf)
)

;;; Regla para identificar productos con bajo stock
(defrule producto-stock-bajo
   (producto (nombre ?nombre) (stock ?s&:(< ?s 10)))
   =>
   (printout t "¡Alerta! El producto " ?nombre " tiene stock bajo: " ?s " unidades." crlf)
)

;;; SECCIÓN 6: REGLAS CON PATRONES COMPLEJOS
;;; Regla para identificar personas con hobby de lectura
(defrule persona-lee
   (persona (nombre ?nombre) (hobbies $? lectura $?))
   =>
   (printout t ?nombre " tiene como hobby la lectura." crlf)
)

;;; Regla para encontrar productos electrónicos caros
(defrule electronica-cara
   (producto (nombre ?nombre) (precio ?p&:(> ?p 1000)) (categoria "Electronica"))
   =>
   (printout t ?nombre " es un producto electrónico caro." crlf)
)

;;; SECCIÓN 7: FUNCIÓN PERSONALIZADA
;;; Función para calcular el descuento de un producto
(deffunction calcular-descuento (?precio ?porcentaje)
   (bind ?descuento (* ?precio (/ ?porcentaje 100)))
   (bind ?precio-final (- ?precio ?descuento))
   (return ?precio-final)
)

;;; SECCIÓN 8: REGLA QUE USA FUNCIÓN PERSONALIZADA
(defrule aplicar-descuento
   (producto (nombre ?nombre) (precio ?precio))
   =>
   (bind ?precio-con-descuento (calcular-descuento ?precio 10))
   (printout t "El precio de " ?nombre " con 10% de descuento es: $" ?precio-con-descuento crlf)
)

;;; Mensaje para indicar que el archivo se ha cargado correctamente
(printout t "Archivo practicabasica.clp cargado correctamente!" crlf)
(printout t "Ejecuta (reset) para cargar los hechos iniciales" crlf)
(printout t "Ejecuta (run) para activar las reglas" crlf)