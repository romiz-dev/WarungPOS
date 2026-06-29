-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 29, 2026 at 01:33 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `warung_apps`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_barang`
--

CREATE TABLE `tbl_barang` (
  `kode` varchar(20) NOT NULL,
  `nama` varchar(225) NOT NULL,
  `harga` int(11) NOT NULL,
  `stok` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_barang`
--

INSERT INTO `tbl_barang` (`kode`, `nama`, `harga`, `stok`) VALUES
('SBN-LFB-BR', 'Sabun Lifebuoy Biru', 20000, 20),
('SNC-OLE-KLG', 'Oleole Biskuit Kaleng', 20000, 15),
('SUS-UMF-250ML', 'Ultra Milk Fullcream 250Ml', 8000, 20);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_pendapatan`
--

CREATE TABLE `tbl_pendapatan` (
  `id_pendapatan` int(11) NOT NULL,
  `total_belanja` int(11) NOT NULL,
  `tanggal` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_pendapatan`
--

INSERT INTO `tbl_pendapatan` (`id_pendapatan`, `total_belanja`, `tanggal`) VALUES
(1, 20000, '2026-06-28 10:37:31'),
(2, 200000, '2026-06-28 10:39:38');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_utang`
--

CREATE TABLE `tbl_utang` (
  `id_utang` int(11) NOT NULL,
  `nama_pengutang` varchar(100) NOT NULL,
  `total_utang` int(11) NOT NULL,
  `status` varchar(20) NOT NULL DEFAULT 'Belum Lunas',
  `tanggal` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_utang`
--

INSERT INTO `tbl_utang` (`id_utang`, `nama_pengutang`, `total_utang`, `status`, `tanggal`) VALUES
(1, 'Najwan', 100000, 'Belum Lunas', '2026-06-28 10:44:45');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_barang`
--
ALTER TABLE `tbl_barang`
  ADD PRIMARY KEY (`kode`),
  ADD UNIQUE KEY `kode_barang` (`kode`);

--
-- Indexes for table `tbl_pendapatan`
--
ALTER TABLE `tbl_pendapatan`
  ADD PRIMARY KEY (`id_pendapatan`);

--
-- Indexes for table `tbl_utang`
--
ALTER TABLE `tbl_utang`
  ADD PRIMARY KEY (`id_utang`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_pendapatan`
--
ALTER TABLE `tbl_pendapatan`
  MODIFY `id_pendapatan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tbl_utang`
--
ALTER TABLE `tbl_utang`
  MODIFY `id_utang` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
