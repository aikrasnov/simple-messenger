echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker build -t pompi1990/messenger_service .
docker push pompi1990/messenger-service:latest
