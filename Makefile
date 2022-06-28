build:
	docker buildx build --push -t ghcr.io/cividi/docker-sync-with-s3 --rm --platform=linux/arm64,linux/amd64 .