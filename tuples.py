#Los tuples son una coleccion de elementos muy similar
#a las listas pero con una diferencia , SON INMUTABLES
#Una vez que un elemento fue asignado a un tuple no 
#puede cambiarse ni re asignarse

#Ocupan menos espacio (eficiencia)
#Se procesan mas rapido que las listas

#Al no ser modificada son a prueba de daños
#Cuando queremos estructuras que no sean modificadas

# mi_tuple = (1,2,(10,20),4)
# mi_tuple = list(mi_tuple)
t = (1,2,3,1,1)

v,w,x,y,z = t

#print(len(t))
#print(t.count(1))
print(t.index(2))

#print(x,y,z) #Solo si los valores coinciden

#print(mi_tuple[2][0])


#mi_tuple[0] = 5 #No me deja , son inmutables
#t = (5,5.6,'ff') #Pueden tener todos los elementos
#print(mi_tuple[0])
# print(mi_tuple[-2])

# mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
# print(mi_tupla.count(2))

# mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
# mi_lista = list(mi_tupla)

mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla