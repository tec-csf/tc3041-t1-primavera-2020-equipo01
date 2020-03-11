-- Script para generar tablas en db2 

-- Partido
CREATE TABLE Partido(siglas VARCHAR(6) PRIMARY KEY NOT NULL, nombreCompleto VARCHAR(45) NOT NULL, nombrePresidente VARCHAR(45) NOT NULL, fecha_inicio DATE NOT NULL, fecha_final DATE NOT NULL, PERIOD BUSINESS_TIME(fecha_inicio, fecha_final))

CREATE UNIQUE INDEX index_presidente_partido ON Partido(nombreCompleto, BUSINESS_TIME WITHOUT OVERLAPS)

-- Colegio 
CREATE TABLE Colegio(numId INT PRIMARY KEY NOT NULL, cantElectores INT NOT NULL)


-- Mesa
CREATE TABLE Mesa(letra CHAR(1) PRIMARY KEY NOT NULL, numColegio INT NOT NULL, FOREIGN KEY(numColegio)REFERENCES Colegio(numId))

-- EleccionMunicipal
CREATE TABLE EleccionMunicipal(fechaElec DATE NOT NULL,letraMesa CHAR(1) NOT NULL, partidoSiglas VARCHAR(6) NOT NULL, cantVotos INT NOT NULL, cantVotosNulos INT NOT NULL, cantVotosBlancos INT NOT NULL, PRIMARY KEY(fechaElec, letraMesa, partidoSiglas), FOREIGN KEY(letraMesa) REFERENCES Mesa(letra), FOREIGN KEY(partidoSiglas) REFERENCES Partido(siglas))

-- EleccionNacional
CREATE TABLE EleccionNacional LIKE EleccionMunicipal

-- ListaMunicipal
CREATE TABLE ListaMunicipal(id VARCHAR(20) NOT NULL PRIMARY KEY, nombre VARCHAR(45) NOT NULL, posicion VARCHAR(45) NOT NULL, afiliacion VARCHAR(6) NOT NULL, FOREIGN KEY(afiliacion) REFERENCES Partido(siglas))

-- Apoderado
CREATE TABLE Apoderado(IFE VARCHAR(20) NOT NULL PRIMARY KEY, nombre VARCHAR(20) NOT NULL, afiliacion VARCHAR(6) NOT NULL, FOREIGN KEY(afiliacion) REFERENCES Partido(siglas))

-- Votante
CREATE TABLE Votante(pasaporte VARCHAR(9) NOT NULL, IFE varchar(20), nombre VARCHAR(45) NOT NULL, fechaNacimiento DATE NOT NULL, direccion VARCHAR(45) NOT NULL, mesaVotar CHAR(1) NOT NULL, afiliacion INT NOT NULL, NAC CHAR(1) NOT NULL, nacionalidad VARCHAR(45), POS CHAR(1), fechaEleccion DATE, idMiembro VARCHAR(45), idMesa CHAR(1), posicion VARCHAR(45), idSuplente VARCHAR(45), sustituye VARCHAR(9), fecha_inicio DATE NOT NULL, fecha_fin DATE NOT NULL, PERIOD BUSINESS_TIME(fecha_inicio, fecha_fin), FOREIGN KEY(mesaVotar) REFERENCES Mesa(letra), FOREIGN KEY(afiliacion) REFERENCES Colegio(numId))

CREATE UNIQUE INDEX index_votante ON Votante(pasaporte, BUSINESS_TIME WITHOUT OVERLAPS)
