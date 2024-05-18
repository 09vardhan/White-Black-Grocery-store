-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: ecom
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `additems`
--

DROP TABLE IF EXISTS `additems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `additems` (
  `item_id` binary(16) NOT NULL,
  `item_name` longtext,
  `dis` longtext NOT NULL,
  `qyt` int NOT NULL DEFAULT '0',
  `category` enum('Electronics','Grocery','Fashion','Home') DEFAULT NULL,
  `price` int NOT NULL,
  `addedby` varchar(50) DEFAULT NULL,
  `imgid` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`item_id`),
  KEY `addedby` (`addedby`),
  CONSTRAINT `additems_ibfk_1` FOREIGN KEY (`addedby`) REFERENCES `admindetails` (`admin_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `additems`
--

LOCK TABLES `additems` WRITE;
/*!40000 ALTER TABLE `additems` DISABLE KEYS */;
INSERT INTO `additems` VALUES (_binary ' π’ía\ÓΩw\‹!H[\Ò','ASIAN Future-01 White Blue Running,Sports,Walking,Gym Shoes for Men','Colour: Multi-Coloured Regular: Comfort Ocassion: Casual Material: Mesh',890,'Fashion',599,'anusha@codegnan.com','Q9eS0t.jpg'),(_binary '8	\„íb\ÓΩw\‹!H[\Ò','Tata Sampann Unpolished Chana Dal, 1kg','RICH TASTE: Tata Sampann Chana Dal is delicious in taste UNPOLISHED DALS: Tata Sampann dals do not undergo any artificial polishing with water, oil or leather, thereby retaining their goodness and wholesome character 5-STEP PROCESS FOR STRINGENT QUALITY CHECKS: Ensures that the grains of dal are uniform and of premium quality CHEF RECOMMENDED: Recommended by Chef Sanjeev Kapoor and Chef Ranveer Brar AMAZING RECIPES: Used in a variety of snacks, salads, soups, and many more ALSO TRY: Try toor dal, urad dal, moong dal, masoor dal, rajma, etc COMMONLY SEARCHED TOPICS: tata sampann chana dal, tata sampann unpolished chana dal, chana dal 1 kg, chana dal, dal, tata sampann dal, tata sampann pulses',8700,'Grocery',118,'anusha@codegnan.com','I2gI3y.jpg'),(_binary 'X	◊∂í[\ÓΩw\‹!H[\Ò','anusha','white shoe for women daily wear',90,'Grocery',890,'anusha@codegnan.com','H7jI3b.jpg'),(_binary 'XhKëí`\ÓΩw\‹!H[\Ò','Max Women Solid Kurta with Crocheted Neck','ManufacturerLifestyle Int Pvt Ltd, Lifestyle Int Pvt Ltd, 77 Degree Town Centre, Building No. 3, West Wing, Off HAL Airport Road, Yamlur, Bangalore-560037 1800-123-1444 PackerLifestyle Int Pvt Ltd, 77 Degree Town Centre, Building No. 3, West Wing, Off HAL Airport Road, Yamlur, Bangalore-560037 1800-123-1444 ImporterLifestyle Int Pvt Ltd, 77 Degree Town Centre, Building No. 3, West Wing, Off HAL Airport Road, Yamlur, Bangalore-560037 1800-123-1444 Item Weight250 g Item Dimensions LxWxH16 x 12 x 5 Centimeters Included Components Kurta Generic Name Blouse',780,'Fashion',290,'anusha@codegnan.com','D8dQ4x.jpg'),(_binary 'f‘≠`ía\ÓΩw\‹!H[\Ò','Nivia Flash 2.0 Badminton Shoes for Men, Rubber Sole with PVC Synthetic Leather Upper and mesh for Sports, Badminton, Volleyball, Squash, Table Tennis, (Blue) UK-9','Die-Cut soft NR EVA sock liner laminated with Polyester fabric. Soft cushion NR EVA Inner insole. Die-Cut soft NR EVA sock liner laminated with Polyester fabric. PVC synthetic leather Upper with mesh. TOE forepart stitching on sole lip gives provides support toe area.',670,'Fashion',949,'anusha@codegnan.com','F1eB4l.jpg'),(_binary 'm\Ó0míb\ÓΩw\‹!H[\Ò','India Gate Basmati Rice Rozana, 5kg','India gate basmati rice - rozana South material features:vegetarian',5000,'Grocery',521,'anusha@codegnan.com','T9wG5r.jpg'),(_binary '•¶!ûíb\ÓΩw\‹!H[\Ò','INDULGE HOMES - White Vase/Flower Vase/Pampas Grass Vase/Ceramic Vase/Round Shaped Vase/Home Decor Centrepiece/Decor Showpiece Donut Vase 6 & 8 Inches (Pack of 2)','THE CLASS A CERAMIC VASES - The flower vase is made of high-quality class A ceramic with glazed finish, with a smooth surface and a clean and solid white, full of artistic sense, showing you a simple, elegant and modern style. HANDMADE CERAMIC VASES MADE BY PROFESSIONALS - We are a company with many years of professional experience in designing, developing and manufacturing the highest quality home vase decorations. EXQUISITE & FLAWLESS DETAILS - Each Pampas Grass decorative vase is professionally designed and handcrafted to form clean and elegant golden ratio lines, fired at 1700 degrees, making it a unique work of art.',675,'Home',849,'anusha@codegnan.com','D9wO0l.jpg'),(_binary '¨Ω√ëí_\ÓΩw\‹!H[\Ò','Max Women Printed Three-Quarter Sleeves Straight Kurta','Colour:AQUA Fabric:100% RAYON Wash : Machine Wash Print : Printed MAX Women Printed Three-quarter Sleeves Straight Kurta',890,'Fashion',780,'anusha@codegnan.com','A0iW6o.jpg'),(_binary '±x2Lía\ÓΩw\‹!H[\Ò','ZEBRONICS Zeb Evolve Wireless Bluetooth in Ear Neckband Earphone, Rapid Charge, Dual Pairing, Magnetic earpiece,Voice Assistant with Mic (Blue)','n Ear Wireless Neckband Earphone Rapid Charge Function: 2 hours usage in 10 minutes charge Up to 17H Playback at 50% Volume Seamless Connectivity with BT5.0 Magnetic Earpiece, Charging time - 1h, Talk time - 12H, Standby time - 40H Dual Pairing Feature Call Function with Media/Volume Controls',896,'Electronics',499,'anusha@codegnan.com','Y1eQ0z.jpg'),(_binary '¡\ˆç˝íe\ÓΩw\‹!H[\Ò','Ac','cool and clean',780,'Electronics',67000,'anusha@codegnan.com','M6lE7l.jpg'),(_binary '‘û	eíb\ÓΩw\‹!H[\Ò','Global Grabbers Polyresin Sitting Buddha Idol Statue Showpiece for Homedecor Decoration Gift Gifting Items-Org_Blk-Bs2-(00), Multicolored','Material: Polyresin Size (L x W x H): 18.5 cm x 8 cm x 24 cm: Weight : 300 gm Colour: Orange Black Care Instruction: Can be washed with water or Wipe with soft clean cloth Made In India',765,'Home',298,'anusha@codegnan.com','G9cS0l.jpg'),(_binary '¸\ﬂ\Œía\ÓΩw\‹!H[\Ò','SOLARA Large Digital Air Fryer for Home Kitchen with 6 Pre set modes for Indian cooking | 3.5L basket |Mobile app with 100+ recipe eBook and Videos | Green','üå≠ HEALTHIER FRIED FOOD: Food cooked in a SOLARA Digital Air Fryer contains up to 85% less fat than traditionally fried foods without losing the delicious tastes and crispy textures. Rapid 360¬∞ air circulation cooks your food more quickly than ovens and with a minuscule amount of oil compared to deep-fried foods. üçü SLEEK AND MODERN LOOK - 3.5 Liters with advanced touch screen menu. Take the guesswork out of cooking with the built-in touch screen menu featuring 6 cooking presets: Fries/Chips, Paneer, Chicken, Steak, Shrimp, Cake, Fish, and Pizza. Equipped with a wide temperature range from 180Fahrenheit to 400Fahrenheit in 10 degree increments and a cooking timer up to 30 minutes üç∞ FREE RECIPE eBOOK and VIDEOS - Recipes in ‡∞§‡±Ü‡∞≤‡±Å‡∞ó‡±Å ‡§π‡§ø‡§®‡•ç‡§¶‡•Ä ‡ÆÆ‡Æø‡Æ¥‡Øç ‡≤ï‡≤®‡≥ç‡≤®‡≤° ‡¥Æ‡¥≤‡¥Ø‡¥æ‡¥≥‡¥Ç We made a 100 page eBook and VIDEOS focused on Indian delicacies with emphasis on local cuisines. All these recipes are tried and tested in our Kitchen. We want to show how Indian delicacies can be made oil free, healthier with our Digital Air Fryer. Comes with non-stick pan equipped with a cool touch handle and button guard to prevent accidental detachment. Shake and flip contents in the middle of your cooking program with the detachable frying basket SOLARA HOME Mobile App - Available for iOS and Android play store. We have more than 30 video recipes and 100+ recipes. Also, you get access to Home Fitness and eBooks',670,'Electronics',3799,'anusha@codegnan.com','N1mH3r.jpg');
/*!40000 ALTER TABLE `additems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admindetails`
--

DROP TABLE IF EXISTS `admindetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admindetails` (
  `admin_id` varchar(6) NOT NULL,
  `admin_name` varchar(20) NOT NULL,
  `admin_email` varchar(50) NOT NULL,
  `admin_mobile` bigint NOT NULL,
  `password` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`admin_email`),
  UNIQUE KEY `admin_id` (`admin_id`),
  UNIQUE KEY `admin_mobile` (`admin_mobile`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admindetails`
--

LOCK TABLES `admindetails` WRITE;
/*!40000 ALTER TABLE `admindetails` DISABLE KEYS */;
INSERT INTO `admindetails` VALUES ('R2yB5v','rishi','anusha@codegnan.com',1234567891,'12');
/*!40000 ALTER TABLE `admindetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contactus`
--

DROP TABLE IF EXISTS `contactus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contactus` (
  `name` varchar(30) NOT NULL,
  `emailid` varchar(40) NOT NULL,
  `message` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contactus`
--

LOCK TABLES `contactus` WRITE;
/*!40000 ALTER TABLE `contactus` DISABLE KEYS */;
INSERT INTO `contactus` VALUES ('rishi','anusha@codegnan.com','contact'),('rishi','anusha@codegnan.com','i need to create account how could i do it ?');
/*!40000 ALTER TABLE `contactus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `ordid` bigint NOT NULL AUTO_INCREMENT,
  `itemid` binary(16) DEFAULT NULL,
  `item_name` longtext,
  `qyt` int DEFAULT NULL,
  `total_price` bigint DEFAULT NULL,
  `user` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`ordid`),
  KEY `itemid` (`itemid`),
  KEY `user` (`user`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`itemid`) REFERENCES `additems` (`item_id`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`user`) REFERENCES `users` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,_binary ' π’ía\ÓΩw\‹!H[\Ò','ASIAN Future-01 White Blue Running,Sports,Walking,Gym Shoes for Men',1,599,'rishi');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `itemid` binary(16) NOT NULL,
  `user` varchar(25) NOT NULL,
  `title` tinytext,
  `review` text,
  `rating` int DEFAULT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`itemid`,`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (_binary '¨Ω√ëí_\ÓΩw\‹!H[\Ò','rishi','product feedback','it was good but a bit poor fabric',3,'2023-12-04 10:47:22'),(_binary '\«	ê\Õ\ÓΩw\‹!H[\Ò','rishi','product feedback','good product',4,'2023-12-02 11:59:45');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` binary(16) DEFAULT NULL,
  `user_name` varchar(25) NOT NULL,
  `u_mobile` bigint DEFAULT NULL,
  `email` varchar(20) NOT NULL,
  `gender` enum('M','F','NAN') DEFAULT NULL,
  `address` varchar(256) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`user_name`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (_binary '\·j˚£ír\ÓΩw\‹!H[\Ò','rishi',6304061929,'anusha@codegnan.com','M','vij','12');
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

-- Dump completed on 2023-12-09 16:43:55
