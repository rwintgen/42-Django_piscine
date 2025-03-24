from django.shortcuts import render
from django.templatetags.static import static
from django.http import HttpResponse, Http404
from django.conf import settings
import psycopg2
import os
import tempfile

# Create your views here.
def connect_to_db():
	return psycopg2.connect(
		dbname=settings.DATABASES['default']['NAME'],
		user=settings.DATABASES['default']['USER'],
		password=settings.DATABASES['default']['PASSWORD'],
		host=settings.DATABASES['default']['HOST'],
		port=settings.DATABASES['default']['PORT'],
	)


def rm_null_str_from_csv(file_path):
	tmp = tempfile.NamedTemporaryFile(delete=False, mode='w', newline='')
	with open(file_path, 'r') as f:
		for line in f:
			tmp.write(line.replace("NULL", "\\N"))
	tmp.close()
	return tmp.name

def init_table(request):
	try:
		with connect_to_db() as conn:
			with conn.cursor() as cur:
				cur.execute("""
					CREATE TABLE IF NOT EXISTS ex08_planets (
						id SERIAL PRIMARY KEY,
						name VARCHAR(64) UNIQUE NOT NULL,
						climate VARCHAR(128),
						diameter INTEGER,
						orbital_period INTEGER,
						population BIGINT,
						rotation_period INTEGER,
						surface_water REAL,
						terrain VARCHAR(128)
					);
				""")
				cur.execute("""
					CREATE TABLE IF NOT EXISTS ex08_people (
						id SERIAL PRIMARY KEY,
						name VARCHAR(64) UNIQUE NOT NULL,
						birth_year VARCHAR(32),
						gender VARCHAR(32),
						eye_color VARCHAR(32),
						hair_color VARCHAR(32),
						height INTEGER,
						mass REAL,
						homeworld VARCHAR(64),
						CONSTRAINT fk_homeworld FOREIGN KEY (homeworld)
						REFERENCES ex08_planets(name) ON DELETE CASCADE
					);
				""")
				conn.commit()
		
		return HttpResponse("OK")
	except Exception as e:
		return HttpResponse("Error: " + str(e), status = 500)

def populate_table(request):
	status = []
	try:
		with connect_to_db() as conn:
			with conn.cursor() as cur:
				planets_path = os.path.join(settings.BASE_DIR, "ex08", "static", "ex08", "planets.csv")
				tmp = rm_null_str_from_csv(planets_path)
				with open(tmp, 'r') as f:
					cur.copy_from(f, "ex08_planets", "\t", columns=('name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain'))
					status.append("OK")

				people_path = os.path.join(settings.BASE_DIR, "ex08", "static", "ex08", "people.csv")
				tmp = rm_null_str_from_csv(people_path)
				with open(tmp, 'r') as f:
					cur.copy_from(f, "ex08_people", "\t", columns=('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld'))
					status.append("OK")

			return HttpResponse("<br>".join(status))
	except Exception as e:
		return HttpResponse("Error: " + str(e), status = 500)

def display_content(request):
	try:
		with connect_to_db() as conn:
			with conn.cursor() as cur:
				cur.execute("""
					SELECT p.name AS character_name, p.homeworld, pl.climate
					FROM ex08_people p
					INNER JOIN ex08_planets pl ON p.homeworld = pl.name
					WHERE pl.climate ILIKE '%windy%'
					ORDER BY p.name;
				""")
				data = cur.fetchall()

		if not data:
			raise Http404()

		context = {
			"css_file" : "ex08/styles.css",
			"characters" : data
		}
		return render(request, "ex08/display.html", context)
	except Exception as e:
		return HttpResponse("No data available")
