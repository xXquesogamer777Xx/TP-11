-- Crear base de datos
CREATE DATABASE Biblioteca;

-- Usar la base de datos creada
USE Biblioteca;

-- Tabla de Autores
CREATE TABLE Autores (
    id_autor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE
);

-- Tabla de Géneros
CREATE TABLE Generos (
    id_genero INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

-- Tabla de Libros
CREATE TABLE Libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    id_autor INT,
    id_genero INT,
    fecha_publicacion DATE,
    FOREIGN KEY (id_autor) REFERENCES Autores(id_autor),
    FOREIGN KEY (id_genero) REFERENCES Generos(id_genero)
);
