from django.shortcuts import render

# Create your views here.
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

def init_table(request):
	try:
		with connect_to_db() as conn:
			with conn.cursor() as cur:
				cur.execute("""
					CREATE TABLE IF NOT EXISTS ex06_movies (
						episode_nb SERIAL PRIMARY KEY,
						title VARCHAR(64) UNIQUE NOT NULL,
						director VARCHAR(32) NOT NULL,
						producer VARCHAR(128) NOT NULL,
						release_date DATE NOT NULL,
						opening_crawl TEXT,
						created TIMESTAMP DEFAULT now(),
						updated TIMESTAMP DEFAULT now()
					);

					CREATE OR REPLACE FUNCTION update_changetimestamp_column()
					RETURNS TRIGGER AS $$
					BEGIN
						NEW.updated = now();
						NEW.created = OLD.created;
						RETURN NEW;
					END;
					$$ LANGUAGE plpgsql;

					CREATE TRIGGER update_films_changetimestamp
					BEFORE UPDATE ON ex06_movies
					FOR EACH ROW EXECUTE FUNCTION update_changetimestamp_column();
				""")
				conn.commit()
		
		return HttpResponse("OK")
	except Exception as e:
		return HttpResponse("Error: " + str(e), status = 500)
