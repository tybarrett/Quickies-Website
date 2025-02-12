import mysql.connector

conn = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                passwd="password",
                                database="quickies",
                                auth_plugin="mysql_native_password")

def get_msgs(page_num):
    pass


def put_msg(data):
    query = f"INSERT INTO messages (`name`, `message`, `page_num`) VALUES (`{data['name']}`, `{data['msg']}`, `{data['page_num']}`);"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
