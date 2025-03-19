class Fruta:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}: ${self.precio:.2f}"

class Salpicon:
    def __init__(self):
        self.frutas = []

    def agregar_frutas(self):
        for _ in range(10):
            nombre = input("Ingrese el nombre de la fruta: ")
            while True:
                try:
                    precio = float(input(f"Ingrese el precio de {nombre}: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un precio válido.")
            self.frutas.append(Fruta(nombre, precio))

    def listar_frutas(self):
        if not self.frutas:
            print("No hay frutas registradas.")
            return
        print("\nLista de frutas:")
        for i, fruta in enumerate(self.frutas, 1):
            print(f"{i}. {fruta}")

    def actualizar_frutas(self):
        for i, fruta in enumerate(self.frutas):
            print(f"{i + 1}. {fruta}")
            nombre = input("Ingrese el nuevo nombre de la fruta: ")
            while True:
                try:
                    precio = float(input(f"Ingrese el nuevo precio de {nombre}: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un precio válido.")
            self.frutas[i] = Fruta(nombre, precio)

    def eliminar_frutas(self):
        for i, fruta in enumerate(self.frutas):
            print(f"{i + 1}. {fruta}")
        indices = input("Ingrese los números de las frutas a eliminar (separados por espacio): ").split()
        for index in sorted([int(i) - 1 for i in indices], reverse=True):
            if 0 <= index < len(self.frutas):
                self.frutas.pop(index)
        print("Frutas eliminadas correctamente.")

    def ordenar_frutas(self):
        for i in range(len(self.frutas) - 1):
            for j in range(i + 1, len(self.frutas)):
                if self.frutas[i].precio < self.frutas[j].precio:
                    self.frutas[i], self.frutas[j] = self.frutas[j], self.frutas[i]
        print("\nFrutas ordenadas de mayor a menor precio:")
        self.listar_frutas()

def menu():
    salpicon = Salpicon()
    while True:
        print("\n--- Menú de Frutas ---")
        print("1. Agregar 10 frutas")
        print("2. Listar frutas")
        print("3. Actualizar frutas")
        print("4. Eliminar frutas")
        print("5. Ordenar frutas por precio")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            salpicon.agregar_frutas()
        elif opcion == "2":
            salpicon.listar_frutas()
        elif opcion == "3":
            salpicon.actualizar_frutas()
        elif opcion == "4":
            salpicon.eliminar_frutas()
        elif opcion == "5":
            salpicon.ordenar_frutas()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()
