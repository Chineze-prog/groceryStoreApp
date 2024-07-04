import mysql.connector

cnx = mysql.connector.connect(user='root', password='Chinezesqlrootpw@1',
                              host='127.0.0.1',
                              database='grocerystoreschema')

cursor = cnx.cursor()

query = (
    "SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
    "FROM grocerystoreschema.products "
    "INNER JOIN grocerystoreschema.uom ON products.uom_id = uom.uom_id"
)

cursor.execute(query)

for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
    print(product_id, name, uom_id, price_per_unit, uom_name)

cnx.close()

#making the output modular

