#Crear tabla Cars

 
CREATE TABLE `lab_mysql`.`Cars` (
  `carsID` INT NOT NULL,
  `VIN` VARCHAR(45) NOT NULL,
  `manufacter` VARCHAR(45) NULL,
  `model` VARCHAR(45) NULL,
  `year` VARCHAR(45) NULL,
  `color` VARCHAR(45) NULL,
  PRIMARY KEY (`carsID`));


#Crear tabla Customers

CREATE TABLE `lab_mysql`.`Customers` (
  `customers ID` INT NOT NULL,
  `Customer ID` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `adress` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `state/province` VARCHAR(45) NULL,
  `country` VARCHAR(45) NULL,
  `postal` INT NULL,
  PRIMARY KEY (`customers ID`));


#Crear tabla Salespersons

CREATE TABLE `lab_mysql`.`Salespersons` (
  `Salespersons ID` INT NOT NULL,
  `staff ID` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `store` VARCHAR(45) NULL,
  PRIMARY KEY (`Salespersons ID`));


#Crear tabla de Invoices


CREATE TABLE `lab_mysql`.`Invoices` (
  `Invoices ID` INT NOT NULL,
  `Invoice Number` INT NOT NULL,
  `date` DATETIME NULL,
  `car` INT NULL,
  `costumer` INT NULL,
  `sales person` INT NULL,
  PRIMARY KEY (`Invoices ID`));














