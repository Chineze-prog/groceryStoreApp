import mysql.connector

#if this function is called multiple times, it will create multiple connections,
# so to prevent that we made a global variable
__cnx = None


def get_sql_connection():
    global __cnx  #for global variables use __

    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='Chinezesqlrootpw@1',
                                      host='127.0.0.1',
                                      database='grocerystoreschema')

    return __cnx
