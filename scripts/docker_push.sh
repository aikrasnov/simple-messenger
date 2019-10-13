echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker build -t messenger_service .
docker tag messenger_service messenger_service:$(date +%Y%m%d%H%M%S)
docker push pompi1990/messenger-service
