#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset



# N.B. If only .env files supported variable expansion...
export CELERY_BROKER_URL="${REDIS_URL}"

if [[ ${DB_SETUP} == "postgres" ]]; then
    echo "Using Postgres..."
    bash ./docker/compose/development/django/wait-for-postgres.sh
elif [[ ${DB_SETUP} == "litestream" ]]; then
    echo "Using Litestream..."
else
    echo "DB_SETUP must be one of 'postgres' or 'litestream' (DB_SETUP=${DB_SETUP})"
    exit 1
fi

echo "Running command: $@"

exec "$@"