#texto = "Este es el texto de Federico"

#resultado = texto[2].upper()
#resultado = texto.lower()
#resultado = texto.split() #Toma como separados los espacios vacios
#resultado = texto.find("s")#En vez de index esto me da un -1 
#resultado = texto.find("Federico")
#resultado = texto.replace("e","x")
#si no encuentra el resultado

#print(resultado)

# a = "Aprender"
# b = "Python"
# c = "es"
# d = "genial"
# e = " ".join([a,b,c,d])
# print(e)

# frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
# resultado = frase.upper()
# print(resultado)
# lista_palabras = ["La","legibilidad","cuenta."]
# resultado = " ".join(lista_palabras)
# print(resultado)

# frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
# resultado = frase.replace("difícil","fácil")
# resultado = frase.replace("mala","buena")
# print(resultado)

#Concatenable
# mi_texto = "hola"+"mundo"
# Multipicable
# mi_texto = "hola"*5
#holaholaholaholahola
# multilineales
# mi_texto = "hola \nmundo"
# mi_texto = """"hola
# mundo"""

# verificar si contiene
# mi_texto = "hola mundo"
# print("hola" in mi_texto) True o False
# len(mi_texto) largo

# nombre = "Carina"
# nombre = "Karina"
#nombre[0] = "K"
#"TypeError": 'str' object does not support item assignment
#Los Strings son inmutables , se puede re asignar, pueden variar = variable

# n1 = "Kari"
# n2 = "na"
# print(n1 * 10)
# poema = """Mil pequeños peces blancos
# como si hirviera
# el color del agua"""
# print("agua" in poema)
# print("sol" not in poema)
# print(len(poema))

# frase = "Repetición"
# fraseMultiplicada = frase * 15
# print(fraseMultiplicada)

# haiku = """Tierra mojada
# mis recuerdos de viaje,
# entre las lluvias"""
# resultado = "no" not in haiku
# print(resultado)

frase = "electroencefalografista"
resultado = len(frase)
print(resultado)