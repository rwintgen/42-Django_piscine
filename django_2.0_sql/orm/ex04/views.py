from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import psycopg2

# Create your views here.
def connect_to_db():
	return psycopg2.connect(
		dbname=settings.DATABASES['default']['NAME'],
		user=settings.DATABASES['default']['USER'],
		password=settings.DATABASES['default']['PASSWORD'],
		host=settings.DATABASES['default']['HOST'],
		port=settings.DATABASES['default']['PORT'],
	)

def init_db(request):
	try:
		with connect_to_db() as conn:
			with conn.cursor() as cur:
				cur.execute("""
					CREATE TABLE IF NOT EXISTS ex04_movies (
						episode_nb SERIAL PRIMARY KEY,
						title VARCHAR(64) UNIQUE NOT NULL,
						opening_crawl TEXT,
						director VARCHAR(32) NOT NULL,
						producer VARCHAR(128) NOT NULL,
						release_date DATE NOT NULL
					);
				""")
				conn.commit()
		
		return HttpResponse("OK")
	except Exception as e:
		return HttpResponse("Error: " + str(e), status = 500)

def populate_table(request):
	movies = [
		(1, "The Phantom Menace", "George Lucas", "Rick McCallum", "1999-05-19"),
		(2, "Attack of the Clones", "George Lucas", "Rick McCallum", "2002-05-16"),
		(3, "Revenge of the Sith", "George Lucas", "Rick McCallum", "2005-05-19"),
		(4, "A New Hope", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-25"),
		(5, "The Empire Strikes Back", "Irvin Kershner", "Gary Kurtz, Rick McCallum", "1980-05-17"),
		(6, "Return of the Jedi", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
		(7, "The Force Awakens", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11"),
	]

	status = []
	try:
		with connect_to_db() as conn:
			with conn.cursor() as cur:
				cur.execute("SELECT episode_nb FROM ex04_movies")
				movies_in_db = {row[0] for row in cur.fetchall()}

				for movie in movies:
					if movie[0] not in movies_in_db:
						try:
							cur.execute("""
								INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
								VALUES (%s, %s, %s, %s, %s);
							""", movie)
							status.append("OK")
						except Exception as e:
							status.append(f"Error: {movie[1]}: {e}")

			return HttpResponse("<br>".join(status))
	except Exception as e:
		return HttpResponse("Error: " + str(e), status = 500)

def display_content(request):
	try:
		with connect_to_db() as conn:
			with conn.cursor() as cur:
				cur.execute("""
					SELECT * FROM ex04_movies ORDER BY episode_nb;
				""")
				data = cur.fetchall()

		if not data:
			raise Http404()

		context = {
			"css_file" : "ex04/styles.css",
			"movies" : data
		}
		return render(request, "ex04/display.html", context)
	except Exception as e:
		return HttpResponse("No data available")

def remove_row(request):
	try:
		with connect_to_db() as conn:
			with conn.cursor() as cur:
				if request.method == "POST":
					to_del = request.POST.get("title")
					cur.execute("""
						DELETE FROM ex04_movies WHERE title = %s
					""", [to_del])
					conn.commit()

				cur.execute("""
					SELECT title FROM ex04_movies ORDER BY episode_nb
				""")
				data = cur.fetchall()
		
		if not data:
			raise Http404()

		context = {
			"css_file" : "ex04/styles.css",
			"movies" : data
		}
		return render(request, "ex04/remove.html", context)
	except Exception as e:
		return HttpResponse("No data available")
