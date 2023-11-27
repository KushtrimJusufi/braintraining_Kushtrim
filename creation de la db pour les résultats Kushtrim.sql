/* création de la base de donné */
DROP DATABASE if EXISTS `ma-dbpy`;
CREATE DATABASE `ma-dbpy`;

USE `ma-dbpy`;
/*création de la table*/

DROP TABLE if EXISTS `result`;

CREATE TABLE `result`(
`id` INT (10) NOT NULL AUTO_INCREMENT,
`name` VARCHAR (45) NOT NULL,
`exercise` VARCHAR (45) NOT NULL,
`date_hour` TIME NOT NULL,
`duration` TIME NULL,
`nbtrials` INT (10) NOT NULL,
`nbsuccess` INT (10) NOT NULL,
PRIMARY KEY (`id`)
);