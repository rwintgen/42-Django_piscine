#!/bin/bash

DB_NAME="djangotraining"
DB_USER="djangouser"
DB_HOST="localhost"
DB_PORT="5432"
DB_PASSWORD="secret"

export PGPASSWORD=$DB_PASSWORD

psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "
DO \$\$
DECLARE
	table_name RECORD;
BEGIN
	FOR table_name IN
		(SELECT tablename FROM pg_tables WHERE schemaname = 'public')
	LOOP
		RAISE NOTICE 'Dropping table: %', table_name.tablename;
		EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(table_name.tablename) || ' CASCADE';
	END LOOP;
END
\$\$;
"

unset PGPASSWORD