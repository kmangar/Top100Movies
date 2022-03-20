from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, "html.parser")


movies = soup.findAll(name="h3", class_="title")
# print(article_tag)
movie_title = []

for movie in movies:
    movie_name = movie.get_text()
    movie_title.append(movie_name)

movie_title.reverse()

with open("movie_list.txt", "w") as file:
    for movie in movie_title:
        file.write(f"{movie}\n")

print(movie_title)




