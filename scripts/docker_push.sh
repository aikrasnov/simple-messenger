echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker build -t messenger_service .
tag=$(date +%Y%m%d%H%M%S)
docker tag messenger_service messenger_service:$tag
docker push pompi1990/messenger-service:$tag
