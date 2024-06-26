# Nango

NextJs & Django had a baby! It's Nango!

This blueprint under steroids speeds up the development of your full stack application by providing a ready-to-use template and automatically builds the bridge between the frontend & backend.

The bridge contains:

- drf serializers
- drf endpoints
- backend routes
- front types
- api call methods

The workflow is simple: 
1. Create a model in your backend
2. Run the `make bridge` command
3. Import type and api call method in your frontend


## Todo

### Blue print

- Django
    - [ ] Structure
    - [ ] Settings
        - [ ] envs files generator
    - [x] Ruff
    - [x] Requirements
    - [ ] Celery
    - [ ] JWT
- NextJs
    - [ ] Structure
    - [ ] Tailwind
    - [ ] Typescript
    - [ ] Eslint
    - [ ] Shadcn
- Github
    - [x] Dependabot (front & back)
    - [ ] CI (Tests, Lint, Build)
    - [x] Pre-commit hook (ruff)
- Docker
    - [ ] Development docker compose (hard coded)
    - [ ] Production docker compose (variables)
- [x] Semantic release
- [x] Mkdocs

### Bridge

- Backend
    - [ ] Endpoint Generator
    - [ ] Serializer Generator
    - [ ] Dynamic routes
    - [ ] Retrieve types from models

- Frontend
    - [ ] API call methods generator
    - [ ] Types generator


