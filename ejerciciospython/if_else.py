def venderalcohol(edad):

	if edad >= 18 : 

		return "Puede comprar alcohol"

	else:

		return "No puede comprar alcohol"


print (venderalcohol(19))

print (venderalcohol(14))



def saludar(nombre):

	nombreMinuscula = nombre.lower()

	if nombreMinuscula == "juan" :

		return "Hola"

	else:

		return "No te conozco"

print (saludar("JuAn"))