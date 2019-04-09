import MySQLdb
import time
import sys

print("Hello, dear client, please wait for databse to initialize")
time.sleep(15)

while True:
    print("\nSelect your option:")
    print("1. Buy book")
    print("2. See books")
    print("3. Exit")
    option = raw_input()
    if option.strip() == '1':
        print("Please enther the id of the book")
        book = str(sys.stdin.readline())
        my = MySQLdb.connect(
                user = 'adm',
                passwd = 'pass',
                host = 'database',
                db = 'tema',
                port = 3306)
        cursor = my.cursor()
        sql = """UPDATE library SET quantity = quantity - 1 WHERE id = %s"""
        values = (book.rstrip(), )
        cursor.execute(sql, values)
        my.commit()
        print(cursor.rowcount, "record(s) affected")
    elif option.strip() == '2':
        books = []
        my = MySQLdb.connect(
                user = 'adm',
                passwd = 'pass',
                host = 'database',
                db = 'tema',
                port = 3306)
        cursor = my.cursor()
        cursor.execute("select * from library") 
        res = cursor.fetchall()
        for x in res:
            books.append(list(x))
        for x in books:
            print(str(x))
    elif option.strip() == '3':
        print("Bye bye")
        exit()
