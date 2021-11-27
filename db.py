from os import path
import sqlite3
class DB():
    def __init__(self):
        if not path.exists("./songs.db"):
            conn = sqlite3.connect('songs.db')
            c = conn.cursor()
            c.execute("""CREATE TABLE songs (name text,author text,album text)""")
            conn.commit()
            conn.close()

    def insert(self, name, author, album):
        try:
            conn = sqlite3.connect('songs.db')
            c = conn.cursor()
            c.execute("INSERT INTO songs VALUES (:name, :author, :album)",
                                {
                                    'name': name,
                                    'author': author,
                                    'album': album 
                                })
            conn.commit()
        except:
            return False 
        finally:
            conn.close()
            return True

    def delete(self, name, author, album):
        try:
            conn = sqlite3.connect('songs.db')
            c = conn.cursor()
            c.execute("DELETE FROM songs WHERE (name = ?) and (author = ?) and (album = ?)",(name,author,album))
            conn.commit()
        except:
            return False 
        finally:
            conn.close()
            return True

    def search(self, str):
        try:
            conn = sqlite3.connect('songs.db')
            c = conn.cursor()
            c.execute("DELETE FROM songs WHERE (name = ?) and (author = ?) and (album = ?)",(name,author,album))
            conn.commit()
        except:
            return False 
        finally:
            conn.close()
            return True

