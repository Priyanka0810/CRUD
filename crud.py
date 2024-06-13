import mysql.connector
from tabulate import tabulate
con = mysql.connector.connect(host="localhost", user="root", password="pri@99", database="python_db")

def insert(name,age,city):
    res = con.cursor()
    sql = "INSERT INTO users(NAME1, AGE, CITY) VALUES(%s,%s,%s)"
    user = (name, age, city)
    res.execute(sql,user)
    con.commit()
    print("----------------------------------")
    print("Data Inserted Successfully ")
    print("----------------------------------")

def update(name,age,city,id):
    res = con.cursor()
    sql = "UPDATE users SET NAME1=%s, AGE=%s, CITY=%s WHERE ID=%s"
    user = (name, age, city,id)
    res.execute(sql,user)
    con.commit()
    print("----------------------------------")
    print("Data Updated Successfully ")
    print("----------------------------------")


def select():
    res = con.cursor()
    sql = "SELECT * FROM users"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))
    print("----------------------------------")

def delete(id):
    res = con.cursor()
    sql = "DELETE FROM users WHERE ID = %s"
    user = (id,)
    res.execute(sql,user)
    con.commit()
    print("----------------------------------")
    print("Data Deleted Successfully ")
    print("----------------------------------")


while True:
    print("1-->Insert data")
    print("2-->Update data")
    print("3-->Select data")
    print("4-->Delete data")
    print("5-->Exit")
    print("----------------------------------")


    choice = int(input("Enter your choice : "))
    print("----------------------------------")

    if choice == 1:
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        city = input("Enter City : ")
        insert(name,age,city)

    elif choice == 2:
        id = input("Enter ID : ")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        city = input("Enter City : ")
        update(name,age,city,id)

    elif choice == 3:
        select()

    elif choice == 4:
        id = input("Enter ID : ")
        delete(id)

    elif choice == 5:
        quit()

    else:
        print("Invalid Selection. Please Try Again!")
