from collections import deque

cola_paciente = deque()

def agregar_paciente():
    nombre = input("Ingrese el nombre del paciente: ").strip()
    if nombre:
        cola_paciente.append(nombre)
        print(f" '{nombre}' agregado a la cola.\n")
    else:
        print("Nombre ingresado incorrecto.")

def Atender_Paciente():
    if cola_paciente:
        paciente = cola_paciente.popleft()
        print(f"Atendiendo paciente: {paciente}")
    else:
        print("No paciente encontrado en la cola.")

