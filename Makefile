# BASIC
up:
	docker compose up
build:
	docker compose up --build
down:
	docker compose down
down_v:
	docker compose down -v
reload:
	make down_v
	make up
