-----Crear esquema donde se guardaran las tablas de pricing----------
--CREATE SCHEMA IF NOT EXISTS pricing;

-----Crear tabla con el historio de pricing----------
CREATE TABLE item_historical_pricing (
    id SERIAL PRIMARY KEY,
    item_id VARCHAR(255),
    ord_closed_dt DATE,
    price NUMERIC(10, 2)
);


COPY item_historical_pricing (ITEM_ID, ORD_CLOSED_DT, PRICE) FROM '/precios_historicos.csv' DELIMITER ',' CSV HEADER;

CREATE ROLE appconexion WITH LOGIN PASSWORD '1234' CREATEDB;

-- Otorga todos los permisos al usuario 'appconexion' sobre el esquema 'pricing'
GRANT ALL PRIVILEGES ON SCHEMA public TO appconexion;

-- Otorga todos los permisos al usuario 'appconexion' sobre la tabla 'item_historical_pricing'
GRANT ALL PRIVILEGES ON TABLE item_historical_pricing TO appconexion;

-- Otorga permisos sobre la secuencia item_historical_pricing_id_seq
GRANT SELECT, UPDATE ON SEQUENCE item_historical_pricing_id_seq TO appconexion;
GRANT USAGE ON SEQUENCE item_historical_pricing_id_seq TO appconexion;