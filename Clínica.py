from collections import deque

cola_paciente = deque()

def agregar_paciente():
    nombre = input("Ingrese el nombre del paciente: ").strip()
    if nombre:
        cola_paciente.append(nombre)
        print(f"✅ '{nombre}' agregado a la cola.\n")

