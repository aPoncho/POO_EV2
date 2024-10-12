-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 12-10-2024 a las 01:07:37
-- Versión del servidor: 8.3.0
-- Versión de PHP: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `empresa`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamentos`
--

DROP TABLE IF EXISTS `departamentos`;
CREATE TABLE IF NOT EXISTS `departamentos` (
  `ID_departamento` int NOT NULL AUTO_INCREMENT,
  `Nombre_d` varchar(60) COLLATE utf8mb4_general_ci NOT NULL,
  `Ubicacion_d` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `Gerente_d` varchar(60) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`ID_departamento`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `departamentos`
--

INSERT INTO `departamentos` (`ID_departamento`, `Nombre_d`, `Ubicacion_d`, `Gerente_d`) VALUES
(2, 'Programacion', 'Viña del mar', 'Lucas Martinez');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

DROP TABLE IF EXISTS `empleados`;
CREATE TABLE IF NOT EXISTS `empleados` (
  `ID_empleado` int NOT NULL AUTO_INCREMENT,
  `RUT_e` char(9) COLLATE utf8mb4_general_ci NOT NULL,
  `Nombre_e` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `Apellido_e` varchar(40) COLLATE utf8mb4_general_ci NOT NULL,
  `Direccion_e` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `Fono_e` int NOT NULL,
  `Correo_e` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `Cargo_e` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `Salario_e` int NOT NULL,
  `Departamento_e` int NOT NULL,
  PRIMARY KEY (`ID_empleado`),
  KEY `FK_EMPLEADO_DEPARTAMENTO` (`Departamento_e`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyectos`
--

DROP TABLE IF EXISTS `proyectos`;
CREATE TABLE IF NOT EXISTS `proyectos` (
  `ID_proyecto` int NOT NULL AUTO_INCREMENT,
  `Nombre_p` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `Descripcion_p` varchar(500) COLLATE utf8mb4_general_ci NOT NULL,
  `Fecha_inicio_p` date NOT NULL,
  `ID_DEPARTAMENTO` int NOT NULL,
  PRIMARY KEY (`ID_proyecto`),
  KEY `FK_PROYECTO_DEPARTAMENTO` (`ID_DEPARTAMENTO`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_de_tiempo`
--

DROP TABLE IF EXISTS `registro_de_tiempo`;
CREATE TABLE IF NOT EXISTS `registro_de_tiempo` (
  `ID_reg_tiempo` int NOT NULL AUTO_INCREMENT,
  `Fecha_r` date NOT NULL,
  `Cantidad_horas` int NOT NULL,
  `Descripcion_r` varchar(300) COLLATE utf8mb4_general_ci NOT NULL,
  `ID_EMPLEADO` int NOT NULL,
  PRIMARY KEY (`ID_reg_tiempo`),
  KEY `FK_REGISTRO_EMPLEADOS` (`ID_EMPLEADO`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD CONSTRAINT `FK_EMPLEADO_DEPARTAMENTO` FOREIGN KEY (`Departamento_e`) REFERENCES `departamentos` (`ID_departamento`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Filtros para la tabla `proyectos`
--
ALTER TABLE `proyectos`
  ADD CONSTRAINT `FK_PROYECTO_DEPARTAMENTO` FOREIGN KEY (`ID_DEPARTAMENTO`) REFERENCES `departamentos` (`ID_departamento`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Filtros para la tabla `registro_de_tiempo`
--
ALTER TABLE `registro_de_tiempo`
  ADD CONSTRAINT `FK_REGISTRO_EMPLEADOS` FOREIGN KEY (`ID_EMPLEADO`) REFERENCES `empleados` (`ID_empleado`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
