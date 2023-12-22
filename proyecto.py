texto = input("Por favor ingrese un texto: ")
texto = texto.lower()
#a = input("Por favor ingrese una letra: ")
#b = input("Por favor ingrese una letra: ")
#c = input("Por favor ingrese una letra: ")

resultado = texto.split()
#valorFinalLargo = len(resultado)
#valorFinalAlRevez = resultado.reverse()
#print(valorFinalLargo)
#print(f"La primera letra de mis elementos es: {resultado[0][0]}")
#print(f"La ultima letra de mis elementos es: {resultado[-1][-1]}")


#Existen dos forma de invertir esto
#Primero con reverse
#resultado.reverse()
#print(resultado)

#El otro slicing
mi_lista_invertida = resultado[::-1]
print(mi_lista_invertida)

existe = "python" in resultado
print(existe)

#letras = a,b,c

#encontradosA = texto.count(a)
#encontradosB = texto.count(b)
#encontradosC = texto.count(c)
#print(encontradosA)
#print(encontradosB)
#print(encontradosC)

#1 Cuantas veces aparece cada letra

