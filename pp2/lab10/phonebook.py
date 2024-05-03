import psycopg2
import os
import csv
from config import load_config



def collecting_info():
        
        """ Извлекать данные из таблицы поставщиков """
        config = load_config()
        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT user_id,name,phone_number FROM phonebook ORDER BY user_id")
                    rows = cur.fetchall()

                    print("The number of parts : ",cur.rowcount)
                    for row in rows:
                        print(row)
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)


def from_csv():
    command = """
        INSERT INTO phonebook(name, phone_number) 
        VALUES(%s, %s)
        """
    try:
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="test") as conn:
            with conn.cursor() as cur:
                script_dir = os.path.dirname(__file__)
                file_path = os.path.join(script_dir, r'C:\Users\Renata2004\Desktop\py\pp2\lab10\numbers.csv')
                with open(file_path, 'r', newline='') as file:
                    rows = csv.reader(file)

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


    

def update_info(user_id, name, phone_number):
    """ Обновление контакта """

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
    """ Удаление контакта """
    rows_deleted = 0
    sql = 'DELETE FROM phonebook WHERE user_id = %s'
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (user_id,))
                rows_deleted = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return rows_deleted


def insert_contact(name, phone_number):
    """ Вставка нового контакта в таблицу phonebook """
    sql = """INSERT INTO phonebook(name, phone_number)
             VALUES(%s, %s) RETURNING user_id;"""
    
    user_id = None
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Выполнение SQL-запроса INSERT
                cur.execute(sql, (name, phone_number))

                # Получение сгенерированного идентификатора
                row = cur.fetchone()
                if row:
                    user_id = row[0]

                # Подтверждение изменений в базе данных
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return user_id
    

if __name__ == '__main__':
    operation = input("Выберите\n1 - записать контакт\n2 - обновить контакт\n3 - пройтись по всем контактам\n4 - удаление контакта\n5 - добавить данные из csv\n")
    if operation == "1":
        name = input("Введите имя нового контакта : ")
        phone_number = int(input("Введите номер телефон : "))
        user_id = insert_contact(name,phone_number)  # Пример вызова функции
        if user_id is not None:
            print("Контакт успешно добавлен. ID:", user_id)
        else:
            print("Ошибка при добавлении контакта.")
    elif operation == "2":
        user_id = input("Введите айди контакта которого хотите обновить : ")
        name = input("Введите новое имя для контакта : ")
        phone_number = int(input("Введите новый номер телефон : "))
        updt = update_info(user_id,name,phone_number)
        if updt is not None:
            print("Контакт успешно изменен")
        else:
            print("Ошибка при изменений")
    elif operation == "3":
        clct = collecting_info()
    elif operation == "4":
        user_id = int(input("Введите айди контакта которого хотите удалить : "))
        dlt = delete_info(user_id)
        if dlt is not None:
            print("Контакт успешно удален")
        else:
            print("Ошибка при удалений")    
    elif operation == "5":
        csvinf = from_csv()



