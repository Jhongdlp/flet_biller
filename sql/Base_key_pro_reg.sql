-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-07-2024 a las 06:30:45
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
(1, 'Laptop ultrafina', 'Tecnologia', 'Laptop', 'Dell', 'Tech Solutions', 15, 1200, 50),
(2, 'Smartphone avanzado', 'Tecnologia', 'Smartphone', 'Samsung', 'Electronics Plus', 15, 899.99, 80),
(3, 'Tablet profesional', 'Tecnologia', 'Tablet', 'Apple', 'Hi-Tech Suppliers', 15, 799.5, 60),
(4, 'Cámara digital 4K', 'Tecnologia', 'Camara digital', 'Canon', 'Gadget World', 15, 699, 70),
(5, 'Auriculares inalámbricos', 'Tecnologia', 'Auriculares', 'Sony', 'Tech Gadgets', 15, 249.99, 90),
(6, 'Monitor curvo 27\"', 'Tecnologia', 'Monitor', 'Samsung', 'Electronics Plus', 15, 399.99, 40),
(7, 'Impresora láser multifuncional', 'Tecnologia', 'Impresora', 'HP', 'Print Solutions', 15, 299.5, 55),
(8, 'Teclado mecánico RGB', 'Tecnologia', 'Teclado', 'Logitech', 'Gaming Gear', 15, 129, 75),
(9, 'Mouse gamer inalámbrico', 'Tecnologia', 'Mouse', 'Razer', 'Gaming Gear', 15, 79.99, 85),
(10, 'Router Wi-Fi 6 de doble banda', 'Tecnologia', 'Router', 'TP-Link', 'Network Solutions', 15, 149.5, 65),
(11, 'Disco duro externo 2TB', 'Tecnologia', 'Disco duro', 'Seagate', 'Storage Solutions', 15, 129.99, 50),
(12, 'Smart TV 55\" 4K HDR', 'Tecnologia', 'Smart TV', 'LG', 'Home Electronics', 15, 799, 30),
(13, 'Altavoces Bluetooth potentes', 'Tecnologia', 'Altavoces', 'JBL', 'Audio Systems', 15, 149.75, 45),
(14, 'Cargador portátil 20000mAh', 'Tecnologia', 'Cargador', 'Anker', 'Power Solutions', 15, 49.99, 95),
(15, 'Auriculares con cancelación de ruido', 'Tecnologia', 'Auriculares', 'Bose', 'Audio Systems', 15, 299, 60),
(16, 'Proyector Full HD 1080p', 'Tecnologia', 'Proyector', 'Epson', 'Visual Solutions', 15, 699.5, 25),
(17, 'Drone con cámara 4K', 'Tecnologia', 'Drone', 'DJI', 'Aerial Systems', 15, 899, 35),
(18, 'Robot aspirador inteligente', 'Tecnologia', 'Robot aspirador', 'iRobot', 'Home Solutions', 15, 349.99, 55),
(19, 'Estación de carga USB multiport', 'Tecnologia', 'Estación de carga', 'Belkin', 'Power Solutions', 15, 59.5, 70),
(20, 'Smartwatch resistente al agua', 'Tecnologia', 'Smartwatch', 'Garmin', 'Wearable Tech', 15, 199, 80),
(21, 'Champú revitalizante', 'Higiene', 'Champu', 'Pantene', 'Beauty Distributors', 15, 8.99, 100),
(22, 'Jabón líquido antibacterial', 'Higiene', 'Jabon', 'Dove', 'Hygiene Co.', 15, 4.5, 120),
(23, 'Crema hidratante facial', 'Higiene', 'Crema facial', 'Neutrogena', 'Skin Care Ltd.', 15, 12.75, 80),
(24, 'Desodorante roll-on', 'Higiene', 'Desodorante', 'Nivea', 'Fresh Products', 15, 3.99, 110),
(25, 'Cepillo dental eléctrico', 'Higiene', 'Cepillo dental', 'Oral-B', 'Health Solutions', 15, 29.99, 70),
(26, 'Enjuague bucal sin alcohol', 'Higiene', 'Enjuague bucal', 'Listerine', 'Oral Care Co.', 15, 5.99, 90),
(27, 'Toallas de papel absorción máxima', 'Higiene', 'Toallas de papel', 'Scott', 'Paper Products', 15, 2.5, 150),
(28, 'Cortauñas de precisión', 'Higiene', 'Cortauñas', 'Revlon', 'Beauty Tools', 15, 1.99, 200),
(29, 'Espuma de afeitar hidratante', 'Higiene', 'Espuma de afeitar', 'Gillette', 'Shaving Supplies', 15, 3.75, 180),
(30, 'Cepillo para el cabello desenredante', 'Higiene', 'Cepillo para el cabe', 'Tangle Teezer', 'Hair Care Ltd.', 15, 12.5, 100),
(31, 'Gel antibacterial 500ml', 'Higiene', 'Gel antibacterial', 'Purell', 'Hygiene Solutions', 15, 6.5, 120),
(32, 'Desinfectante multiusos', 'Higiene', 'Desinfectante', 'Lysol', 'Clean Solutions', 15, 4.99, 130),
(33, 'Loción corporal humectante', 'Higiene', 'Loción corporal', 'Nivea', 'Skin Care Ltd.', 15, 7.25, 140),
(34, 'Papel higiénico triple hoja pack 12', 'Higiene', 'Papel higiénico', 'Charmin', 'Paper Products', 15, 6.99, 160),
(35, 'Esponja de baño suave', 'Higiene', 'Esponja de baño', 'Dove', 'Shower Essentials', 15, 2.25, 170),
(36, 'Toallitas desmaquillantes', 'Higiene', 'Toallitas desmaquill', 'Neutrogena', 'Skin Care Ltd.', 15, 4.75, 110),
(37, 'Bálsamo labial protector SPF 15', 'Higiene', 'Bálsamo labial', 'Carmex', 'Lip Care Co.', 15, 1.99, 190),
(38, 'Pasta dental blanqueadora', 'Higiene', 'Pasta dental', 'Colgate', 'Oral Care Co.', 15, 3.5, 130),
(39, 'Gel de ducha revitalizante', 'Higiene', 'Gel de ducha', 'Nivea', 'Shower Essentials', 15, 4.25, 150),
(40, 'Esponja exfoliante facial', 'Higiene', 'Esponja facial', 'Swisspers', 'Skin Care Tools', 15, 1.75, 180),
(41, 'Sneakers deportivos', 'Ropa', 'Sneakers', 'Nike', 'Sport Gear Inc.', 15, 120, 60),
(42, 'Bufanda de lana', 'Ropa', 'Bufanda', 'Burberry', 'Fashion Trends', 15, 55.75, 40),
(43, 'Gorra ajustable', 'Ropa', 'Gorra', 'New Era', 'Headwear Masters', 15, 25.5, 50),
(44, 'Calcetines deportivos pack 5', 'Ropa', 'Calcetines', 'Puma', 'Footwear Experts', 15, 15.99, 70),
(45, 'Sudadera con capucha', 'Ropa', 'Sudadera', 'Under Armour', 'Active Wear Co.', 15, 40.25, 30),
(46, 'Pantalones vaqueros slim fit', 'Ropa', 'Pantalones vaqueros', 'Levi\'s', 'Denim Fashion', 15, 59.99, 55),
(47, 'Camisa de algodón manga larga', 'Ropa', 'Camisa', 'Tommy Hilfiger', 'Designer Apparel', 15, 69.5, 45),
(48, 'Vestido elegante para ocasiones', 'Ropa', 'Vestido', 'Zara', 'Fashion Trends', 15, 89.75, 25),
(49, 'Chaquetón acolchado invierno', 'Ropa', 'Chaquetón', 'H&M', 'Outerwear Co.', 15, 79.99, 35),
(50, 'Zapatos formales cuero', 'Ropa', 'Zapatos', 'Clarks', 'Footwear Experts', 15, 99.5, 20),
(51, 'Sombrero de ala ancha', 'Ropa', 'Sombrero', 'Goorin Bros', 'Headwear Masters', 15, 45, 15),
(52, 'Falda plisada moda juvenil', 'Ropa', 'Falda', 'Forever 21', 'Fashion Trends', 15, 29.99, 40),
(53, 'Pijama suave y confortable', 'Ropa', 'Pijama', 'Victoria\'s Secret', 'Sleepwear Co.', 15, 39.99, 30),
(54, 'Bufanda de seda pura', 'Ropa', 'Bufanda', 'Hermès', 'Luxury Accessories', 15, 199, 10),
(55, 'Guantes de cuero premium', 'Ropa', 'Guantes', 'Ralph Lauren', 'Designer Apparel', 15, 79.5, 25),
(56, 'Bañador deportivo hombre', 'Ropa', 'Bañador', 'Speedo', 'Swimwear Experts', 15, 34.75, 20),
(57, 'Mochila resistente y espaciosa', 'Ropa', 'Mochila', 'JanSport', 'Backpack Essentials', 15, 49.99, 30),
(58, 'Pantalón deportivo running', 'Ropa', 'Pantalón deportivo', 'Adidas', 'Sport Gear Inc.', 15, 49.5, 40),
(59, 'Camiseta básica cuello redondo', 'Ropa', 'Camiseta', 'Gap', 'Casual Wear', 15, 19.99, 50),
(60, 'Chaqueta ligera primavera', 'Ropa', 'Chaqueta', 'Columbia', 'Outdoor Gear', 15, 69.99, 35),
(61, 'Taladro percutor', 'Herramientas', 'Taladro', 'Bosch', 'Tool Masters', 15, 120, 60),
(62, 'Destornillador kit 20 piezas', 'Herramientas', 'Destornillador', 'Stanley', 'Hardware Solutions', 15, 35.75, 50),
(63, 'Cinta métrica 5 metros', 'Herramientas', 'Cinta métrica', 'Makita', 'Measure It Ltd.', 15, 12.99, 40),
(64, 'Sierra circular portátil', 'Herramientas', 'Sierra circular', 'Dewalt', 'Cutting Edge Tools', 15, 180, 30),
(65, 'Lijadora orbital', 'Herramientas', 'Lijadora', 'Black+Decker', 'Sanders Inc.', 15, 65.5, 25),
(66, 'Martillo de carpintero', 'Herramientas', 'Martillo', 'Estwing', 'Tool Masters', 15, 29.99, 55),
(67, 'Alicate de corte profesional', 'Herramientas', 'Alicate', 'Klein Tools', 'Hardware Solutions', 15, 24.5, 65),
(68, 'Nivel láser autonivelante', 'Herramientas', 'Nivel láser', 'Bosch', 'Measure It Ltd.', 15, 149.99, 45),
(69, 'Destornillador eléctrico recargable', 'Herramientas', 'Destornillador', 'Worx', 'Power Tools', 15, 49.95, 70),
(70, 'Pistola de calor profesional', 'Herramientas', 'Pistola de calor', 'Milwaukee', 'Heat Tools', 15, 89.5, 35),
(71, 'Brocas para madera y metal 50 piezas', 'Herramientas', 'Brocas', 'DeWalt', 'Drill Bits Co.', 15, 39.99, 60),
(72, 'Llave de trinquete reversible', 'Herramientas', 'Llave de trinquete', 'Craftsman', 'Tool Masters', 15, 19.99, 80),
(73, 'Cepillo eléctrico para carpintería', 'Herramientas', 'Cepillo', 'Ryobi', 'Woodworking Tools', 15, 79.75, 50),
(74, 'Generador eléctrico portátil 3000W', 'Herramientas', 'Generador eléctrico', 'Honda', 'Power Solutions', 15, 699, 20),
(75, 'Taladro inalámbrico 20V', 'Herramientas', 'Taladro', 'Makita', 'Cordless Tools', 15, 179.5, 40),
(76, 'Sierra de calar pendular', 'Herramientas', 'Sierra de calar', 'Bosch', 'Cutting Edge Tools', 15, 129, 30),
(77, 'Brocas para hormigón SDS-Plus', 'Herramientas', 'Brocas para hormigón', 'Bosch', 'Drill Bits Co.', 15, 24.99, 25),
(78, 'Escalera de aluminio plegable', 'Herramientas', 'Escalera', 'Louisville', 'Ladders Inc.', 15, 89.99, 35),
(79, 'Compresor de aire portátil', 'Herramientas', 'Compresor de aire', 'Porter-Cable', 'Air Tools', 15, 149.99, 55),
(80, 'Detector de voltaje sin contacto', 'Herramientas', 'Detector de voltaje', 'Klein Tools', 'Electrical Tools', 15, 19.5, 50),
(81, 'Arroz blanco 5kg', 'Alimentos', 'Arroz', 'Molinos', 'Grain Suppliers', 15, 10.5, 100),
(82, 'Aceite de oliva extra virgen', 'Alimentos', 'Aceite', 'La Española', 'Olive Oil Co.', 15, 8.25, 120),
(83, 'Lentejas 1kg', 'Alimentos', 'Lentejas', 'Goya', 'Pulses Importers', 15, 3.99, 80),
(84, 'Pasta spaghetti integral', 'Alimentos', 'Pasta', 'Barilla', 'Pasta Experts', 15, 2.5, 110),
(85, 'Miel de abeja pura 500g', 'Alimentos', 'Miel', 'Nature\'s Nate', 'Honey Suppliers', 15, 7.75, 90),
(86, 'Café colombiano tostado', 'Alimentos', 'Café', 'Juan Valdez', 'Coffee Co.', 15, 15.99, 70),
(87, 'Chocolate negro 70% cacao', 'Alimentos', 'Chocolate', 'Ghirardelli', 'Chocolates Inc.', 15, 4.5, 150),
(88, 'Nueces mixtas crudas', 'Alimentos', 'Nueces', 'Planters', 'Nut Suppliers', 15, 6.99, 130),
(89, 'Mermelada de fresa artesanal', 'Alimentos', 'Mermelada', 'Bonne Maman', 'Jam Makers', 15, 3.25, 180),
(90, 'Salsa de tomate italiana', 'Alimentos', 'Salsa de tomate', 'Rao\'s', 'Pasta Sauce Co.', 15, 5.5, 160),
(91, 'Cereal de avena con frutas', 'Alimentos', 'Cereal', 'Quaker', 'Cereal Co.', 15, 4.75, 140),
(92, 'Galletas integrales de avena', 'Alimentos', 'Galletas', 'Nature Valley', 'Snack Co.', 15, 3.99, 170),
(93, 'Leche de almendras sin azúcar', 'Alimentos', 'Leche', 'Silk', 'Dairy Alternatives', 15, 2.99, 190),
(94, 'Té verde matcha en polvo', 'Alimentos', 'Te', 'Matcha Love', 'Tea Suppliers', 15, 12.5, 100),
(95, 'Sardinas en aceite de oliva', 'Alimentos', 'Sardinas', 'Ortiz', 'Seafood Co.', 15, 1.99, 200),
(96, 'Aceitunas verdes rellenas', 'Alimentos', 'Aceitunas', 'Mario', 'Olives Co.', 15, 3.25, 180),
(97, 'Sopa instantánea de miso', 'Alimentos', 'Sopa', 'Maruchan', 'Soup Co.', 15, 0.99, 220),
(98, 'Mantequilla de maní natural', 'Alimentos', 'Mantequilla de mani', 'Jif', 'Nut Butters', 15, 4.99, 150),
(99, 'Caramelos de menta sin azúcar', 'Alimentos', 'Caramelos', 'Altoids', 'Candy Co.', 15, 1.5, 240),
(100, 'Agua mineral natural 1.5L', 'Alimentos', 'Agua mineral', 'Evian', 'Beverage Co.', 15, 0.75, 260);

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
