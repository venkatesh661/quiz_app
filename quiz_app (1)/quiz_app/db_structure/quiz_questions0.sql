CREATE DATABASE  IF NOT EXISTS `quiz` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `quiz`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: quiz
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questions` (
  `qid` int NOT NULL AUTO_INCREMENT,
  `subject` varchar(45) DEFAULT NULL,
  `question` longtext,
  `option1` varchar(500) DEFAULT NULL,
  `option2` varchar(500) DEFAULT NULL,
  `option3` varchar(500) DEFAULT NULL,
  `option4` varchar(500) DEFAULT NULL,
  `answer` int DEFAULT NULL,
  `bcol` varchar(45) DEFAULT 'white',
  `status` varchar(45) DEFAULT '0',
  PRIMARY KEY (`qid`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (1,'Python','Which of the following is the correct extension of the Python file?','.python','.pl','.py','.p',3,'white','0'),(2,'Python','Which of the following character is used to give single-line comments in Python?','//','#','!','/*',2,'white','0'),(4,'Python','Which keyword is used for function in Python language?','Function','def','Fun','Define',2,'white','0'),(5,'Python','What does pip stand for python?','Pip Installs Python','Pip Installs Packages','Preferred Installer Program','All of the mentioned',3,'white','0'),(6,'Python','Which of the following functions is a built-in function in python?','factorial()','print()','seed()','sqrt()',2,'white','0'),(7,'Python',' Which of the following is not a core data type in Python programming?','Tuples','Lists','Class','Dictionary',3,'white','0'),(8,'Python','Which of these is the definition for packages in Python?','A set of main modules','A folder of python modules','A number of files containing Python definitions and statements','A set of programs making use of Python modules',2,'white','0'),(9,'Python','Which one of the following is not a keyword in Python language?','pass',' eval','assert','nonlocal',2,'white','0'),(11,'Python','Which of the following is used to define a block of code in Python language?','Indentation','Key','Brackets','All of the mentioned',1,'white','0'),(17,'Chemistry','Full form of H2O ?','hydrogen monoxide','helium dioxide','mineral water','dihydrogen monoxide',4,NULL,'0'),(18,'Chemistry','hydrogen number ?','2','3','7','9',2,NULL,'0');
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-09 10:07:41
