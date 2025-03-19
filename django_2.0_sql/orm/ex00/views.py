from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import psycopg2

# Create your views here.
def init_db(request):
	try:
		with psycopg2.connect(
			dbname=settings.DATABASES['default']['NAME'],
			user=settings.DATABASES['default']['USER'],
			password=settings.DATABASES['default']['PASSWORD'],
			host=settings.DATABASES['default']['HOST'],
			port=settings.DATABASES['default']['PORT'],
		) as conn:
			with conn.cursor() as cur:
				cur.execute("""
					CREATE TABLE IF NOT EXISTS ex00_movies (
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