import pymysql

# Función para obtener los datos del producto por ID
def get_product_data(product_id):
    try:
        # Conectar a la base de datos MySQL
        bd = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="billify"
        )

        # Crear un cursor para ejecutar consultas en la base de datos
        mcursor = bd.cursor()
        # Crear una consulta SQL para obtener los datos del producto de la base de datos
        sql = "SELECT ID_PROD, NOM_PROD, TIP_PROD, IVA_PRO, PRE_PRO, EXIS_PRO FROM productos WHERE ID_PROD = %s"
        # Ejecutar la consulta SQL con parámetros
        mcursor.execute(sql, (product_id,))
        # Obtener el resultado de la consulta
        result = mcursor.fetchone()
        bd.close()
        return result
    except pymysql.MySQLError as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None
