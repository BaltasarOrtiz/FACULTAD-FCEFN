
; (load "C:/Users/balta/Documents/GitHub/FACULTAD-FCEFN/IA/clips/repasoclips/e1.clp")

(deftemplate numeros
    (multislot lista)
)

(defrule inicializar-numeros
    =>
    (assert (numeros (lista 1 2 3 4 5 6 7 8 9 10)))
)

(defrule procesar-numeros
    (numeros (lista $?lista))
    =>
    (bind ?suma 0)
    (bind ?contador 0)

    (foreach ?num ?lista
        (if (numberp ?num)
        then
            (bind ?suma (+ ?suma ?num))
            (bind ?contador (+ ?contador 1))
        )
    )

    (if (> ?contador 0)
        then
        (bind ?promedio (/ ?suma ?contador))
        (printout t "La suma es " ?suma " y el promedio es " ?promedio crlf)
        else
        (printout t "No se encontraron números" crlf)
    )
)