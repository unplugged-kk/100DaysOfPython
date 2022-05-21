import json
from pathlib import Path

# writing json

# movies = [
#     {"id": 1, "title": "Terminator", "Year": 1989},
#     {"id": 2, "title": "Avatar", "Year": 2015},
# ]

# data = json.dumps(movies)
# print(data)

# Path("movies.json").write_text(data)

# Reading json

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[1])
