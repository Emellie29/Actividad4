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

def Mostrar_Colar():
    if cola_paciente:
        print(f"Cola actual de pacientes: ")
        for i, paciente in enumerate(cola_paciente, start=1):
            print(f"{i}. {paciente}")
            print()
        else:
            print("la cola esta vacia")

            def menu():
                while True:
                    print("🧾 Menú de Recepción")
                    print("1️⃣ Agregar paciente")
                    print("2️⃣ Atender paciente")
                    print("3️⃣ Mostrar cola")
                    print("4️⃣ Salir")

                    opcion = input("Seleccione una opción (1-4): ").strip()

                    if opcion == "1":
                        agregar_paciente()
                    elif opcion == "2":
                        atender_paciente()
                    elif opcion == "3":
                        mostrar_cola()
                    elif opcion == "4":
                        print("👋 Saliendo del programa.")
                        break
                    else:
                        print("❌ Opción inválida. Intente nuevamente.\n")

            if __name__ == "__main__":
                menu()
