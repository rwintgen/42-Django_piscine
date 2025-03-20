from django.shortcuts import render

# Create your views here.
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

def populate_table():

def display_content():