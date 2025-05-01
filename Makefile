run:
	docker compose up -d

build:
	docker compose build
	docker compose up -d

init:
	poetry install --no-root

migrate:
	docker compose exec blog python manage.py makemigrations
	docker compose exec blog python manage.py migrate

test:
	docker compose exec blog python manage.py test --keepdb --failfast

dump-model:
	docker compose exec blog python manage.py dumpdata $(model) --indent 2 > ./fixtures/development.json

dump-all:
	docker compose exec blog python manage.py dumpdata \
	--exclude sessions \
	--exclude contenttypes \
	--exclude auth.Permission \
	--natural-foreign --natural-primary \
	--indent 2 > ./fixtures/development.json

logs:
	docker compose logs blog -f

load-fixtures:
	docker compose exec blog python manage.py loaddata ./fixtures/development.json

superuser:
	docker compose exec blog python manage.py createsuperuser

shell:
	docker compose exec blog python manage.py shell


add-package:
	@if [ -z "$(package)" ]; then \
		echo "You must provide a package name: make add-package package=nome_do_pacote"; \
		exit 1; \
	fi
	poetry add $(package)
	poetry export -f requirements.txt --without-hashes -o requirements.txt
	@echo "Pacote '$(package)' sucesssfully added to requirements.txt"

add-dev-pack:
	@if [ -z "$(package)" ]; then \
		echo "You must provide a package name: make add-dev-package package=nome_do_pacote"; \
		exit 1; \
	fi
	poetry add $(package) --dev
	poetry export -f requirements.txt --without-hashes -o requirements.txt
	@echo "Pacote '$(package)' sucesssfully added to requirements.txt"