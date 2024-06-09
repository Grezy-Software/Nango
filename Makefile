SHELL := /bin/bash
.PHONY: setup
OS := $(shell uname)


setup:
# Frontend
pnpm -i
# Backend
ifeq ($(OS), Darwin)       # Mac OS X
	./setup/setup-osx.sh
else ifeq ($(OS), Linux)
	if [ "ID_LIKE=debian" != "" ]; then ./setup/scripts/setup-debian.sh; fi
else
	@echo "Unsupported OS: $(OS). Please follow the manual installation."
endif