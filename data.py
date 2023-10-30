import sqlite3 as sq


# создает таблицу, если она еще не создана.
def create_data():
    with sq.connect("id_table.db") as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
                chat_id INTEGER,
                user_id INTEGER PRIMARY KEY AUTOINCREMENT)""")


# функция возращает список кортежей. в кортеже возращается id чата, пользователя.
def return_users_id(chat):
    create_data()
    with sq.connect("id_table.db") as con:
        cur = con.cursor()
        cur.execute(
            "SELECT chat_id, user_id FROM users WHERE chat_id = ?", (chat,))
        members = [member[1] for member in cur]
        return members


# функция записывает в БД пользователя, его группу
def reg_users_id(chat, users):
    create_data()
    with sq.connect("id_table.db") as con:
        cur = con.cursor()
        for user in users:
            cur.execute(
                "REPLACE INTO users (chat_id, user_id) VALUES(?, ?)", (chat, user))


def delete_users_id(chat):  # функция удаляет из БД пользователей
    create_data()
    with sq.connect("id_table.db") as con:
        cur = con.cursor()
        cur.execute(
            "DELETE FROM users WHERE chat_id = ?", (chat))


def clear_table():  # функция очищает БД
    create_data()
    with sq.connect("id_table.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM users")
        con.commit()
