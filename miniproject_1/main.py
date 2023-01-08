from film import Film
from series import Series
from documentary import Documentary
from clip import Clip
from prettytable import PrettyTable

PRODUCTS = []

def read_from_database():
    with open("database.txt", encoding="utf8") as f:
        
        for line in f:
            result = line.split(",")

            if result[2] == "Series":
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
    f = open("database.txt", "w")
    f = open("database.txt", "a")
    for product in PRODUCTS:
        
        if isinstance(product , Series):
            line = str(product.ID +","+ product.name +",Series,NOT DEFINED,"+ product.director +","+ str(product.score) + "," + product.url + ",NOT DEFINED," + product.casts[0] + "," + product.casts[1] + "," + product.casts[2] + "," + str(product.seasons) + "," + str(product.episodes))
        elif isinstance(product , Film):
            line = str(product.ID +","+ product.name +",Movie,"+ product.year+ "," + product.director +","+ str(product.score) + "," + product.url +","+ product.duration +","+ product.casts[0] + "," + product.casts[1] + "," + product.casts[2] + ",NOT DEFINED,NOT DEFINED")
        elif isinstance(product , Documentary):
            line = str(product.ID +","+ product.name +",Documentary,"+ product.year+ "," + product.director +","+ str(product.score) + "," + product.url +","+ product.duration +","+ product.casts[0] + "," + product.casts[1] + "," + product.casts[2] + ",NOT DEFINED,NOT DEFINED")
        elif isinstance(product , Clip):
            line = str(product.ID +","+ product.name +",Short,"+ product.year+ "," + product.director +","+ str(product.score) + "," + product.url +","+ product.duration +","+ product.casts[0] + "," + product.casts[1] + "," + product.casts[2] + ",NOT DEFINED,NOT DEFINED")
        
        f.write(line.strip()+"\n")
    f.close()


def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show List")
    print("6- Download")
    print("7- Advance Search")
    print("8- Exit")

def add():
    choice = input("Enter the type of the Media you want to add: ").lower()
        
    if choice == "series":
        Series.add(PRODUCTS)
        
    elif choice == "film":
        Film.add(PRODUCTS)
    
    elif choice == "documentary":
        Documentary.add(PRODUCTS)
    
    elif choice == "clip":
        Clip.add(PRODUCTS)

    print("You added an item successfully!")

def edit():
    user_input = input("Enter the ID of the Media you want to edit: ")
    for product in PRODUCTS:
        if product.ID == user_input:
            product.edit()
        break
    else:
        print("your entered ID is not found!")

def remove():
    user_input = input("Enter the ID of the Media you want to remove: ")
    for product in PRODUCTS:
        if product.ID == user_input:
            product.remove(PRODUCTS)
        break
    else:
        print("your entered ID is not found!")

def search():
    user_input = input("Enter the ID (000) or name of the media: ")
    for product in PRODUCTS:
        if product.ID == user_input or product.name == user_input:
            product.showInfo()
            break
    else:
        print("your entered ID or name is not found!")

def show_list():
    series = []
    film = []
    documentary =[]
    clip =[]

    for object in PRODUCTS:
        if isinstance(object , Series):
            series.append(object)

        elif isinstance(object , Film):
            film.append(object)

        elif isinstance(object , Documentary):
            documentary.append(object)

        elif isinstance(object , Clip):
            clip.append(object)

    choice = input("Enter the type of the Media you want to see: ").lower()
    
    if choice == "series":
        my_table = PrettyTable()
        my_table.field_names = ["ID", "Name", "Director", "Score", "cast", "Seasons", "Episodes"]
        for line in series:   
            my_table.add_row([line.ID, line.name, line.director, line.score, line.casts, line.seasons, line.episodes])
        print(my_table)

    elif choice == "film":
        my_table = PrettyTable()
        my_table.field_names = ["ID", "Name", "Year", "Director", "Score", "Duration", "cast"]
        for line in film:
            my_table.add_row([line.ID, line.name, line.year, line.director, line.score, line.duration, line.casts])
        print(my_table)

    elif choice == "documentary":
        my_table = PrettyTable()
        my_table.field_names = ["ID", "Name", "Year", "Director", "Score", "Duration", "cast"]
        for line in documentary:
            my_table.add_row([line.ID, line.name, line.year, line.director, line.score, line.duration, line.casts])
        print(my_table)

    elif choice == "clip":
        my_table = PrettyTable()
        my_table.field_names = ["ID", "Name", "Year", "Director", "Score", "Duration", "cast"]
        for line in clip:
            my_table.add_row([line.ID, line.name, line.year, line.director, line.score, line.duration, line.casts])
        print(my_table)

def download():
    user_input = input("Enter the ID of the Media you want to download: ")
    for product in PRODUCTS:
        if product.ID == user_input:
            product.download()
        break
    else:
        print("your entered ID is not found!")        

def advance_search():
    result = []
    a = int(input("Enter the min length(minute): "))
    b = int(input("Enter the max length(minute): "))

    for product in PRODUCTS:
        if not isinstance(product , Series):
            product.advance_search(result, a, b)

    my_table = PrettyTable()
    my_table.field_names = ["ID", "Name", "Year", "Director", "Score", "Duration", "cast"]
    for line in result:
        my_table.add_row([line.ID, line.name, line.year, line.director, line.score, line.duration, line.casts])
    print(my_table)

print("Welcome to Multimedia management service")
print("Loading...")
read_from_database()
print("Data loaded successfully")

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
        download()
    elif choice == 7:
        advance_search() 
    elif choice == 8:       
        write_to_database()
        exit(0)
    else:
        print("your choice is incorrect")
