-- Crear la base de datos
CREATE DATABASE BasculaBano;

USE BasculaBano;

CREATE TABLE Usuario (
    idUsuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT,
    email VARCHAR (100) NOT NULL, 
    altura DECIMAL(5, 2) -- Altura en m
);

CREATE TABLE Mediciones (
    idMedicion INT AUTO_INCREMENT PRIMARY KEY,
    idUsuario INT,
    fecha DATE NOT NULL,
    peso DECIMAL(5, 2), -- Peso en kg
    FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario)
);
INSERT INTO Usuario (idUsuario, nombre, email, edad, altura)
VALUES 
(1, 'Juan Perez', 'juan@example.com', 30, 1.75),
(2, 'Maria Lopez', 'maria@example.com', 28, 1.60),
(3, 'Carlos Gomez', 'carlos@example.com', 35, 1.80);
INSERT INTO Mediciones (idMecicion,idUsuario, fecha, peso)
VALUES
(1, 2, 01-02-2024, 65),
(2, 2, 02-03-2024, 64),
(3, 1, 05-04-2024, 75);




SELECT idUsuario, edad FROM Usuario;

