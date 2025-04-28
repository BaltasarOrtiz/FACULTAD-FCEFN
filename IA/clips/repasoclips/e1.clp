; Sistema de Inventario Simple
;   Crea un template para productos con nombre, precio, cantidad y categoría
; Implementa reglas para:
;   Identificar productos con stock bajo (menos de 5 unidades)
;   Calcular el valor total del inventario (precio × cantidad)
;   Listar productos por categoría

(deftemplate producto
   (slot nombre (type STRING))
   (slot precio (type FLOAT))
   (slot cantidad (type INTEGER))
   (slot categoria (type STRING))
)

(defrule inicializarProductos
    => 
    (assert (producto (nombre "Producto A") (precio 10.0) (cantidad 20) (categoria "Categoria 1")))
    (assert (producto (nombre "Producto B") (precio 5.0) (cantidad 3) (categoria "Categoria 2")))
    (assert (producto (nombre "Producto C") (precio 15.0) (cantidad 10) (categoria "Categoria 1")))
    (assert (producto (nombre "Producto D") (precio 8.0) (cantidad 0) (categoria "Categoria 3")))
)

(defrule stockBajo
    (producto (nombre ?nombre) (precio ?precio) (cantidad ?cantidad) (categoria ?categoria))
    (test (< ?cantidad 5)) 
    =>
    (printout t "El producto " ?nombre " tiene stock bajo: " ?cantidad " unidades restantes." crlf)
)