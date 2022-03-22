# import beautiful soup for webscraping and requests for grabing the website
from bs4 import BeautifulSoup
import requests

# make a get request to the website
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

# extract the text
movies_webpage = response.text

# use beautifulsoup and html.parser/lxml
soup = BeautifulSoup(movies_webpage, "html.parser")

# use findAll to get the movie names
movies = soup.findAll(name="h3", class_="title")

# initialize and store movies
# use the for loop to store the movie in the list
movie_title = [movie.getText() for movie in movies]

# reverses the list because the websites list the movies in descending order
movie_title.reverse()

# creates a txt file containing the top 100 movies
with open("movie_list.txt", "w") as file:
    for movie in movie_title:
        file.write(f"{movie}\n")

print(movie_title)




