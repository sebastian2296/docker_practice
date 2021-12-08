def invertir(cadena):
	texto_final = []
	for letter in list(cadena):
		if letter.isupper():
			texto_final.append(letter.lower())
		else:
			texto_final.append(letter.upper())


	return "".join(texto_final)


def app():
	cadena = input('What String would you like to invert?: ')

	try:
		
		cadena = float(cadena)
		print("Sorry, that's not a string. Try again.")
		app()

	except:

		if isinstance(cadena, str):
			prueba = invertir(cadena=cadena)
			print(prueba)


app()