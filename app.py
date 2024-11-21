import mysql.connector

# Configuración de la conexión
def conectar():
    return mysql.connector.connect(
        host="localhost",      # O cambia a la IP de tu servidor de base de datos si no está en localhost
        user="tu_usuario",     # Usa tu usuario de MySQL
        password="tu_contraseña",  # Usa tu contraseña de MySQL
        database="Biblioteca"  # El nombre de la base de datos que creaste
    )

# Función para agregar un libro
def agregar_libro(titulo, id_autor, id_genero, fecha_publicacion):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO Libros (titulo, id_autor, id_genero, fecha_publicacion) VALUES (%s, %s, %s, %s)"
    valores = (titulo, id_autor, id_genero, fecha_publicacion)
    cursor.execute(query, valores)
    conexion.commit()
    print(f"Libro '{titulo}' agregado exitosamente.")
    conexion.close()

# Función para listar libros
def listar_libros():
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT Libros.id_libro, Libros.titulo, Autores.nombre, Generos.nombre, Libros.fecha_publicacion FROM Libros JOIN Autores ON Libros.id_autor = Autores.id_autor JOIN Generos ON Libros.id_genero = Generos.id_genero"
    cursor.execute(query)
    for libro in cursor.fetchall():
        print(libro)
    conexion.close()

# Función para actualizar título de un libro
def actualizar_titulo(id_libro, nuevo_titulo):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "UPDATE Libros SET titulo = %s WHERE id_libro = %s"
    valores = (nuevo_titulo, id_libro)
    cursor.execute(query, valores)
    conexion.commit()
    print(f"Libro ID {id_libro} actualizado exitosamente.")
    conexion.close()

# Función para eliminar un libro
def eliminar_libro(id_libro):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "DELETE FROM Libros WHERE id_libro = %s"
    valores = (id_libro,)
    cursor.execute(query, valores)
    conexion.commit()
    print(f"Libro ID {id_libro} eliminado exitosamente.")
    conexion.close()

# Menú principal de la aplicación
def menu():
    while True:
        print("\nGestión de Biblioteca")
        print("1. Agregar libro")
        print("2. Listar libros")
        print("3. Actualizar libro")
        print("4. Eliminar libro")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            id_autor = int(input("ID del Autor: "))
            id_genero = int(input("ID del Género: "))
            fecha_publicacion = input("Fecha de Publicación (YYYY-MM-DD): ")
            agregar_libro(titulo, id_autor, id_genero, fecha_publicacion)
        elif opcion == "2":
            listar_libros()
        elif opcion == "3":
            id_libro = int(input("ID del Libro a actualizar: "))
            nuevo_titulo = input("Nuevo título: ")
            actualizar_titulo(id_libro, nuevo_titulo)
        elif opcion == "4":
            id_libro = int(input("ID del Libro a eliminar: "))
            eliminar_libro(id_libro)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

# Ejecutar la aplicación
if __name__ == "__main__":
    menu()

