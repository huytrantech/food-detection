import pymongo


def init_client(host="localhost", port=27017, username="", password=""):
    conn_auth = ""
    if len(username) > 0 and len(password) > 0:
        conn_auth = "{}:{}@".format(username, password)
    connection_str = "mongodb://{}{}:{}/".format(conn_auth, host, port)
    return pymongo.MongoClient(connection_str)

