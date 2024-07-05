from sqlConnection import get_sql_connection


def get_all_products(sql_connection):
    cursor = sql_connection.cursor()

    query = (
        "SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
        "FROM grocerystoreschema.products "
        "INNER JOIN grocerystoreschema.uom ON products.uom_id = uom.uom_id"
    )

    cursor.execute(query)
    response = []

    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            "product_id": product_id,
            "name": name,
            "uom_id": uom_id,
            "price_per_unit": price_per_unit,
            "uom_name": uom_name
        })

    return response


def insert_new_product(sql_connection, product):
    cursor = sql_connection.cursor()

    #handling parameterized queries
    query = (
        "INSERT INTO grocerystoreschema.products (name, uom_id, price_per_unit) "
        "VALUES (%s, %s, %s)"
    )

    data = (product["product_name"], product["uom_id"], product["price_per_unit"])
    cursor.execute(query, data)
    sql_connection.commit()
    return cursor.lastrowid #returns the row_id of the last row that was inserted


def delete_product(sql_connection, product_id):
    cursor = sql_connection.cursor()
    query = ("DELETE FROM grocerystoreschema.products WHERE product_id = " + str(product_id))
    cursor.execute(query)
    sql_connection.commit()


#making the output modular
if __name__ == "__main__":
    connection = get_sql_connection()

    print(get_all_products(connection))

    print(delete_product(connection, 14))

    connection.close()

"""
    print(
        insert_new_product(
            connection,
            {
                "product_name": "cabbage",
                "uom_id": 1,
                "price_per_unit": 10,
            }
        )
    )
"""
