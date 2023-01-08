from prettytable import PrettyTable
from media import Media
from time_format import My_Time

class Documentary(Media):
    def __init__(self, ID, name , year, director , IMDB_score, url, duration, casts,):
        super().__init__(ID,  name , director , IMDB_score , url , casts)

        #additional properties of class Documentary
        self.year = year
        self.duration = duration

        #methods
    def showInfo(self):
        my_table = PrettyTable()
        my_table.field_names = ["ID", "Name", "Year", "Director", "Score", "Duration", "cast"]
        my_table.add_row([self.ID, self.name, self.year, self.director, self.score, self.duration, self.casts])
        print(my_table)

    @staticmethod   
    def add(other):
        
        ID = input("Enter the ID: ")  
        name = input("Enter the Name: ")
        year = input("Enter the year of production: ")
        director = input("Enter the name of director: ")
        score = input("Enter the IMDB score: ")
        url = input("Enter the URL of trailer on Youtube: ")
        duration = input("Enter the duration: ")
        casts = input("Enter the names of three stars with comma in betweens: ")

        new_obj = Documentary(ID, name, year, director, score, url, duration, casts)
        other.append(new_obj)

    def edit(self):
        print("You have chosen", self.name, "to be edited")
        print("which data you wanna edit?")
        print("1- Name")
        print("2- Year of Production")
        print("3- Director")
        print("4- Score")
        print("5- URL")
        print("6- Duration")
        print("7- Casts")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            new_name = input("Enter the new Name: ")
            self.name = new_name
        elif choice == 2:
            new_year = input("Enter the new Year: ")
            self.year = new_year
        elif choice == 3:
            new_director = input("Enter the new Director: ")
            self.director = new_director
        elif choice == 4:
            new_score = input("Enter the new Score: ")
            self.score = new_score
        elif choice == 5:
            new_url = input("Enter the new URL: ")
            self.url = new_url
        elif choice == 6:
            new_duration = input("Enter the new Duration: ")
            self.duration = new_duration
        elif choice == 7:
            new_casts = input("Enter the new Casts: ")
            self.casts = new_casts

        print("Data is updated successfully!")

    def advance_search(self, other , a , b):
        time = self.duration.split(":")
        t = My_Time(int(time[0]), int(time[1]))
        result = t.time_to_min()
        if result >= a and result <= b :
            other.append(self)
