-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 24, 2025 at 02:57 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask_users`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_orders`
--

CREATE TABLE `tbl_orders` (
  `order_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `payment_method` varchar(50) NOT NULL,
  `order_date` date NOT NULL DEFAULT curdate()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_orders`
--

INSERT INTO `tbl_orders` (`order_id`, `user_id`, `name`, `address`, `payment_method`, `order_date`) VALUES
(1, 5, 'marian', 'Stralsunder str 14', 'credit-card', '2025-01-16'),
(2, 5, 'marian', 'Stralsunder str 14', 'credit-card', '2025-01-16'),
(3, 5, 'marian', 'Stralsunder str 14', 'paypal', '2025-01-16'),
(4, 5, 'marian', 'Stralsunder str 14', 'paypal', '2025-01-16'),
(5, 5, 'marian', 'Stralsunder str 14', 'paypal', '2025-01-16'),
(6, 5, 'marian', 'Stralsunder str 14', 'paypal', '2025-01-16'),
(7, 5, 'marian', 'Stralsunder str 14', 'paypal', '2025-01-16'),
(8, 5, 'marian', 'Stralsunder str 14', 'paypal', '2025-01-16'),
(9, 5, 'marian', 'Stralsunder str 14', 'paypal', '2025-01-16'),
(10, 5, 'marian', 'Stralsunder str 14', 'paypal', '2025-01-16'),
(11, 5, 'jj', 'jj', 'credit-card', '2025-01-16'),
(12, 16, 'angel', 'merighdamm', 'credit-card', '2025-01-16'),
(13, 17, '444', '444', 'credit-card', '2025-01-16'),
(17, 21, 'marian', 'Stralsunder str 14', 'credit-card', '2025-01-16'),
(24, 22, 'marian', 'Stralsunder str 14', 'paypal', '2025-01-20'),
(26, 1, 'marian', 'Stralsunder str 14', 'credit-card', '2025-01-22'),
(27, 24, 'gghuj', 'hh', 'paypal', '2025-01-22'),
(28, 25, 'shamisa', 'berlin', 'paypal', '2025-01-22'),
(29, 24, 'shamisa', 'berlin', 'paypal', '2025-01-23'),
(30, 26, 'elje', 'vito', 'credit-card', '2025-01-23'),
(31, 26, 'Marian Brito', 'Stralsunder str 14', 'paypal', '2025-01-23'),
(32, 27, 'Marian Brito', 'Stralsunder str 14', 'paypal', '2025-01-24');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_products`
--

CREATE TABLE `tbl_products` (
  `product_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `image` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_products`
--

INSERT INTO `tbl_products` (`product_id`, `name`, `price`, `image`) VALUES
(1, 'smartphone', 1299.99, 'image1.jpg'),
(2, 'laptop', 800.99, 'image2.jpg'),
(3, 'headphones', 120.99, 'image3.jpg'),
(4, 'smartwatch', 300.99, 'image4.jpg'),
(5, 'camera', 300.99, 'image5.jpg'),
(6, 'game console', 500.99, 'image6.jpg'),
(7, 'keyboard', 74.99, 'image7.jpg'),
(8, 'monitor', 129.99, 'image8.jpg'),
(11, 'mouse', 50.99, 'image9.jpg'),
(12, 'smart tv', 300.99, 'image10.jpg'),
(16, 'speaker', 79.99, 'image11.jpg'),
(17, 'ipad', 700.99, 'image12.jpg'),
(18, 'printer', 300.99, 'image13.jpg'),
(19, 'external flash', 100.99, 'image14.jpg'),
(20, 'usbc cable', 20.99, 'image15.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_shopppingcart`
--

CREATE TABLE `tbl_shopppingcart` (
  `cart_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_shopppingcart`
--

INSERT INTO `tbl_shopppingcart` (`cart_id`, `user_id`, `product_id`, `quantity`) VALUES
(6, 9, 1, 3),
(7, 9, 2, 1),
(8, 9, 4, 1),
(9, 9, 3, 1),
(55, 16, 3, 1),
(83, 1, 4, 8),
(89, 1, 19, 1),
(90, 1, 11, 1),
(98, 24, 3, 1),
(99, 24, 5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_users`
--

CREATE TABLE `tbl_users` (
  `username` varchar(20) NOT NULL,
  `user_id` int(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_users`
--

INSERT INTO `tbl_users` (`username`, `user_id`, `password`) VALUES
('marian@gmail.com', 1, '123'),
('marianb@gmail.com', 2, 'jj'),
('marian@gmail.comhh', 3, '123'),
('marian@gmail.com', 4, '123456'),
('jose@gmail.com', 5, '321'),
('carucijose69', 6, 'mayi'),
('marian7@gmail.com', 7, '321'),
('marian7@gmail.com1', 8, '123'),
('marian7@gmail.com2', 9, '1234'),
('jose123', 10, '123'),
('jose123', 11, '456'),
('jose@gmail.com', 12, '321'),
('jose@gmail.com', 13, '321'),
('jose@gmail.com', 14, '321'),
('jose@gmail.com', 15, '321'),
('angel@gmail.com', 16, '1234'),
('david.alejandro.vasq', 17, 'GALA100'),
('mayi123', 21, '123'),
('mari123', 22, '123'),
('marian@gmail.com', 23, '123'),
('jose@gmail.com', 24, '123'),
('shamisa', 25, '123'),
('carucijose69@gmqil.c', 26, 'Caru3107'),
('marian1', 27, '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_orders`
--
ALTER TABLE `tbl_orders`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `tbl_orders_ibfk_1` (`user_id`);

--
-- Indexes for table `tbl_products`
--
ALTER TABLE `tbl_products`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `tbl_shopppingcart`
--
ALTER TABLE `tbl_shopppingcart`
  ADD PRIMARY KEY (`cart_id`),
  ADD KEY `fk_product` (`product_id`),
  ADD KEY `fk_user` (`user_id`);

--
-- Indexes for table `tbl_users`
--
ALTER TABLE `tbl_users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_orders`
--
ALTER TABLE `tbl_orders`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `tbl_products`
--
ALTER TABLE `tbl_products`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `tbl_shopppingcart`
--
ALTER TABLE `tbl_shopppingcart`
  MODIFY `cart_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;

--
-- AUTO_INCREMENT for table `tbl_users`
--
ALTER TABLE `tbl_users`
  MODIFY `user_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tbl_orders`
--
ALTER TABLE `tbl_orders`
  ADD CONSTRAINT `tbl_orders_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `tbl_users` (`user_id`) ON DELETE CASCADE;

--
-- Constraints for table `tbl_shopppingcart`
--
ALTER TABLE `tbl_shopppingcart`
  ADD CONSTRAINT `fk_product` FOREIGN KEY (`product_id`) REFERENCES `tbl_products` (`product_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_user` FOREIGN KEY (`user_id`) REFERENCES `tbl_users` (`user_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
