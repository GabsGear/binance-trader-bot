-- MySQL dump 10.13  Distrib 5.5.59, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: protrader
-- ------------------------------------------------------
-- Server version	5.5.59-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bot`
--

DROP TABLE IF EXISTS `bot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bot` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `exchange` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `strategy` int(5) NOT NULL,
  `profit` float(8,8) NOT NULL,
  `pid` int(10) NOT NULL,
  `status` int(11) NOT NULL,
  `stoploss` float(8,8) NOT NULL,
  `name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=287 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bot`
--

LOCK TABLES `bot` WRITE;
/*!40000 ALTER TABLE `bot` DISABLE KEYS */;
INSERT INTO `bot` VALUES (21,36,'bittrex',0,0.01000000,28488,0,0.01000000,'','2018-03-27 21:02:42','2018-03-27 21:02:42'),(202,36,'bittrex',0,0.01000000,28482,0,0.01000000,'','2018-04-10 22:36:37','2018-04-10 22:36:37'),(239,37,'bittrex',0,0.01500000,8845,2,0.02000000,'AdNDPNii','2018-04-18 21:07:40','2018-04-18 21:07:40'),(278,42,'binance',2,0.03000000,24571,1,0.01000000,'hlvBxQN1','2018-04-29 15:59:18','2018-04-29 15:59:30'),(280,4,'binance',3,0.01000000,21111,0,0.01000000,'Dh9AMB8h','2018-04-30 21:04:37','2018-04-30 21:04:37'),(281,46,'binance',0,0.01000000,0,0,0.01000000,'uOpjx4No','2018-05-12 01:11:48','2018-05-12 01:11:48'),(282,46,'bittrex',3,0.03000000,0,0,0.01000000,'GHPs9oaI','2018-05-12 01:12:59','2018-05-12 01:12:59'),(285,48,'binance',4,0.02000000,0,0,0.01000000,'ga7mKGAo','2018-05-21 02:24:02','2018-05-21 02:24:02'),(286,48,'binance',1,0.02000000,0,0,0.01000000,'8UidVDLX','2018-05-21 02:24:38','2018-05-21 02:24:38');
/*!40000 ALTER TABLE `bot` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `migrations`
--

DROP TABLE IF EXISTS `migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `migrations` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `migration` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `batch` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `migrations`
--

LOCK TABLES `migrations` WRITE;
/*!40000 ALTER TABLE `migrations` DISABLE KEYS */;
INSERT INTO `migrations` VALUES (1,'2014_10_12_000000_create_users_table',1),(2,'2014_10_12_100000_create_password_resets_table',2),(3,'2017_12_07_124621_create_table_transactions',2),(4,'2017_12_08_183609_create_bot_table',3);
/*!40000 ALTER TABLE `migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `password_resets`
--

DROP TABLE IF EXISTS `password_resets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `password_resets` (
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `token` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `password_resets`
--

LOCK TABLES `password_resets` WRITE;
/*!40000 ALTER TABLE `password_resets` DISABLE KEYS */;
INSERT INTO `password_resets` VALUES ('alechaito@gmail.com','9c1tZoUq95bL2Gahy11I','2018-04-14 10:01:49'),('alechaito@gmail.com','UNRd9NeUHwpWzEo4HWXm','2018-04-14 11:21:29'),('alechaito@gmail.com','ltQb6QlL9lo0yomiNGt4','2018-04-14 11:23:24'),('alechaito@gmail.com','g0ugceN0EBzjgGlV0Gv1','2018-04-14 11:26:19'),('alechaito@gmail.com','ytmzxLNrjZ0VzHnLFL6J','2018-04-14 11:28:30'),('alechaito@gmail.com','LxTVGgsBPaZ0oheABdsM','2018-04-14 11:29:08'),('alechaito@gmail.com','LWVT2fhdcfsQU59t92Nx','2018-04-14 11:29:36'),('alechaito@gmail.com','f3jGiPnEYYzytXGyWydX','2018-04-14 11:33:52'),('alechaito@gmail.com','yDEsiFUVVsWsAKQXgyW7','2018-04-14 11:34:14'),('alechaito@gmail.com','xSKTTd0JqGTmfBytcKvY','2018-04-14 11:34:24'),('alechaito@gmail.com','HXL4NpC8L8WJ0kCjNLQR','2018-04-14 11:50:57'),('alechaito@gmail.com','hS9XXREc764BHn58w1pt','2018-04-14 11:51:13'),('alechaito@gmail.com','9jp0IAt9AqpOGFsh9EZx','2018-04-14 11:55:59'),('alechaito@gmail.com','ATxBlFneFdeKssgYMJ6w','2018-04-14 11:58:08'),('alechaito@gmail.com','79PqbW5XA5auw8ZNCDgR','2018-04-15 04:25:56'),('alechaito@gmail.com','OoE2SufRVZsFQeX2f9Zj','2018-04-15 04:27:37'),('alechaito@gmail.com','7sNjCgclIO1lihFyXs93','2018-04-15 04:35:30'),('alechaito@gmail.com','SoYHP6UvL9yw9d2qivyI','2018-04-15 04:36:17'),('alechaito@gmail.com','CFq5CIm5Nyw9Ci440r5h','2018-04-15 04:37:24');
/*!40000 ALTER TABLE `password_resets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `item_name` varchar(100) NOT NULL,
  `currency` varchar(10) NOT NULL,
  `amount` float(8,8) NOT NULL,
  `tx_id` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `status` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES (2,3,'Protrader','USD',0.00056157,'CPCD4JAKNBAG6SFR2XG0TJJEY5','34dLC3DDSt8x5gAmBhf7wyPaUgd1muATTR',-1),(3,1,'ProTraderBot-Prata-30-dias','LTC',0.32202616,'CPCD7FRYYP23OTJLRP1L569ILV','LbEptyxHX3nNkPZgVUMrwBvSomHdekC1Z4',-1),(4,1,'ProTraderBot-Prata-30-dias','LTC',0.32202616,'CPCD0QVHC1JNYYCZOOEHZKJVHM','LiP4Phctt8ftgfJW8SzfdjfhSWMZ4RwApL',-1),(5,1,'ProTraderBot-Prata-30-dias','BTC',0.00541632,'CPCD5IEOK5UO2EENOVDCG21OTX','39h4RRo7cop1PaidusRsFADAJwSKSGgejR',-1),(6,1,'ProTraderBot-Prata-30-dias','BTC',0.00545180,'CPCD3G0MZMMRXWXOTPIBPWTF7C','37FK5NUrEte6X63jzrfq8E3348ZrYR5aHw',-1),(7,1,'ProTraderBot-Prata-30-dias','LTC',0.32452637,'CPCD748PMAALPSZSJESHTYHVYV','LUR9r69WCKVoQUvpqFUEmL4x39agT9ZxQL',-1),(8,1,'ProTraderBot-Prata-30-dias','BTC',0.00543306,'CPCD2BISMHZQHZNYDCGPFA5YQK','32tr1bLpZzbYMcf4y9KYDQCrJ3U61H6Y3D',-1),(9,1,'ProTraderBot-Prata-30-dias','BTC',0.00543306,'CPCD68TPEJMVQEIXHVQ1TFMACT','3FjxNWEzkTJ8AULRaSmj7sYmSmu8bPjGpu',-1),(10,1,'ProTraderBot-Prata-30-dias','BTC',0.00543306,'CPCD7C5AYQBJUOKTPOROZD9QWA','3PdDbZj2g1Uh33CUjrGpA92FWmELwtC1nQ',-1),(11,1,'ProTraderBot-Prata-30-dias','BTC',0.00543306,'CPCD1VDRMIJNIC064JEESFL4KM','35WpHViK8hWsZKxNdkBCv9dhSC96RW6XRG',-1),(12,1,'ProTraderBot-Prata-30-dias','BTC',0.00543306,'CPCD3NRESTCJFBOWNJ87GUCO5O','3A9kZZkvF7DrUbVpnY6xK2WxMHrb8XmTN7',-1),(13,1,'ProTraderBot-Prata-90-dias','LTC',0.73813277,'CPCD2HDEXXF4HCXHSHUDYKC7HU','LPcew4PqzQ34VbqwBJSfF5HqUCTXaQ111o',-1),(14,1,'ProTraderBot-Prata-30-dias','ETH',0.07626549,'CPCD1REMHSF2BZLNE85NKKRBI6','0x05a72b59ba834be18fe3dbc8d87e3bcc5463cac9',-1),(15,1,'ProTraderBot-Prata-30-dias','BTC',0.00516778,'CPCD1LLMVEQHAHZAJR4V6P51XW','3Li4MuNF5yN6SPCRnySsxxsJVABmFiRMed',0),(16,1,'ProTraderBot-Prata-30-dias','BTC',0.00513753,'CPCD5XD2GIKYJBT7UN0UJTNSOT','3D8m3SVsySy8noYgdVPsykCAs6s894CGXe',0),(17,1,'ProTraderBot-Prata-30-dias','BTC',0.00513753,'CPCD7VTXIPEPYV4LJB4RJPZ1T3','3A7j6nTY57SDJhHckWnWJ91Fbvg5tGd9fh',0),(18,1,'ProTraderBot-Prata-30-dias','BTC',0.00514527,'CPCD2VYOFWRWAQLORJ1HPUVBUN','3Ci3Jci6hMM2LLvF81SX2tE97LLAi6skvo',0),(19,1,'ProTraderBot-Prata-30-dias','BTC',0.00514527,'CPCD7JG7AX1FPZMRHNWDSPQEKW','33WgEXUcU5gB92ZS45arvMdGQPQAhCSqta',0),(20,1,'ProTraderBot-Ouro-30-dias','BTC',0.00771790,'CPCD2DZ5WOQAWHZ6XOT5FY80ZL','32tGCNvRPtYN1zobi1JyeowVYkB7YFz4c4',0),(21,1,'ProTraderBot-Prata-30-dias','ETH',0.06865137,'CPCD6QU4ZM6PAXMYVR85QNM8JQ','0x02a7cff734ad0722953f003f5a5865dcc608eec6',0),(22,1,'ProTraderBot-Prata-30-dias','BTC',0.00514527,'CPCD50X4BRWQXXPGX2AYXIWPPG','35GygpCxzxTKEGMN4hpzBcfyw8YSYw7N3u',0),(23,1,'ProTraderBot-Prata-30-dias','BTC',0.00513755,'CPCD0G2JIVMOVMFNJX2EGZBIZC','3JLxi3ykiPPovT1mn6xX5PYmLD7WuTHTmC',0),(24,1,'ProTraderBot-Prata-30-dias','ETH',0.06886503,'CPCD3RHVIOZEWIOJ608YRJKMSK','0x90cdb5c9dc3c34a5017fe2637d4173f4a8805503',0),(25,1,'ProTraderBot-Prata-30-dias','BTC',0.00509036,'CPCD0TEJNYPPJU9HVXTIHZJUQF','3C8gLRBdB61tjSbZdEvbqDuvyKcccUePB2',0),(26,1,'ProTraderBot-Prata-30-dias','BTC',0.00509036,'CPCD676KPIZWLVRD7954KV3FBZ','3DJjfimt4FnhrV4N3YgnT3uxEx7MkSQQo2',0),(27,1,'ProTraderBot-Prata-30-dias','BTC',0.00509036,'CPCD0VSXAQUKXQV6YVOQ2ULASG','3M1sWPGr7dCwVSLDEzBm6rurbFyYmNHSPF',0),(28,1,'ProTraderBot-Prata-30-dias','BTC',0.00509036,'CPCD3ASQAFBQAKJLZQA02GPBJP','3LS1AmwQczFK7saMwbjcqWpEgLZWRAYG9S',0),(29,1,'ProTraderBot-Prata-30-dias','BTC',0.00509036,'CPCD4RVX3BWCKKCB4MCHSBWS0P','3HnFFh8sPGUwQjS5CEa3U6nttFWn4uxANN',0),(30,1,'ProTraderBot-Prata-30-dias','BTC',0.00509036,'CPCD08GIZ0YV3A1FPPDZEP3XHT','3Jr4nxdgNvrvSihXwZPhngxEckyVTteEPF',0),(31,1,'ProTraderBot-Prata-30-dias','BTC',0.00508153,'CPCD5WREGZDGIGAHCLTDXYIIVX','3KeZ4r4JT7crutTYVF3Q7nwq5R7RiAAc7q',0),(32,1,'ProTraderBot-Prata-30-dias','LTC',0.29198214,'CPCD32U5EY6NIM1QEH9IAJQF7A','LhDWJ8RviduddDS4h52yKEgbzLWfhvb4Qv',0),(33,1,'ProTraderBot-Prata-30-dias','LTC',0.29198214,'CPCD4PUYBVTLOTBJ5WSM8KZGHN','LVDcSoHjrarass1jWPWS5CQqW3CcKUEj8X',0),(34,1,'ProTraderBot-Prata-30-dias','BTC',0.00508153,'CPCD4ZVZAOC95DE0XHGYEFLDFO','3MZRAKste4Gtt27jKEADHtu8J7ADTyssf6',0),(35,1,'ProTraderBot-Prata-30-dias','BTC',0.00508153,'CPCD2VYZ8EQJOO7ZGMX1U8IYDK','3JQ1CJRb5oGYmFkQrpfGAoop8tjjHBnrsy',0),(36,1,'ProTraderBot-Ouro-90-dias','LTC',0.99152267,'CPCD6Z8FAQV1QV1EQJJ2ZRROAX','LL3D1dhRJkEPxMotVac2urwALz8j6Eo2Vt',0);
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transactions` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `bot_id` int(5) NOT NULL,
  `market` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `currency` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `buy_value` double(16,8) NOT NULL,
  `sell_value` double(16,8) DEFAULT NULL,
  `amount` double(16,8) NOT NULL,
  `status` int(5) NOT NULL DEFAULT '0',
  `date_open` timestamp NULL DEFAULT NULL,
  `date_close` timestamp NULL DEFAULT NULL,
  `buy_uuid` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `sell_uuid` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=279 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES (269,21,'BTC','STORJ',0.00010532,NULL,9494.87276870,0,NULL,NULL,NULL,NULL),(276,21,'BTC','STORJ',0.00010191,NULL,9812.57972721,0,NULL,NULL,NULL,NULL),(277,21,'BTC','STORJ',0.00010100,0.00010202,9900.99009901,1,NULL,NULL,NULL,NULL),(278,21,'BTC','STORJ',0.00010100,0.00010202,9900.99009901,1,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `remember_token` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `bit_key` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `bit_secret` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `bin_key` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `bin_secret` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `credits` float(5,2) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'alech','alechaito@gmail.com','$2y$10$5SZjpURg.xdshas0Sre0/eDx9hDoeBthr.kuDuqCxO8Ik0T0D7uxO','5b506BeiuTF3rH7Bpch9JxGEQCSSxJ0Yx9bRzxqkfBlNm4rFTGRKQ7D5Be1Z','','','','',0.00,'2017-12-08 20:03:33','2018-04-30 06:25:46'),(2,'ramon','ramon@gmail.com','$2y$10$c05sasB1Wq0xWf3GEOD3kOpylW7.6V8YLA.TFW.1h2TMJonz0zavu','Q8QUgoezziFHVlf4WgGkkHIqXc8UHqhGfSD3aV8JvBP8WYinfPa1hhA5Szps',NULL,NULL,'','0',0.00,'2018-02-16 01:45:21','2018-02-16 01:45:21'),(3,'matheus','matheus@gmail.com','$2y$10$kx.gLlUgfkVodI5lVlTnCei3SqbVXZ/ibzpkDZW4uAowIjQy2wJ2O','AEuEVgdUw8fYMaPdXVcex4tL1r3HsKGbIifkIhdGF1bryuHBhk1yyjUak4ER',NULL,NULL,'','0',0.00,'2018-02-17 14:44:11','2018-02-17 14:44:11'),(4,'gabriel','gabriel@gmail.com','$2y$10$9QJO1CmqiBgaQzRW9fv/cOfdHG2cnPXVkNSfhsCJ2A.1JN2BwEySi','pEpUt12H7wYMPIlw5Ckdhry86SOq8uV7KddplzjzmKxzd3Fpf8hQKVZS6Exr',NULL,NULL,'Du96lndpL2qQcKogKCUi7hYuFTYO06MIiZoFf6oq0guxmXJTv0tomd5yAt0xev6i','r76Q8Q35KipGTmY4BRuQqx1LDp3fWFvMjGYK9avKZnvbXVAzitWNKupzUtoQ34Uj',0.00,'2018-02-17 14:44:35','2018-04-23 05:13:07'),(5,'bruno','bruno@gmail.com','$2y$10$1DOjy4Nq4cWk9G5O3Cros.qcbS0gTRWs4NV3mKXrYmDSrTUfaiIbG',NULL,NULL,NULL,'','0',0.00,'2018-02-17 14:45:58','2018-02-17 14:45:58'),(8,'kkk','t@gmail.com','$2y$10$m4TtDS0dg/F454FOj0FqrOa1PXG1eeFM8867rumzmWnMRrqhnxZoO',NULL,NULL,NULL,'','0',0.00,'2018-02-21 22:37:15','2018-02-21 22:37:15'),(9,'kkk','s@gmail.com','$2y$10$POaYKN/LrmDlRScyNIYFqOexNEv7CaTTXuLJ7LCW1zYaq/ws6zLki',NULL,NULL,NULL,'','0',0.00,'2018-02-21 22:39:06','2018-02-21 22:39:06'),(10,'kkk','s@gmail.com','$2y$10$HXiUpHMejUush8hZnbKsi.iZmdA16KGrBlrEPcuR2.Mn92JCtrhwm',NULL,NULL,NULL,'','0',0.00,'2018-02-21 22:40:08','2018-02-21 22:40:08'),(11,'kkk','s@gmail.com','$2y$10$a/la4/B.nl6RN/HUl7d.Z.okFvS.vJbCcdxZ6yLQS0nhAMGz1Okl2',NULL,NULL,NULL,'','0',0.00,'2018-02-21 22:41:18','2018-02-21 22:41:18'),(12,'ale chaito','o@gmail.com','$2y$10$wSgosbAZJECfnpk2AH7xr.D9CAhTvwAgijTMd59GutyUP5hWC8fvO','aKTRJXAyu1HkzGpLbMkejXHsyh9NPskyTIyHU9qvRhiHUvb4NziG2o4pUmNI',NULL,NULL,'','0',0.00,'2018-02-21 22:56:38','2018-02-21 22:56:38'),(13,'aaa','lk@gmail.com','$2y$10$0sGOOeU0fkznmPAFAtmh2uMA3xpf7QBBeFaPN7KBNkU57wTxRxQY6','XcwNJGnZXzkNrLDcYfzA2mZZrirskQY3rbTbrpuwiEcW7JGwNYmuV9TiSnw8',NULL,NULL,'','0',0.00,'2018-02-21 23:02:12','2018-02-21 23:02:12'),(14,'Paulo Laux','paulo.laux@gmail.com','$2y$10$Yl/VQ9uAB.Ij.qBVpE1LCeecxT5NJ827ZOjD2gVokmTVpLsaQtZOO',NULL,NULL,NULL,'','0',0.00,'2018-02-25 17:35:30','2018-02-25 17:35:30'),(15,'Rafael Silva Gomes','phaelsg@gmail.com','$2y$10$xUoLaSg3yc8H8RSgWQX6jenOqYfJ.Fkmu9tfOCjr8fLu63L8zTIY.','NGKVOtwWBWUZRo3qjKYDgpe838TEAgToxrYoZoc05X1EawEIkZSeEnLmrS88',NULL,NULL,'','0',0.00,'2018-02-25 17:48:16','2018-02-25 17:48:16'),(16,'MAURICIO DE LIMA CARDOSO','mauriciocardoso896@gmail.com','$2y$10$KodCheMOnJxwKRqOu8GhrOtoNffv9tHUeAt4Ul3rEYSa5Ffz45ogm',NULL,NULL,NULL,'','0',0.00,'2018-02-25 18:38:40','2018-02-25 18:38:40'),(17,'marck eduardo grechi e gonsalves','marckdemolay@gmail.com','$2y$10$sYiYhOxoSoMuVUGR3pmzUOqlyAYYiP4Yii0eMzGWyG9eazCFA5ZI6',NULL,NULL,NULL,'','0',0.00,'2018-02-26 00:20:17','2018-02-26 00:20:17'),(18,'Gabriel Domene','domenee.g@gmail.com','$2y$10$9QJO1CmqiBgaQzRW9fv/cOfdHG2cnPXVkNSfhsCJ2A.1JN2BwEySi',NULL,NULL,NULL,'','0',0.00,'2018-02-26 00:44:48','2018-02-26 00:44:48'),(19,'Bruno Wagner Abranches Barros','brunogzo@hotmail.com','$2y$10$8kZx4rtKo5M4wbIRAyKMW.X1MBMtB2nszbAWXLwx0N3TMlixrhJkm',NULL,NULL,NULL,'','0',0.00,'2018-02-26 00:46:14','2018-02-26 00:46:14'),(20,'Luan Rodrigues Silva','cbluan@gmail.com','$2y$10$x62fe97jqLvB183qQtEZpuw95oSv93U3nJR.9PyKZ4L/OncuSIsne',NULL,NULL,NULL,'','0',0.00,'2018-02-26 01:39:20','2018-02-26 01:39:20'),(21,'Felipe Tremel','ftremel@hotmail.com','$2y$10$PixO5gB3DkXV.OoYsiy6g.dMRKQlcAY72os9OPRBIydna5dEfFEJW',NULL,NULL,NULL,'','0',0.00,'2018-02-26 02:15:10','2018-02-26 02:15:10'),(22,'Matheus Quiterio','matheus.quiterio@hotmail.com','$2y$10$/943b7T6NPMDywxdB/fGl.yO3AIec92Yhum/2AePKOl516YLMP5D2',NULL,NULL,NULL,'','0',0.00,'2018-02-26 03:45:41','2018-02-26 03:45:41'),(23,'Teste Trader','testetrader@t.com','$2y$10$z0EPZvmXALgEXnSGcsjNYe7B5dwNsnb35jyFxNlpvytpD2HTmBF1S',NULL,NULL,NULL,'','0',0.00,'2018-02-26 15:41:49','2018-02-26 15:41:49'),(33,'gabriel ghellere','gabriel_ghellere@hotmail.com','$2y$10$J0i.orKpfkmrD7D81PgXOuYIiMl/ZbydikF0FT1agv2CIry3S5Cx2','Vmumm7lwU5ftCOxnNeyjBuOtMUjDKTjRaLxbLLd94q0mVE3kYdBCN33PpZL6',NULL,NULL,'','0',0.00,'2018-03-14 13:23:08','2018-03-14 13:23:08'),(36,'João Carlos Freitas','jcfreitas.s@hotmail.com','$2y$10$N8KNySzA8NuDnBIcP2E4KezrqbPnOItJjuVF3D/Vw0/.5N5QI3Vum','ISh7BrfmnHqtZ4le5wXRFy5YsW8IAKqrTigN8lODujDf5kfx9nOj2zevVwmD',NULL,NULL,'','0',0.00,'2018-03-27 20:13:39','2018-03-27 20:13:39'),(37,'aaa','admin@gmail.com','$2y$10$ifQdfF46CpSFx5gjdZYvEuSYwQs0sbcXgAXOUebb1LZHRvubaQTHC','36la1mxpkIngIu6BCMVLShdK2xewQZlQhlhPd7dMlhkAn1lzp5u4H4JvwoOh',NULL,NULL,NULL,NULL,0.00,'2018-04-18 20:54:12','2018-04-18 20:54:12'),(38,'Juan Batista Diz','juan_diz2@hotmail.com','$2y$10$Ek.qGHOnDUIZ5eF8Fs6qAOhwtoBHTeCUGHdl2jzRJaZX1PMdwlg8G',NULL,NULL,NULL,NULL,NULL,0.00,'2018-04-25 21:56:07','2018-04-25 21:56:07'),(39,'Jessé rocha de freitas','diamantejesserocha@gmail.com','$2y$10$Lysn2OMN8RvepV6psM9dX.QHveaQu9PzPb8ujBE5cguB7wHeIt116',NULL,NULL,NULL,NULL,NULL,0.00,'2018-04-26 03:04:58','2018-04-26 03:04:58'),(40,'fabio alves pacheco','fab.pacheco0@gmail.com','$2y$10$1FRXyashlbYVgc1or4kxN.ZW5R09qhFXGJbk5St8V6GU4581aza02',NULL,NULL,NULL,NULL,NULL,0.00,'2018-04-26 04:36:55','2018-04-26 04:36:55'),(41,'Gustavo','protrader@atrative.com.br','$2y$10$rBDqS34mC1m9uYaRpk7l5uvoSLtJBJFUShmCurl8GsbMdD5ppwIbK',NULL,NULL,NULL,NULL,NULL,0.00,'2018-04-26 18:27:37','2018-04-26 18:27:37'),(42,'Thiago Dantas','thiago_dantas83@hotmail.com','$2y$10$QFYCElfNdYI72DfRhalpi.1d7iGPWFIXllgxfLFWhJomG4hOk1ESW',NULL,NULL,NULL,NULL,NULL,0.00,'2018-04-29 15:51:09','2018-04-29 15:51:09'),(43,'Jorge Maia','jorgeconave@gmail.com','$2y$10$k/44pIOnaivwonj6rwKv.O0p3eB9Agx3De0GJTMMN9Ncg2pwjGb0G','8qCyKQenEVsSrifWNC5f7Jnw6DkYlWdKj2cxCJHhu30wZfQoBLfmQqiWljwM',NULL,NULL,NULL,NULL,0.00,'2018-05-06 02:39:31','2018-05-06 02:39:31'),(44,'Alexandre custodio','falecomocustodio@gmail.com','$2y$10$8kv2rxVSD8BjNlXhglMj4OdZTjrgA7mkoe5lerjhNjdx3niheXXsy',NULL,NULL,NULL,NULL,NULL,0.00,'2018-05-06 21:34:19','2018-05-06 21:34:19'),(45,'Everton Lopes','elodigitalcoins@gmail.com','$2y$10$cj.rJK9jL4OdMtiHOMQbaexrccAIZt8ovOhzuOp0ArZ03ko7PBaO.',NULL,NULL,NULL,NULL,NULL,0.00,'2018-05-09 14:56:00','2018-05-09 14:56:00'),(46,'Deibson Silva','deibsonsilva001@gmail.com','$2y$10$m1CzYvokzqY/sh1rgnfkAew7R8uNlXXH3Jo9pskYsaj04/qqoF2pi','zcHioZ3f5uxJRMW3S5xx5xu9JsrttziHLqnB9TvzPplhmo4JudPdtQwM65cR',NULL,NULL,NULL,NULL,0.00,'2018-05-12 01:10:18','2018-05-12 01:10:18'),(47,'victor hortolani dos santos','victorballfield94@gmail.com','$2y$10$MkCVFAEFJCYC7/Oy6hWPBe8HzMN6QJMmIkV6cqlSZnXT7sfHbVcaK',NULL,NULL,NULL,NULL,NULL,0.00,'2018-05-19 07:00:34','2018-05-19 07:00:34'),(48,'Elisangela de Jesus Belchior','lisabelchior@gmail.com','$2y$10$RVbIl2JTzNwwOGKNs3WR8.FZF6iozhNeHIj3FrpJ067PJDuSgLwtu',NULL,NULL,NULL,NULL,NULL,0.00,'2018-05-21 02:18:58','2018-05-21 02:18:58'),(49,'dasgdsfgfdgfd','leonardo.benelli9@gmail.com','$2y$10$bKwO6Zr1cjysAc1nnimKW.LqQZYnPloNJlOy1T.lPHTuZ8H7fNHMm','aN3XFbvBqGjXD01zEsJmtIJVOdOLfP7VFoI9ZGlrnSzWt0XySQlNCRI5F1rW',NULL,NULL,NULL,NULL,0.00,'2018-05-22 00:31:36','2018-05-22 00:31:36'),(50,'hgh','michael12345608@hotmail.com','$2y$10$K6WYWYMILyVPTvQhQIQUaeySHhbpmdUexGaT9czc6bs1ckn1cFysW','8SyrF8fUkfTmLzuXlhNjahfj4bMDaZnjCkXT56RNqVXxGEfvizI5VTrvR2Lh',NULL,NULL,NULL,NULL,0.00,'2018-05-22 05:56:29','2018-05-22 05:56:29');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-12  3:38:49
