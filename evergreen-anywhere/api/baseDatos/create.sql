CREATE TABLE activo (
  id    VARCHAR(20)    PRIMARY KEY,
  nombre    VARCHAR(50),
  cantidad     INTEGER(10),
  tipo      INTEGER(10),
  fecha_adquisicion        TIMESTAMP   NOT NULL,
  valor_Compra      INTEGER(10),
  depreciacion_anual         FLOAT(10),
  precio_final       INTEGER(10)
  
)