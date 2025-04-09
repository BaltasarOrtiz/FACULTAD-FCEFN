; Item3

(defrule hechos
   =>
	(assert (mujer Ana))
	(assert (mujer Susana))
	(assert (mujer Carolin))
	(assert (mujer Maria))

	(assert (hombre Luis))
   (assert (hombre David))
   (assert (hombre Tomas))
	(assert (hombre Juan))
   (assert (hombre Pedro))

   (assert (madre-de Ana Susana))
   (assert (madre-de Carolin Tomas))
   (assert (madre-de Maria Juan))

   (assert (padre-de Luis Susana))
   (assert (padre-de David Tomas))
   (assert (padre-de Tomas Pedro))
   (assert (padre-de Tomas Juan))

   (assert (madre-de Ana Susana))
   (assert (madre-de Carolin Tomas))
   (assert (madre-de Susana Juan))
   (assert (madre-de Maria Pedro))

   (assert (casados Ana Luis))
   (assert (casados Susana Tomas))
   (assert (casados Carolin David))
)

(defrule abuelos
   ?x <- (madre-de ?y ?z)
   ?y <- (madre-de ?a ?b)
   =>
   (assert (abuela-de ?x ?a))
   (assert (abuela-de ?x ?b))
   printout t "La madre de " ?y " es la abuela de " ?x crlf
)

; "C:/Users/balta/Documents/GitHub/FACULTAD-FCEFN/IA/clips/practico/item3.clp"