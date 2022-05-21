from distutils.file_util import move_file
import sqlite3
import json
from pathlib import Path

# Initial load using json to sqlite DB and writing to DB

# movies = json.loads(Path("movies.json").read_text())

# print(movies)

# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?,?,?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))

# Reading from SQlite DB

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)
