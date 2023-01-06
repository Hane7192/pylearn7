from Film import Film
from Series import Series
from Documentary import Documentary
from Clip import Clip

PRODUCTS = []

def read_from_database():
    f = open("database.txt", "r")

    for line in f:
        result = line.split(",")

        if result[2] == "series":
            series_obj = Series(result[0], result[1], result[4], result[5], result[6], [result[8], result[9], result[10]], result[11], result[12])
            PRODUCTS.append(series_obj)

        elif result[2] == "Movie":
            Film_obj = Film(result[0], result[1], result[3], result[4], result[5], result[6], result[7], [result[8], result[9], result[10]])
            PRODUCTS.append(Film_obj)

        elif result[2] == "Documentary":
            documentary_obj = Documentary(result[0], result[1], result[3], result[4], result[5], result[6], result[7], [result[8], result[9], result[10]])
            PRODUCTS.append(documentary_obj)

        else:
            clip_obj = Clip(result[0], result[1], result[3], result[4], result[5], result[6], result[7], [result[8], result[9], result[10]])
            PRODUCTS.append(clip_obj)

    f.close()

def write_to_database():
    ...


def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show")
    print("6- Show List")
    print("7- Exit")

def add():
    ...

def edit():
    ...

def remove():
    ...

def search():
    ...

def show():
    ...

# def show_list():
    # choice = input("Enter the type of the Media you want to see or type all to see the whole list: ").lower()
    # if choice == "series":
    #     for 

print("Welcome to Multimedia management service")
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
        show()
    # elif choice == 6:
    #     show_list()
    elif choice == 7:
        write_to_database()
        exit(0)
    else:
        print("your choice is incorrect")
