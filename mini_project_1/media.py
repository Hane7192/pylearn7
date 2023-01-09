import pytube

class Media:
    def __init__(self , ID,  name , director , IMDB_score , url , casts):
        #properties
        self.ID = ID
        self.name = name
        self.director = director
        self.score = IMDB_score
        self.url = url
        self.casts = casts

        #methods
    def download(self):
        link = str(self.url)
        first_stream = pytube.YouTube(link).streams.first()
        first_stream.download(output_path = "./", filename = (str(self.name) + ".mp4"))
        

    def remove(self, other):
        other.remove(self)
        print(self.name, "is removed successfully!")

    
        