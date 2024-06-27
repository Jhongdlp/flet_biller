-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-06-2024 a las 11:38:51
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `billify`
--
CREATE DATABASE IF NOT EXISTS `billify` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `billify`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `llave`
--

CREATE TABLE `llave` (
  `LLAVE_STR` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `llave`
--

INSERT INTO `llave` (`LLAVE_STR`) VALUES
('\'AIEX6oB6mrLmw_1LdwZFvEKRSOHgOJaTk10bViMmBIY=\'');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `ID_PROD` int(20) NOT NULL,
  `NOM_PROD` varchar(40) NOT NULL,
  `TIP_PROD` varchar(40) NOT NULL,
  `TIP_ESP_PROD` varchar(20) DEFAULT NULL,
  `MAR_PRO` varchar(40) NOT NULL,
  `PROVE_PRO` varchar(40) NOT NULL,
  `IVA_PRO` int(10) NOT NULL,
  `PRE_PRO` double NOT NULL,
  `EXIS_PRO` int(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`ID_PROD`, `NOM_PROD`, `TIP_PROD`, `TIP_ESP_PROD`, `MAR_PRO`, `PROVE_PRO`, `IVA_PRO`, `PRE_PRO`, `EXIS_PRO`) VALUES
(1, 'Laptop Gaming', 'Tecnología', 'Laptop', 'ASUS', 'TechSupply Inc.', 15, 1500, 10),
(2, 'Smartphone 5G', 'Tecnología', 'Celular', 'Samsung', 'Mobile Solutions', 15, 999.99, 20),
(3, 'Tablet Pro', 'Tecnología', 'Tablet', 'Apple', 'Apple Authorized Reseller', 15, 1200, 15),
(4, 'Auriculares Bluetooth', 'Tecnología', 'Auriculares', 'Sony', 'Sound Experts', 15, 199.99, 30),
(5, 'Smartwatch', 'Tecnología', 'Reloj Inteligente', 'Garmin', 'Wearable Tech Co.', 15, 299.99, 25),
(6, 'Cámara DSLR', 'Tecnología', 'Cámara', 'Canon', 'Camera World', 15, 899.99, 12),
(7, 'Monitor 4K', 'Tecnología', 'Monitor', 'LG', 'Display Universe', 15, 450, 18),
(8, 'Router WiFi 6', 'Tecnología', 'Router', 'TP-Link', 'Network Gear', 15, 129.99, 22),
(9, 'Teclado Mecánico', 'Tecnología', 'Teclado', 'Logitech', 'Keyboard Masters', 15, 89.99, 35),
(10, 'SSD 1TB', 'Tecnología', 'Almacenamiento', 'Samsung', 'Storage Solutions', 15, 150, 40),
(11, 'Impresora Multifunción', 'Tecnología', 'Impresora', 'HP', 'Office Supplies Co.', 15, 220, 25),
(12, 'Altavoz Inteligente', 'Tecnología', 'Altavoz', 'Amazon', 'Smart Home Gadgets', 15, 99.99, 30),
(13, 'Cámara de Seguridad', 'Tecnología', 'Cámara', 'Nest', 'Home Security Inc.', 15, 150, 18),
(14, 'Consola de Videojuegos', 'Tecnología', 'Consola', 'Sony', 'Gaming World', 15, 499.99, 15),
(15, 'Disco Duro Externo', 'Tecnología', 'Almacenamiento', 'WD', 'Data Storage Solutions', 15, 89.99, 40),
(16, 'Microondas Digital', 'Tecnología', 'Electrodoméstico', 'Samsung', 'Home Appliances', 15, 180, 10),
(17, 'Reproductor Blu-ray', 'Tecnología', 'Reproductor', 'Sony', 'Entertainment Systems', 15, 120, 20),
(18, 'Proyector 1080p', 'Tecnología', 'Proyector', 'Epson', 'Visual Tech Supplies', 15, 450, 12),
(19, 'Barra de Sonido', 'Tecnología', 'Audio', 'Bose', 'Sound Innovations', 15, 299.99, 22),
(20, 'Cámara de Acción', 'Tecnología', 'Cámara', 'GoPro', 'Action Cameras Inc.', 15, 399.99, 18),
(21, 'Lector de Libros Electrónicos', 'Tecnología', 'E-Reader', 'Amazon', 'Digital Books Co.', 15, 129.99, 30),
(22, 'Termostato Inteligente', 'Tecnología', 'Termostato', 'Nest', 'Smart Home Solutions', 15, 250, 15),
(23, 'Sistema de Altavoces', 'Tecnología', 'Audio', 'JBL', 'Music Accessories', 15, 199.99, 25),
(24, 'Cargador Rápido USB-C', 'Tecnología', 'Accesorio', 'Anker', 'Mobile Accessories', 15, 39.99, 50),
(25, 'Cámara Web HD', 'Tecnología', 'Cámara', 'Logitech', 'Computer Accessories', 15, 89.99, 35),
(26, 'Controlador de Juegos', 'Tecnología', 'Accesorio', 'Microsoft', 'Gaming Accessories', 15, 59.99, 40),
(27, 'Smart TV 55\"', 'Tecnología', 'Televisión', 'LG', 'Home Entertainment', 15, 799.99, 10),
(28, 'Panel Solar Portátil', 'Tecnología', 'Energía', 'Renogy', 'Green Energy Solutions', 15, 249.99, 20),
(29, 'Mando a Distancia Universal', 'Tecnología', 'Accesorio', 'Logitech', 'Remote Controls Inc.', 15, 99.99, 30),
(30, 'Cámara Compacta', 'Tecnología', 'Cámara', 'Sony', 'Photo Gear', 15, 299.99, 20),
(31, 'Smartphone de Gama Alta', 'Tecnología', 'Celular', 'Apple', 'Mobile Solutions', 15, 1200, 25),
(32, 'Portátil Ultrabook', 'Tecnología', 'Laptop', 'Dell', 'TechSupply Inc.', 15, 1400, 15),
(33, 'Servidor NAS', 'Tecnología', 'Almacenamiento', 'Synology', 'Data Storage Solutions', 15, 500, 8),
(34, 'Enchufe Inteligente', 'Tecnología', 'Accesorio', 'TP-Link', 'Smart Home Gadgets', 15, 25.99, 45),
(35, 'Tarjeta Gráfica', 'Tecnología', 'Componente', 'NVIDIA', 'PC Parts Co.', 15, 699.99, 12),
(36, 'Controlador de Voz', 'Tecnología', 'Accesorio', 'Amazon', 'Voice Control Devices', 15, 49.99, 50),
(37, 'Sistema de Realidad Virtual', 'Tecnología', 'Accesorio', 'Oculus', 'VR World', 15, 399.99, 10),
(38, 'Placa Madre', 'Tecnología', 'Componente', 'ASUS', 'PC Parts Co.', 15, 299.99, 20),
(39, 'Kit de Cámaras de Seguridad', 'Tecnología', 'Cámara', 'Arlo', 'Home Security Inc.', 15, 599.99, 12),
(40, 'Impresora 3D', 'Tecnología', 'Impresora', 'Creality', '3D Printing Supplies', 15, 350, 8),
(41, 'Drone con Cámara', 'Tecnología', 'Drone', 'DJI', 'Aerial Innovations', 15, 999.99, 7),
(42, 'Reproductor de Música Portátil', 'Tecnología', 'Audio', 'Sony', 'Music Accessories', 15, 199.99, 15),
(43, 'Smartphone de Gama Media', 'Tecnología', 'Celular', 'Xiaomi', 'Mobile Solutions', 15, 400, 30),
(44, 'Repetidor WiFi', 'Tecnología', 'Red', 'Netgear', 'Network Gear', 15, 59.99, 25),
(45, 'Batería Externa', 'Tecnología', 'Accesorio', 'Anker', 'Mobile Accessories', 15, 49.99, 50),
(46, 'Home Assistant', 'Tecnología', 'Asistente', 'Google', 'Smart Home Gadgets', 15, 129.99, 30),
(47, 'Kit de Desarrollo Arduino', 'Tecnología', 'Electrónica', 'Arduino', 'Electronic Components', 15, 79.99, 20),
(48, 'Sensor de Movimiento', 'Tecnología', 'Sensor', 'Philips', 'Smart Home Solutions', 15, 49.99, 35),
(49, 'Kit de Iluminación Inteligente', 'Tecnología', 'Iluminación', 'Philips', 'Smart Home Solutions', 15, 199.99, 18),
(50, 'Smartphone Básico', 'Tecnología', 'Celular', 'Nokia', 'Mobile Solutions', 15, 100, 40);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro`
--

CREATE TABLE `registro` (
  `USUARIOS` varchar(40) NOT NULL,
  `CORREOS` varchar(40) NOT NULL,
  `CLAVES` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `registro`
--

INSERT INTO `registro` (`USUARIOS`, `CORREOS`, `CLAVES`) VALUES
('tomas', 'tomas@gmail.com', 'tomas'),
('joel', 'joel', 'gAAAAABmOtI8w_h9xgAEPjhDQj8ZFTn-Cbj2MxmlK7gyrRuOIkyIpun4IihGHevVcCcxq9M5pUTV5IPaBPXqhp0jerBHftNkOw=='),
('jhon', 'jhon', 'gAAAAABmOtrL46ieEFhYwQa2HU9MSbkWPy64aaKzCUXgj31CroMjmkadxzywK8tSr-VO5QQg_Eth4PkgFJdyhvqA0WM7sXT_XA=='),
('ander', 'ander', 'gAAAAABmQZHchL3IXgYJlfavL_lejRLwfTFRX1EUhy4x_ZbpVBhBtP0JNjKhaycRrNGx2Ja46a8Qc9haP8qcyjtv0yGuJIRTBw=='),
('.', '.', 'gAAAAABmQn0QfoY2QCwSEiM1LWE6tyiW5mSEZNroLyX8De8ll1d6pbH1tcfpZl28GlARz8vSx_dxEdGtjIkKZuLkqVjdQ2QSrA=='),
('marcelo', 'marcelo@gmail.com', 'gAAAAABmTgTZcBtkHfS4_nP-VEEzXRJ8cZuMFThiTs2W35JXb9pwjtJ4oGeM-qV8zLM5rhxC5HnZ1xhdWngAamxQiW5AKqaNHQ=='),
('a', 'asd', 'gAAAAABmTgTnYKWyjGwjRhJxdJbdVTvluDosWn_rVfjE1-4T22DpvCA0LDrU3UgMcfUMoJ50aLvfbLy1kihfXl7ghrn-DUCClw=='),
('Alejandro', 'alejandro@gmail.com', 'gAAAAABmTgkLLzvA0j_7W-_R-zryvxIPQnAAjF8eojXQ0HOgYjQ2S-OMPSC4YL-YF-tbU3Diyw1R0RpbDsTlV-c1V8rXOsin1g==');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `llave`
--
ALTER TABLE `llave`
  ADD PRIMARY KEY (`LLAVE_STR`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`ID_PROD`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
