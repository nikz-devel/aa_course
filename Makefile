kafkastart:
	@docker-compose up -d

kafkastop:
	@docker-compose stop

build-auth:
	docker build -t popug-auth:dev auth

build-manager:
	docker build -t popug-manager:dev task-manager

up-auth:
	docker run --rm --name popug-auth -p 8080:5000 popug-auth:dev

up-manager:
	docker run --rm --name popug-manager -p 8000:5000 popug-manager:dev

