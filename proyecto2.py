texto = input("Ingresa un texto a elección: ")
letras = [] #Creo mi lista vacia

texto = texto.lower()

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
#Cantidad de letras que haya en mi texto en el indice 0
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])
print(f"Cantidad de veces {letras[0]} en mi texto es : {cantidad_letras1}")
print(f"Cantidad de veces {letras[1]} en mi texto es : {cantidad_letras2}")
print(f"Cantidad de veces {letras[2]} en mi texto es : {cantidad_letras3}")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]# Primer indice
letra_final = texto[-1]#con este el uyltimo
#Es mas sencillo porque ni siquiera lo transformo a lista, es un string
#Entonces le pregunto por la primera posición y con -1 por la ultima
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al revés va a decir {texto_invertido}")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic = { True:"si",False:"no" }
print(f"La palabra 'Python' { dic[buscar_python] } se encuentra en el texto")