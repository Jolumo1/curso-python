inventario_dinosaurios = [
    ("Rexy", "Tyrannosaurus Rex", 1, "Saludable"),
    ("Blue", "Velociraptor", 2, "Saludable"),
    ("Charlie", "Velociraptor", 2, "Necesita Atención"),
    ("Delta", "Velociraptor", 2, "Saludable"),
    ("Echo", "Velociraptor", 2, "Saludable"),
    ("Braquiosaurio_1", "Braquiosaurio", 3, "Saludable"),
    ("Triceratops_1", "Triceratops", 4, "Saludable"),
    ("Spino", "Spinosaurus", 5, "Necesita Atención"),
    ("Pterodáctilo_1", "Pterodáctilo", 6, "Saludable"),
    ("Rexy_Junior", "Tyrannosaurus Rex", 1, "Necesita Atención"),
]

print("--- Informe del Inventario de Dinosaurios de Jurassic Park ---")

# 1. Contar el número total de dinosaurios
total_dinosaurios = 0
for dinosaurio in inventario_dinosaurios:
    total_dinosaurios += 1 # Incrementa el contador por cada dinosaurio en la lista
print(f"\nNúmero total de dinosaurios en el parque: {total_dinosaurios}")

# 2. Identificar y listar los nombres de todos los Velociraptors
velociraptors_list = []
for dinosaurio in inventario_dinosaurios:
    if dinosaurio[1] == "Velociraptor": # Comprueba si la especie (índice 1) es "Velociraptor"
        velociraptors_list.append(dinosaurio[0]) # Añade el nombre (índice 0) a la lista
print(f"\n--- Listado de Velociraptors ---")
print(f"Velociraptors encontrados: {velociraptors_list}")

# 3. Determinar cuántos dinosaurios necesitan atención médica
dinosaurios_necesitan_atencion = 0
for dinosaurio in inventario_dinosaurios:
    if dinosaurio[3] == "Necesita Atención": # Comprueba si el estado de salud (índice 3) es "Necesita Atención"
        dinosaurios_necesitan_atencion += 1 # Incrementa el contador
print(f"\n--- Dinosaurios que necesitan atención médica ---")
print(f"Número de dinosaurios que necesitan atención médica: {dinosaurios_necesitan_atencion}")

# 4. Simular una "inspección de recinto" para el Recinto 2
def inspeccionar_recinto(recinto_numero):
    print(f"\n--- Inspección del Recinto {recinto_numero} ---")
    print(f"Dinosaurios en el Recinto {recinto_numero}:")
    for dinosaurio in inventario_dinosaurios:
        if dinosaurio[2] == recinto_numero: # Comprueba si el recinto (índice 2) coincide con el recinto_numero dado
            print(f"- Nombre: {dinosaurio[0]}, Estado: {dinosaurio[3]}")

inspeccionar_recinto(2) # Llama a la función para inspeccionar el Recinto 2