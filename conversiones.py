import sys

#Variables
sol_peruano = float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar_americano = float(sys.argv[3])
pesos_clp = int(sys.argv[4])

#Transformacion
conv_soles = pesos_clp * sol_peruano
conv_arg = pesos_clp * peso_argentino
conv_dolar = pesos_clp * dolar_americano

#Resultados
print(f'''
Los {pesos_clp} pesos equivalen a:
{conv_soles} Soles
{conv_arg} Pesos Argentinos
{conv_dolar} Dólares''')