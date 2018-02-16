

import media
import fresh_tomatoes

wolf_of_wall_street = media.Movie("Wolf of Wall Street",
	"A man starts a sketchy company and becomes rich",
	"https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",
	"https://www.youtube.com/watch?v=iszwuX1AK6A", "R")


superbad = media.Movie("Superbad", 
	"High school kids are about to graduate", 
	"https://upload.wikimedia.org/wikipedia/en/8/8b/Superbad_Poster.png", 
	"https://www.youtube.com/watch?v=4eaZ_48ZYog", "R")

donnie_darko = media.Movie("Donnie Darko", 
	"A troubled teen is visited by a man in a rabbit suit with a message that the world is ending",
	"https://upload.wikimedia.org/wikipedia/en/d/db/Donnie_Darko_poster.jpg", 
	"https://www.youtube.com/watch?v=bzLn8sYeM9o", "R")

get_him_to_the_greek = media.Movie("Get Him To The Greek",
	"A man must get a rockstar to the concert he is going to play",
	"https://upload.wikimedia.org/wikipedia/en/c/c2/Get_Him_to_the_Greek.jpg",
	"https://www.youtube.com/watch?v=N6ixkr0-qvo", "R")

edge_of_tomorrow = media.Movie("Edge of Tomorrow",
	"A soldier relives the same day over and over","https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
	"https://www.youtube.com/watch?v=vw61gCe2oqI", "PG-13")

jaws = media.Movie("Jaws","Great white shark eats people",
	"https://upload.wikimedia.org/wikipedia/en/e/eb/JAWS_Movie_poster.jpg",
	"https://www.youtube.com/watch?v=U1fu_sA7XhE","PG")


movies = [wolf_of_wall_street, superbad, donnie_darko, get_him_to_the_greek, edge_of_tomorrow, jaws]
fresh_tomatoes.open_movies_page(movies)


