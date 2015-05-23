from random import random
import json
from tabulate import tabulate


class Song:

    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.__length = length

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.__length)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist

    def __hash__(self):
        return hash(self.__str__())

    def get_length(self):
        return self.__length

    def prepare_json(self):
        song_dict = self.__dict__
        return {key: song_dict[key] for key in song_dict if not key.startswith("_")}

    def length(self, seconds=False, minutes=False, hours=False):
        result = self.__length.split(":")
        if seconds is True:
            if len(result) == 2:
                return int(result[0])*60 + int(result[1])
            elif len(result) == 3:
                return int(result[0])*3600 + int(result[1])*60 + int(result[2])
        elif minutes is True:
            if len(result) == 2:
                return int(result[0])
            elif len(result) == 3:
                return int(result[0])*60 + int(result[1])
        elif hours is True:
            return int(result[0])
        return self.__length


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.Playlist = []

    def has_song(self, song):
        return song in self.Playlist

    def add_song(self, song):
        # if self.has_song(song):
        #     raise Exception("Song already exists")
        self.Playlist.append(song)

    def remove_song(self, song):
        if not self.has_song(song):
            raise Exception("Song not in playlist")
        self.Playlist.remove(song)

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def total_length(self):
        sumsongs = 0
        for song in self.Playlist:
            sumsongs += song.length(seconds=True)
        return str(sumsongs)

    def artists(self):
        artistsdict = {}
        for song in self.Playlist:
            if song.artist not in artistsdict:
                artistsdict[song.artist] = 0
        for song in self.Playlist:
            if song.artist in artistsdict.keys():
                artistsdict[song.artist] += 1
        return artistsdict

#First case - True Repeat and False shuffle
    def firstcase(self):
        if self.currentsongindex == len(self.Playlist):
            self.currentsongindex = 0
        self.currentsongindex += 1
        return self.Playlist[self.currentsongindex - 1]

# Second case - False Repeat and False shuffle
    def secondcase(self):
        if self.currentsongindex == len(self.Playlist):
            raise Exception("Playlist is over")
        self.currentsongindex += 1
        return self.Playlist[self.currentsongindex - 1]

# Third case - False repeat and True shuffle
    def thirdcase(self):
        self.currentsongindex = int(random()*len(self.Playlist))
        if len(self.playedsongs) == len(self.Playlist):
            raise Exception("Playlist is over")
        while self.Playlist[self.currentsongindex] in self.playedsongs:
            self.currentsongindex = int(random()*len(self.Playlist))
        self.playedsongs.append(self.Playlist[self.currentsongindex])
        return self.Playlist[self.currentsongindex]

    #Fourth case - True Repeat and True shuffle
    def fourthcase(self):
        self.currentsongindex = int(random()*len(self.Playlist))
        if len(self.playedsongs) == len(self.Playlist):
            self.playedsongs = []
        while self.Playlist[self.currentsongindex] in self.playedsongs:
            self.currentsongindex = int(random()*len(self.Playlist))
        self.playedsongs.append(self.Playlist[self.currentsongindex])
        return self.Playlist[self.currentsongindex]

    def next_song(self):
            if self.repeat is True and self.shuffle is False:
                self.firstcase()
            elif self.repeat is False and self.shuffle is False:
                self.secondcase()
            elif self.repeat is False and self.shuffle is True:
                self.thirdcase()
            else:
                self.fourthcase()

    def pprint_playlist(self):
        headers = ["Artist", "Song", "Length"]
        table = []

        for song in self.Playlist:
            table.append([song.artist, song.title, song.get_length()])

        print(tabulate(table, headers=headers))

    def prepare_json(self):
        data = {
            "name": self.name,
            "songs": [song.prepare_json() for song in self.Playlist]
        }

        return data

    def save(self, indent=True):
        filename = self.name.replace(" ", "-") + ".json"

        with open(filename, "w") as f:
            f.write(json.dumps(self.prepare_json(), indent=indent))

    @staticmethod
    def load(filename):
        with open(filename, "r") as f:
            contents = f.read()
            data = json.loads(contents)
            p = Playlist(data["name"])

            for dict_song in data["songs"]:
                song = Song(artist=dict_song["artist"], title=dict_song["title"], album=dict_song["album"], length=dict_song["length"])
                p.add_song(song)

            return p

    currentsongindex = 0
    playedsongs = []

playlist = Playlist("Polina's playlist")
song1 = Song("Nina", "Ed Sheeran", "X", "04:11")
song2 = Song("How to Save a Life", "The Fray", "How to Save a Life", "04:23")
song3 = Song("Random song", "Random artist", "Random album", "04:10")
playlist.add_song(song1)
playlist.add_songs([song2, song3])
print(playlist.total_length())
# playlist.remove_song(song2)
print(playlist.total_length())
print(playlist.artists())
playlist.pprint_playlist()
# playlist.save()
# new_playlist = playlist.load("OneRepublic.json")
# print(new_playlist.total_length())
