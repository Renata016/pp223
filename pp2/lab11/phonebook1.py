import psycopg2
from config import load_config


def collecting_info():
    """Извлекать данные из таблицы поставщиков"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT phonebook.user_id, name, phone_number FROM phonebook ORDER BY user_id")
                rows = cur.fetchall()

                print("The number of parts : ", cur.rowcount)
                for row in rows:
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def update_info(user_id, name, phone_number):
    """Обновление контакта"""
    update_row_count = 0

    sql = """UPDATE phonebook
             SET name = %s, phone_number = %s
             WHERE user_id = %s"""
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Выполнение SQL-запроса UPDATE
                cur.execute(sql, (name, phone_number, user_id))
                update_row_count = cur.rowcount

            # Подтверждение изменений в базе данных
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return update_row_count


def delete_info(user_id):
    """Удаление контакта"""
    rows_deleted = 0
    sql = 'DELETE FROM phonebook WHERE user_id = %s'
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (user_id,))
                rows_deleted = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return rows_deleted


def update_or_insert_contact(name, phone_number):
    """Обновление номера телефона существующего контакта или вставка нового контакта"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Проверяем существует ли контакт с таким именем
                cur.execute("SELECT user_id FROM phonebook WHERE name = %s", (name,))
                existing_contact = cur.fetchone()
                if existing_contact:
                    # Если контакт существует, обновляем его номер телефона
                    cur.execute("UPDATE phonebook SET phone_number = %s WHERE name = %s", (phone_number, name))
                else:
                    # Если контакт не существует, вставляем новый контакт
                    cur.execute("INSERT INTO phonebook (name, phone_number) VALUES (%s, %s) RETURNING user_id",
                                (name, phone_number))
                    user_id = cur.fetchone()[0]
                    return user_id  # Возвращаем идентификатор нового пользователя
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def search_records(pattern):
    """Поиск записей по шаблону"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT user_id, name, phone_number FROM phonebook WHERE name LIKE %s OR phone_number LIKE %s",
                            (f'%{pattern}%', f'%{pattern}%'))
                rows = cur.fetchall()

                print("Matching records:")
                for row in rows:
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def insert_or_update_user(name, phone_number):
    """Вставка нового пользователя по имени и телефону, обновление телефона, если пользователь уже существует"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Проверяем существует ли контакт с таким именем
                cur.execute("SELECT user_id FROM phonebook WHERE name = %s", (name,))
                existing_contact = cur.fetchone()
                if existing_contact:
                    # Если контакт существует, обновляем его номер телефона
                    cur.execute("UPDATE phonebook SET phone_number = %s WHERE name = %s", (phone_number, name))
                    print("Контакт успешно обновлен.")
                else:
                    # Если контакт не существует, вставляем новый контакт
                    cur.execute("INSERT INTO phonebook (name, phone_number) VALUES (%s, %s)", (name, phone_number))
                    print("Новый контакт успешно добавлен.")
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def insert_many_users(users):
    """Вставка нескольких новых пользователей по списку имени и телефона"""
    config = load_config()
    incorrect_data = []
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for user in users:
                    name, phone_number = user
                    if len(str(phone_number)) != 10:  # Checking correctness of phone number
                        incorrect_data.append(user)
                    else:
                        cur.execute("INSERT INTO phonebook (name, phone_number) VALUES (%s, %s)", (name, phone_number))
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return incorrect_data


def query_with_pagination(limit, offset):
    """Запрос данных из таблиц с пагинацией (по лимиту и смещению)"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT user_id, name, phone_number FROM phonebook LIMIT %s OFFSET %s", (limit, offset))
                rows = cur.fetchall()

                print("Paginated records:")
                for row in rows:
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)



def delete_by_username_or_phone(pattern): 
    """Удаление данных из таблиц по имени пользователя или номеру телефона""" 
    config = load_config()  # Предположим, что функция load_config определена где-то в вашем коде 
    try: 
        with psycopg2.connect(**config) as conn: 
            with conn.cursor() as cur: 
                cur.execute("DELETE FROM phonebook WHERE name = %s OR phone_number = %s", (pattern, pattern)) 
                if cur.rowcount == 0: 
                    print("There is no such contact") 
                else: 
                    conn.commit() 
                    print("Successfully deleted") 
    except (Exception, psycopg2.DatabaseError) as error: 
        print(error)


if __name__ == '__main__':
    operation = input("Select\n1 - record contact\n2 - update contact\n3 - go through all contacts\n4 - delete contact\n"
                      "5 - search records\n6 - insert or update user\n7 - insert multiple users\n"
                      "8 - paginated data query\n9 - delete data by user name or phone number\n")

    if operation == "1":
        name = input("Enter new contact name : ")
        phone_number = int(input("Enter a phone number: "))
        user_id = update_or_insert_contact(name, phone_number)  # Пример вызова функции
        if user_id is not None:
            print("Contact is added or updated. ID:", user_id)
        else:
            print("An error.")
    elif operation == "2":
        user_id = input("Enter the ID of the contact you want to add : ")
        name = input("Enter new contact name : ")
        phone_number = int(input("Enter new phone number : "))
        updt = update_info(user_id, name, phone_number)
        if updt is not None:
            print("THe contact is edited successfully")
        else:
            print("An error")
    elif operation == "3":
        clct = collecting_info()
    elif operation == "4":
        user_id = int(input("ID of the contact you want to delete: "))
        dlt = delete_info(user_id)
        if dlt is not None:
            print("The contact is successfully deleted")
        else:
            print("An error")
    elif operation == "5":
        pattern = input("Enter a template to search for records: ")
        search_records(pattern)
    elif operation == "6":
        name = input("Enter a user name: ")
        phone_number = input("Enter user's phone number: ")
        insert_or_update_user(name, phone_number)
    elif operation == "7":
        users = []
        n = int(input("Enter a number of users "))
        for i in range(n):
            name = input("Enter a name of a user: ")
            phone_number = input("Enter user's phone number: ")
            users.append((name, phone_number))
        incorrect_data = insert_many_users(users)
        if incorrect_data:
            print("The following data was entered incorrectly:", incorrect_data)
    elif operation == "8":
        limit = int(input("Enter the record limit: "))
        offset = int(input("Enter the offset: "))
        query_with_pagination(limit, offset)
    elif operation == "9":
        pattern = input("Enter the user name or phone number to delete: ")
        delete_by_username_or_phone(pattern)