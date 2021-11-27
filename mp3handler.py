import moviepy.editor as mp
import eyed3
from os import remove as rm

def toMp3(mp4):
    mp3 = mp4.split('.mp4')[0] + ".mp3" 
    
    #Cargamos el fichero .mp4
    clip = mp.VideoFileClip(mp4)

    #Lo escribimos como audio y `.mp3`
    clip.audio.write_audiofile(mp3, verbose=False, logger=None)

    rm(mp4)

    return mp3

def getTags(mp3):
    try:
        mp3File = eyed3.load(mp3)
        return [mp3File.tag.title,mp3File.tag.artist,mp3File.tag.album]
    except Exception as e:
        return [] 

def setTags(mp3, title, artist, album):
    try:
        mp3File = eyed3.load(mp3)
        mp3File.tag.title = title
        mp3File.tag.artist = artist
        mp3File.tag.album = album
        mp3File.tag.save()
        return True
    except Exception as e:
        return False
