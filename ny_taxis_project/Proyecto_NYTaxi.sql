-- 1. Crear la base de datos
CREATE DATABASE nyc_taxi_practice;
USE nyc_taxi_practice;

DROP TABLE IF EXISTS trips; -- Esto borra la tabla si se creó a medias para evitar conflictos
CREATE TABLE trips (
    tpep_pickup_datetime DATETIME,
    tpep_dropoff_datetime DATETIME,
    trip_distance FLOAT,
    fare_amount FLOAT,
    tip_amount FLOAT,
    total_amount FLOAT,
    duration_seconds FLOAT
);


    
    
    

    