from collections import deque

# Crear una cola FIFO de pacientes
cola_pacientes = deque()

# Función para agregar un paciente a la cola
def agregar_paciente(nombre):
    cola_pacientes.append(nombre)
    print(f"Paciente '{nombre}' ha sido agregado a la cola.")

# Función para atender al siguiente paciente
def atender_paciente():
    if cola_pacientes:
        paciente_atendido = cola_pacientes.popleft()
        print(f"Atendiendo al paciente: {paciente_atendido}")
    else:
        print("No hay pacientes en la cola.")

# Función para mostrar la cola actual
def mostrar_cola():
    if cola_pacientes:
        print("Cola actual de pacientes:")
        for i, paciente in enumerate(cola_pacientes, start=1):
            print(f"{i}. {paciente}")
    else:
        print("La cola está vacía.")

# Ejemplo de uso
agregar_paciente("Ana")
agregar_paciente("Luis")
mostrar_cola()
atender_paciente()
mostrar_cola()