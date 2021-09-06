import os
import random


def play():
    songs_dir = "C:\\Users\\avina\\PycharmProjects\\pythonProject\\music"
    songs = os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir, songs[random.randrange(0, len(songs))]))
    quit()
