from Media import Media

class Film(Media):
    def __init__(self, ID, name , year, director , IMDB_score , url , duration, casts):
        super().__init__()

        #additional properties of class Film
        self.year = year
        self.duration = duration


        #methods
    def showInfo(self):
        print("ID\t\tName\t\t\t\t\t\tYear\t\tDirector\t\t\t\tIMDB Score\t\tduration\t\tCasts")
        print(self.ID,"\t\t",self.name,"\t\t\t\t\t\t", self.year, "\t\t", self.director, "\t\t\t\t", self.score, "\t\t", self.duration, "\t\t", self.casts)
      
    