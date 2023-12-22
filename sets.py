#son una coleccion de elementos al igual que las listas
#pero con algunas diferencias que los hacen muy particulares
#declarar de dos
#set (1,2,3,4,5,6) o usando llaves sin usar la palabra set {1,2,3,4,5,6}
#si se escribe con set solo permite un solo argumento por ende
#debes pasar tus argumentos con corchetes set ([1,2,3,4,5,6])
#sin set y con llaves puedes poner todos tus elementos directamente
#En un set los elementos no se repiten
#Si agregas un valor repetido python automaticamente lo descarta
#No estan ordenados en indices
#Los sets no pueden contener listas y diccionarios

#mi_set = set([1,2,3,4,5])
#mi_set = set((1,2,3,4,5))
#print(mi_set)

# otro_set = {1,2,3}
# print(otro_set)
#mi_set = set((1,2,3,4,5,(1,2,3,4),1,1,1,1,2,2,2))
# print(type(mi_set))
# print(mi_set)
#mi_set = set((1,2,3,4,5))
#print(len(mi_set))
#print(2 in mi_set)#Return True o False
#Si hay elementos repetidos los omite
#Recordar que no se pueden añadir listas
#Acepta tuples porque los tuples son inmutables
#Si fuera algo que se pueda cambiar no tendria sentido

#s1 = {1,2,3}

# s1.add(4)
# print(s1)
# s1.remove(4)
# print(s1)

#discard funciona igual que remove con la diferencia de 
# si le pido que descarte un elemento que  no existe
# no me dara error, solo continua
#s1.discard(6)
#s1.pop() #En tuples pop elmina un elemento de forma aleatoria
#No recomendado
# print(s1)

#s1.clear() #Vacia a nuestro set

# s2 = {3,4,5}
# s3 = s1.union(s2)
# print(s3)

# mi_set_1 = {1, 2, "tres", "cuatro"}
# mi_set_2 = {"tres", 4, 5} 
# mi_set_3 = mi_set_1.union(mi_set_2)
# print(mi_set_3)

# sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
# print(sorteo.pop())
# print(sorteo)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
print(sorteo.add("Damián"))
print(sorteo)
