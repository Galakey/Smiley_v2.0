import json
class Anime:
    def __init__(self, anime):
        self.__entryID = anime["entryID"]
        self.__title = anime["title"]
        self.__episode = anime["episode"]
        self.__watch = anime["watch"]
        self.__mal = anime["mal"]
        self.Methods = {"entryID": self.getEntryID, "title": self.getTitle,
                        "episode": self.getTitle, "watch": self.getWatch, "mal": self.getMal}

    def getEntryID(self):
        return self.__entryID

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title
        Data.updateAnime(self)

    def getEpisode(self):
        return self.__episode

    def setEpisode(self, episode):
        if episode == int:
            self.__episode = episode
        Data.updateAnime(self)

    def getWatch(self):
        return self.__watch

    def setWatch(self, watch):
        self.__watch = watch
        Data.updateAnime(self)

    def getMal(self):
        return self.__mal

    def setMal(self, mal):
        self.__mal = mal
        Data.updateAnime(self)


class Data:
    __data = "./data.json"

    def getAnime(self, entryID: int):
        anime = {}
        with open(self.__data, "r+") as file:
            data = json.load(file)
            for i in data["anime"]:
                if i["entryID"] == entryID:
                    anime["entryID"] = entryID
                    for x in data["animeVals"]:
                        #finish this :D

    def updateAnime(self, anime: Anime):
        if anime == Anime:
            with open(self.__data, "r+") as file:
                data = json.load(file)
                for i in data["anime"]:
                    if i["entryID"] == anime.getEntryID():
                        for x in anime.Methods:
                            i[x] = anime.Methods[x]()
                        file.seek(0)
                        json.dump(data, file, indent=4)
                        file.truncate()
                        file.close()
                        return

    def addAnime(self, title: str, episode: int, watch: str, mal: str):
        # add more data validation for passed input
        anime = {}
        with open(self.__data, "r+") as file:
            data = json.load(file)
            data["entryIDCount"] += 1
            anime["entryID"] = data["entryIDCount"]
            anime["title"] = title
            anime["episode"] = episode
            anime["watch"] = watch
            anime["mal"] = mal

            data["anime"].append(anime)
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

    def delAnime(self, anime):
        if anime == Anime:
            with open(self.__data, "r+") as file:
                data = json.load(file)
                for i in data["anime"]:
                    if i["entryID"] == anime.getEntryID():
                        data.pop(i)
                        file.seek(0)
                        json.dump(data, file, indent=4)
                        file.truncate()
                        file.close()
                        return

