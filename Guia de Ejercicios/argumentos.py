import sys

nombre = sys.argv[1]
apellido = sys.argv[2]
edad = sys.argv[3]
ciudad = sys.argv[4]

print(f'Mi nombre es {nombre}')
print(f'Mi apellido es {apellido}')
print(f'Mi edad es {edad}')
print(f'Vivo en {ciudad}')
print(f'El nombre se este archivo es {sys.argv[0]}')

print(type(sys.argv))