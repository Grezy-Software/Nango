SHELL := /bin/bash
.PHONY: setup
OS := $(shell uname)

setup-front:
	pnpm -i

setup-back:
ifeq ($(OS), Darwin)       # Mac OS X
	./setup/setup-osx.sh
else ifeq ($(OS), Linux)
	if [ "ID_LIKE=debian" != "" ]; then ./setup/scripts/setup-debian.sh; fi
else
	echo "Unsupported OS: $(OS). Please follow the manual installation."
endif

setup:
	# make setup-front
	make setup-back

up: 
	docker compose -f docker/development-postgres.yml up -d --build --remove-orphans
down:
	docker compose -f docker/development-postgres.yml down

bridge:
	echo -e "Work in progress..."
