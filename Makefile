default:
	pip2 install -r requirements.txt

db:
	python tournament/manage.py makemigrations
	python tournament/manage.py migrate --no-initial-data
	python tournament/manage.py migrate

clean:
	find ./ -name *.pyc -delete
	find ./ -name *.~ -delete
	find ./ -name \#*\# -delete
	find ./ -name \*~ -delete
