import sqlite3


def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()


def update(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?,price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()


def search(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store WHERE item = '%s'" % item)
    result = cur.fetchall()
    conn.close()
    if result:
        return True
    else:
        return False


create_table()
print("Program using SQLite")
while True:
    n = int(input("Choose from Following:\n1.Insert\n2.View All\n3.Delete\n4.Update\n5.Exit\nEnter your choice:"))
    if n == 5:
        break
    elif n == 1:
        item1 = input("Enter item name:")
        if search(item1):
            print("Item Already Exists")
        else:
            quantity1 = int(input("Enter quantity:"))
            price1 = float(input("Enter price:"))
            insert(item1, quantity1, price1)
            print("Item Added Successfully")
        continue
    elif n == 2:
        print(view())
        continue
    elif n == 3:
        item1 = input("Enter item name:")
        if not search(item1):
            print("Item Doesnt Exists")
        else:
            delete(item1)
            print("Item Deleted Successfully")
        continue
    elif n == 4:
        item1 = input("Enter item name to update:")
        if not search(item1):
            print("Item Doesnt Exists")
        else:
            quantity1 = int(input("Enter new quantity:"))
            price1 = float(input("Enter new price:"))
            update(item1, quantity1, price1)
            print("Item Updated Successfully")
        continue
    else:
        print("Wrong Choice.Try Again")
        continue
print("Thank You for using my program!")
