-- prepares MySQL server for the project

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';