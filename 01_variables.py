### Variables ###

my_string_variable = 'My str variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable) 

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True 
print(my_bool_variable) 

# Concatenación de variables en un print
print(my_string_variable, str(my_int_variable), my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# AlgunasFunciones del sistema
print(len(my_string_variable))

# Variables en una sola línea. ¡No abusar de esta sintaxis!
name, surname, alias, age = "Pepe", "Perez", "pepito", 25
print("Me llamo:", name, surname, "Y mi edad es:", age, "Y mi alias es:", alias)

# Inputs
"""
name = input("¿Cual es tu nombre?: ")
age = input("¿Cual es tu edad?: ")
print(name)
print(age)
"""

# Cambiamos su tipo
name = 25
age = "Pepe" 
print(name)
print(age)

# ¿Forzamos el tipo?
adrress: str = "Calle Falsa"
adrress = 12
adrress = True
adrress = 12.5
print(type(adrress))
