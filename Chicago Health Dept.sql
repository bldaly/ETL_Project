-- Create and use inspection_db
CREATE DATABASE inspection_db;
USE inspection_db;

-- Create Two Tables
CREATE TABLE food_violation (
  Inspection_id INT PRIMARY KEY,
  DBA_Name TEXT,
  Rating TEXT,
  Price_point INT,
  Risk INT,
  Address TEXT,
  City TEXT,
  State TEXT,
  Zip INT,
  Inspection TEXT,
  Results TEXT,
  Latitude INT,
  Longitude INT
  );
  
  drop table food_violation
  
  SELECT * from food_violation

CREATE TABLE county (
  id INT PRIMARY KEY,
  county_name TEXT,
  license_count INT,
  county_id INT
);