import MySQLdb
import time
import sys

print("Hello from administration platform, please wait for databse to initialize")
time.sleep(15)

while True:
    print("\nSelect your option:")
    print("1. Add book")
    print("2. Remove book")
    print("3. See books")
    print("4. Exit")
    option = raw_input()
    if option.strip() == '1':
        print("title, author, price, quantity, id")
        book = str(sys.stdin.readline())
        book2 = book.rstrip("\n")
        book3 = book2.split(" ")
        title = book3[0]
        author = book3[1] + " " + book3[2]
        price = int(book3[3])
        quantity = int(book3[4])
        id1 = book3[5]
        my = MySQLdb.connect(
                user = 'adm',
                passwd = 'pass',
                host = 'database',
                db = 'tema',
                port = 3306)
        cursor = my.cursor()
        sql = "INSERT INTO library(title, author, price, quantity, id) VALUES(%s, %s, %s, %s, %s)"
        values = (title, author, price, quantity, id1)
        cursor.execute(sql, values)
        my.commit()
    elif option.strip() == '2':
        print("Insert the id of the book you want to remove")
        id1 = str(raw_input())
        my = MySQLdb.connect(
                user = 'adm',
                passwd = 'pass',
                host = 'database',
                db = 'tema',
                port = 3306)
        cursor = my.cursor()
        sql = "DELETE FROM library WHERE id = %s"
        cursor.execute(sql, (id1,))
        my.commit()
    elif option.strip() == '3':
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
    elif option.strip() == '4':
        print("Bye bye")
        exit()
