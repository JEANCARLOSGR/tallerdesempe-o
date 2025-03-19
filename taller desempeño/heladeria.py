import uuid  # Importamos la librería para generar identificadores únicos

class Heladeria:
    def __init__(self):
        # Inicializamos una lista vacía para almacenar los helados
        self.helados = []

    def generar_id(self):
        # Generamos un ID único para cada helado, usando los primeros 8 caracteres de un UUID
        return str(uuid.uuid4())[:8]

    def crear_helado(self):
        # Solicitamos el nombre del helado y validamos que no esté vacío
        nombre = input("Ingrese el nombre del helado: ").strip()
        while not nombre:
            nombre = input("El nombre no puede estar vacío. Ingrese el nombre del helado: ").strip()
        
        # Solicitamos la descripción del helado y validamos que no esté vacía
        descripcion = input("Ingrese la descripción del helado: ").strip()
        while not descripcion:
            descripcion = input("La descripción no puede estar vacía. Ingrese la descripción del helado: ").strip()
        
        # Solicitamos el precio y validamos que sea un número positivo
        while True:
            try:
                precio = float(input("Ingrese el precio unitario del helado: "))
                if precio <= 0:
                    raise ValueError("El precio debe ser un número positivo.")
                break
            except ValueError as e:
                print("Entrada inválida:", e)
        
        # Creamos un diccionario con los datos del helado y lo añadimos a la lista
        helado = {"id": self.generar_id(), "nombre": nombre, "descripcion": descripcion, "precio": precio}
        self.helados.append(helado)
        print("Helado agregado con éxito!\n")

    def ver_helados(self):
        # Mostramos la lista de helados registrados
        if not self.helados:
            print("No hay helados registrados.\n")
            return
        print("Lista de helados:")
        for h in self.helados:
            print(f"ID: {h['id']} | Nombre: {h['nombre']} | Descripción: {h['descripcion']} | Precio: ${h['precio']:.2f}")
        print()

    def modificar_helado(self):
        # Permite modificar los datos de un helado existente
        if not self.helados:
            print("No hay helados registrados para modificar.\n")
            return
        
        self.ver_helados()
        helado_id = input("Ingrese el ID del helado a modificar: ").strip()
        
        for i in range(len(self.helados)):
            if self.helados[i]["id"] == helado_id:
                # Permite modificar nombre y descripción, si el usuario deja vacío, mantiene el valor anterior
                self.helados[i]["nombre"] = input(f"Nuevo nombre ({self.helados[i]['nombre']}): ").strip() or self.helados[i]["nombre"]
                self.helados[i]["descripcion"] = input(f"Nueva descripción ({self.helados[i]['descripcion']}): ").strip() or self.helados[i]["descripcion"]
                while True:
                    try:
                        nuevo_precio = input(f"Nuevo precio (${self.helados[i]['precio']:.2f}): ").strip()
                        if nuevo_precio:
                            nuevo_precio = float(nuevo_precio)
                            if nuevo_precio <= 0:
                                raise ValueError("El precio debe ser positivo.")
                            self.helados[i]["precio"] = nuevo_precio
                        break
                    except ValueError as e:
                        print("Entrada inválida:", e)
                print("Helado modificado con éxito!\n")
                return
        print("ID no encontrado.\n")

    def eliminar_helado(self):
        # Permite eliminar un helado a partir de su ID
        if not self.helados:
            print("No hay helados registrados para eliminar.\n")
            return
        
        self.ver_helados()
        helado_id = input("Ingrese el ID del helado a eliminar: ").strip()
        
        for i in range(len(self.helados)):
            if self.helados[i]["id"] == helado_id:
                del self.helados[i]
                print("Helado eliminado con éxito!\n")
                return
        print("ID no encontrado.\n")

    def menu(self):
        # Muestra el menú principal del sistema de gestión de helados
        while True:
            print("\nMenú de Gestión de Helados:")
            print("1. Crear un helado")
            print("2. Ver lista de helados")
            print("3. Modificar un helado")
            print("4. Eliminar un helado")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == "1":
                self.crear_helado()
            elif opcion == "2":
                self.ver_helados()
            elif opcion == "3":
                self.modificar_helado()
            elif opcion == "4":
                self.eliminar_helado()
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Intente nuevamente.\n")

# Punto de entrada principal del programa
if __name__ == "__main__":
    heladeria = Heladeria()
    heladeria.menu()