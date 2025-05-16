create_backend_image:
	docker build -t fsad-backend .

start_docker_compose:
	docker-compose up

deploy: create_backend_image start_docker_compose