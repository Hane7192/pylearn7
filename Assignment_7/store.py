
import qrcode
PRODUCTS = []
bill = []


def read_from_database():
    f = open("database.txt", "r")

    for line in f:
        result = line.split(",")
        my_dict = {"code": result[0], "name": result[1], "price": result[2], "count": result[3]}
        PRODUCTS.append(my_dict)

    f.close()

def write_to_database():
    f = open("database.txt", "w")
    f = open("database.txt", "a")
    for product in PRODUCTS:
        line = str(product["code"] +","+ product["name"] +","+ product["price"] +","+ str(product["count"]))
        f.write(line.strip()+"\n")
    f.close()

def make_qr_code():
    user_input = input("Enter the code of the product: ")
    for product in PRODUCTS:
        if product["code"] == user_input:
            img = qrcode.make(product)
            img.save("img.png")


def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show List")
    print("6- Buy")
    print("7- Make QR-code")
    print("8- Exit")

def add():
    code = input("Enter the code: ")
    name = input("Enter the name: ")
    price = input("Enter the price: ")
    count = input("Enter the count: ")
    new_product = {"code": code, "name": name, "price": price, "count": count}
    PRODUCTS.append(new_product)
    print("You added an item succestully!")

def edit():
    user_input = input("Enter the code of the product: ")
    for product in PRODUCTS:
        if product["code"] == user_input:
            print("You have chosen", product["name"], "to be edited")
            print("which data you wanna edit?")
            print("1- Name")
            print("2- Price")
            print("3- Count")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                new_name = input("Enter the new Name: ")
                product["name"] = new_name
            elif choice == 2:
                new_price = input("Enter the new Price: ")
                product["price"] = new_price
            elif choice == 3:
                new_count = input("Enter the new Count: ")
                product["count"] = new_count
            print("Data is updated successfully!")
            print("code\t\tname\t\tprice\t\tcount")
            print(product["code"], "\t\t", product["name"], "\t\t", product["price"], "\t\t", product["count"])
            break
    else:
        print("your entered code is not found!")

def remove():
    user_input = input("Enter the code of the product: ")
    for product in PRODUCTS:
        if product["code"] == user_input:
            PRODUCTS.remove(product)
            print(product["name"], "is removed successfully!")
            break
    else:
        print("your entered code is not found!")

def search():
    user_input = input("Enter the code or name of the product: ")
    for product in PRODUCTS:
        if product["code"] == user_input or product["name"] == user_input:
            print(product["code"], "\t\t", product["name"], "\t\t", product["price"])
            break
    else:
        print("your entered code is not found!")                    

def show_list():
    print("code\t\tname\t\tprice")
    for product in PRODUCTS:
        print(product["code"], "\t\t", product["name"], "\t\t", product["price"])

def buy():
    total = 0
    while True:
        user_input = input("Enter the code of the product: ")
        for product in PRODUCTS:
            if product["code"] == user_input:
                num = int(input("Enter the number of this product you want to add to your basket: "))
                count = int(product["count"])
                if num < count:
                    count -= num
                    product["count"] = count
                    product["num"]= num
                    bill.append(product)
                else:
                    print("Insufficient inventory")    

        ans = input("Do you wany to continue? (Y/N)? ")
        if ans == "N":
            print("code\t\tname\t\tprice\t\tnum")
            for item in bill:
                print(item["code"], "\t\t", item["name"], "\t\t", item["price"], "\t\t", item["num"])
                total += (int(item["price"])*int(item["num"]))
            sum = {"sum": total}
            bill.append(sum) 
            print("\t\tsum\t=\t", total )
            break

print("Welcome to Hane store")
print("Loading...")
read_from_database()
print("Data loaded.")
 
while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        make_qr_code()
    elif choice == 8:
        write_to_database()
        exit(0)
    else:
        print("your choice is incorrect")
