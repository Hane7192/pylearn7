from Media import Media

class Series(Media):
    def __init__(self, ID, name , director , IMDB_score , url , casts, seasons, episodes):
        super().__init__()

        #additional properties of class Series
        self.seasons = seasons
        self.episodes = episodes

        #methods
    def showInfo(self):
        print("ID\t\tName\t\t\t\t\t\tDirector\t\t\t\tIMDB Score\t\tCasts\t\t\t\t\t\t\t\t\t\t\t\tNumber of Seasons\t\tNumber of Episodes")
        print(self.ID,"\t\t",self.name,"\t\t\t\t\t\t", self.director, "\t\t\t\t", self.score, "\t\t", self.casts, "\t\t\t\t\t\t\t\t\t\t\t\t", self.seasons, "\t\t", self.episodes )
        