# BASIC
up:
	docker compose up -d
build:
	docker compose up --build -d
down:
	docker compose down
down_v:
	docker compose down -v
reload:
	make down_v
	make build
