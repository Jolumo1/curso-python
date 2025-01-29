###
# soluciones.py
# Soluciones a los ejercicios del archivo exercises.py
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

# Solución:
nombre = "Carlos"  # Reemplázalo con tu nombre
ciudad = "Buenos Aires"  # Reemplázalo con tu ciudad

print(nombre)
print(ciudad)

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")

# Variables dadas en el enunciado
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

# Solución:
print("Tipo de a:", type(a))
print("Tipo de b:", type(b))
print("Tipo de c:", type(c))
print("Tipo de d:", type(d))
print("Tipo de e:", type(e))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena '12345' a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

# Solución:
cadena = "12345"
numero_entero = int(cadena)  # Convertir cadena a entero
numero_float = float(numero_entero)  # Convertir entero a float

print("Número entero:", numero_entero)
print("Número como float:", numero_float)

float_num = 3.99
entero_convertido = int(float_num)  # Se trunca el decimal

print("Float original:", float_num)
print("Float convertido a entero (se trunca la parte decimal):", entero_convertido)

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# Solución:
nombre = "midudev"
edad = 18
altura = 1.90

# Imprimir presentación con f-string
print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

# Solución:
# Redondeamos directamente el valor de pi sin almacenarlo en una variable
resultado = int(round(3.1416) / 2)
print("Valor de PI (aproximado):", 3.1416)
print("PI redondeado:", round(3.1416))
print("División entera de PI redondeado entre 2:", resultado)
