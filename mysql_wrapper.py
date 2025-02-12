import mysql.connector

conn = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                passwd="password",
                                database="quickies",
                                auth_plugin="mysql_native_password")

def get_msgs(page_num):
    query = f"SELECT * FROM messages WHERE page_num=%s;"
    cursor = conn.cursor(prepared=True)
    cursor.execute(query, (page_num, ))
    results = cursor.fetchall()
    print(results)
    return results


def put_msg(data):
    # query = f"INSERT INTO messages (user_name, message, page_num) VALUES ('{data['name']}', '{data['msg']}', '{data['page_num']}');"
    query = f"INSERT INTO messages (user_name, message, page_num) VALUES (%s, %s, %s');"
    cursor = conn.cursor(prepared=True)
    cursor.execute(query, (data["name"], data["msg"], data["page_num"]))
    conn.commit()
    cursor.close()
