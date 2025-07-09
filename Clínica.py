class Farmacia:
    def __init__(self):
        self.pila_medicamentos = []
    def agregar_medicamento(self, medicamento):
        self.pila_medicamentos.append(medicamento)
        print(f"Medicamento '{medicamento}' agregado con éxito.")
    def entregar_medicamento(self):
        if self.pila_medicamentos:
            medicamento = self.pila_medicamentos.pop()
            print(f"Medicamento entregado: '{medicamento}'")
        else:
            print("No hay medicamentos para entregar.")
            def mostrar_pila(self):
                if self.pila_medicamentos:
                    print("Listado actual de medicamentos (de abajo hacia arriba):")
                    for i, med in enumerate(self.pila_medicamentos): print(f"{i + 1}. {med}")
                else:
                    print("La lista de medicamentos está vacía.")
  # Menú de elección
        def menu():
            farmacia = Farmacia()
            while True:
                print("******Menú de farmacia******")
                print("1 Agregar medicamento")
                print("2 Entregar medicamento")
                print("3 Mostrar medicamentos actuales")
                print("4 Salir")
                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    nombre = input("Ingrese el medicamento: ")
                    farmacia.agregar_medicamento(nombre)
                elif opcion == "2":
                    farmacia.entregar_medicamento()
                elif opcion == "3":
                    farmacia.mostrar_pila()
                elif opcion == "4":
                    print("Cerrando el programa.")
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
            if __name__ == "__main__":
                menu()
