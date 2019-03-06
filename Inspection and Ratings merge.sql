CREATE DATABASE ETLproject_db;
USE ETLproject_db;

create TABLE inspection (
  Inspection_id varchar(50),
  DBA_Name varchar(50),
  Risk varchar(50),
  Address varchar(50),
  Inspection_Date varchar(100),
  Results VARCHAR(50),
  Latitude float,
  Longitude float
);
  
select * from inspection

create TABLE reviews (
  Inspection_ID varchar(50),
  Rest_name varchar(50),
  Latitude varchar(100),
  Longitude varchar(100),
  Ratings varchar(50)
  );
  
select * from reviews
  
SELECT i.Inspection_id, i.DBA_Name, i.Risk, i.Address, i.Results, i.Inspection_Date, r.ratings
from inspection i
JOIN reviews r ON
i.Inspection_id=r.Inspection_ID;









  