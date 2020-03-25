all: build push

build:
	docker build -f docker/prod.Dockerfile -t registry.gitlab.com/ahmadsyafiq93/billplz-poc .

push:
	docker push registry.gitlab.com/ahmadsyafiq93/billplz-poc
