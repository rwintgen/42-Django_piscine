from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies

# Create your views here.
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
	for episode_nb, title, director, producer, release_date in movies:
		try:
			Movies.objects.create(
				episode_nb=episode_nb,
				title=title,
				director=director,
				producer=producer,
				release_date=release_date
			)
			status.append("OK")
		except Exception as e:
			status.append(f"Error: {title}: {e}")

	return HttpResponse("<br>".join(status))


def display_content(request):
	data = Movies.objects.all()

	if not data:
		return HttpResponse("No data available")

	context = {
		"css_file" : "ex03/styles.css",
		"movies" : data
	}
	return render(request, "ex03/display.html", context)