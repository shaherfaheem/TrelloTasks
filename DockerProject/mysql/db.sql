CREATE DATABASE databasetest;
USE databasetest;

CREATE TABLE tasks (id bigint(20) PRIMARY KEY NOT NULL AUTO_INCREMENT, task varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL, employee varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL, status varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL, priority varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL, startdate varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL, duration varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL, deadline varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=2343;
CREATE TABLE accounts (id bigint(20) PRIMARY KEY NOT NULL AUTO_INCREMENT, uname varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL, email varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL, pword varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=2343;
