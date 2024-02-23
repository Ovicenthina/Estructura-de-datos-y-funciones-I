import sys

#Manejo de error
if len(sys.argv)!=2:
    print('Por favor, proporcionar el nombre del archivo como argumento.')
    sys.exit(1)

#definicion de variable
archivo = sys.argv[1]

with open (f"{archivo}", "r", encoding="utf-8") as file:
    texto =file.read()

#Calculo
contar_caracteres = len(set(texto))
contar_palabras = len(set(texto.split(" ")))

#Resultados
print(f'El número de caracteres distintos es: {contar_caracteres}')
print(f'El número de palabras distintas es: {contar_palabras}')