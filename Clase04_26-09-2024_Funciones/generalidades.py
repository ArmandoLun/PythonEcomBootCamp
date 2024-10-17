def sumar(x,y):
    return x+y

suma_lambda = lambda x,y: x+y

suma1 = sumar(5,2)
suma2 = suma_lambda(5,2)

print(suma1)
print(suma2)

lista_valores = [2,4,5,7,8,9,10,3,12]
nueva_lista = []
print("lista_valores",lista_valores)
for elementos in lista_valores:
    nueva_lista.append(elementos*2)
print("nueva_lista",nueva_lista)

#Lista por comprension
nueva_lista2 = [el*2 for el in lista_valores if el>2]
print(nueva_lista2)

# map, aplica una funcion a todos los elemntos de un objeto iterable
nueva_valores_map = map(lambda x: x*2, lista_valores)
print("nueva_valores_map",nueva_valores_map)
print("nueva_valores_map casteado:",list(nueva_valores_map))

# filter, filtra por una condicion en una funcion
nueva_valores_filter = filter(lambda x: x%2 == 0,lista_valores)
print("nueva_valores_filter:",nueva_valores_filter)
print("nueva_valores_filter:",list(nueva_valores_filter))

# reduce, a partir de una lista combina todos los valores en un solo valor
from functools import reduce
nueva_valores_reduce = reduce(lambda x,y: x+y, lista_valores)
