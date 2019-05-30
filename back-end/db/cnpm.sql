-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 30, 2019 at 05:42 PM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cnpm`
--

-- --------------------------------------------------------

--
-- Table structure for table `bien_lai`
--

CREATE TABLE `bien_lai` (
  `ngay_dong` datetime NOT NULL,
  `nguoi_dong` varchar(12) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `phu_phi` int(11) NOT NULL,
  `mo_ta` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `ma_bien_lai` varchar(12) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `chi_so`
--

CREATE TABLE `chi_so` (
  `ma_phong` varchar(12) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `thang` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `cs_dien` int(11) NOT NULL DEFAULT '0',
  `cs_nuoc` int(11) NOT NULL DEFAULT '0',
  `ma_bien_lai` varchar(12) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `khach_tro`
--

CREATE TABLE `khach_tro` (
  `ten` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `sdt` varchar(12) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `dia_chi` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `cmnd` varchar(12) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `nghe_nghiep` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `noi_lam_viec` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `ngay_thue` date NOT NULL,
  `phong_thue` varchar(12) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `tinh_trang` int(11) NOT NULL DEFAULT '1' COMMENT '(1) đang thuê (0) ngừng thuê'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `khach_tro`
--

INSERT INTO `khach_tro` (`ten`, `sdt`, `dia_chi`, `cmnd`, `nghe_nghiep`, `noi_lam_viec`, `ngay_thue`, `phong_thue`, `tinh_trang`) VALUES
('Nguyễn Văn Hóa', '0987654321', '123 đường 3/2, quận 10, tp HCM', '123456789', 'sinh viên', 'Đại học Khoa học tự nhiên', '2019-04-30', 'A001', 1);

-- --------------------------------------------------------

--
-- Table structure for table `phong_tro`
--

CREATE TABLE `phong_tro` (
  `ma_phong` varchar(12) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `thong_tin` text CHARACTER SET utf8 COLLATE utf8_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `phong_tro`
--

INSERT INTO `phong_tro` (`ma_phong`, `thong_tin`) VALUES
('A001', NULL),
('A002', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `phuong_tien`
--

CREATE TABLE `phuong_tien` (
  `so_xe` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `chu_xe` varchar(12) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `loai_xe` varchar(12) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `phuong_tien`
--

INSERT INTO `phuong_tien` (`so_xe`, `chu_xe`, `loai_xe`) VALUES
('51-S1-12345', '123456789', 'Honda');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` varchar(12) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT 'id của khách trọ là số CMND',
  `mat_khau` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL DEFAULT '12345' COMMENT 'mật khẩu',
  `account_type` int(11) NOT NULL DEFAULT '0' COMMENT 'phân loại người cùng: admin/chủ trọ (1), khách (0)'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `mat_khau`, `account_type`) VALUES
('123456789', '12345', 0),
('371603879', '12345', 1),
('admin', 'admin', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bien_lai`
--
ALTER TABLE `bien_lai`
  ADD PRIMARY KEY (`ma_bien_lai`),
  ADD KEY `Dongtien` (`nguoi_dong`);

--
-- Indexes for table `chi_so`
--
ALTER TABLE `chi_so`
  ADD KEY `chiso_phong` (`ma_phong`),
  ADD KEY `bienlai_chiso` (`ma_bien_lai`);

--
-- Indexes for table `khach_tro`
--
ALTER TABLE `khach_tro`
  ADD PRIMARY KEY (`cmnd`),
  ADD KEY `phong_thue` (`phong_thue`);

--
-- Indexes for table `phong_tro`
--
ALTER TABLE `phong_tro`
  ADD PRIMARY KEY (`ma_phong`);

--
-- Indexes for table `phuong_tien`
--
ALTER TABLE `phuong_tien`
  ADD KEY `chuxe_phuongtien` (`chu_xe`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bien_lai`
--
ALTER TABLE `bien_lai`
  ADD CONSTRAINT `Dongtien` FOREIGN KEY (`nguoi_dong`) REFERENCES `khach_tro` (`cmnd`);

--
-- Constraints for table `chi_so`
--
ALTER TABLE `chi_so`
  ADD CONSTRAINT `bienlai_chiso` FOREIGN KEY (`ma_bien_lai`) REFERENCES `bien_lai` (`ma_bien_lai`),
  ADD CONSTRAINT `chiso_phong` FOREIGN KEY (`ma_phong`) REFERENCES `phong_tro` (`ma_phong`);

--
-- Constraints for table `khach_tro`
--
ALTER TABLE `khach_tro`
  ADD CONSTRAINT `phong_thue` FOREIGN KEY (`phong_thue`) REFERENCES `phong_tro` (`ma_phong`),
  ADD CONSTRAINT `user_khach` FOREIGN KEY (`cmnd`) REFERENCES `user` (`id`);

--
-- Constraints for table `phuong_tien`
--
ALTER TABLE `phuong_tien`
  ADD CONSTRAINT `chuxe_phuongtien` FOREIGN KEY (`chu_xe`) REFERENCES `khach_tro` (`cmnd`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
