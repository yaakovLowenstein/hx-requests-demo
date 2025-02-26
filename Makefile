dc:
	docker-compose $(cmd)
up:
	docker-compose up -d
attach:
	docker attach menu-web
down:
	docker-compose down --remove-orphans
poetry:
	docker-compose run --rm web poetry $(cmd)
padd:
	docker-compose run --rm web poetry add $(cmd)
pinstall:
	docker-compose run --rm web poetry install
clean:
	docker-compose down -v --remove-orphans
migrate:
	poetry run  python manage.py migrate $(cmd)
mm:
	poetry run  python manage.py makemigrations
manage:
	poetry run python manage.py $(cmd)
createsuperuser:
	docker-compose run --rm web poetry run python manage.py createsuperuser
run:
	poetry run python manage.py runserver 0.0.0.0:8000
