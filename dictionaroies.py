#mi_dic = {'c1':'valor1','c2':'valor2','c3':'valor3'} #No tienen indice
#No importa el orden
#Si podemos acceder a traves de su llave
#Llave no se pued erepetir, valores si
#diccionario = {'c1':'valor1','c2':'valor2'}
#print(diccionario)

#resultado = diccionario['c1']

#print(resultado)
#Los dict pueden tener todo tipo de datos
# cliente = {
#         'nombre':'Juan',
#         'apellido':'Fuentes',
#         'peso':88,
#         'talla':1.76}
# consulta = cliente['apellido']
# print(consulta)
# dic = {
#     'c1':55,
#     'c2': [10,20,30],
#     'c3':{'s1':100,'s2':200}
#     }
#Imprime lo que sea que haya en el diccionario en su clave 2
#y dentro de eso en su llave 1
#print(dic['c2'][1])#Para consultar listas dentro de un dic
#print(dic['c3']['s2'])
# dic = {'c1':['a','b','c'],'c2':['d','e','f']}
# resultado = dic['c2'][1].upper()
# print(resultado)
# dic = {1:'a',2:'b'}
# print(dic)

# mi_dict = {
#     "valores_1":{
#         "v1":3,
#         "v2":6
#     },
#     "puntos":{
#         "points1":9,
#         "points2":[10,300,15]
#         }
#     }
# print(mi_dict["puntos"]["points2"][1])

mi_dic = {
    "nombre":"Karen", 
    "apellido":"Jurgens", 
    "edad":35, 
    "ocupacion":"Periodista"
}
mi_dic["edad"] = 36 #Modifica
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"] = 'Colombia' #Agrega

print(mi_dic)

# dic[3] = 'c' #==> Agrega

# print(dic)

#dic[2] = 'B' #==> Sobre escribe

# print(dic)

# print(dic.keys()) #==> Todas las llaves que tiene

# print(dic.values()) #==> Solo los valores

# print(dic.items()) # ==> Todo lo del diccionario

# mi_dic = {
#     "nombre" : "Karen",
#     "apellido" : "Jurgens",
#     "edad" : 35,
#     "ocupacion" : "Periodista"
# }

