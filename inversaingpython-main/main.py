ice_creams = []  # Lista para almacenar los helados
id_counter = 1  # Contador para asignar IDs únicos

while True:
    print("\nGestión de Helados")
    print("1. Agregar un helado")
    print("2. Ver lista de helados")
    print("3. Modificar un helado")
    print("4. Eliminar un helado")
    print("5. Salir")
    
    option = input("Seleccione una opción: ")
    
    if option == "1":  # Agregar un helado
        name = input("Ingrese el nombre del helado: ")
        description = input("Ingrese la descripción del helado: ")
        price_input = input("Ingrese el precio del helado: ")
        
        if price_input.isdigit():
            price = float(price_input)
            ice_cream = {"id": id_counter, "name": name, "description": description, "price": price}
            ice_creams.append(ice_cream)
            id_counter += 1
            print("Helado agregado correctamente.")
        else:
            print("Error: El precio debe ser un número.")
    
    elif option == "2":  # Ver lista de helados
        if len(ice_creams) == 0:
            print("No hay helados registrados.")
        else:
            print("\nLista de Helados:")
            for ice_cream in ice_creams:
                print(f"ID: {ice_cream['id']}, Nombre: {ice_cream['name']}, Descripción: {ice_cream['description']}, Precio: ${ice_cream['price']}")
    
    elif option == "3":  # Modificar un helado
        id_modify = input("Ingrese el ID del helado a modificar: ")
        
        if id_modify.isdigit():
            id_modify = int(id_modify)
            found = False
            
            for ice_cream in ice_creams:
                if ice_cream["id"] == id_modify:
                    new_name = input("Nuevo nombre (deje en blanco para no cambiar): ")
                    new_description = input("Nueva descripción (deje en blanco para no cambiar): ")
                    new_price = input("Nuevo precio (deje en blanco para no cambiar): ")
                    
                    if new_name:
                        ice_cream["name"] = new_name
                    if new_description:
                        ice_cream["description"] = new_description
                    if new_price.isdigit():
                        ice_cream["price"] = float(new_price)
                    
                    print("Helado modificado correctamente.")
                    found = True
                    break
            
            if not found:
                print("Error: No se encontró un helado con ese ID.")
        else:
            print("Error: El ID debe ser un número.")
    
    elif option == "4":  # Eliminar un helado
        id_delete = input("Ingrese el ID del helado a eliminar: ")
        
        if id_delete.isdigit():
            id_delete = int(id_delete)
            found = False
            
            for ice_cream in ice_creams:
                if ice_cream["id"] == id_delete:
                    ice_creams.remove(ice_cream)
                    print("Helado eliminado correctamente.")
                    found = True
                    break
            
            if not found:
                print("Error: No se encontró un helado con ese ID.")
        else:
            print("Error: El ID debe ser un número.")
    
    elif option == "5":  # Salir
        print("Saliendo del programa...")
        break