import os

MONGO_URI = os.environ["MONGO_URI"]
MONGO_DB_NAME = "vetsalud"

REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_PORT = int(os.environ["REDIS_PORT"])

# Nombres de las colecciones.
COL_PACIENTES = "pacientes"
COL_PROPIETARIOS = "propietarios"
COL_VETERINARIOS = "veterinarios"
COL_CONSULTAS = "consultas"
COL_VACUNACIONES = "vacunaciones"
COL_STOCK = "stock_farmaceutico"
