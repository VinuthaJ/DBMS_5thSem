-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Aug 01, 2021 at 04:08 PM
-- Server version: 8.0.21
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbms`
--

DELIMITER $$
--
-- Procedures
--
DROP PROCEDURE IF EXISTS `manu_spare`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `manu_spare` (IN `name` VARCHAR(20))  NO SQL
SELECT s.sid, s.Sname from spare s, manu m where m.mid = s.mid and m.Mname=name$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
CREATE TABLE IF NOT EXISTS `account` (
  `Bid` int DEFAULT NULL,
  `Sid` int DEFAULT NULL,
  `Sname` varchar(20) DEFAULT NULL,
  `Cp` double DEFAULT NULL,
  `sp` double DEFAULT NULL,
  `quantities_sold` int DEFAULT NULL,
  `profit` double DEFAULT NULL,
  KEY `Bid` (`Bid`),
  KEY `Sid` (`Sid`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`Bid`, `Sid`, `Sname`, `Cp`, `sp`, `quantities_sold`, `profit`) VALUES
(1, 1, 'bumper', 20, 30, 12, 120),
(2, 1, 'bumper', 20, 30, 15, 150),
(3, 1, 'bumper', 20, 30, 18, 180),
(4, 1, 'bumper', 20, 30, 17, 170),
(5, 1, 'bumper', 20, 30, 18, 180),
(3, 2, 'bumper', 25, 40, 11, 165),
(4, 2, 'bumper', 25, 40, 13, 195),
(5, 2, 'bumper', 25, 40, 16, 240),
(1, 3, 'bumper', 25, 35, 13, 130),
(2, 3, 'bumper', 25, 35, 14, 140),
(3, 3, 'bumper', 25, 35, 8, 80),
(4, 3, 'bumper', 25, 35, 16, 160),
(5, 3, 'bumper', 25, 35, 12, 120),
(4, 4, 'bumper', 30, 40, 14, 140),
(2, 4, 'bumper', 30, 40, 11, 110),
(1, 4, 'bumper', 30, 40, 16, 160),
(3, 4, 'bumper', 30, 40, 13, 130),
(5, 4, 'bumper', 30, 40, 10, 100),
(2, 5, 'bumper', 20, 30, 15, 150),
(3, 5, 'bumper', 20, 30, 19, 190),
(4, 5, 'bumper', 20, 30, 13, 130),
(5, 5, 'bumper', 20, 30, 16, 160),
(1, 6, 'headlight', 30, 40, 12, 120),
(2, 6, 'headlight', 30, 40, 11, 110),
(3, 6, 'headlight', 30, 40, 15, 150),
(4, 6, 'headlight', 30, 40, 16, 160),
(5, 6, 'headlight', 30, 40, 10, 100),
(1, 7, 'headlight', 25, 35, 12, 120),
(2, 7, 'headlight', 25, 35, 15, 150),
(3, 7, 'headlight', 25, 35, 12, 120),
(4, 7, 'headlight', 25, 35, 17, 170),
(5, 7, 'headlight', 25, 35, 15, 150),
(1, 8, 'headlight', 30, 40, 13, 130),
(2, 8, 'headlight', 30, 40, 18, 180),
(3, 8, 'headlight', 30, 40, 14, 140),
(4, 8, 'headlight', 30, 40, 13, 130),
(5, 8, 'headlight', 30, 40, 15, 150),
(1, 9, 'headlight', 35, 45, 12, 120),
(2, 9, 'headlight', 35, 45, 23, 230),
(2, 9, 'headlight', 35, 45, 12, 120),
(3, 9, 'headlight', 35, 45, 15, 150),
(4, 9, 'headlight', 35, 45, 14, 140),
(5, 9, 'headlight', 35, 45, 16, 160),
(1, 10, 'headlight', 30, 35, 12, 60),
(2, 10, 'headlight', 30, 35, 15, 75),
(3, 10, 'headlight', 30, 35, 17, 85),
(4, 10, 'headlight', 30, 35, 17, 85),
(5, 10, 'headlight', 30, 35, 13, 65),
(1, 11, 'clutch', 30, 40, 15, 150),
(2, 11, 'clutch', 30, 40, 9, 90),
(3, 11, 'clutch', 30, 40, 10, 100),
(4, 11, 'clutch', 30, 40, 9, 90),
(5, 11, 'clutch', 30, 40, 18, 180),
(1, 12, 'clutch', 35, 45, 15, 150),
(2, 12, 'clutch', 35, 45, 12, 120),
(3, 12, 'clutch', 35, 45, 8, 80),
(4, 12, 'clutch', 35, 45, 17, 170),
(5, 12, 'clutch', 35, 45, 11, 110),
(1, 13, 'clutch', 30, 45, 13, 195),
(2, 13, 'clutch', 30, 45, 11, 165),
(3, 13, 'clutch', 30, 45, 18, 270),
(4, 13, 'clutch', 30, 45, 18, 270),
(2, 14, 'clutch', 35, 45, 18, 180),
(1, 14, 'clutch', 35, 45, 12, 120),
(5, 13, 'clutch', 30, 45, 13, 195),
(3, 14, 'clutch', 35, 45, 15, 150),
(4, 14, 'clutch', 35, 45, 16, 160),
(5, 14, 'clutch', 35, 45, 16, 160),
(1, 15, 'clutch', 25, 30, 13, 65),
(2, 15, 'clutch', 25, 30, 14, 70),
(3, 15, 'clutch', 25, 30, 16, 80),
(4, 15, 'clutch', 25, 30, 11, 55),
(5, 15, 'clutch', 25, 30, 17, 85),
(1, 16, 'Brakes', 10, 20, 13, 130),
(2, 16, 'Brakes', 10, 20, 7, 70),
(3, 16, 'Brakes', 10, 20, 17, 170),
(4, 16, 'Brakes', 10, 20, 14, 140),
(5, 16, 'Brakes', 10, 20, 15, 150),
(1, 17, 'Brakes', 15, 20, 15, 75),
(2, 17, 'Brakes', 15, 20, 18, 90),
(3, 17, 'Brakes', 15, 20, 18, 90),
(4, 17, 'Brakes', 15, 20, 14, 70),
(5, 17, 'Brakes', 15, 20, 10, 50),
(1, 18, 'Brakes', 20, 25, 15, 75),
(2, 18, 'Brakes', 20, 25, 11, 55),
(3, 18, 'Brakes', 20, 25, 14, 70),
(4, 18, 'Brakes', 20, 25, 16, 80),
(5, 18, 'Brakes', 20, 25, 9, 45),
(1, 19, 'Brakes', 15, 20, 13, 65),
(2, 19, 'Brakes', 15, 20, 11, 55),
(3, 19, 'Brakes', 15, 20, 15, 75),
(4, 19, 'Brakes', 15, 20, 14, 70),
(5, 19, 'Brakes', 15, 20, 17, 85),
(1, 20, 'Brakes', 10, 12, 13, 26),
(2, 20, 'Brakes', 10, 12, 11, 22),
(3, 20, 'Brakes', 10, 12, 15, 30),
(4, 20, 'Brakes', 10, 12, 16, 32),
(5, 20, 'Brakes', 10, 12, 8, 16);

--
-- Triggers `account`
--
DROP TRIGGER IF EXISTS `pro_up`;
DELIMITER $$
CREATE TRIGGER `pro_up` BEFORE UPDATE ON `account` FOR EACH ROW BEGIN
    IF new.profit = 'yes' THEN
        SET new.profit = (new.sp - new.Cp)*new.quantities_sold;
    END IF;
END
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `prof`;
DELIMITER $$
CREATE TRIGGER `prof` BEFORE INSERT ON `account` FOR EACH ROW BEGIN
    IF new.profit = 'yes' THEN
        SET new.profit = (new.sp - new.Cp)*new.quantities_sold;
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `branch`
--

DROP TABLE IF EXISTS `branch`;
CREATE TABLE IF NOT EXISTS `branch` (
  `bid` int NOT NULL AUTO_INCREMENT,
  `Loc` varchar(20) DEFAULT NULL,
  `Phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `branch`
--

INSERT INTO `branch` (`bid`, `Loc`, `Phone`) VALUES
(2, 'Rajajinagar', '7428730894'),
(3, 'Malleshwaram', '7231746184'),
(4, 'Jayanagar', '70221716182'),
(5, 'Banashankari', '7231746185'),
(1, 'Sadashivnagar', '7231746187');

-- --------------------------------------------------------

--
-- Table structure for table `branch_customer`
--

DROP TABLE IF EXISTS `branch_customer`;
CREATE TABLE IF NOT EXISTS `branch_customer` (
  `Bid` int DEFAULT NULL,
  `Cid` int DEFAULT NULL,
  `Sid` int DEFAULT NULL,
  `Quantities_bought` int DEFAULT NULL,
  KEY `Bid` (`Bid`),
  KEY `Sid` (`Sid`),
  KEY `Cid` (`Cid`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `branch_customer`
--

INSERT INTO `branch_customer` (`Bid`, `Cid`, `Sid`, `Quantities_bought`) VALUES
(2, 3, 4, 2),
(1, 1, 1, 23),
(1, 2, 2, 3),
(3, 4, 13, 2),
(5, 0, 10, 5),
(1, 2, 2, 1),
(2, 101, 2, 2),
(1, 1, 1, 12);

-- --------------------------------------------------------

--
-- Table structure for table `branch_manu`
--

DROP TABLE IF EXISTS `branch_manu`;
CREATE TABLE IF NOT EXISTS `branch_manu` (
  `Bid` int DEFAULT NULL,
  `Mid` int DEFAULT NULL,
  `Sid` int DEFAULT NULL,
  `quantities_order` int DEFAULT NULL,
  `oid` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`oid`),
  KEY `Bid` (`Bid`),
  KEY `Mid` (`Mid`),
  KEY `Sid` (`Sid`)
) ENGINE=MyISAM AUTO_INCREMENT=103 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `branch_manu`
--

INSERT INTO `branch_manu` (`Bid`, `Mid`, `Sid`, `quantities_order`, `oid`) VALUES
(2, 3, 2, 12, 4),
(2, 2, 1, 23, 5),
(3, 2, 1, 23, 6),
(2, 2, 2, 12, 10),
(1, 2, 2, 12, 11),
(1, 1, 1, 20, 98),
(2, 2, 3, 70, 99);

--
-- Triggers `branch_manu`
--
DROP TRIGGER IF EXISTS `mini`;
DELIMITER $$
CREATE TRIGGER `mini` BEFORE INSERT ON `branch_manu` FOR EACH ROW BEGIN
    
        IF new.quantities_order < 10 THEN
         SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'minimum order not satisified';
        END IF;
   
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `cid` int NOT NULL AUTO_INCREMENT,
  `Cname` varchar(20) DEFAULT NULL,
  `Phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=MyISAM AUTO_INCREMENT=106 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`cid`, `Cname`, `Phone`) VALUES
(100, 'Subhash', '8731716189'),
(101, 'sumukh', '8904724469'),
(102, 'Vinutha', '7231746183'),
(103, 'Vishakha', '7231746184'),
(104, 'sherlock', '9221221221');

-- --------------------------------------------------------

--
-- Table structure for table `manu`
--

DROP TABLE IF EXISTS `manu`;
CREATE TABLE IF NOT EXISTS `manu` (
  `Mid` int NOT NULL AUTO_INCREMENT,
  `Mname` varchar(20) DEFAULT NULL,
  `loc` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Mid`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `manu`
--

INSERT INTO `manu` (`Mid`, `Mname`, `loc`) VALUES
(2, 'bmw', 'yelehanka'),
(3, 'audi', 'hebbal'),
(4, 'honda', 'peenya'),
(5, 'toyota', 'madiwala'),
(1, 'suzuki', 'banaswadi');

-- --------------------------------------------------------

--
-- Table structure for table `spare`
--

DROP TABLE IF EXISTS `spare`;
CREATE TABLE IF NOT EXISTS `spare` (
  `Sid` int NOT NULL AUTO_INCREMENT,
  `Sname` varchar(20) DEFAULT NULL,
  `Mid` int DEFAULT NULL,
  PRIMARY KEY (`Sid`),
  KEY `Mid` (`Mid`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `spare`
--

INSERT INTO `spare` (`Sid`, `Sname`, `Mid`) VALUES
(1, 'bumper', 1),
(2, 'bumper', 2),
(3, 'bumper', 3),
(4, 'bumper', 4),
(5, 'bumper', 5),
(6, 'headlight', 1),
(7, 'headlight', 2),
(8, 'headlight', 3),
(9, 'headlight', 4),
(10, 'headlight', 5),
(11, 'clutch', 1),
(12, 'clutch', 2),
(13, 'clutch', 3),
(14, 'clutch', 4),
(15, 'clutch', 5),
(16, 'Brake_wire', 1),
(17, 'Brake_wire', 2),
(18, 'Brake_wire', 3),
(19, 'Brake_wire', 4),
(20, 'Brake_wire', 5),
(21, 'silencer', 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
